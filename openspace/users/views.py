from flask import render_template, flash, redirect, \
    request, g, session, Blueprint, url_for
from flask.ext.login import login_required, login_user, logout_user, current_user

from app import lm

from app.users.models import User

users = Blueprint('users', __name__, url_prefix='/users')

@lm.user_loader
def loadUser(user):
    return User.query.get(int(user))

@users.before_request
def before_request():
    g.user = current_user

@users.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        user.check_passwd(request.form['password'])
        if user and user.is_active():
            print 0
            login_user(user)
            print 0
            return redirect(url_for('home.index'))
    return redirect(url_for('home.login'))
    

@users.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.index'))
