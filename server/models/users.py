from flask.ext.login import UserMixin

from server.models.logistics import Address, CreditCard

from server import app, db, login_manager



class User(db.Model, UserMixin):
    id =        db.Column(db.Integer, primary_key=True)

    username =  db.Column(db.String(64), unique=True)
    email =     db.Column(db.String(64), unique=True)
    password =  db.Column(db.String(255))

    address = db.relationship('Address', backref='user', uselist=False)
    creditcard = db.relationship('CreditCard', backref='user', uselist=False)


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)
