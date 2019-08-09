"""
A micro-service passing back enhanced information from Astronomy
Picture of the Day (APOD).

Adapted from code in https://github.com/nasa/planetary-api

Created on August 3, 2019

@author=samyanez94 @email=samuelyanez94@gmail.com
"""
from flask import jsonify

import logging
import re

# Logging
logging.basicConfig(level=logging.DEBUG)

# Allowed fields
ALLOWED_FIELDS = ['concept_tags', 'date', 'hd', 'count', 'start_date', 'end_date', 'thumbnails']

# Validate parameters
def validate(parameters):
    logging.debug("'_validate' called")
    for parameter in parameters:
        if parameter not in ALLOWED_FIELDS:
            return False
    return True

# Response in case of errors
def abort(code, msg, service_version):
    logging.debug("'_abort' called")
    response = jsonify(code=code, msg=msg, service_version=service_version)
    response.status_code = code

    return response

# Add additional fields to the response
def additional_fields(response, thumbnails, service_version):
    logging.debug("'additional_fields' called")

    url = response['url']
    media_type = response['media_type']

    # Check for thumbnails
    if url and media_type == 'video' and thumbnails:
        response['thumbnail_url'] = _get_thumbnails(url)

    # Add service version
    response['version'] = service_version

    # Remove NASA's service version
    del response['service_version']

# Video thumbnails
def _get_thumbnails(url):
    logging.debug("'_get_thumbnails' called")

    video_thumb = ""

    # Get ID from YouTube URL
    if "youtube" in url or "youtu.be" in url:
        youtube_id_regex = re.compile("(?:(?<=(v|V)/)|(?<=be/)|(?<=(\?|\&)v=)|(?<=embed/))([\w-]+)")
        video_id = youtube_id_regex.findall(url)
        video_id = ''.join(''.join(elements) for elements in video_id).replace("?", "").replace("&", "")
        video_thumb = "https://img.youtube.com/vi/" + video_id + "/maxresdefault.jpg"

    # Get ID from Vimeo URL
    elif "vimeo" in url:
        vimeo_id_regex = re.compile("(?:/video/)(\d+)")
        vimeo_id = vimeo_id_regex.findall(url)[0]
        # Make API call to get thumbnail URL
        response = requests.get("https://vimeo.com/api/v2/video/" + vimeo_id + ".json").json()
        video_thumb = response['thumbnail_large']

    return video_thumb
