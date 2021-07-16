from . import admin
from .views import UserAdminView, TagAdminView, CustomView
from .. import models

admin.add_view(TagAdminView(models.Tag, db.session, category="Models"))
admin.add_view(CustomView(models.Article, db.session, category="Models"))
admin.add_view(UserAdminView(models.User, db.session, category="Models"))