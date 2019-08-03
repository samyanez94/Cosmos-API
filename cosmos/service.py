"""
A micro-service passing back enhanced information from Astronomy
Picture of the Day (APOD).

Adapted from code in https://github.com/nasa/planetary-api

@author=samyanez94 @email=samuelyanez94@gmail.com
"""

from flask import Flask, redirect

import logging

# Service version
SERVICE_VERSION = 'v1'

# Method name
API_METHOD_NAME = 'cosmos'

# Allowed fields
ALLOWED_FIELDS = ['concept_tags', 'date', 'hd', 'count', 'start_date', 'end_date', 'thumbs']

# Postman documentation
DOCUMENTATION_URL = 'https://documenter.getpostman.com/view/4492878/SVYnRLcm?version=latest'

# Flask app
app = Flask(__name__)

# Logging
logging.basicConfig(level=logging.DEBUG)

# Utilities

def _validate(parameters):
    logging.debug('Validation called')
    for parameter in parameters:
        if argument not in ALLOWED_FIELDS:
            return False
    return True

def _abort(code, msg):
    logging.debug('Abort called')
    response = jsonify(service_version=SERVICE_VERSION, msg=msg, code=code)
    response.status_code = code

    return response

# Endpoints

@app.route('/')
def home():
    return redirect(DOCUMENTATION_URL, code=302)

@app.route('/' + SERVICE_VERSION + '/' + API_METHOD_NAME + '/', methods=['GET'])
def apod():
    logging.info('API called')
    try:
        # Querry params
        parameters = request.args

        if not _validate(parameters):
            return _abort(400, 'Bad Request: Incorrect fields passed.')

        # Get individual querry params
        input_date = parameters.get('date')
        count = parameters.get('count')
        start_date = parameters.get('start_date')
        end_date = parameters.get('end_date')
        use_concept_tags = parameters.get('concept_tags', False)
        thumbs = args.get('thumbs', False)

    # Handle errors
    except Exception as exception:

        type = type(exception)

        if type == ValueError or 'BadRequest' in str(type):
            return _abort(400, str(exception) + '.')
        else:
            return _abort(500, 'Internal Service Error', usage=False)

# Error handling

@app.errorhandler(404)
def page_not_found(e):
    """
    Return a custom 404 error.
    """
    logging.info('Invalid page request: ' + e)
    return _abort(404, 'Sorry, this page was not found in our servers.')

@app.errorhandler(500)
def application_error(e):
    """
    Return a custom 500 error.
    """
    logging.info('Internal error: ' + e)
    return _abort(500, 'Sorry, there was an internal error:' + e)

if __name__ == '__main__':
    app.run()
