from flask.ext.login import UserMixin

from server import app, db, login_manager



class User(db.Model, UserMixin):
    id =        db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(64), unique=True)
    email =     db.Column(db.String(64), unique=True)
    password =  db.Column(db.String(255))



@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)
