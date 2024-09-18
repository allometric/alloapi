from flask import Blueprint
from src.controllers.model_controller import models

# main blueprint to be registered with application
api = Blueprint('api', __name__)

# register user with api blueprint
api.register_blueprint(models, url_prefix="/models")