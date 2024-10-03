import pytest
from . import app

@pytest.fixture
def client():
  with app.test_client() as client:
    yield client

def pytest_sessionstart(session):
  # Set up test database with data
  models = app.db['models']

  models.insert_one({
    "_id": "aaaaaaa",
    "descriptors": {
      "region": ["US-OR", "US-WA"]
    }
  })

  models.insert_one({
    "_id": "bbbbbbb",
    "descriptors": {
      "region": ["US-WA"]
    }
  })


def pytest_sessionfinish(session, exitstatus):
  models = app.db['models']
  models.drop()