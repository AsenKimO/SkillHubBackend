import json
from db import db
from flask import Flask, request

from db import User, Product

app = Flask(__name__)
db_filename = "skillhub.db"

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
    return success_response({"users": [u.simple_ser() for u in User.query.all()]})

# create a user
@app.route("/api/users/", methods={"POST"})
def create_user():
    body = json.loads(request.data)

    # check for bad request
    name = body.get("name")
    title = body.get("title")
    email = body.get("email")
    website = body.get("website")
    image_url = body.get("image_url")
    if not (name and title and email and website and image_url):
        return failure_response("User field(s) not provided", 400)

    new_user = User(
        name = name,
        title = title,
        email = email,
        website = website,
        image_url = image_url
    )

    db.session.add(new_user)
    db.session.commit()
    return success_response(new_user.serialize(), 201)

# get a specific user
@app.route("/api/users/<int:user_id>/")
def get_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()

    # case if user does not exist in db
    if not user:
        return failure_response("User not found")
    
    return success_response(user.serialize())

# delete a specific user
@app.route("/api/users/<int:user_id>/", methods=["DELETE"])
def delete_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()

    # case if user does not exist in db
    if not user:
        return failure_response("User not found")
    
    # delete
    db.session.delete(user)
    db.session.commit()
    return success_response(user.serialize())

# add/create a product for a user
@app.route("/api/users/<int:user_id>/products/", methods={"POST"})
def add_product_for_user(user_id):
    body = json.loads(request.data)
    user = User.query.filter_by(id=user_id).first()
    
    # case if user does not exist in db
    if not user:
        return failure_response("User not found")
    
    # check for bad request
    name = body.get("name")
    price = body.get("price")
    description = body.get("description")
    if not (name and price and description):
        return failure_response("Product field(s) not provided", 400)
    
    # create product
    product = Product(
        name = name,
        price = price,
        description = description,
        user_id = user_id
    )
    
    # update list of products of user at user_id
    db.session.add(product)
    db.session.commit()

    # add course of assignment JSON
    productJSON = product.serialize()
    productJSON["user"] = user.simple_ser()

    return success_response(productJSON, 201)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)