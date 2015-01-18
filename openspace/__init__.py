from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

# literally serves no purpose ?????
app.secret_key = "420blazeityoloswagfuck"

db = SQLAlchemy(app)

# login stuff below
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login.auth'

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

# setup create page 
from openspace.create.views import create
app.register_blueprint(create)

# setup upload blueprint
from openspace.upload.views import upload
app.register_blueprint(upload)

# setup dashboard blueprint
from openspace.dashboard.views import dashboard
app.register_blueprint(dashboard)
