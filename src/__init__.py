from flask import Flask, current_app
from flask_cors import CORS
import os
from src.config.config import Config
from dotenv import load_dotenv
from flask_pymongo import PyMongo
from src.routes import api

mongo = PyMongo()

def create_app(config):
  # Declare flask application
  app = Flask(__name__)

  CORS(
    app,
    resources={r"/*": {"origins": "http://localhost:5174"}}
  )

  if config == "dev":
    config = Config().dev_config
  elif config == "production":
    config = Config().production_config
  elif config == "test":
    config = Config().test_config

  # Make app use dev config
  app.env = config.ENV

  # Set the URI and DB NAME in the config
  app.config['MONGO_URI'] = config.MONGODB_URI
  app.config['DB_NAME'] = config.DB_NAME

  app.config['HOST'] = config.HOST
  app.config['PORT'] = config.PORT
  app.config['DEBUG'] = config.DEBUG

  app.config['MODEL_LIMIT'] = config.MODEL_LIMIT

  mongo.init_app(app)

  app.register_blueprint(api)

  db = mongo.cx[app.config['DB_NAME']]

  setattr(app, 'db', db)

  return app