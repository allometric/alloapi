from src import app
from flask import Blueprint, request, jsonify
from bson.json_util import dumps, loads
from src import mongo

models = Blueprint("models", __name__)

@models.route("/", methods = ["GET"])
def get_models():
  model_id = request.args.get("model_id")
  res = mongo.db.models.find({"model_id": model_id})
  listed = list(res)

  for doc in listed:
    if '_id' in doc:
      doc['_id'] = str(doc['_id'])

  return jsonify(listed)