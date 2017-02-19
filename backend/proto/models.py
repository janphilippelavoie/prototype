from proto import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), unique=True)
    password = db.Column(db.String(), unique=False)

    def __init__(self, email, password):
        self.email = email.lower()
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.email
