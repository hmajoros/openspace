from flask import render_template, Blueprint

signup = Blueprint('signup', __name__, url_prefix='/signup')

@signup.route('/', methods=['GET', 'POST'])
def index():
    return render_template('signup.html', title='signup')


