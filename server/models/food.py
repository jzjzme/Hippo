from server import app, db, login_manager



foodtagtable = db.Table('foodtagtable',
    db.Column('food_tag_id', db.Integer, db.ForeignKey('food_tag.id')),
    db.Column('food_entry_id', db.Integer, db.ForeignKey('food_entry.id'))
)

class FoodEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255))
    details = db.Column(db.Text)
    nutrition = db.Column(db.Text)
    ingredients = db.Column(db.Text)

    active = db.Column(db.Boolean, default=False)

    upvotes = db.Column(db.Integer, default=0)
    downvotes = db.Column(db.Integer, default=0)

    imageurl_icon = db.Column(db.String(255))
    imageurl_full = db.Column(db.String(255))

    price = db.Column(db.Float)

    tags = db.relationship('FoodTag', secondary=foodtagtable, backref=db.backref('food_entries', lazy='dynamic'))

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))



foodtagusertable = db.Table('foodtagusertable',
    db.Column('food_tag_id', db.Integer, db.ForeignKey('food_tag.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

class FoodTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255))

    tags = db.relationship('User', secondary=foodtagusertable, backref=db.backref('food_tags', lazy='dynamic'))



class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255))
    details = db.Column(db.Text)

    neighborhood_id = db.Column(db.Integer, db.ForeignKey('neighborhood.id'))

    food_entries = db.relationship('FoodEntry', backref='restaurant', lazy='dynamic')



class Neighborhood(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255))
    zipcode = db.Column(db.String(5))

    restaurants = db.relationship('Restaurant', backref='neighborhood', lazy='dynamic')
