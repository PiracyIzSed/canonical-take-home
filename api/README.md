Application Backend (REST API)
==========

This folder contains the basic CRUD apis for the domain models of the applications. 

Components & Frameworks Used
==========

- Poetry: For dependency and package management
- FastAPI: To build the web server for the application
- Pytest: To test the api code.
- SQLAlchemy: As the ORM for interacting with the database
- Alembic: For database migrations
- Postgresql: The database of choice for the application
- Docker: To package the application and run as a service

Quickstart
==========

Run the following commands to bootstrap your environment with
`poetry`: :

    git clone https://github.com/PiracyIzSed/canonical-take-home.git
    cd api
    poetry install
    poetry shell

Then create `.env` file (or rename and modify `.env.example`) in project
root and set environment variables for application: :

    export POSTGRES_DB=postgres POSTGRES_PORT=5432 POSTGRES_USER=postgres POSTGRES_PASSWORD=postgres POSTGRES_HOST=localhost
    touch .env
    echo APP_ENV=dev >> .env
    echo DATABASE_URL=postgresql+asyncpg://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB >> .env
    echo SECRET_KEY=$(openssl rand -hex 32) >> .env

To run the web application in debug use:

    alembic upgrade head
    poetry run uvicorn --host=0.0.0.0 service:application --reload

If you run into the following error in your docker container:

> sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) could not
> connect to server: No such file or directory Is the server running
> locally and accepting connections on Unix domain socket
> \"/tmp/.s.PGSQL.5432\"?

Ensure the DATABASE\_URL variable is set correctly in the
[.env]{.title-ref} file. It is most likely caused by POSTGRES\_HOST not
pointing to its localhost.

> DATABASE\_URL=postgresql://postgres:<postgres@0.0.0.0>:5432/postgres

Run tests
=========

Tests for this project are defined in the `tests/` folder.

Set up environment variable `DATABASE_URL` or set up `database_url` 
in `app/core/settings/test.py` to run the tests against a real database.
Or, just unset the `DATABASE_URL` environment variable from `.env` and 
set the environment variable `APP_ENV` to `dev` to use an in memory
database to run the tests

This project uses [pytest](https://docs.pytest.org/) to define tests
because it allows you to use the `assert` keyword with good formatting
for failed assertations.

To run all the tests of a project, simply run the `pytest` command: :
```shell
    > pytest
    =========================================== test session starts ========================================================
    platform win32 -- Python 3.10.7, pytest-7.1.3, pluggy-1.0.0
    rootdir: api, configfile: pyproject.toml, testpaths: tests
    plugins: anyio-3.6.1, asyncio-0.19.0, cov-3.0.0, env-0.6.2
    asyncio: mode=auto
    collected 26 items

    tests\test_api\test_errors\test_422_error.py .                                                                   [  3%]
    tests\test_api\test_errors\test_error.py .                                                                       [  7%]
    tests\test_api\test_routes\test_games.py ............                                                            [ 53%]
    tests\test_api\test_routes\test_users.py ...........                                                             [ 96%]
    tests\test_schemas\test_rw_model.py .                                                                            [100%] 

    =========================================== 26 passed in 4.20s ========================================================
``` 
If you want to run a specific test, you can do this with
[this](https://docs.pytest.org/en/latest/usage.html#specifying-tests-selecting-tests)
pytest feature: :

    $ pytest tests/test_api/test_routes/test_games.py::test_user_can_delete_a_game

Deployment with Docker
======================

You must have `docker` and `docker-compose` tools installed to work with
material in this section. First, create `.env` file like in
[Quickstart]{.title-ref} section or modify `.env.example`.
`POSTGRES_HOST` must be specified as [db]{.title-ref} or modified in
`docker-compose.yml` also. Then just run:
    
    docker-compose up -d db
    docker-compose up -d app

Application will be available on `localhost` in your browser.

Web routes
==========

All routes are available on `/docs` or `/redoc` paths with Swagger or
ReDoc.

Project structure
=================

Files related to application are in the `app` or `tests` directories.
Application parts are:

    app
    ├── api              - web related stuff.
    │   ├── dependencies - dependencies for routes definition.
    │   ├── errors       - definition of error handlers.
    │   └── routes       - web routes.
    ├── core             - application configuration, startup events, logging.
    ├── db               - db related stuff.
    │   ├── migrations   - manually written alembic migrations.
    │   └── repositories - all crud stuff.
    ├── models           - pydantic models for this application.
    │   ├── domain       - main models that are used almost everywhere.
    │   └── schemas      - schemas for using in web routes.
    ├── resources        - strings that are used in web responses.
    └── services         - logic that is not just crud related.
