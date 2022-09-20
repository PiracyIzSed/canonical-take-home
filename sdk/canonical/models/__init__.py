# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from canonical.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from canonical.model.body_games_create_game_api_games_post import BodyGamesCreateGameApiGamesPost
from canonical.model.body_games_update_game_api_games_id_patch import BodyGamesUpdateGameApiGamesIdPatch
from canonical.model.body_users_create_user_api_users_post import BodyUsersCreateUserApiUsersPost
from canonical.model.body_users_update_user_api_users_id_patch import BodyUsersUpdateUserApiUsersIdPatch
from canonical.model.game import Game
from canonical.model.game_in_create import GameInCreate
from canonical.model.game_in_response import GameInResponse
from canonical.model.game_in_update import GameInUpdate
from canonical.model.http_validation_error import HTTPValidationError
from canonical.model.list_of_games_in_response import ListOfGamesInResponse
from canonical.model.list_of_users_in_response import ListOfUsersInResponse
from canonical.model.location_inner import LocationInner
from canonical.model.user import User
from canonical.model.user_in_create import UserInCreate
from canonical.model.user_in_response import UserInResponse
from canonical.model.user_in_update import UserInUpdate
from canonical.model.validation_error import ValidationError
