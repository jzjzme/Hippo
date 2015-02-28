from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy



# Flask app
app = Flask(__name__)



# Load config
app.config.from_object('server.serversettings')



# Plugins and extensions
db = SQLAlchemy(app)



# App contents



# Create db
db.create_all()
