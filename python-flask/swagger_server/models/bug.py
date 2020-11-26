# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.debug_state import DebugState  # noqa: F401,E501
from swagger_server import util


class Bug(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, user: str=None, info: str=None, timestamp: datetime=None, state: DebugState=None):  # noqa: E501
        """Bug - a model defined in Swagger

        :param id: The id of this Bug.  # noqa: E501
        :type id: str
        :param user: The user of this Bug.  # noqa: E501
        :type user: str
        :param info: The info of this Bug.  # noqa: E501
        :type info: str
        :param timestamp: The timestamp of this Bug.  # noqa: E501
        :type timestamp: datetime
        :param state: The state of this Bug.  # noqa: E501
        :type state: DebugState
        """
        self.swagger_types = {
            'id': str,
            'user': str,
            'info': str,
            'timestamp': datetime,
            'state': DebugState
        }

        self.attribute_map = {
            'id': 'id',
            'user': 'user',
            'info': 'info',
            'timestamp': 'timestamp',
            'state': 'state'
        }
        self._id = id
        self._user = user
        self._info = info
        self._timestamp = timestamp
        self._state = state

    @classmethod
    def from_dict(cls, dikt) -> 'Bug':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Bug of this Bug.  # noqa: E501
        :rtype: Bug
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Bug.


        :return: The id of this Bug.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Bug.


        :param id: The id of this Bug.
        :type id: str
        """

        self._id = id

    @property
    def user(self) -> str:
        """Gets the user of this Bug.


        :return: The user of this Bug.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user: str):
        """Sets the user of this Bug.


        :param user: The user of this Bug.
        :type user: str
        """

        self._user = user

    @property
    def info(self) -> str:
        """Gets the info of this Bug.


        :return: The info of this Bug.
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info: str):
        """Sets the info of this Bug.


        :param info: The info of this Bug.
        :type info: str
        """

        self._info = info

    @property
    def timestamp(self) -> datetime:
        """Gets the timestamp of this Bug.


        :return: The timestamp of this Bug.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: datetime):
        """Sets the timestamp of this Bug.


        :param timestamp: The timestamp of this Bug.
        :type timestamp: datetime
        """

        self._timestamp = timestamp

    @property
    def state(self) -> DebugState:
        """Gets the state of this Bug.


        :return: The state of this Bug.
        :rtype: DebugState
        """
        return self._state

    @state.setter
    def state(self, state: DebugState):
        """Sets the state of this Bug.


        :param state: The state of this Bug.
        :type state: DebugState
        """

        self._state = state
