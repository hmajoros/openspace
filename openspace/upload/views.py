from flask import render_template, Blueprint, g, session
from flask.ext.login import current_user

upload = Blueprint('upload', __name__, url_prefix='/upload')

@upload.before_request
def before_request():
    g.user = current_user

@upload.route('/')
def index():
    return render_template('upload.html', title='Upload', user=current_user)
