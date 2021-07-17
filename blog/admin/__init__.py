from flask_admin import Admin

from .classes import TagAdminView, MyAdminIndexView, UserAdminView, CustomAdminView
from .. import models
from ..instruments import db

admin = Admin(
    name="Blog Admin",
    index_view=MyAdminIndexView(),
    template_mode="bootstrap4"
)

admin.add_view(TagAdminView(models.Tag, db.session, category="Models"))
admin.add_view(UserAdminView(models.User, db.session, category="Models"))
admin.add_view(CustomAdminView(models.Article, db.session, category="Models"))
