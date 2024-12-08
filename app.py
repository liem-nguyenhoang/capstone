import os
from flask import Flask, request, jsonify, abort
from flask_cors import CORS 
from auth.auth import AuthError, requires_auth
from models import setup_db, Movie, Actor
 
def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # Movie
    @app.route('/movies', methods=['GET'])
    @requires_auth('view:movies')
    def get_movies(payload):
        """
        Retrieve a list of all movies.
        """
        movies = Movie.query.all()
        return jsonify({"success": True, "movies": [movie.format() for movie in movies]})

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie(payload):
        """
        Create a new movie.
        """
        body = request.get_json()

        if not body or 'title' not in body or 'release_date' not in body:
            abort(400, description="Title and release date are required.")

        new_movie = Movie(
            title=body['title'],
            release_date=body['release_date']
        )
        new_movie.insert()
        return jsonify({"success": True, "created": new_movie.id})

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('update:movies')
    def update_movie(payload, movie_id):
        """
        Update details of an existing movie.
        """
        movie = Movie.query.get(movie_id)
        if not movie:
            abort(404, description=f"Movie with ID {movie_id} not found.")

        body = request.get_json()
        movie.title = body.get('title', movie.title)
        movie.release_date = body.get('release_date', movie.release_date)
        movie.update()

        return jsonify({"success": True, "updated": movie.format()})

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(payload, movie_id):
        """
        Delete a movie by its ID.
        """
        movie = Movie.query.get(movie_id)
        if not movie:
            abort(404, description=f"Movie with ID {movie_id} not found.")

        movie.delete()
        return jsonify({"success": True, "deleted": movie_id})

    # Actor
    @app.route('/actors', methods=['GET'])
    @requires_auth('view:actors')
    def get_actors(payload):
        """
        Retrieve a list of all actors.
        """
        actors = Actor.query.all()
        return jsonify({"success": True, "actors": [actor.format() for actor in actors]})

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor(payload):
        """
        Create a new actor.
        """
        body = request.get_json()
        required_fields = ['name', 'age', 'gender', 'movie_id']

        if not body or any(field not in body for field in required_fields):
            abort(400, description="All fields (name, age, gender, movie_id) are required.")

        new_actor = Actor(
            name=body['name'],
            age=body['age'],
            gender=body['gender'],
            movie_id=body['movie_id']
        )
        new_actor.insert()
        return jsonify({"success": True, "created": new_actor.id})

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('update:actors')
    def update_actor(payload, actor_id):
        """
        Update details of an existing actor.
        """
        actor = Actor.query.get(actor_id)
        if not actor:
            abort(404, description=f"Actor with ID {actor_id} not found.")

        body = request.get_json()
        actor.name = body.get('name', actor.name)
        actor.age = body.get('age', actor.age)
        actor.gender = body.get('gender', actor.gender)
        actor.movie_id = body.get('movie_id', actor.movie_id)

        actor.update()
        return jsonify({"success": True, "updated": actor.format()})

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(payload, actor_id):
        """
        Delete an actor by its ID.
        """
        actor = Actor.query.get(actor_id)
        if not actor:
            abort(404, description=f"Actor with ID {actor_id} not found.")

        actor.delete()
        return jsonify({"success": True, "deleted": actor_id})

    # Error Handling
    '''
    Example error handling for unprocessable entity
    '''


    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422


    '''
    @DONE implement error handlers using the @app.errorhandler(error) decorator
        each error handler should return (with approprate messages):
                jsonify({
                        "success": False,
                        "error": 404,
                        "message": "resource not found"
                        }), 404

    '''

    '''
    @DONE implement error handler for 404
        error handler should conform to general task above
    '''
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': True,
            'error': 404,
            'message': 'Resource Not Found'
        }), 404


    '''
    @DONE implement error handler for AuthError
        error handler should conform to general task above
    '''
    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            'success': False, 
            'error': error.status_code,
            'message': error.error['description']
        }), error.status_code

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False, 
            'error': 400, 
            'message': 'Bad Request'
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': 'Unauthorized'
        }), 401

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': True, 
            'error': 405,
            'message': 'Method Not Allowed'
        }), 405

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'Internal Server Error'
        }), 500
    
    return app

app = create_app()
if __name__ == "__main__":
    app.run()