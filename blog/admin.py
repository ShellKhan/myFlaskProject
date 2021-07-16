from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for
from flask_login import current_user

from . import models
from .instruments import db


class MyAdminIndexView(AdminIndexView):

    @expose("/")
    def index(self):
        if not (current_user.is_authenticated and current_user.is_staff):
            return redirect(url_for("auth.login"))
        return super().index()


class CustomView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_staff

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("auth.login"))


class TagAdminView(CustomView):
    column_searchable_list = ("name",)
    column_filters = ("name",)
    can_export = True
    export_types = ["csv", "xlsx"]
    create_modal = True
    edit_modal = True


class UserAdminView(CustomView):
    column_exclude_list = ("password",)
    column_searchable_list = ("firstname", "lastname", "is_staff", "email")
    column_filters = ("firstname", "lastname", "is_staff", "email")
    column_editable_list = ("firstname", "lastname", "is_staff")
    can_create = True
    can_edit = True
    can_delete = False


admin = Admin(name="Blog Admin", index_view=MyAdminIndexView(), template_mode="bootstrap4")

admin.add_view(TagAdminView(models.Tag, db.session, category="Models"))
