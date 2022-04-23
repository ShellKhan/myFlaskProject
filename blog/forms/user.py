from flask_wtf import FlaskForm
from wtforms import validators, StringField, PasswordField, SubmitField


class UserRegisterForm(FlaskForm):
    email = StringField('Почтовый адрес', [
        validators.DataRequired(),
        validators.Email(),
    ])
    name = StringField('Имя')
    password = PasswordField('Пароль', [
        validators.DataRequired(),
        validators.Length(min=8),
    ])
    confirm = PasswordField('Повторите пароль', [
        validators.DataRequired(),
        validators.EqualTo('password', message="Passwords must match"),
    ])
    submit = SubmitField('Зарегистрировать')
