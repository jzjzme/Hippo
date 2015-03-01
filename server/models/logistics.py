from server import app, db, login_manager



class Address(db.Model):
    id =        db.Column(db.Integer, primary_key=True)

    line_1 = db.Column(db.String(255))
    line_2 = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    zipcode = db.Column(db.String(255))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))



class CreditCard(db.Model):
    id =        db.Column(db.Integer, primary_key=True)

    credit_card_number = db.Column(db.String(16))
    expiration_month = db.Column(db.String(2))
    expiration_year = db.Column(db.String(2))
    security_code = db.Column(db.String(4))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))