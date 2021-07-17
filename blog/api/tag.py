from flask_combo_jsonapi import ResourceDetail, ResourceList

from ..instruments import db
from ..schemas import TagSchema
from ..models import Tag


class TagList(ResourceList):
    schema = TagSchema
    data_layer = {
        "session": db.session,
        "model": Tag,
    }


class TagDetail(ResourceDetail):
    schema = TagSchema
    data_layer = {
        "session": db.session,
        "model": Tag,
    }
