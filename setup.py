from setuptools import setup

# Requirements
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# Long description
long_description = open('README.md').read()

# Version
version = 1.0

setup(
    name='cosmos-api',
    description='A python micro-service built using the Flask microframework that passes back enhanced information from Astronomy Picture of the Day.',
    long_description=long_description,
    url='https://github.com/samyanez94/cosmos-api',
    version=version,
    license='LICENSE',
    keywords='apod api nasa cosmos',

    maintainer='Samuel Yanez',
    maintainer_email='samuelyanez94@gmail.com',

    packages=['cosmos'],

    install_requires=requirements,
)
