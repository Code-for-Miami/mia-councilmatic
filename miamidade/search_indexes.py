from councilmatic_core.haystack_indexes import BillIndex
from haystack import indexes
from miamidade.models import MiamiDadeBill
from datetime import datetime
from django.conf import settings
import pytz

app_timezone = pytz.timezone(settings.TIME_ZONE)

class MiamiDadeBillIndex(BillIndex, indexes.Indexable):

    topics = indexes.MultiValueField(faceted=True)

    def get_model(self):
        return MiamiDadeBill

    def prepare(self, obj):
        data = super(MiamiDadeBillIndex, self).prepare(obj)
        
        boost = 0
        if obj.last_action_date:
            now = app_timezone.localize(datetime.now())

            # obj.last_action_date can be in the future
            weeks_passed = (now - obj.last_action_date).days / 7 + 1
            boost = 1 + 1.0 / max(weeks_passed, 1)

        data['boost'] = boost

        return data

    def prepare_topics(self, obj):
        return obj.topics
