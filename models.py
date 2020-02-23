from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def setup_db(app):
    db.app = app
    db.init_app(app)
    db.create_all()


actors_identifier = db.Table('actors_identifier', db.Model.metadata,
    db.Column('actor_id', db.Integer, db.ForeignKey('actors.id'),
              primary_key=True),
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'),
              primary_key=True)
)


class Actor(db.Model):
    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    age = db.Column(db.Integer)

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'catchphrase': self.catchphrase
        }


class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    genre = db.Column(db.String(20))
    actors = db.relationship('Actor', secondary=actors_identifier,
                             lazy='subquery',
                             backref=db.backref('movies', lazy=True))
