import os
import unittest
from api import create_api
from models import db, Actor, Movie


class ApiTestCase(unittest.TestCase):
    """This class represents the capstone api test case"""

    def inserts(self):
        """Do some initial inserts for the test"""
        actor = Actor(
            id=1,
            name='Robert De Niro',
            age=76
        )
        self.db.session.add(actor)

        actor = Actor(
            id=2,
            name='Al Pacino',
            age=79
        )
        self.db.session.add(actor)

        movie = Movie(
            id=1,
            title='The Irishman',
            genre='Drama/Crime',
            actors=[actor]
        )
        self.db.session.add(movie)

        self.db.session.commit()
        self.db.session.close()

    def setUp(self):
        """Define test variables and initialize app"""
        self.api = create_api()
        self.api.app_context().push()
        self.client = self.api.test_client
        self.headers = {'Authorization': f'Bearer {os.getenv("TOKEN")}'}

        self.db = db
        self.db.init_app(self.api)

        self.db.session.commit()
        self.db.drop_all()
        self.db.create_all()

        self.inserts()

    def tearDown(self):
        """Executed after reach test"""
        self.db.session.rollback()
        self.db.drop_all()
        self.db.session.close()

    def test_db(self):
        """Test if the data was correctly inserted in the db"""
        actors = Actor.query.all()
        self.assertEqual(isinstance(actors, list), True)
        self.assertEqual(isinstance(actors[0], Actor), True)
        movies = Movie.query.all()
        self.assertEqual(isinstance(movies, list), True)
        self.assertEqual(isinstance(movies[0], Movie), True)

    def test_get_actors(self):
        """Test get actors"""
        r = self.client().get('/api/actors', headers=self.headers)
        self.assertEqual(r.status_code, 200)

    def test_post_actors(self):
        """Test post actors"""
        r = self.client().post('/api/actors',
                               headers=self.headers,
                               json={
                                   'id': 3,
                                   'name': 'Joe Pesci',
                                   'age': 76
                               })
        self.assertEqual(r.status_code, 200)

    def test_patch_actors(self):
        """Test patch actors"""
        r = self.client().patch('/api/actors/3',
                                headers=self.headers,
                                json={'age': 77}
                                )
        self.assertEqual(r.status_code, 200)

    def test_delete_actors(self):
        """Test delete actors"""
        r = self.client().delete('/api/actors/3', headers=self.headers)
        self.assertEqual(r.status_code, 200)

    def test_get_movies(self):
        """Test get movies"""
        r = self.client().get('/api/movies', headers=self.headers)
        self.assertEqual(r.status_code, 200)

    def test_post_movies(self):
        """Test post movies"""
        r = self.client().post('/api/movies',
                               headers=self.headers,
                               json={
                                   'title': 'The Irishman',
                                   'genre': 'Drama/Crime',
                                   'actors': [1]
                               })
        self.assertEqual(r.status_code, 201)

    def test_patch_movies(self):
        """Test patch movies"""
        r = self.client().patch('/api/movies/2',
                                headers=self.headers,
                                json={
                                    'actors': [1, 2]
                                })
        self.assertEqual(r.status_code, 200)

    def test_delete_movies(self):
        """Test delete movies"""
        r = self.client().delete('/api/movies/2', headers=self.headers)
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()
