from flask import render_template, Blueprint, request, redirect, url_for
from werkzeug import check_password_hash

import os
import mysql.connector

from openspace import login_manager
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

        query = ("SELECT user_name, user_password FROM users WHERE user_name = %(user_name)s")
        cursor.execute(query, { 'user_name': request.form['username'] })
        row = cursor.fetchone()

        if row is not None:
            if check_password_hash(row[1], request.form['password']):
                return redirect(url_for('home.index'))

        cursor.close()
        conn.close()
            
    return redirect(url_for('login.index'))

