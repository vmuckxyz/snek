# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.debug_state import DebugState  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAdminController(BaseTestCase):
    """AdminController integration test stubs"""

    def test_get_user_state(self):
        """Test case for get_user_state

        Gets the current game state of the user with the given ID.
        """
        response = self.client.open(
            '/vmuckxyz/snek/1.0.0/debug/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_mimic_bug_by_id(self):
        """Test case for mimic_bug_by_id

        Copies the game snapshot associated with a given bug to a new user, and associates that user with the current session.
        """
        response = self.client.open(
            '/vmuckxyz/snek/1.0.0/mimicbug/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_mimic_user_by_id(self):
        """Test case for mimic_user_by_id

        
        """
        response = self.client.open(
            '/vmuckxyz/snek/1.0.0/mimicuser/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
