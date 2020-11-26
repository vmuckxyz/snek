import connexion
import six

from swagger_server.models.bug import Bug  # noqa: E501
from swagger_server.models.sign_in_request import SignInRequest  # noqa: E501
from swagger_server import util


def bug_id_get(id):  # noqa: E501
    """bug_id_get

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: Bug
    """
    return 'do some magic!'


def get_index():  # noqa: E501
    """Get (or redirect to) the HTML interface.  Also handles checking the auth cookie.

     # noqa: E501


    :rtype: str
    """
    return 'do some magic!'


def get_terms():  # noqa: E501
    """Terms of Service

    Returns the Terms of Service for this game.  # noqa: E501


    :rtype: str
    """
    return 'do some magic!'


def sign_in_user(body):  # noqa: E501
    """Logs in and returns the authentication cookie

     # noqa: E501

    :param body: A JSON object containing the login and password.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = SignInRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
