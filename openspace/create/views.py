from flask import render_template_string, Blueprint, g, session
from flask.ext.login import current_user

create = Blueprint('create', __name__, url_prefix='/create')

@create.before_request
def before_request():
    g.user = current_user

@create.route('/')
def index():

    title = "cool" 
    text = "wow"
 

    return render_template_string("{{ title }} is cool! So if {{ text }}", **context)