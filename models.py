from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def setup_db(app):

    db.app = app
    db.init_app(app)
    db.create_all()


class Person(db.Model):
    __tablename__ = 'People'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    catchphrase = db.Column(db.String)

    def __init__(self, name, catchphrase=""):
        self.name = name
        self.catchphrase = catchphrase

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'catchphrase': self.catchphrase
        }
