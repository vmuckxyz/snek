import connexion
import six

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.debug_state import DebugState  # noqa: E501
from swagger_server.models.game_state import GameState  # noqa: E501
from swagger_server.models.inventory import Inventory  # noqa: E501
from swagger_server.models.option import Option  # noqa: E501
from swagger_server.models.quest import Quest  # noqa: E501
from swagger_server.models.sign_up_request import SignUpRequest  # noqa: E501
from swagger_server import util


def create_user(body):  # noqa: E501
    """create_user

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = SignUpRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_current_state():  # noqa: E501
    """get_current_state

     # noqa: E501


    :rtype: DebugState
    """
    return 'do some magic!'


def get_inventory():  # noqa: E501
    """Gets the user&#x27;s item inventory, including active equipment

    Get the current user&#x27;s inventory. # noqa: E501


    :rtype: Inventory
    """
    return 'do some magic!'


def get_map():  # noqa: E501
    """get_map

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def get_options():  # noqa: E501
    """get_options

     # noqa: E501


    :rtype: List[Option]
    """
    return 'do some magic!'


def get_quests():  # noqa: E501
    """Get the user&#x27;s quest list

     # noqa: E501


    :rtype: List[Quest]
    """
    return 'do some magic!'


def next(body, full=None):  # noqa: E501
    """Processes a user interaction, and returns the next state of the game.

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param full: 
    :type full: str

    :rtype: GameState
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def post_new_bug():  # noqa: E501
    """post_new_bug

    Creates a new bug.  Copies the user&#x27;s current game state and attaches it to the bug. # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def resume(full=None):  # noqa: E501
    """Gets the current state of the UI based on the state of the user&#x27;s game session.

     # noqa: E501

    :param full: 
    :type full: str

    :rtype: GameState
    """
    return 'do some magic!'


def set_options(body):  # noqa: E501
    """set_options

     # noqa: E501

    :param body: 
    :type body: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = [Option.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def sign_out():  # noqa: E501
    """sign_out

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'
