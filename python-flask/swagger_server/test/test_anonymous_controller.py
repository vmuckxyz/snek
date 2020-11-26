# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.bug import Bug  # noqa: E501
from swagger_server.models.sign_in_request import SignInRequest  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAnonymousController(BaseTestCase):
    """AnonymousController integration test stubs"""

    def test_bug_id_get(self):
        """Test case for bug_id_get

        
        """
        response = self.client.open(
            '/vmuckxyz/snek/1.0.0/bug/{id}'.format(id='id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_index(self):
        """Test case for get_index

        Get (or redirect to) the HTML interface.  Also handles checking the auth cookie.
        """
        response = self.client.open(
            '/vmuckxyz/snek/1.0.0/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_terms(self):
        """Test case for get_terms

        Terms of Service
        """
        response = self.client.open(
            '/vmuckxyz/snek/1.0.0/tos',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sign_in_user(self):
        """Test case for sign_in_user

        Logs in and returns the authentication cookie
        """
        body = SignInRequest()
        response = self.client.open(
            '/vmuckxyz/snek/1.0.0/signin',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
