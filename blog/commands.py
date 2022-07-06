import click
from werkzeug.security import generate_password_hash
from .instruments import db


@click.command('init-db')
def init_db():
    from wsgi import app
    # import models for creating tables
    from blog.models.user import User

    db.create_all(app=app)


@click.command('create-init-user')
def create_init_user():
    from blog.models.user import User
    from wsgi import app

    with app.app_context():
        db.session.add(
            User(email='example@example.com', password=generate_password_hash('12345'))
        )
        db.session.commit()
