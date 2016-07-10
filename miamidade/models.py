from django.conf import settings
from councilmatic_core.models import Bill, Event
from datetime import datetime
import pytz
from .helpers import subj_classifier

app_timezone = pytz.timezone(settings.TIME_ZONE)

class MiamiDadeBill(Bill):

    class Meta:
        proxy = True

    # makes a friendly name using bill type & number, e.g. 'Introduction 643-2015'
    # this is what is used as the title (heading) for bills throughout the site (bill listing, bill detail)
    @property
    def friendly_name(self):
        nums = self.identifier.split(' ')[-1]
        return self.bill_type.title() + ' ' + nums

    # the date that a bill was passed, if it has been passed
    @property
    def date_passed(self):
        return self.actions.filter(classification='passage').order_by('-order').first().date if self.actions.all() else None

    # whether or not a bill has reached its final 'completed' status
    # what the final status is depends on bill type
    def _terminal_status(self, history, bill_type):
        if history:
            if bill_type.lower() == 'ordinance':
                if 'passage' in history:
                    return 'Passed'
                elif 'failure' in history or 'committe-failure' in history:
                    return 'Failed'
            if bill_type.lower() in ['order', 'appointment','resolution']:
                if 'passage' in history:
                    return 'Approved'
                else:
                    return False

        return False

    # this is b/c we don't have data on bills voted against, only bills passed -
    # everything else is just left to die silently ¯\_(ツ)_/¯
    # turns out that ~80% of nyc bills that get passed, are passed within
    # 2 months of the last action
    # using 6 months instead of 2 months for cutoff, to minimize incorrectly labeling
    # in-progress legislation as stale
    def _is_stale(self, last_action_date):
        if last_action_date:
            timediff = datetime.now().replace(tzinfo=app_timezone) - last_action_date
            return (timediff.days > 180)
        else:
            return True

    # the 'current status' of a bill, inferred with some custom logic
    # this is used in the colored label in bill listings
    @property
    def inferred_status(self):
        actions = self.actions.all().order_by('-order')
        classification_hist = [a.classification for a in actions]
        last_action_date = actions[0].date if actions else None
        bill_type = self.bill_type
        print( self.classification )

        if bill_type.lower() in ['communication', 'oath of office']:
            return None
        if self._terminal_status(classification_hist, bill_type):
            return self._terminal_status(classification_hist, bill_type)
        elif self._is_stale(last_action_date):
            return 'Stale'
        else:
            return 'Active'

    # this is used for the text description of a bill in bill listings
    # the abstract is usually friendlier, so we want to use that whenever it's available,
    # & have the description as a fallback
    @property
    def listing_description(self):
        if self.abstract:
            return self.abstract
        else:
            return self.description

    # You know what, I think we do want tags like Chicago, but Miami-Dade
    # doesn't really need to have that "Routine" / "Non-routine" stuff.
    @property
    def topics(self):
        return subj_classifier(self.subject)


class MiamiDadeEvent(Event):

    class Meta:
        proxy = True

    @classmethod
    def most_recent_past_city_council_meeting(cls):
        if hasattr(settings, 'CITY_COUNCIL_MEETING_NAME'):
            return cls.objects.filter(name__icontains=settings.CITY_COUNCIL_MEETING_NAME)\
                  .filter(start_time__lt=datetime.now()).order_by('-start_time').first()
        else:
            return None
