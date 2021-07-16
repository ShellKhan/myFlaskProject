from flask_admin import Admin

from .views import MyAdminIndexView

admin = Admin(
    name="Blog Admin",
    index_view=MyAdminIndexView(),
    template_mode="bootstrap4"
)