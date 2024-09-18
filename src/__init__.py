from flask import Flask
import os
from src.config.config import Config
from dotenv import load_dotenv
from flask_pymongo import PyMongo

# Load environment variables
load_dotenv()

# Declare flask application
app = Flask(__name__)

# Get dev configuration
config = Config().dev_config

# Make app use dev config
app.env = config.ENV

# Set fields for mongodb
mongo_user = os.environ.get('MONGODB_USER')
mongo_pass = os.environ.get('MONGODB_PASS')

# Create the URI
mongo_uri = "mongodb+srv://{}:{}@allocluster.81k2sis.mongodb.net/allodata?retryWrites=true&w=majority&appName=AlloCluster".format(mongo_user, mongo_pass)

# Set the URI in the config
app.config['MONGO_URI'] = mongo_uri

print(mongo_uri)

mongo = PyMongo(app)

from src.routes import api
app.register_blueprint(api, url_prefix = "/api")

from src.models.allomodel_model import AlloModel