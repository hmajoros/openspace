from flask import render_template, Blueprint

logout = Blueprint('logout', __name__, url_prefix='/logout')

@logout.route('/')
def index():
    return render_template('home.html', title='logout')




