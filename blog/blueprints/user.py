from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound
from blog.models.user import User

user = Blueprint(
    name='user',
    import_name=__name__,
    static_folder='../static',
    url_prefix='/users',
)


@user.route('/')
def user_list():
    users = User.query.all()
    return render_template('users/list.html',users=users)


@user.route('/<int:pk>')
@login_required
def profile(pk: int):
    selected_user = User.query.filter_by(id=pk).one_or_none()
    if not selected_user:
        raise NotFound(f"User #{pk} doesn't exist!")

    return render_template('users/profile.html',user=selected_user)
