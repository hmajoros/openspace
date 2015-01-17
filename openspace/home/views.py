from flask import render_template, Blueprint
import os
import mysql.connector
from mysql.connector import errorcode

home = Blueprint('home', __name__)

@home.route('/')
def index():
    connectToDB()
    return render_template('home.html', title='Home')

def connectToDB():
    config = {
        'user': os.environ['DB_USER'],
        'password': os.environ['DB_PASSWORD'],
        'host': os.environ['DB_HOST'],
        'database': os.environ['DB_NAME'],
        'raise_on_warnings': True,
    }

    cnx = mysql.connector.connect(**config)
    cnx.close()
