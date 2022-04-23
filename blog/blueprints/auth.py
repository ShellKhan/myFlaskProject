from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import logout_user, login_user, login_required, current_user
from werkzeug.security import check_password_hash

from blog.forms.auth import UserLoginForm
from blog.models.user import User

auth = Blueprint(
    name='auth',
    import_name=__name__,
    static_folder='../static',
)


# @auth.route('/login', methods=('GET',))
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('user.profile', pk=current_user.id))
# 
#     return render_template('auth/login.html',)
# 
# 
# @auth.route('/login', methods=('POST',))
# def login_post():
#     email = request.form.get('email')
#     password = request.form.get('password')
# 
#     user = User.query.filter_by(email=email).first()
# 
#     if not user or not check_password_hash(user.password, password):
#         flash('Check your login details')
#         return redirect(url_for('.login'))
# 
#     login_user(user)
#     return redirect(url_for('user.profile', pk=user.id))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))

    form = UserLoginForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).one_or_none()
        if (user is None) or (not check_password_hash(user.password, form.password.data)):
            return render_template("auth/login.html", form=form, error="invalid username or password")

        login_user(user)
        return redirect(url_for('user.profile', pk=current_user.id))

    return render_template("auth/login.html", form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))
