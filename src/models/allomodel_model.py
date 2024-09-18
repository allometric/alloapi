from src import mongo

class AlloModel:
  def __init__(self, collection):
    self.collection = collection

  def get_model(self, id):
    return self.collection.find({"model_id": id})