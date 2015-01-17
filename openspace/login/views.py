from flask import render_template, Blueprint, request, redirect, url_for
from werkzeug import check_password_hash

import os
import mysql.connector

from openspace.users.models import User


login = Blueprint('login', __name__, url_prefix='/login')

@login.route('/', methods=['GET', 'POST'])
def index():
    return render_template('login.html', title='login')

@login.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':

        db_user = os.environ['DB_USER']
        db_pass = os.environ['DB_PASSWORD']
        db_host = os.environ['DB_HOST']
        db_name = os.environ['DB_NAME']

        conn = mysql.connector.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
        cursor = conn.cursor()

        query = ("SELECT user_name, user_password FROM users WHERE user_name = '%s'")
        
        cursor.execute(query, request.form['username'])

        if cursor is not None:
            for (user_name, user_password) in cursor:
                u = User(user_name, user_password)

        # TODO: Nothing works!@@~~~!~!@~!
        # need an if statement here to check if the user password in database matches password submitted in form

        # somthing like these maybe???
        # if  user.check_password(request.form['password']):
        # if check_password_hash(u.get_user_password, request.form['password']):

        cursor.close()
        conn.close()

        return redirect(url_for('login.index'))
            
    return redirect(url_for('login.index'))

# def getPassHash(username):
#     db_user = os.environ['DB_USER']
#     db_pass = os.environ['DB_PASSWORD']
#     db_host = os.environ['DB_HOST']
#     db_name = os.environ['DB_NAME']

#     cnx = mysql.connector.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
#     cursor = cnx.cursor()
#     query = ("SELECT user_password FROM users WHERE user_name = %s")

#     cursor.execute(query, username)

#     for (user_password) in cursor:
#         hashpass = user_password

#     cursor.close()
#     cnx.close()

#     return hashpass


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
