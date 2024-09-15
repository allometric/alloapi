from flask import Flask
import os
from src.config.config import Config
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Declare flask application
app = Flask(__name__)

# Get dev configuration
config = Config().dev_config

# Make app use dev config
app.env = config.ENV

# Set fields for mongodb
app.config['MONGODB_USER'] = os.environ.get('MONGODB_USER')
app.config['MONGODB_PASS'] = os.environ.get('MONGODB_PASS')

# 