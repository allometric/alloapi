import os
from dotenv import load_dotenv

if 'GITHUB_ACTIONS' not in os.environ:
  load_dotenv()

class ProductionConfig:
  def __init__(self):
    self.ENV = "production"
    self.DEBUG = False
    self.PORT = 80
    self.HOST = '0.0.0.0'
    self.MODEL_LIMIT = 50
    self.MONGODB_URI = os.getenv("MONGODB_URL")
    self.DB_NAME = "allodata"