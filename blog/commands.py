import click
from werkzeug.security import generate_password_hash
from .instruments import db
from .models import User, Tag


@click.command('create-init-user')
def create_init_user():
    from wsgi import app

    with app.app_context():
        db.session.add(
            User(
                email='admin',
                firstname='Admin',
                lastname='Adminov',
                password=generate_password_hash('123'),
                is_staff=True
            )
        )
        db.session.commit()


@click.command("create-tags")
def create_tags():
    from wsgi import app

    with app.app_context():
        for name in [
            "flask",
            "django",
            "python",
            "sqlalchemy",
            "news",
            "gb",
            "sqlite",
        ]:
            tag = Tag(name=name)
            db.session.add(tag)
        db.session.commit()
