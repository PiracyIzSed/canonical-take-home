CLI Application
==========

This folder contains the cli application used to interact with APIs.

Components & Frameworks Used
==========

- Poetry: For dependency and package management
- Typer: To build the CLI Interface
- Pytest: To test the api code.
- sdk: As the python client to interact with the APIs

Quickstart
==========

First, install the cli using,

    pip install poetry
    poetry install

Make sure the Application is running is running using,
    
    docker compose up -d

Export environment variable `API_URL` as,

    export API_URL=http://localhost:8000

Or, You could also create a configuration file named `config.json` in the directory, with the following contents:
    ```json
    {
        "api_url": "http://localhost:8000"
    }
    ```

Now run the command as:

    poetry run cli

Run tests
=========

Tests for this project are defined in the `tests/` folder.

This project uses [pytest](https://docs.pytest.org/) to define tests
because it allows you to use the `assert` keyword with good formatting
for failed assertations.

To run all the tests of a project, simply run the `pytest` command: :
```shell
    > pytest
    =============================================== test session starts =============================================================
    platform win32 -- Python 3.10.7, pytest-7.1.3, pluggy-1.0.0
    rootdir: cli, configfile: pyproject.toml, testpaths: tests
    plugins: cov-3.0.0
    collected 20 items

    tests\test_cli.py .                                                                                                 [  5%]
    tests\test_games.py .......                                                                                         [ 40%]
    tests\test_users.py ........                                                                                        [ 80%]
    tests\test_validator.py ..xx                                                                                        [100%]

    =========================================== 18 passed, 2 xfailed in 1.07s ========================================================
``` 
If you want to run a specific test, you can do this with
[this](https://docs.pytest.org/en/latest/usage.html#specifying-tests-selecting-tests)
pytest feature: :

    $ pytest tests/test_games.py::test_can_get_game

Project structure
=================

Files related to application are in the `app` or `tests` directories.
Application parts are:

    cli
    ├── cli              - application code
    │   ├── games        - `games` command arguments and options
    │   ├── users        - `users` command argument and options
    │   ├── app.py       - Main application object
    │   ├── config.py    - Configuration file for the application
    │   └── main.py      - Main file to initialize the application
    └── tests            - The tests for the application
