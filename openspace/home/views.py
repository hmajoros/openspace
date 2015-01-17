from flask import render_template, Blueprint

home = Blueprint('home', __name__)

@home.route('/')
def index():
    return render_template('home.html', title='home')




