from flask import render_template, Blueprint, g, session
from flask.ext.login import current_user
# import os
# import mysql.connector
# from mysql.connector import errorcode

# from openspace.users.models import User

home = Blueprint('home', __name__)

@home.before_request
def before_request():
    g.user = current_user

@home.route('/')
def index():
    return render_template('home.html', title='Home', user=current_user)

# def connectToDB():
#     config = {
#         'user': os.environ['DB_USER'],
#         'password': os.environ['DB_PASSWORD'],
#         'host': os.environ['DB_HOST'],
#         'database': os.environ['DB_NAME'],
#         'raise_on_warnings': True,
#     }

#     cnx = mysql.connector.connect(**config)
#     return cnx

# def getUsers(cnx):
#     cursor = cnx.cursor()
#     cursor.execute("SELECT user_name, user_password, first_name, last_name FROM users")
    
#     users = []

#     for (user_name, user_password, first_name, last_name) in cursor:
#         u = User(user_name, user_password, first_name, last_name)
#         users.append(u) 

#     return users
