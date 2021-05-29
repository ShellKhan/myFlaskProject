from flask_login import UserMixin
from blog.instruments import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = password
