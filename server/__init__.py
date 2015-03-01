from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager



# Flask app
app = Flask(__name__)



# Load config
app.config.from_object('server.serversettings')



# Plugins and extensions
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)



# App contents
from server.models import *
from server.api import *
from server.servefront import *


# Create db
db.create_all()
