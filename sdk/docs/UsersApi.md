# cannonical.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_create_user_api_users_post**](UsersApi.md#users_create_user_api_users_post) | **POST** /api/users | Users:Create-User
[**users_delete_user_api_users_id_delete**](UsersApi.md#users_delete_user_api_users_id_delete) | **DELETE** /api/users/{id} | Users:Delete-User
[**users_get_user_api_users_id_get**](UsersApi.md#users_get_user_api_users_id_get) | **GET** /api/users/{id} | Users:Get-User
[**users_list_users_api_users_get**](UsersApi.md#users_list_users_api_users_get) | **GET** /api/users | Users:List-Users
[**users_update_user_api_users_id_patch**](UsersApi.md#users_update_user_api_users_id_patch) | **PATCH** /api/users/{id} | Users:Update-User


# **users_create_user_api_users_post**
> UserInResponse users_create_user_api_users_post(body_users_create_user_api_users_post)

Users:Create-User

### Example


```python
import time
import cannonical
from cannonical.api import users_api
from cannonical.model.body_users_create_user_api_users_post import BodyUsersCreateUserApiUsersPost
from cannonical.model.user_in_response import UserInResponse
from cannonical.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cannonical.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cannonical.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    body_users_create_user_api_users_post = BodyUsersCreateUserApiUsersPost(
        user=UserInCreate(
            name="name_example",
            age=1.0,
            email="email_example",
        ),
    ) # BodyUsersCreateUserApiUsersPost | 

    # example passing only required values which don't have defaults set
    try:
        # Users:Create-User
        api_response = api_instance.users_create_user_api_users_post(body_users_create_user_api_users_post)
        pprint(api_response)
    except cannonical.ApiException as e:
        print("Exception when calling UsersApi->users_create_user_api_users_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body_users_create_user_api_users_post** | [**BodyUsersCreateUserApiUsersPost**](BodyUsersCreateUserApiUsersPost.md)|  |

### Return type

[**UserInResponse**](UserInResponse.md)

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

# **users_delete_user_api_users_id_delete**
> users_delete_user_api_users_id_delete(id)

Users:Delete-User

### Example


```python
import time
import cannonical
from cannonical.api import users_api
from cannonical.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cannonical.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cannonical.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    id = 1.0 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Users:Delete-User
        api_instance.users_delete_user_api_users_id_delete(id)
    except cannonical.ApiException as e:
        print("Exception when calling UsersApi->users_delete_user_api_users_id_delete: %s\n" % e)
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

# **users_get_user_api_users_id_get**
> UserInResponse users_get_user_api_users_id_get(id)

Users:Get-User

### Example


```python
import time
import cannonical
from cannonical.api import users_api
from cannonical.model.user_in_response import UserInResponse
from cannonical.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cannonical.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cannonical.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    id = 1.0 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Users:Get-User
        api_response = api_instance.users_get_user_api_users_id_get(id)
        pprint(api_response)
    except cannonical.ApiException as e:
        print("Exception when calling UsersApi->users_get_user_api_users_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**UserInResponse**](UserInResponse.md)

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

# **users_list_users_api_users_get**
> ListOfUsersInResponse users_list_users_api_users_get()

Users:List-Users

### Example


```python
import time
import cannonical
from cannonical.api import users_api
from cannonical.model.list_of_users_in_response import ListOfUsersInResponse
from cannonical.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cannonical.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cannonical.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    name = "name_example" # str |  (optional)
    age = 1 # int |  (optional)
    limit = 20 # int |  (optional) if omitted the server will use the default value of 20
    offset = 0 # int |  (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Users:List-Users
        api_response = api_instance.users_list_users_api_users_get(name=name, age=age, limit=limit, offset=offset)
        pprint(api_response)
    except cannonical.ApiException as e:
        print("Exception when calling UsersApi->users_list_users_api_users_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional]
 **age** | **int**|  | [optional]
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 20
 **offset** | **int**|  | [optional] if omitted the server will use the default value of 0

### Return type

[**ListOfUsersInResponse**](ListOfUsersInResponse.md)

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

# **users_update_user_api_users_id_patch**
> UserInResponse users_update_user_api_users_id_patch(id, body_users_update_user_api_users_id_patch)

Users:Update-User

### Example


```python
import time
import cannonical
from cannonical.api import users_api
from cannonical.model.user_in_response import UserInResponse
from cannonical.model.body_users_update_user_api_users_id_patch import BodyUsersUpdateUserApiUsersIdPatch
from cannonical.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cannonical.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cannonical.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    id = 1.0 # int | 
    body_users_update_user_api_users_id_patch = BodyUsersUpdateUserApiUsersIdPatch(
        user=UserInUpdate(
            email="email_example",
            age=1,
        ),
    ) # BodyUsersUpdateUserApiUsersIdPatch | 

    # example passing only required values which don't have defaults set
    try:
        # Users:Update-User
        api_response = api_instance.users_update_user_api_users_id_patch(id, body_users_update_user_api_users_id_patch)
        pprint(api_response)
    except cannonical.ApiException as e:
        print("Exception when calling UsersApi->users_update_user_api_users_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |
 **body_users_update_user_api_users_id_patch** | [**BodyUsersUpdateUserApiUsersIdPatch**](BodyUsersUpdateUserApiUsersIdPatch.md)|  |

### Return type

[**UserInResponse**](UserInResponse.md)

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

