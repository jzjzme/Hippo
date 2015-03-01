from flask.ext.login import UserMixin

from server import app, db, login_manager



class Food(db.Model):
    title = db.Column(db.String(255))
    price = db.Column(db.Float)
    