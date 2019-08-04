"""
A micro-service passing back enhanced information from Astronomy
Picture of the Day (APOD).

Adapted from code in https://github.com/nasa/planetary-api

Created on August 3, 2019

@author=samyanez94 @email=samuelyanez94@gmail.com
"""
from flask import Flask, request, redirect, jsonify

# Relative imports for Heroku
from .client import *
from .utility import *

import logging

# Service version
SERVICE_VERSION = 'v1'

# Method name
API_METHOD_NAME = 'cosmos'

# Postman documentation
DOCUMENTATION_URL = 'https://documenter.getpostman.com/view/4492878/SVYnRLcm?version=latest'

# Flask app
app = Flask(__name__)

# Logging
logging.basicConfig(level=logging.DEBUG)

# Endpoints

@app.route('/')
def home():
    return redirect(DOCUMENTATION_URL, code=302)

@app.route('/' + SERVICE_VERSION + '/' + API_METHOD_NAME + '/', methods=['GET'])
def apod():
    try:
        # Querry params
        parameters = request.args

        # Validate params
        if not validate(parameters):
            return abort(400, 'Bad Request: Incorrect fields passed.', SERVICE_VERSION)

        # Get individual querry params
        input_date = parameters.get('date')
        count = parameters.get('count')
        start_date = parameters.get('start_date')
        end_date = parameters.get('end_date')
        concept_tags = parameters.get('concept_tags', False)
        thumbnails = parameters.get('thumbnails', False)

        # Route to the appropiate method

        if not input_date and not count and not start_date and not end_date:
            return response_for_today_date(concept_tags, thumbnails, SERVICE_VERSION)

        elif not count and not start_date and not end_date and input_date:
            return response_for_single_date(input_date, concept_tags, thumbnails, SERVICE_VERSION)

        elif not input_date and not start_date and not end_date and count:
            return response_for_random_dates(count, concept_tags, thumbnails, SERVICE_VERSION)

        elif not input_date and not count and start_date and end_date:
            return response_for_ranged_dates(start_date, end_date, concept_tags, thumbnails, SERVICE_VERSION)

    # Handle errors
    except Exception as exception:

        exception_type = type(exception)

        if exception_type == ValueError or 'BadRequest' in str(exception_type):
            return abort(400, str(exception), SERVICE_VERSION)
        else:
            return abort(500, 'Internal Service Error', SERVICE_VERSION)

# Error handling

@app.errorhandler(404)
def page_not_found(error):
    return abort(error.code, str(error), SERVICE_VERSION)

@app.errorhandler(500)
def application_error(error):
    return abort(error.code, str(error), SERVICE_VERSION)

if __name__ == '__main__':
    app.run()
