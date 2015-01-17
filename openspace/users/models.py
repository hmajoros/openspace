# from flask_login import UserMixin
# 
# from werkzeug import generate_password_hash, check_password_hash
# 
# from app import db
# 
# class User(db.model, UserMixin)
#     user_id = db.Column(db.Integer, primary_key=True)
#     user_name = db.Column(db.String(120), unique=True)
#     user_password = db.Column(db.String(120))
#     first_name = db.Column(db.String(120))
#     last_name = db.Column(db.String(120))
#     birthdate = db.Column(db.String(120))
# 
#     def __init__(self, user_id=None, user_name=None, user_password=None, first_name=None, last_name=None, birthday=None):
#         self.active = False
#         self.user_id = user_id
#         self.user_name = user_name
#         self.first_name = first_name
#         self.last_name = last_name
#     
#     def is_active(self):
#         return self.active
# 
#     def set_password(self, _password):
#         self.password = generate_password_hash(_password)
# 
#     def check_password(self, _password):
#         if check_password_hash(self.password, _password):
#                 self.active = True
# 
#     def get_user_id(self):
#         return self.user_id
#         
