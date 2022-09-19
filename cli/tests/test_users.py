import httpretty
import json

def test_error_on_invalid_email(runner, app):
    result = runner.invoke(app, ["create", "--email", "not_a_valid_email"])
    assert result.exit_code == 2

@httpretty.activate
def test_can_create_user(runner, app, server_url, test_user_response):
    httpretty.register_uri(
        method="POST",
        uri=f"{server_url}/api/users",
        body=json.dumps(test_user_response),
        status=201
    )
    result = runner.invoke(app, ["users", "create", "--email", "test@email.com", "--name", "test-game", "--age", 17 ])
    assert result.exit_code == 0

@httpretty.activate
def test_error_on_getting_non_existent_user(runner, app, server_url):
    non_existent_user_id = 99
    httpretty.register_uri(
        method="GET",
        uri=f"{server_url}/api/users/{non_existent_user_id}",
        status=404
    )
    result = runner.invoke(app, ["users", "get", "--id", "-i", non_existent_user_id])
    assert result.exit_code == 1

@httpretty.activate
def test_can_list_users(runner, app, server_url, test_user_response):
    users = {
        "count": 1,
        "users": [ test_user_response["user"]]
    }
    httpretty.register_uri(
        method="GET",
        uri=f"{server_url}/api/users",
        body=json.dumps(users),
        status=200
    )
    result = runner.invoke(app, ["users", "list"])
    assert result.exit_code == 0

@httpretty.activate
def test_can_get_user(runner, app, server_url, test_user_response):

    httpretty.register_uri(
        method="GET",
        uri=f"{server_url}/api/users/{test_user_response['user']['id']}",
        body=json.dumps(test_user_response),
        status=200
    )
    result = runner.invoke(app, ["users", "get", "--id", test_user_response['user']['id']])
    assert result.exit_code == 0

@httpretty.activate
def test_can_update_user_age(runner, app, server_url, test_user_response):
    new_age = 88
    test_user_response["user"]["age"] = new_age
    httpretty.register_uri(
        method="PATCH",
        uri=f"{server_url}/api/users/{test_user_response['user']['id']}",
        body=json.dumps(test_user_response),
        status=200
    )
    result = runner.invoke(app, ["users", "update", "--id", test_user_response["user"]["id"], "--age", new_age])
    assert result.exit_code == 0
    assert  str(new_age) in result.stdout

@httpretty.activate
def test_can_update_user_email(runner, app, server_url, test_user_response):
    new_email =  "new@email.com"
    test_user_response["user"]["email"] = new_email
    httpretty.register_uri(
        method="PATCH",
        uri=f"{server_url}/api/users/{test_user_response['user']['id']}",
        body=json.dumps(test_user_response),
        status=200
    )
    result = runner.invoke(app, ["users", "update", "--id", test_user_response["user"]["id"], "--email", new_email])
    assert result.exit_code == 0
    assert new_email in result.stdout

@httpretty.activate
def test_can_delete_user(runner, app, server_url, test_user_response):
    httpretty.register_uri(
        method="DELETE",
        uri=f"{server_url}/api/users/{test_user_response['user']['id']}",
        status=204
    )
    result = runner.invoke(app, ["users", "delete", "--id", test_user_response["user"]["id"]], input="y")

    assert result.exit_code == 0
    assert "successfully" in result.stdout