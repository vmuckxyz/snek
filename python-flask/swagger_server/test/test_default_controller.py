# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.debug_state import DebugState  # noqa: E501
from swagger_server.models.game_state import GameState  # noqa: E501
from swagger_server.models.inventory import Inventory  # noqa: E501
from swagger_server.models.option import Option  # noqa: E501
from swagger_server.models.quest import Quest  # noqa: E501
from swagger_server.models.sign_up_request import SignUpRequest  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_create_user(self):
        """Test case for create_user

        
        """
        body = SignUpRequest()
        response = self.client.open(
            '/vmuckxyz/snek/1.0.0/newuser',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_current_state(self):
        """Test case for get_current_state

        
        """
        response = self.client.open(
            '/vmuckxyz/snek/1.0.0/debug',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_inventory(self):
        """Test case for get_inventory

        Gets the user's item inventory, including active equipment
        """
        response = self.client.open(
            '/vmuckxyz/snek/1.0.0/inv',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_map(self):
        """Test case for get_map

        
        """
        response = self.client.open(
            '/vmuckxyz/snek/1.0.0/map',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_options(self):
        """Test case for get_options

        
        """
        response = self.client.open(
            '/vmuckxyz/snek/1.0.0/options',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_quests(self):
        """Test case for get_quests

        Get the user's quest list
        """
        response = self.client.open(
            '/vmuckxyz/snek/1.0.0/quests',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_next(self):
        """Test case for next

        Processes a user interaction, and returns the next state of the game.
        """
        body = Body()
        query_string = [('full', 'full_example')]
        response = self.client.open(
            '/vmuckxyz/snek/1.0.0/next',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_new_bug(self):
        """Test case for post_new_bug

        
        """
        response = self.client.open(
            '/vmuckxyz/snek/1.0.0/bug/new',
            method='POST',
            content_type='text/plain')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_resume(self):
        """Test case for resume

        Gets the current state of the UI based on the state of the user's game session.
        """
        query_string = [('full', 'full_example')]
        response = self.client.open(
            '/vmuckxyz/snek/1.0.0/resume',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_set_options(self):
        """Test case for set_options

        
        """
        body = [Option()]
        response = self.client.open(
            '/vmuckxyz/snek/1.0.0/options',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sign_out(self):
        """Test case for sign_out

        
        """
        response = self.client.open(
            '/vmuckxyz/snek/1.0.0/signout',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
