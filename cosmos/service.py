"""
A micro-service passing back enhanced information from Astronomy
Picture of the Day (APOD).

Adapted from code in https://github.com/nasa/planetary-api

Created on August 3, 2019

@author=samyanez94 @email=samuelyanez94@gmail.com
"""
from datetime import datetime, date
from flask import Flask, request, redirect, jsonify
from utility import _parse

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
    logging.info("'_validate' called")
    for parameter in parameters:
        if parameter not in ALLOWED_FIELDS:
            return False
    return True

def _validate_date(date):
    logging.info("'_validate_date' called")

    today = datetime.today().date()

    # Date of the first APOD
    begin = datetime(1995, 6, 16).date()

    # Validate date
    if (date > today) or (date < begin):
        today_string = today.strftime('%b %d, %Y')
        begin_string = begin.strftime('%b %d, %Y')

        raise ValueError('Date must be between %s and %s.' % (begin_string, today_string))

def _abort(code, msg):
    logging.info("'_abort' called")
    response = jsonify(service_version=SERVICE_VERSION, msg=msg, code=code)
    response.status_code = code

    return response

# Creating the response

def _handler(date=None, concept_tags=False, thumbnails=False):
    """
    Returns the response object to be served through the API.
    """

    logging.info("'_handler' called")

    try:
        page_props = _parse(date, thumbnails)

        if concept_tags:
                page_props['concepts'] = "'concept_tags' functionality is turned off in current service."

        return page_props

    except Exception as exception:
        return _abort(500, 'Internal Service Error')

def _response_for_date(date, concept_tags, thumbnails):
    """
    Returns the JSON data for a specific date, which must be a string of the form YYYY-MM-DD. If date is None, then it defaults to the current date.
    """

    logging.info("'_response_for_date' called")

    if date:
        # Create date object
        date = datetime.strptime(date, '%Y-%m-%d').date()

        # Validate date
        _validate_date(date)

    # Get response
    response = _handler(date, concept_tags, thumbnails)
    response['version'] = SERVICE_VERSION

    # Convert response object to JSON
    return jsonify(response)

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

        # Validate params
        if not _validate(parameters):
            return _abort(400, 'Bad Request: Incorrect fields passed.')

        # Get individual querry params
        input_date = parameters.get('date')
        count = parameters.get('count')
        start_date = parameters.get('start_date')
        end_date = parameters.get('end_date')
        concept_tags = parameters.get('concept_tags', False)
        thumbnails = parameters.get('thumbs', False)

        if not count and not start_date and not end_date:
            return _response_for_date(input_date, concept_tags, thumbnails)

    # Handle errors
    except Exception as exception:

        exception_type = type(exception)

        if exception_type == ValueError or 'BadRequest' in str(exception_type):
            return _abort(400, str(exception) + '.')
        else:
            return _abort(500, 'Internal Service Error')

# Error handling

@app.errorhandler(404)
def page_not_found(error):
    """
    Return a custom 404 error.
    """
    return _abort(error.code, str(error))

@app.errorhandler(500)
def application_error(error):
    """
    Return a custom 500 error.
    """
    return _abort(error.code, str(error))

if __name__ == '__main__':
    app.run()
