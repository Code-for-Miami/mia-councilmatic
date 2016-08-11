from django.shortcuts import render
from datetime import date, timedelta
from miamidade.models import MiamiDadeBill, MiamiDadeEvent
from councilmatic_core.models import Action
from councilmatic_core.views import *
from django.conf import settings


class MiamiDadeIndexView(IndexView):
    template_name = 'miamidade/index.html'
    bill_model = MiamiDadeBill
    event_model = MiamiDadeEvent

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        
        upcoming_meetings = list(self.event_model.upcoming_committee_meetings())

        date_cutoff = self.event_model.most_recent_past_city_council_meeting().start_time

        # populating activity at last council meeting
        meeting_activity = {}
        meeting_activity['actions'] = Action.actions_on_date(date_cutoff.date())
        meeting_bills = list(set([a.bill for a in meeting_activity['actions']]))
        meeting_activity['bills'] = meeting_bills
        
        # populating recent activitiy (since last council meeting)
        recent_activity = {}

        new_bills = MiamiDadeBill.new_bills_since(date_cutoff)
        recent_activity['new'] = new_bills
        
        updated_bills = MiamiDadeBill.updated_bills_since(date_cutoff)

        # getting topic counts for meeting bills
        topic_hierarchy = settings.TOPIC_HIERARCHY
        topic_tag_counts = {}

        # put together data blob for topic hierarchy
        for parent_blob in topic_hierarchy:
            parent_blob['count'] = 0
            for child_blob in parent_blob['children']:
                child_name = child_blob['name']
                child_blob['count'] = topic_tag_counts[child_name] if child_name in topic_tag_counts else 0
                parent_blob['count'] += child_blob['count']
                for gchild_blob in child_blob['children']:
                    gchild_name = gchild_blob['name']
                    gchild_blob['count'] = topic_tag_counts[gchild_name] if gchild_name in topic_tag_counts else 0

        seo = {}
        seo.update(settings.SITE_META)
        seo['image'] = '/static/images/city_hall.jpg'

        return {
            'meeting_activity': meeting_activity,
            'recent_activity': recent_activity,
            'last_council_meeting': self.event_model.most_recent_past_city_council_meeting(),
            'next_council_meeting': self.event_model.next_city_council_meeting(),
            'upcoming_committee_meetings': upcoming_meetings,
            'topic_hierarchy': topic_hierarchy,
            'seo': seo,
        }

class MiamiDadeAboutView(AboutView):
    template_name = 'miamidade/about.html'

class MiamiDadeBillDetailView(BillDetailView):
    model = MiamiDadeBill

    def get_object(self, queryset=None):
        """
        Returns a bill based on slug. If no bill found,
        looks for bills based on legistar id (so that
        urls from old Chicago councilmatic don't break)
        """

        if queryset is None:
            queryset = self.get_queryset()

        slug = self.kwargs.get(self.slug_url_kwarg)
        if slug is None:
            raise AttributeError("Generic detail view %s must be called with "
                                 "either an object pk or a slug."
                                 % self.__class__.__name__)

        # Try looking up by slug
        if slug is not None:
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})

        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404("No bill found matching the query")

        return obj

class MiamiDadeCouncilMembersView(CouncilMembersView):

    def get_seo_blob(self):
        seo = {}
        seo.update(settings.SITE_META)
        seo['site_desc'] = "Look up your local Alderman, and see what they're doing in your ward & your city"
        seo['image'] = '/static/images/chicago_map.jpg'
        seo['title'] = 'Wards & Aldermen - Chicago Councilmatic'

        return seo
