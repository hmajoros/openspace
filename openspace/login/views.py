from flask import render_template, Blueprint, request, redirect, url_for, g, session
from werkzeug import check_password_hash
from flask.ext.login import login_required, login_user, current_user

import os
import mysql.connector

from openspace import login_manager
from openspace.users.models import User


login = Blueprint('login', __name__, url_prefix='/login')

@login_manager.user_loader
def loadUser(user_id):
    db_user = os.environ['DB_USER']
    db_pass = os.environ['DB_PASSWORD']
    db_host = os.environ['DB_HOST']
    db_name = os.environ['DB_NAME']

    conn = mysql.connector.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
    cursor = conn.cursor()
    query = ("SELECT user_id, user_name, user_password, first_name, last_name, email FROM users WHERE user_id = %(user_id)s")
    cursor.execute(query, { 'user_id' : user_id })
    
    row = cursor.fetchone()
    if row is not None:
        u = User(row[0], row[1], row[2], row[3], row[4], row[5])
        return u
    return None

@login.before_request
def before_request():
    g.user = current_user

@login.route('/', methods=['GET', 'POST'])
def index():
    return render_template('login.html', title='login', user=current_user)

@login.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':

        db_user = os.environ['DB_USER']
        db_pass = os.environ['DB_PASSWORD']
        db_host = os.environ['DB_HOST']
        db_name = os.environ['DB_NAME']

        conn = mysql.connector.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
        cursor = conn.cursor()

        query = ("SELECT user_id, user_name, user_password, first_name, last_name, email FROM users WHERE user_name = %(user_name)s")
        cursor.execute(query, { 'user_name': request.form['username'] })
        row = cursor.fetchone()

        if row is not None:
            u = User(row[0], row[1], row[2], row[3], row[4], row[5])
            if check_password_hash(row[2], request.form['password']):
                # log us in
                # print "print before"

                # print u.is_authenticated()

                login_user(u)

                # print "we're logged in!"
                return redirect(url_for('home.index'))

        cursor.close()
        conn.close()
            
    return redirect(url_for('login.index'))

