# Geolocation Api

The primary goal of this project is Testing around dependencies.

## Table of Contents

1. [Dependencies](#dependencies)
1. [Getting Started](#getting-started)
1. [Database](#database)
1. [Application Structure](#application-structure)
1. [Testing](#testing)
1. [Swagger](#swagger)

## Dependencies

You will need [docker](https://docs.docker.com/engine/installation/) and [docker-compose](https://docs.docker.com/compose/install/).

## Getting Started

First, clone the project:

```bash
$ git clone https://github.com/knowbee/geolocation_api.git <my-project-name>
$ cd <my-project-name>
```

Create `.env` and update it referring to `.env-sample`

Then install dependencies and check that it works

### Docker

```bash
$ docker compose up --build --remove-orphans
```

### Local

```bash
$ pip install pipenv
$ pipenv shell        # Start a virtual environment
$ flask run        # Run your local python server
```

If everything works, you should see the available routes [here](http://127.0.0.1:5000/api/docs).

## Database

The database is in [PostgreSql](https://www.postgresql.org/).

Locally, you can connect to your database using :

```bash
$ docker exec -it db psql -U postgres
```

## Application Structure

The application structure presented in this project is grouped primarily by file type.

```
.
├── database
│   └── config.py              # Project configuration settings
│   └── db.py                  # Environment-specific configuration files for geolocation api
│   └── models.py              # Python classes modeling the database
├── migrations                 # Database's migrations settings
│   └── versions               # Database's migrations versions generated by alembic
├── resources
│   └── geolocation.py          # Rest verbs related to the geolocation routes
│   └── routes.py               # Routes definitions and links to their associated resources
└── services
│   └── google_map_service.py  # Google map service
└── static
│   └── swagger.json  # Resources documentation
└── test                    # Unit tests source code
└── app.py                  # app configuration
└── server.py               # Server entry point

```

## Testing

To add a unit test, simply create a `test_*.py` file anywhere in `./test/`, prefix your test classes with `Test` and your testing methods with `test_`. Unittest will run them automaticaly.

To run tests locally simply do:

```bash
$ python -m unittest discover
```

When you execute docker-compose, tests will be run inside the container before the server start:

```bash
$ docker compose up --build --remove-orphans
```

## Swagger

Our API needs a description of its routes and how to interact with them.
You can easily do that with the swagger package included in this project.
Simply update `swagger.json` in the static folder the resources of your API.
The Swagger UI will be available [here](http://127.0.0.1:5000/api/docs/).
