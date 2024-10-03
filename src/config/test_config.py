import os
from dotenv import load_dotenv

if 'GITHUB_ACTIONS' not in os.environ:
  load_dotenv()

class TestConfig:
  def __init__(self):
    self.ENV = "test"
    self.DEBUG = True
    self.PORT = 3000
    self.HOST = '0.0.0.0'
    self.MODEL_LIMIT = 50
    self.MONGODB_URI = os.getenv("MONGODB_URL_DEV")
    self.DB_NAME = "test"