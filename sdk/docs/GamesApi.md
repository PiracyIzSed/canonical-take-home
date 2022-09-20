# canonical.GamesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**games_create_game_api_games_post**](GamesApi.md#games_create_game_api_games_post) | **POST** /api/games | Games:Create-Game
[**games_delete_game_api_games_id_delete**](GamesApi.md#games_delete_game_api_games_id_delete) | **DELETE** /api/games/{id} | Games:Delete-Game
[**games_get_game_api_games_id_get**](GamesApi.md#games_get_game_api_games_id_get) | **GET** /api/games/{id} | Games:Get-Game
[**games_list_games_api_games_get**](GamesApi.md#games_list_games_api_games_get) | **GET** /api/games | Games:List-Games
[**games_update_game_api_games_id_patch**](GamesApi.md#games_update_game_api_games_id_patch) | **PATCH** /api/games/{id} | Games:Update-Game


# **games_create_game_api_games_post**
> GameInResponse games_create_game_api_games_post(body_games_create_game_api_games_post)

Games:Create-Game

### Example


```python
import time
import canonical
from canonical.api import games_api
from canonical.model.http_validation_error import HTTPValidationError
from canonical.model.game_in_response import GameInResponse
from canonical.model.body_games_create_game_api_games_post import BodyGamesCreateGameApiGamesPost
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = canonical.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with canonical.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = games_api.GamesApi(api_client)
    body_games_create_game_api_games_post = BodyGamesCreateGameApiGamesPost(
        game=GameInCreate(
            title="title_example",
            age_rating=1.0,
            publisher="publisher_example",
            description="description_example",
            logo_url="logo_url_example",
        ),
    ) # BodyGamesCreateGameApiGamesPost | 

    # example passing only required values which don't have defaults set
    try:
        # Games:Create-Game
        api_response = api_instance.games_create_game_api_games_post(body_games_create_game_api_games_post)
        pprint(api_response)
    except canonical.ApiException as e:
        print("Exception when calling GamesApi->games_create_game_api_games_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_games_create_game_api_games_post** | [**BodyGamesCreateGameApiGamesPost**](BodyGamesCreateGameApiGamesPost.md)|  |

### Return type

[**GameInResponse**](GameInResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **games_delete_game_api_games_id_delete**
> games_delete_game_api_games_id_delete(id)

Games:Delete-Game

### Example


```python
import time
import canonical
from canonical.api import games_api
from canonical.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = canonical.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with canonical.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = games_api.GamesApi(api_client)
    id = 1.0 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Games:Delete-Game
        api_instance.games_delete_game_api_games_id_delete(id)
    except canonical.ApiException as e:
        print("Exception when calling GamesApi->games_delete_game_api_games_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **games_get_game_api_games_id_get**
> GameInResponse games_get_game_api_games_id_get(id)

Games:Get-Game

### Example


```python
import time
import canonical
from canonical.api import games_api
from canonical.model.http_validation_error import HTTPValidationError
from canonical.model.game_in_response import GameInResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = canonical.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with canonical.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = games_api.GamesApi(api_client)
    id = 1.0 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Games:Get-Game
        api_response = api_instance.games_get_game_api_games_id_get(id)
        pprint(api_response)
    except canonical.ApiException as e:
        print("Exception when calling GamesApi->games_get_game_api_games_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**GameInResponse**](GameInResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **games_list_games_api_games_get**
> ListOfGamesInResponse games_list_games_api_games_get()

Games:List-Games

### Example


```python
import time
import canonical
from canonical.api import games_api
from canonical.model.http_validation_error import HTTPValidationError
from canonical.model.list_of_games_in_response import ListOfGamesInResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = canonical.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with canonical.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = games_api.GamesApi(api_client)
    publisher = "publisher_example" # str |  (optional)
    title = "title_example" # str |  (optional)
    limit = 20 # int |  (optional) if omitted the server will use the default value of 20
    offset = 0 # int |  (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Games:List-Games
        api_response = api_instance.games_list_games_api_games_get(publisher=publisher, title=title, limit=limit, offset=offset)
        pprint(api_response)
    except canonical.ApiException as e:
        print("Exception when calling GamesApi->games_list_games_api_games_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publisher** | **str**|  | [optional]
 **title** | **str**|  | [optional]
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 20
 **offset** | **int**|  | [optional] if omitted the server will use the default value of 0

### Return type

[**ListOfGamesInResponse**](ListOfGamesInResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **games_update_game_api_games_id_patch**
> GameInResponse games_update_game_api_games_id_patch(id, body_games_update_game_api_games_id_patch)

Games:Update-Game

### Example


```python
import time
import canonical
from canonical.api import games_api
from canonical.model.body_games_update_game_api_games_id_patch import BodyGamesUpdateGameApiGamesIdPatch
from canonical.model.http_validation_error import HTTPValidationError
from canonical.model.game_in_response import GameInResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = canonical.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with canonical.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = games_api.GamesApi(api_client)
    id = 1.0 # int | 
    body_games_update_game_api_games_id_patch = BodyGamesUpdateGameApiGamesIdPatch(
        game=GameInUpdate(
            title="title_example",
            description="description_example",
            publisher="publisher_example",
            age_rating=1,
        ),
    ) # BodyGamesUpdateGameApiGamesIdPatch | 

    # example passing only required values which don't have defaults set
    try:
        # Games:Update-Game
        api_response = api_instance.games_update_game_api_games_id_patch(id, body_games_update_game_api_games_id_patch)
        pprint(api_response)
    except canonical.ApiException as e:
        print("Exception when calling GamesApi->games_update_game_api_games_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **body_games_update_game_api_games_id_patch** | [**BodyGamesUpdateGameApiGamesIdPatch**](BodyGamesUpdateGameApiGamesIdPatch.md)|  |

### Return type

[**GameInResponse**](GameInResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

