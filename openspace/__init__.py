from flask import Flask
from flask.ext.login import LoginManager

app = Flask(__name__)

# # login stuff below
# lm = LoginManager()
# lm.init_app(app)
# lm.login_view = 'login.index'

# setup home blueprint
from openspace.home.views import home
app.register_blueprint(home)

# setup login blueprint
from openspace.login.views import login
app.register_blueprint(login)

# setup logout blueprint
from openspace.logout.views import logout
app.register_blueprint(logout)

# setup signup blueprint
from openspace.signup.views import signup
app.register_blueprint(signup)

# create page
from openspace.create.views import create
app.register_blueprint(create)