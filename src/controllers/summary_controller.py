from flask import Blueprint, request, jsonify, current_app, abort

summary = Blueprint("summary", __name__)

@summary.route("/<summary_id>", methods = ["GET"])
def get_summary(summary_id):
  filter = {"_id": summary_id}
  res = current_app.db.summary.find(filter)

  listed = list(res)

  if len(listed) > 1:
    abort(500, "More than one summary found with this id")
  
  summary_doc = listed[0]
  summary_doc['_id'] = str(summary_doc['_id'])

  return jsonify(summary_doc)