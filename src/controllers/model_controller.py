from src import app, config
from flask import Blueprint, request, jsonify
from bson.json_util import dumps, loads
from src import mongo

models = Blueprint("models", __name__)

descriptor_keys = ["country", "region"]
taxa_keys = ["family", "genus", "species"]

def listify(request_args):
  """Ensures each argument is wrapped in a list if it isn't already

  Args:
      request_args (_type_): _description_
  """

  for key in request_args:
    request_args[key] = request_args[key].split(',')

  return request_args

def build_models_filter(request_args):
  """Builds a mongo filter from user provided query parameters

  This function takes arguments specified in a GET request and structures them
  into the proper format for `Collection.find`. More specifically, the user is
  free to provide `model_id`, `country`, `region` [etc] query parameters, and
  this function maps them appropriately to the structure of the `model`
  documents in the database.

  Args:
      request_args (_type_): _description_
  """
  defined_keys = request_args.keys()
  find_obj = {}

  for key in defined_keys:
    if key in descriptor_keys:
      key_fmt = "descriptors." + key
    elif key in taxa_keys:
      key_fmt = "descriptors.taxa." + key
    elif key == "response":
      key_fmt = "response.name"
    elif key == "covariates":
      key_fmt = "covariates.name"
    else:
      key_fmt = key
    
    find_obj[key_fmt] = {
      "$in": request_args[key]
    }

  return find_obj

@models.route("/", methods = ["GET"])
def get_models():
  # Makes our arguments mutable
  args_dict = dict(request.args)

  listified_args = listify(args_dict)
  filter = build_models_filter(listified_args)

  res = mongo.db.models.find(filter, limit = config.MODEL_LIMIT)
  listed = list(res)

  for doc in listed:
    if '_id' in doc:
      doc['_id'] = str(doc['_id'])

  return jsonify(listed)