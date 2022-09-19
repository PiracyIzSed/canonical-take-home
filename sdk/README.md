# cannonical-api
API SDK for python (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.0
- Package version: 1.0.0

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https:////.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https:////.git`)

Then import the package:
```python
import cannonical
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cannonical
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import cannonical
from pprint import pprint
from cannonical.api import games_api
from cannonical.model.body_games_create_game_api_games_post import BodyGamesCreateGameApiGamesPost
from cannonical.model.body_games_update_game_api_games_id_patch import BodyGamesUpdateGameApiGamesIdPatch
from cannonical.model.game_in_response import GameInResponse
from cannonical.model.http_validation_error import HTTPValidationError
from cannonical.model.list_of_games_in_response import ListOfGamesInResponse
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cannonical.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with cannonical.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = games_api.GamesApi(api_client)
    body_games_create_game_api_games_post = BodyGamesCreateGameApiGamesPost(
        game=GameInCreate(
            title="title_example",
            age_rating=1.0,
            publisher="publisher_example",
            description="description_example",
        ),
    ) # BodyGamesCreateGameApiGamesPost | 

    try:
        # Games:Create-Game
        api_response = api_instance.games_create_game_api_games_post(body_games_create_game_api_games_post)
        pprint(api_response)
    except cannonical.ApiException as e:
        print("Exception when calling GamesApi->games_create_game_api_games_post: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*GamesApi* | [**games_create_game_api_games_post**](docs/GamesApi.md#games_create_game_api_games_post) | **POST** /api/games | Games:Create-Game
*GamesApi* | [**games_delete_game_api_games_id_delete**](docs/GamesApi.md#games_delete_game_api_games_id_delete) | **DELETE** /api/games/{id} | Games:Delete-Game
*GamesApi* | [**games_get_game_api_games_id_get**](docs/GamesApi.md#games_get_game_api_games_id_get) | **GET** /api/games/{id} | Games:Get-Game
*GamesApi* | [**games_list_games_api_games_get**](docs/GamesApi.md#games_list_games_api_games_get) | **GET** /api/games | Games:List-Games
*GamesApi* | [**games_update_game_api_games_id_patch**](docs/GamesApi.md#games_update_game_api_games_id_patch) | **PATCH** /api/games/{id} | Games:Update-Game
*UsersApi* | [**users_create_user_api_users_post**](docs/UsersApi.md#users_create_user_api_users_post) | **POST** /api/users | Users:Create-User
*UsersApi* | [**users_delete_user_api_users_id_delete**](docs/UsersApi.md#users_delete_user_api_users_id_delete) | **DELETE** /api/users/{id} | Users:Delete-User
*UsersApi* | [**users_get_user_api_users_id_get**](docs/UsersApi.md#users_get_user_api_users_id_get) | **GET** /api/users/{id} | Users:Get-User
*UsersApi* | [**users_list_users_api_users_get**](docs/UsersApi.md#users_list_users_api_users_get) | **GET** /api/users | Users:List-Users
*UsersApi* | [**users_update_user_api_users_id_patch**](docs/UsersApi.md#users_update_user_api_users_id_patch) | **PATCH** /api/users/{id} | Users:Update-User


## Documentation For Models

 - [BodyGamesCreateGameApiGamesPost](docs/BodyGamesCreateGameApiGamesPost.md)
 - [BodyGamesUpdateGameApiGamesIdPatch](docs/BodyGamesUpdateGameApiGamesIdPatch.md)
 - [BodyUsersCreateUserApiUsersPost](docs/BodyUsersCreateUserApiUsersPost.md)
 - [BodyUsersUpdateUserApiUsersIdPatch](docs/BodyUsersUpdateUserApiUsersIdPatch.md)
 - [Game](docs/Game.md)
 - [GameInCreate](docs/GameInCreate.md)
 - [GameInResponse](docs/GameInResponse.md)
 - [GameInUpdate](docs/GameInUpdate.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [ListOfGamesInResponse](docs/ListOfGamesInResponse.md)
 - [ListOfUsersInResponse](docs/ListOfUsersInResponse.md)
 - [LocationInner](docs/LocationInner.md)
 - [User](docs/User.md)
 - [UserInCreate](docs/UserInCreate.md)
 - [UserInResponse](docs/UserInResponse.md)
 - [UserInUpdate](docs/UserInUpdate.md)
 - [ValidationError](docs/ValidationError.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in cannonical.apis and cannonical.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from cannonical.api.default_api import DefaultApi`
- `from cannonical.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import cannonical
from cannonical.apis import *
from cannonical.models import *
```
