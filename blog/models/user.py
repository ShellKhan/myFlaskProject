from flask_login import UserMixin
from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash

from ..instruments import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    password = db.Column(db.String(255), unique=True, nullable=False)
    is_staff = db.Column(db.Boolean, nullable=False, default=False)

    author = relationship('Author', uselist=False, back_populates='user')

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)
