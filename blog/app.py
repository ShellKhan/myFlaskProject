from flask import Flask, render_template

from .admin import admin
from .instruments import db, login_manager, migrate, csrf
from .blueprints import auth, user, author, article
from .models import User
from . import commands


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('blog.configs')

    @app.route("/")
    def index():
        return render_template("index.html")

    register_instruments(app)
    register_blueprints(app)
    register_commands(app)
    return app


def register_instruments(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    csrf.init_app(app)
    admin.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app):
    app.register_blueprint(auth)
    app.register_blueprint(user)
    app.register_blueprint(author)
    app.register_blueprint(article)


def register_commands(app):
    app.cli.add_command(commands.create_init_user)
    app.cli.add_command(commands.create_tags)
