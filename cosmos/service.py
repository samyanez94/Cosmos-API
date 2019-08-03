"""
A micro-service passing back enhanced information from Astronomy
Picture of the Day (APOD).

Adapted from code in https://github.com/nasa/planetary-api

@author=samyanez94 @email=samuelyanez94@gmail.com
"""

from flask import Flask, redirect

# Postman documentation
DOCUMENTATION_URL = 'https://documenter.getpostman.com/view/4492878/SVYnRLcm?version=latest'

app = Flask(__name__)

# Endpoints

@app.route('/')
def home():
    return redirect(DOCUMENTATION_URL, code=302)

if __name__ == '__main__':
    app.run()
