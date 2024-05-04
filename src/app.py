import json
from db import db
from flask import Flask, request

from db import User, Skill

app = Flask(__name__)
db_filename = "cms.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()

# -------------------------- GENERALIZED RESPONSES ----------------------------

def success_response(data, code=200):
    return json.dumps(data), code

def failure_response(message, code=404):
    return json.dumps({"error": message}), code

# ----------------------------- USER ENDPOINTS --------------------------------

# get all users
@app.route("/api/users/")
def get_all_users():
    return

# create a user
@app.route("/api/users/", methods={"POST"})
def create_user():
    return

# get a specific user
@app.route("/api/users/<int:user_id>/")
def get_user_by_id(user_id):
    return

# delete a specific user
@app.route("/api/users/<int:user_id>/", methods=["DELETE"])
def delete_user_by_id(user_id):
    return

# add/create a skill for a user
@app.route("/api/users/<int:user_id>/skills/", methods={"POST"})
def add_skill_to_user(user_id):
    return

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)