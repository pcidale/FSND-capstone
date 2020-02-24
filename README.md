# FSND Capstone: Casting Agency
**API link:** (https://pcidale-fsnd-capstone.herokuapp.com/)

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in api.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Environment Variables

Before starting the API, it's required to define these variables:

* `DATABASE_URL`
* `AUTH0_DOMAIN`
* `AUTH0_ALGORITHMS`
* `AUTH0_AUDIENCE`

## Running the server

To run the server, execute:

```
export FLASK_APP=api.py
flask run --reload
```

## Casting Agency Specifications

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

## Roles and Permissions

### Casting Assistant

* GET:actors
* GET:movies

### Casting Director

* All permissions a *Casting Assistant* has
* POST:actor
* DELETE:actor
* PATCH:actor
* PATCH:movie

## Executive Producer

* All permissions a *Casting Director* has
* POST:movie
* DELETE:movie

## Endpoints

* GET /actors and /movies
* DELETE /actors/<actor_id> and /movies/<movie_id>
* POST /actors and /movies
* PATCH /actors/<actor_id> and /movies/<movie_id>

## Testing

### Unittest

To run the tests:

```
python test_api.py
```

### Postman

Open Postman and import the collection ./fsnd-capstone.postman_collection.json in order to perform the tests according to each role.
