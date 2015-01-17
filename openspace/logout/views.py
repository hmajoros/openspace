from flask import render_template, Blueprint, redirect, url_for, g, session
from openspace import login_manager
from flask.ext.login import login_required, logout_user, current_user

logout = Blueprint('logout', __name__, url_prefix='/logout')

@logout.before_request
def before_request():
    g.user = current_user

@logout.route('/')
@login_required
def index():
    logout_user()
    return redirect(url_for('home.index'))




