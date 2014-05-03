from app import db

class User(db.Model):
    id = db.Column(db.String(6), primary_key = True)
    password = db.Column(db.String(10))
    role = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % (self.id)

    def get_id(self):
        return unicode(self.id)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False


class LostProp(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String)
    type = db.Column(db.String)
    colour = db.Column(db.String)
    borough = db.Column(db.String)
    loser_postcode = db.Column(db.String)
    street = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    telephone = db.Column(db.String)
    email = db.Column(db.String)
    address = db.Column(db.String)
    postcode = db.Column(db.String)
    city = db.Column(db.String)
    status = db.Column(db.String)

    def __repr__(self):
        return '<LostProp %r>' % (self.description)

class Types(db.Model):
    type = db.Column(db.String, primary_key = True)
    number = db.Column(db.Integer)

    def __repr__(self):
        return '<Type %r>' % (self.type)

class FoundProp(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String)
    type = db.Column(db.String)
    colour = db.Column(db.String)
    borough = db.Column(db.String)
    finder_postcode = db.Column(db.String)
    street = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    telephone = db.Column(db.String)
    email = db.Column(db.String)
    police = db.Column(db.Integer)
    address = db.Column(db.String)
    postcode = db.Column(db.String)
    city = db.Column(db.String)
    status = db.Column(db.String)

    def __repr__(self):
        return '<LostProp %r>' % (self.description)