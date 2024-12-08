import os
from flask import Flask,   jsonify 
from flask_cors import CORS 
from auth.auth import AuthError, requires_auth

app = Flask(__name__) 
CORS(app)


@app.route("/drinks", methods=['GET'])
@requires_auth('view:movies')
def get_drinks(payload):
      return jsonify({
        'success': True, 
    }), 200

 
if __name__ == "__main__":
    app.run()

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

