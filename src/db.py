from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# ------------------------------ USER MODEL -----------------------------------

class User(db.Model):
    """
    User Model
    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = False)
    title = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False)
    website = db.Column(db.String, nullable = False)
    image_url = db.Column(db.String, nullable = False)
    products = db.relationship("Product", cascade="delete")

    def __init__(self, **kwargs):
        """
        Initialize User object/entry
        """
        self.name = kwargs.get("name", "")
        self.title = kwargs.get("title", "")
        self.email = kwargs.get("email", "")
        self.website = kwargs.get("website", "")
        self.image_url = kwargs.get("image_url", "")

    def serialize(self):
        """
        Serialize a User object
        """
        return {
            "id": self.id,
            "name": self.name,
            "title": self.title,
            "email": self.email,
            "website": self.website,
            "image_url": self.image_url,
            "products": [p.serialize() for p in self.products]
        }
    
    def simple_ser(self):
        """
        Simple serialization
        """
        return{
            "id": self.id,
            "name": self.name,
            "title": self.title,
            "email": self.email,
            "website": self.website,
            "image_url": self.image_url
        }

# ------------------------------ SKILL MODEL ----------------------------------

class Product(db.Model):
    """
    Product Model
    """
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = False)
    price = db.Column(db.Float, nullable = False)
    description = db.Column(db.String, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)

    def __init__(self, **kwargs):
        """
        Initialize Product object/entry
        """
        self.name = kwargs.get("name", "")
        self.price = kwargs.get("price", 0.)
        self.description = kwargs.get("description", "")
        self.user_id = kwargs.get("user_id")

    def serialize(self):
        """
        Serialize an Product object
        """
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "description": self.description
        }