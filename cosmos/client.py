"""
A micro-service passing back enhanced information from Astronomy
Picture of the Day (APOD).

Adapted from code in https://github.com/nasa/planetary-api

Created on August 3, 2019

@author=samyanez94 @email=samuelyanez94@gmail.com
"""
from flask import jsonify
from utility import *

import requests

# Path for NASA's APOD API
PATH = 'https://api.nasa.gov/planetary/apod'

# API key
KEY = "FXB3EPLmocrxkpi0lo7jUkk3ctVWBYBpy3byAYdc"

# Fetching the response from the NASA API

def _fetch(concept_tags):
    return requests.get(PATH, {'api_key' : KEY, 'concept_tags' : concept_tags}).json()

def _fetch_single_date(date, concept_tags):
    return requests.get(PATH, {'api_key' : KEY, 'date' : date, 'concept_tags' : concept_tags}).json()

def _fetch_random(count, concept_tags):
    return requests.get(PATH, {'api_key' : KEY, 'count' : count, 'concept_tags' : concept_tags}).json()

def _fetch_ranged_dates(start_date, end_date, concept_tags):
    return requests.get(PATH, {'api_key' : KEY, 'start_date' : start_date, 'end_date' : end_date, 'concept_tags' : concept_tags}).json()

def response_for_today_date(concept_tags, thumbnails, service_version):

    logging.info("'_response_for_today_date' called")

    response = _fetch(concept_tags)

    additional_fields(response, thumbnails, service_version)

    return jsonify(response)

def response_for_single_date(date, concept_tags, thumbnails, service_version):

    logging.info("'_response_for_single_date' called")

    response = _fetch_single_date(date, concept_tags)

    additional_fields(response, thumbnails, service_version)

    return jsonify(response)

def response_for_random_dates(count, concept_tags, thumbnails, service_version):

    logging.info("'_response_for_random_dates' called")

    response = _fetch_random(count, concept_tags)

    for apod in response:
        additional_fields(apod, thumbnails, service_version)

    return jsonify(response)

def response_for_ranged_dates(start_date, end_date, concept_tags, thumbnails, service_version):

    logging.info("'_response_for_ranged_dates' called")

    response = _fetch_ranged_dates(start_date, end_date, concept_tags)

    for apod in response:
        additional_fields(apod, thumbnails, service_version)

    return jsonify(response)
