from combojsonapi.event.resource import EventsResource
from flask_combo_jsonapi import ResourceDetail, ResourceList

from ..instruments import db
from ..schemas import TagSchema
from ..models import Tag


class TagEvents(EventsResource):

    def event_get_tag_count(self, *args, **kwargs):
        return {'count': Tag.query.count()}

    def event_get_tag_ugu(self, *args, **kwargs):
        return {'ugu': 'UGU!'}


class TagList(ResourceList):
    events = TagEvents
    schema = TagSchema
    data_layer = {
        "session": db.session,
        "model": Tag,
    }


class TagDetail(ResourceDetail):
    events = TagEvents
    schema = TagSchema
    data_layer = {
        "session": db.session,
        "model": Tag,
    }
