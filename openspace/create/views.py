from flask import render_template, Blueprint, g, session
from flask.ext.login import current_user

create = Blueprint('create', __name__, url_prefix='/create')

@create.before_request
def before_request():
    g.user = current_user

@create.route('/')
def index():
    return render_template('create.html', title='Create', user=current_user)