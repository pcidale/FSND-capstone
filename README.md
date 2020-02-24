# FSND Capstone: Casting Agency
**API link:** (https://pcidale-fsnd-capstone.herokuapp.com/)

## Scope and Motivation

The scope of this project was suggested by the Udacity team to put into practice all modules that we studied so far:

* SQL and Data Modeling for the Web
* API Development and Documentation
* Identity and Access  Management
* Server Deployment, Containerization and Testing

In addition, it's been used Postman Collections for testing all API’s resources and Heroku for deployment.

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

GET /actors
- Fetches a dictionary of actors, represented with the id in the database, name and age
- Request Arguments: None
- Returns: A object containing a list of actors and a success boolean

```
GET /actors
{
  "actors": [
      {
        "age": 79,
        "id": 2,
        "name": "Al Pacino"
      },
      {
        "age": 76,
        "id": 1,
        "name": "Robert De Niro"
      }
    ],
  "success": true
}
```

GET /actors/<user_id>
- Fetches a dictionary with the specific actor, represented with the id in the database, name and age
- Request Arguments: user id
- Returns: A object containing a list with the actor and a success boolean

```
GET /actors/1
{
  "actor": [
    {
      "age": 75,
      "id": 1,
      "name": "Robert de Niro"
    }
  ],
  "success": true
}
```

GET /movies
- Fetches a dictionary of movies, represented with the id in the database, title, genre and a list with all the actors presented in the movie
- Request Arguments: None
- Returns: A object containing a list of movies and a success boolean

```
GET /movies
{
  "movies": [
    {
      "actors": [
        {
          "age": 75,
          "id": 1,
          "name": "Robert de Niro"
        }
      ],
      "genre": "Drama/Crime",
      "id": 1,
      "title": "The Irishman"
    }
  ],
  "success": true
}
```

GET /movies/<movie_id>
- Fetches a dictionary with the specific movie, represented with the id in the database, title, genre and a list with all the actors 
- Request Arguments: movie id
- Returns: A object containing a list with the movie and a success boolean

```
GET /movies/1
{
  "movie": {
    "actors": [
      {
        "age": 75,
        "id": 1,
        "name": "Robert de Niro"
      }
    ],
    "genre": "Drama/Crime",
    "id": 1,
    "title": "The Irishman"
  },
  "success": true
}
```

POST /actors
- Inserts a new actor in database
- Request Arguments: body JSON with the necessary data (name and age)
- Returns: the formatted object

```
POST /actors
body {
	"id": 1,
	"name": "Robert De Niro",
	"age": 75
}

{
  "actor": [
    {
      "age": 75,
      "id": 1,
      "name": "Robert de Niro"
    }
  ],
  "success": true
}
```

POST /movies
- Inserts a new movie in database
- Request Arguments: body JSON with the necessary data (title, genre and a list of actors ids)
- Returns: the formatted object

```
POST /movies
body {
	"id": 1,
	"title": "The Irishman",
	"genre": "Drama/Crime",
	"actors": [1, 2]
}

{
  "movie": [
    {
      "actors": [
        {
          "age": 75,
          "id": 1,
          "name": "Robert De Niro"
        },
        {
          "age": 79,
          "id": 2,
          "name": "Al Pacino"
        }
      ],
      "genre": "Drama/Crime",
      "id": 1,
      "title": "The Irishman"
    }
  ],
  "success": true
}
```

PATCH /actors/<actor_id> and /movies/<movie_id>

* DELETE /actors/<actor_id> and /movies/<movie_id>

## Testing

### Unittest

To run the tests:

```
python test_api.py
```

### Postman

Open Postman and import the collection ./fsnd-capstone.postman_collection.json in order to perform the tests according to each role.
