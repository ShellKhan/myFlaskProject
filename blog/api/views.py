from flask import Blueprint

from ..instruments import csrf, api

api_blueprint = Blueprint('api', __name__)
csrf.exempt(api_blueprint)
