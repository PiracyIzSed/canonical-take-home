import copy
import json
import os
from unittest import mock
from typer.testing import CliRunner
import pytest


@pytest.fixture
def runner():
    runner = CliRunner()
    yield runner


@pytest.fixture
def server_url():
    return "http://test-app.com:8080"


@pytest.fixture
def test_user_response():
    return copy.deepcopy(
        {
            "user": {
                "age": 14,
                "name": "jeff",
                "email": "jeff@email.com",
                "createdAt": "2022-09-19T13:48:07.892930Z",
                "updatedAt": "2022-09-19T13:48:07.892930Z",
                "id": 1,
            }
        }
    )


@pytest.fixture
def test_game_response():
    return copy.deepcopy(
        {
            "game": {
                "ageRating": 14,
                "title": "test-game-1",
                "description": "This is a test game",
                "publisher": "Test Publisher",
                "logoUrl": "https://image-game.com/game.png",
                "createdAt": "2022-09-19T13:48:07.892930Z",
                "updatedAt": "2022-09-19T13:48:07.892930Z",
                "id": 1,
            }
        }
    )


@pytest.fixture
def app(server_url):
    with mock.patch.dict(
        os.environ, {"API_URL": server_url}, clear=True
    ) as config_mock:
        from cli.main import app

        yield app
