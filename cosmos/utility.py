"""
A micro-service passing back enhanced information from Astronomy
Picture of the Day (APOD).

Adapted from code in https://github.com/nasa/planetary-api

Created on August 3, 2019

@author=samyanez94 @email=samuelyanez94@gmail.com
"""

import requests
import logging
import datetime

# Logging
logging.basicConfig(level=logging.DEBUG)

# Path for NASA's APOD API
PATH = 'https://api.nasa.gov/planetary/apod'

# API key
KEY = "DEMO_KEY"

def _get_apod(date=None, thumbnails=False):

    logging.info("'_get_apod' called")

    parameters = {
        'api_key' : KEY
    }

    if date:
        date = date.strftime('%Y-%m-%d')
        parameters.update({'date' : date})

    return requests.get(PATH, parameters).json()



def _parse(date=None, thumbnails=False):
    """
    Accepts a date in '%Y-%m-%d' format. Returns the URL of the APOD image of that day.
    """
    logging.info("'_parse' called")

    return _get_apod(date, thumbnails)
