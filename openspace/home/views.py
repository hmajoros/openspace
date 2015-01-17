from flask import render_template, Blueprint
import os
import mysql.connector
from mysql.connector import errorcode

from openspace.users.models import User

home = Blueprint('home', __name__)

@home.route('/')
def index():
    cnx = connectToDB()
    users = getUsers(cnx)
    return render_template('home.html', title='Home', user_data=users)

def connectToDB():
    config = {
        'user': os.environ['DB_USER'],
        'password': os.environ['DB_PASSWORD'],
        'host': os.environ['DB_HOST'],
        'database': os.environ['DB_NAME'],
        'raise_on_warnings': True,
    }

    cnx = mysql.connector.connect(**config)
    return cnx

def getUsers(cnx):
    cursor = cnx.cursor()
    cursor.execute("SELECT user_name, user_password, first_name, last_name FROM users")
    
    users = []

    for (user_name, user_password, first_name, last_name) in cursor:
        u = User(user_name, user_password, first_name, last_name)
        users.append(u) 

    return users
