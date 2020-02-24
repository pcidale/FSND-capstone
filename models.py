from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def setup_db(app):
    db.app = app
    db.init_app(app)
    db.drop_all()
    db.create_all()


movie_cast = db.Table('movie_cast',
    db.Column('actor_id', db.Integer, db.ForeignKey('actors.id')),
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'))
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
            'age': self.age
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    def __repr__(self):
        return f'<Actor id: "{self.id}", name: "{self.name}">'


class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    genre = db.Column(db.String(20))
    actors = db.relationship(
        'Actor',
        secondary=movie_cast,
        backref=db.backref('movies', lazy='dynamic')
    )

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'genre': self.genre,
            'actors': [actor.format() for actor in self.actors]
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def update():
        db.session.commit()

    def __repr__(self):
        return f'<Movie id: "{self.id}", title: "{self.title}">'
