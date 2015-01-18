from flask import render_template_string, Blueprint, g, session, request
from flask.ext.login import current_user, login_required

view = Blueprint('create', __name__, url_prefix='/view')

@view.before_request
def before_request():
    g.user = current_user

@view.route('/')
@login_required
def index():
    if request.args.get('page_id') is not None:


        return render_template_string(template, ())
    return redirect(url_for('dashboard.index'))