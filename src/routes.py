from flask import Blueprint
from src.controllers.model_controller import models, model
from src.controllers.summary_controller import summary

# main blueprint to be registered with application
api = Blueprint('api', __name__)

# register user with api blueprint
api.register_blueprint(models, url_prefix="/models")
api.register_blueprint(model, url_prefix="/model")
api.register_blueprint(summary, url_prefix="/summary")