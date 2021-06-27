import click
from werkzeug.security import generate_password_hash
from .instruments import db


@click.command('create-init-user')
def create_init_user():
    from .models.user import User
    from wsgi import app

    with app.app_context():
        db.session.add(
            User(
                email='example@example.com',
                firstname='admin',
                password=generate_password_hash('123'),
                is_staff=True
            )
        )
        db.session.commit()
