from flask import render_template, Blueprint, g, session
from flask.ext.login import current_user

dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard.before_request
def before_request():
    g.user = current_user

@dashboard.route('/')
def index():
    return render_template('dashboard.html', title='Dashboard', user=current_user)

