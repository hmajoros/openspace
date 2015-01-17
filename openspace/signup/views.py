from flask import render_template, Blueprint, request
from openspace.users.models import User
from werkzeug import generate_password_hash
import mysql.connector

signup = Blueprint('signup', __name__, url_prefix='/signup')

@signup.route('/', methods=['GET', 'POST'])
def index():
    return render_template('signup.html', title='signup')

@signup.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST'
    username = request.form['username']
    password = request.form['password']
    hashed_password = generate_password_hash(password)
    email = request.form['email']

    conn = connectToDB()
    cursor = conn.cursor()

    add_user = ("INSERT INTO users "
                "(user_name, user_password, first_name, last_name, email) "
                "VALUES (%s, %s, %s, %s, %s)")
    user = (username, hashed_password, 

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
