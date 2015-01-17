from flask import render_template, Blueprint, request, redirect, url_for, g, session
from werkzeug import generate_password_hash
import os
import mysql.connector
from flask.ext.login import current_user

signup = Blueprint('signup', __name__, url_prefix='/signup')

@signup.before_request
def before_request():
    g.user = current_user


@signup.route('/', methods=['GET', 'POST'])
def index():
    return render_template('signup.html', title='signup', user=current_user)

@signup.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        email = request.form['email']
        firstname = request.form['firstname']
        lastname = request.form['lastname']

        userExists = doesUserExist(username)

        if userExists:
            script = Markup('$(function() { $("#usernameTaken").addClass("visible"); });')
            return render_template("signup.html", title='Sign Up', injectedJS=script)

        emailExists = doesEmailExist(email)

        if emailExists:
            script = Markup('$(function() { $("#emailTaken").addClass("visible"); });')
            return render_template("signup.html", title='Sign Up', injectedJS=script)

        db_user = os.environ['DB_USER']
        db_pass = os.environ['DB_PASSWORD']
        db_host = os.environ['DB_HOST']
        db_name = os.environ['DB_NAME']

        conn = mysql.connector.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
        cursor = conn.cursor()

        user_id = cursor.lastrowid

        add_user = ("INSERT INTO users "
                    "(user_name, user_password, first_name, last_name, email, user_id) "
                    "VALUES (%s, %s, %s, %s, %s, %s)")
        user = (username, hashed_password, firstname, lastname, email, user_id)

        cursor.execute(add_user, user)
        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for('home.index'))
    return redirect(url_for('signup.index'))

def doesUserExist(username):
    db_user = os.environ['DB_USER']
    db_pass = os.environ['DB_PASSWORD']
    db_host = os.environ['DB_HOST']
    db_name = os.environ['DB_NAME']

    conn = mysql.connector.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
    cursor = conn.cursor()

    query = "SELECT user_name FROM users"

    cursor.execute(query)

    users = [item[0].encode("utf-8") for item in cursor.fetchall()]
    print users

    if username in users:
        cursor.close()
        conn.close()
        return True

    cursor.close()
    conn.close()
    return False

def doesEmailExist(email):
    db_user = os.environ['DB_USER']
    db_pass = os.environ['DB_PASSWORD']
    db_host = os.environ['DB_HOST']
    db_name = os.environ['DB_NAME']

    conn = mysql.connector.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
    cursor = conn.cursor()

    query = "SELECT email FROM users"

    cursor.execute(query)

    emails = [item[0].encode("utf-8") for item in cursor.fetchall()]

    if email in emails:
        cursor.close()
        conn.close()
        return True

    cursor.close()
    conn.close()
    return False
