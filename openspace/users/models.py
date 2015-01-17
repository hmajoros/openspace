from werkzeug import generate_password_hash, check_password_hash
from flask_login import UserMixin

from openspace import db

class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(255), unique=True)
    user_password = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255))

    def __init__(self, user_id=None, user_name=None, user_password=None, first_name=None, last_name=None, email=None):
        self.active = True
        self.auth = False
        self.user_id = user_id
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.user_password = generate_password_hash(user_password)
    
    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def check_password(self, password):
        return check_password_hash(self.user_password, password)

    def get_user_name(self):
        return self.user_name

    def get_user_first_name(self):
        return self.first_name

    def get_user_last_name(self):
        return self.last_name

    def get_user_password(self):
        return self.user_password

    def get_id(self):
        return self.user_id


