import connexion
import six

from swagger_server.models.debug_state import DebugState  # noqa: E501
from swagger_server import util


def get_user_state(id):  # noqa: E501
    """Gets the current game state of the user with the given ID.

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: DebugState
    """
    return 'do some magic!'


def mimic_bug_by_id(id):  # noqa: E501
    """Copies the game snapshot associated with a given bug to a new user, and associates that user with the current session.

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def mimic_user_by_id(id):  # noqa: E501
    """mimic_user_by_id

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: None
    """
    return 'do some magic!'
