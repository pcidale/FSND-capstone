from flask import Blueprint, jsonify, request, abort
from auth import AuthError, requires_auth
from models import Actor, Movie
api_blueprint = Blueprint('capstone-api', __name__)


@api_blueprint.route('/actors')
@requires_auth('get:actors')
def get_actors():
    """
    Reserved endpoint for users with permission 'get:actors', allowing
    them to get all actors from the database
    :return: status code and json containing the newly created drink
    """
    actors = [actor.format() for actor in Actor.query.all()]
    return jsonify({
        'success': True,
        'actors': actors
    }), 200


@api_blueprint.route('/actors/<int:actor_id>')
@requires_auth('get:actors')
def get_actor(actor_id):
    """
    Reserved endpoint for users with permission 'get:actors', allowing
    them to get a specific actor from the database
    :return: status code and json containing the newly created drink
    """
    actor = Actor.query.get(actor_id)
    if actor:
        return jsonify({
            'success': True,
            'actor': [actor.format()]
        }), 200
    else:
        abort(404, f'Actor id {actor_id} not found')


@api_blueprint.route('/actors', methods=['POST'])
@requires_auth('post:actors')
def post_actors():
    """
    Reserved endpoint for users with permission 'post:actors', allowing
    them to create new actor in the database
    :return: status code and json containing the newly created drink
    """
    actor = Actor()
    for attribute, value in request.json.items():
        setattr(actor, attribute, value)
    actor.insert()
    return jsonify({
        'success': True,
        'actor': [actor.format()]
    }), 201


@api_blueprint.route('/actors/<int:actor_id>', methods=['PATCH'])
@requires_auth('patch:actors')
def patch_actors(actor_id):
    """
    Reserved endpoint for users with permission 'patch:actors', allowing
    them to modify an actor in the database
    :return: status code and json containing the newly created drink
    """
    actor = Actor.query.get(actor_id)
    if actor:
        for attribute, value in request.json.items():
            setattr(actor, attribute, value)
        actor.update()
        return jsonify({
            'success': True,
            'actor': actor.format()
        }), 200
    else:
        abort(404, f'Actor id {actor_id} not found')


@api_blueprint.route('/actors/<int:actor_id>', methods=['DELETE'])
@requires_auth('delete:actors')
def delete_actors(actor_id):
    """
    Reserved endpoint for users with permission 'delete:actors', allowing
    them to delete an actor in the database
    :return: status code and json containing the newly created drink
    """
    actor = Actor.query.get(actor_id)
    if actor:
        actor.delete()
        return jsonify({
            'success': True,
            'actor_id': actor_id
        }), 200
    else:
        abort(404, f'Actor id {actor_id} not found')


@api_blueprint.route('/movies')
@requires_auth('get:movies')
def get_movies():
    """
    Reserved endpoint for users with permission 'get:movies', allowing
    them to get all movies from the database
    :return: status code and json containing the newly created drink
    """
    movies = [movie.format() for movie in Movie.query.all()]
    return jsonify({
        'success': True,
        'movies': movies
    }), 200


@api_blueprint.route('/movies/<int:movie_id>')
@requires_auth('get:movies')
def get_movie(movie_id):
    """
    Reserved endpoint for users with permission 'get:movies', allowing
    them to get a specific movie from the database
    :return: status code and json containing the newly created drink
    """
    movie = Movie.query.get(movie_id)
    if movie:
        return jsonify({
            'success': True,
            'movie': movie.format()
        }), 200
    else:
        abort(404, f'Movie id {movie_id} not found')


@api_blueprint.route('/movies', methods=['POST'])
@requires_auth('post:movies')
def post_movies():
    """
    Reserved endpoint for users with permission 'post:movies', allowing
    them to create new movie in the database
    :return: status code and json containing the newly created drink
    """
    movie = Movie()
    for attribute, value in request.json.items():
        if attribute == 'actors':
            actors = [Actor.query.get(actor_id) for actor_id in value]
            movie.actors = actors
        else:
            setattr(movie, attribute, value)
    movie.insert()
    return jsonify({
        'success': True,
        'movie': [movie.format()]
    }), 201


@api_blueprint.route('/movies/<int:movie_id>', methods=['PATCH'])
@requires_auth('patch:movies')
def patch_movies(movie_id):
    """
    Reserved endpoint for users with permission 'patch:movies', allowing
    them to modify an movie in the database
    :return: status code and json containing the newly created drink
    """
    movie = Movie.query.get(movie_id)
    if movie:
        for attribute, value in request.json.items():
            if attribute == 'actors':
                actors = [Actor.query.get(actor_id) for actor_id in value]
                movie.actors = actors
            else:
                setattr(movie, attribute, value)
        movie.update()
        return jsonify({
            'success': True,
            'movie': [movie.format()]
        }), 200
    else:
        abort(404, f'Movie id {movie_id} not found')


@api_blueprint.route('/movies/<int:movie_id>', methods=['DELETE'])
@requires_auth('delete:movies')
def delete_movies(movie_id):
    """
    Reserved endpoint for users with permission 'delete:actors', allowing
    them to delete a movie in the database
    :param movie_id: movie identifier
    :return: status code and json containing the newly created drink
    """
    movie = Movie.query.get(movie_id)
    if movie:
        movie.delete()
        return jsonify({
            'success': True,
            'movie_id': movie_id
        }), 200
    else:
        abort(404, f'Movie id {movie_id} not found')


# Error Handling
@api_blueprint.errorhandler(400)
def bad_request(error):
    """
    Handler for bad request
    :param error: error message
    :return: status code and json with error message
    """
    return jsonify({
        'success': False,
        'error': 400,
        'message': str(error)
    }), 400


@api_blueprint.errorhandler(404)
def page_not_found(error):
    """
    Handler for resources not found
    :param error: error message
    :return: status code and json with error message
    """
    return jsonify({
        'success': False,
        'error': 404,
        'message': str(error)
    }), 404


@api_blueprint.errorhandler(422)
def unprocessable(error):
    """
    Handler for unprocessable errors
    :param error: error message
    :return: status code and json with error message
    """
    return jsonify({
        'success': False,
        'error': 422,
        'message': str(error)
    }), 422


@api_blueprint.errorhandler(500)
def internal_server_error(error):
    """
    Handler for internal errors
    :param error: error message
    :return: status code and json with error message
    """
    return jsonify({
        'success': False,
        'error': 500,
        'message': str(error)
    }), 500


@api_blueprint.errorhandler(AuthError)
def handle_auth_error(exception):
    """
    Authentication error handler for scoped endpoints
    :param exception: AuthError instance
    :return: response: status code and the error description
    """
    response = jsonify(exception.error)
    response.status_code = exception.status_code
    return response
