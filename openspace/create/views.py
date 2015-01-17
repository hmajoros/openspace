from flask import render_template, Blueprint

create = Blueprint('create', __name__, url_prefix='/create')

@create.route('/')
def index():
    return render_template('create.html', title='Create')