import proto


class User(proto.db.Model):
    id = proto.db.Column(proto.db.Integer, primary_key=True)
    username = proto.db.Column(proto.db.String(80), unique=True)
    email = proto.db.Column(proto.db.String(120), unique=True)
    password = proto.db.Column(proto.db.String(80), unique=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
