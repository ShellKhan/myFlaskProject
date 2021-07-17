from flask_combo_jsonapi import ResourceDetail, ResourceList

from ..instruments import db
from ..schemas import UserSchema
from ..models import User


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
    }
