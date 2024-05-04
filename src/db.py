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
    username = db.Column(db.String, nullable = False)
    password = db.Column(db.String, nullable = False)
    rating = db.Column(db.Float, nullable = False)
    skills = db.relationship("Skill", cascade="delete")

    def __init__(self, **kwargs):
        """
        Initialize User object/entry
        """
        self.name = kwargs.get("name", "")
        self.username = kwargs.get("username", "")
        self.password = kwargs.get("password", "")
        self.rating = kwargs.get("rating", 0.)

    def serialize(self):
        """
        Serialize a User object
        """
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "password": self.password,
            "skills": [s.serialize() for s in self.skills]
        }
    
    def simple_ser(self):
        """
        Simple serialization
        """
        return{
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "password": self.password
        }

# ------------------------------ SKILL MODEL ----------------------------------

class Skill(db.Model):
    """
    Skill Model
    """
    __tablename__ = "skills"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    skill_name = db.Column(db.String, nullable = False)
    difficulty = db.Column(db.Integer, nullable = False)
    estimate_payrate = db.Column(db.Float, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)

    def __init__(self, **kwargs):
        """
        Initialize Skill object/entry
        """
        self.skill_name = kwargs.get("skill_name", "")
        self.difficulty = kwargs.get("difficulty", 0)
        self.estimate_payrate = kwargs.get("estimate_payrate", 0.)
        self.user_id = kwargs.get("user_id")

    def serialize(self):
        """
        Serialize an Skill object
        """
        return {
            "id": self.id,
            "skill_name": self.skill_name,
            "difficulty": self.difficulty,
            "estimate_payrate": self.estimate_payrate
        }