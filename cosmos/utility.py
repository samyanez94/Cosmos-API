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
import re

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

def _get_thumbnails(url):
    video_thumb = ""
    if "youtube" in url or "youtu.be" in url:
        # Get ID from YouTube URL
        youtube_id_regex = re.compile("(?:(?<=(v|V)/)|(?<=be/)|(?<=(\?|\&)v=)|(?<=embed/))([\w-]+)")
        video_id = youtube_id_regex.findall(url)
        video_id = ''.join(''.join(elements) for elements in video_id).replace("?", "").replace("&", "")
        video_thumb = "https://img.youtube.com/vi/" + video_id + "/maxresdefault.jpg"
    elif "vimeo" in url:
        # Get ID from Vimeo URL
        vimeo_id_regex = re.compile("(?:/video/)(\d+)")
        vimeo_id = vimeo_id_regex.findall(url)[0]
        # Make API call to get thumbnail URL
        response = requests.get("https://vimeo.com/api/v2/video/" + vimeo_id + ".json").json()
        video_thumb = response['thumbnail_large']

    return video_thumb
