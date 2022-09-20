import httpretty
import json


@httpretty.activate
def test_can_create_game(runner, app, server_url, test_game_response):
    httpretty.register_uri(
        method="POST",
        uri=f"{server_url}/api/games",
        body=json.dumps(test_game_response),
        status=201,
    )
    result = runner.invoke(
        app,
        [
            "games",
            "create",
            "--title",
            "test-game-1",
            "--publisher",
            "Test Publisher",
            "--age-rating",
            17,
            "--description",
            "This is a test game",
            "--logo-url",
            "https://image-game.com/game.png",
        ],
    )
    assert result.exit_code == 0, result.exception
    assert "test-game-1" in result.stdout


@httpretty.activate
def test_can_create_game_without_logo(runner, app, server_url, test_game_response):
    httpretty.register_uri(
        method="POST",
        uri=f"{server_url}/api/games",
        body=json.dumps(test_game_response),
        status=201,
    )
    result = runner.invoke(
        app,
        [
            "games",
            "create",
            "--title",
            "test-game-1",
            "--publisher",
            "Test Publisher",
            "--age-rating",
            17,
            "--description",
            "This is a test game",
        ],
    )
    assert result.exit_code == 0, result.stdout
    assert "test-game-1" in result.stdout


@httpretty.activate
def test_error_on_getting_non_existent_game(runner, app, server_url):
    non_existent_user_id = 99
    httpretty.register_uri(
        method="GET", uri=f"{server_url}/api/games/{non_existent_user_id}", status=404
    )
    result = runner.invoke(app, ["games", "get", "--id", non_existent_user_id])
    assert result.exit_code == 1, result.exception


@httpretty.activate
def test_can_list_games(runner, app, server_url, test_game_response):
    games = {"count": 1, "games": [test_game_response["game"]]}
    httpretty.register_uri(
        method="GET", uri=f"{server_url}/api/games", body=json.dumps(games), status=200
    )
    result = runner.invoke(app, ["games", "list"])
    assert result.exit_code == 0, result.exception


@httpretty.activate
def test_can_get_game(runner, app, server_url, test_game_response):
    httpretty.register_uri(
        method="GET",
        uri=f"{server_url}/api/games/{test_game_response['game']['id']}",
        body=json.dumps(test_game_response),
        status=200,
    )
    result = runner.invoke(
        app, ["games", "get", "--id", test_game_response["game"]["id"]]
    )
    assert result.exit_code == 0, result.exception


@httpretty.activate
def test_can_update_game_publisher(runner, app, server_url, test_game_response):
    new_publisher = "Updated Publisher"
    test_game_response["game"]["publisher"] = new_publisher
    httpretty.register_uri(
        method="PATCH",
        uri=f"{server_url}/api/games/{test_game_response['game']['id']}",
        body=json.dumps(test_game_response),
        status=200,
    )
    result = runner.invoke(
        app,
        [
            "games",
            "update",
            "--id",
            test_game_response["game"]["id"],
            "--publisher",
            new_publisher,
        ],
    )
    assert result.exit_code == 0, result.stdout
    assert str(new_publisher) in result.stdout


@httpretty.activate
def test_can_update_game_title(runner, app, server_url, test_game_response):
    new_title = "test-game-new"
    test_game_response["game"]["title"] = new_title
    httpretty.register_uri(
        method="PATCH",
        uri=f"{server_url}/api/games/{test_game_response['game']['id']}",
        body=json.dumps(test_game_response),
        status=200,
    )
    result = runner.invoke(
        app,
        [
            "games",
            "update",
            "--id",
            test_game_response["game"]["id"],
            "--title",
            new_title,
        ],
    )
    assert result.exit_code == 0, result.exception
    assert new_title in result.stdout


@httpretty.activate
def test_can_delete_game(runner, app, server_url, test_game_response):
    httpretty.register_uri(
        method="DELETE",
        uri=f"{server_url}/api/games/{test_game_response['game']['id']}",
        status=204,
    )
    result = runner.invoke(
        app, ["games", "delete", "--id", test_game_response["game"]["id"]], input="y"
    )

    assert result.exit_code == 0, result.exception
    assert "successfully" in result.stdout
