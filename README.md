# Cosmos API

A python micro-service built using the [Flask micro-framework](http://flask.pocoo.org) that passes back enhanced information from [Astronomy Picture of the Day](https://apod.nasa.gov/apod/astropix.html).

This micro-service is adapted from NASA's [apod-api](https://github.com/nasa/apod-api).

## Table of contents
1. [Getting Started](#getting_started)
    1. [Standard environment](#standard_environment)
    2. [Heroku](#heroku)
2. [Documentation](#documentation)
4. [Authors](#author)

## Getting started <a name="getting_started"></a>

### Standard environment <a name="standard_environment"></a>

1. Clone the repo
```bash
git clone https://github.com/samyanez94/cosmos-api
```
2. `cd` into the new directory
```bash
cd cosmos-api
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run the server (Requires Python 3)
```bash
python cosmos/service.py
```

### Heroku deployment <a name="heroku"></a>

1. Clone the repo
```bash
git clone https://github.com/samyanez94/cosmos-api
```
2. `cd` into the new directory
```bash
cd apod-api
```
3. Install Heroku
```bash
brew install heroku/brew/heroku
```
4. Login to Heroku
```bash
heroku login
```
5. Create the app
```bash
heroku create
```
6. Run the app locally
```bash
heroku local
```
7. Deploy
```bash
git push heroku master
```

## Documentation <a name="documentation"></a>

[API documentation](https://documenter.getpostman.com/view/4492878/SVYnRLcm?version=latest)

## Author <a name="author"></a>
* Samuel Yanez ~ [samyanez94](https://github.com/samyanez94)

## License

MIT © Samuel Yanez
