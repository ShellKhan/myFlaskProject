from flask import Flask, render_template
from .instruments import db, login_manager, migrate, csrf
from .models.user import User
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

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app):
    from .blueprints.auth import auth
    from .blueprints.person import person
    from .blueprints.report import report
    from .blueprints.user import user

    app.register_blueprint(auth)
    app.register_blueprint(person)
    app.register_blueprint(report)
    app.register_blueprint(user)


def register_commands(app):
    app.cli.add_command(commands.create_init_user)
