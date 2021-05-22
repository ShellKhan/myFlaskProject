from flask import Flask, render_template
from .blueprints.report import report
from .blueprints.person import person
from .models.database import db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/blog.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    @app.route("/")
    def index():
        return render_template("index.html")

    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(person)
    app.register_blueprint(report)
