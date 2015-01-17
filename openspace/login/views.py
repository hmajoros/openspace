from flask import render_template, Blueprint

login = Blueprint('login', __name__, url_prefix='/login')

@login.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html', title='login')



