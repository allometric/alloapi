from flask import Blueprint, request, jsonify, current_app, abort
from bson.json_util import dumps, loads

models = Blueprint("models", __name__)
model = Blueprint("model", __name__)

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

def dictify(request_args):
  args_dict = {}

  for key in request_args:
    args_dict[key] = request_args.getlist(key)

  return args_dict

def get_pub_doc(pub_id):
  filter = {"_id": pub_id}
  res = current_app.db.publications.find(filter)

  listed = list(res)

  if len(listed) > 1:
    abort(500, "More than one publication found with this id")

  pub_doc = listed[0]

  return pub_doc

@models.route("/", methods = ["POST"])
def get_models():
  filter = request.json

  # TODO sanitize filter
  res = current_app.db.models.find(
    filter, limit = current_app.config['MODEL_LIMIT']
  )

  listed = list(res)

  citation_arg = request.args.get("citation")

  for doc in listed:
    if '_id' in doc:
      doc['_id'] = str(doc['_id'])

    if citation_arg == "true":
      pub_doc = get_pub_doc(doc['pub_id'])
      doc['citation'] = pub_doc['citation']

  return jsonify(listed)


@model.route("/<model_id>", methods = ["GET"])
def get_model(model_id):
  filter = {"_id": model_id}
  res = current_app.db.models.find(filter)

  listed = list(res)

  if len(listed) > 1:
    abort(500, "More than one model found with this id")
  
  model_doc = listed[0]
  model_doc['_id'] = str(model_doc['_id'])

  citation_arg = request.args.get("citation")

  if citation_arg == "true":
    pub_id = model_doc['pub_id']
    pub_doc = get_pub_doc(pub_id)

    model_doc['citation'] = pub_doc['citation']

  return jsonify(model_doc)