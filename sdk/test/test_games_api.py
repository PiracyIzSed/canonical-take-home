"""
    Dev

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import canonical
from canonical.api.games_api import GamesApi  # noqa: E501


class TestGamesApi(unittest.TestCase):
    """GamesApi unit test stubs"""

    def setUp(self):
        self.api = GamesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_games_create_game_api_games_post(self):
        """Test case for games_create_game_api_games_post

        Games:Create-Game  # noqa: E501
        """
        pass

    def test_games_delete_game_api_games_id_delete(self):
        """Test case for games_delete_game_api_games_id_delete

        Games:Delete-Game  # noqa: E501
        """
        pass

    def test_games_get_game_api_games_id_get(self):
        """Test case for games_get_game_api_games_id_get

        Games:Get-Game  # noqa: E501
        """
        pass

    def test_games_list_games_api_games_get(self):
        """Test case for games_list_games_api_games_get

        Games:List-Games  # noqa: E501
        """
        pass

    def test_games_update_game_api_games_id_patch(self):
        """Test case for games_update_game_api_games_id_patch

        Games:Update-Game  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
