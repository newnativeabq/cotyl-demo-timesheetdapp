"""
Connection Object

Contains information about accessing an interface by describing
the message schema, destination, and protocol of the connection and 
push/open methods to send data to the interface.
"""

from pydantic import BaseModel
from typing import Any

import logging 
logger = logging.getLogger(__name__)



class ConnectionBase(BaseModel):
    name: str
    schema_name: str
    destination: str
    protocol: str



class Connection(ConnectionBase):
    def __init__(self, **data: Any) -> None:
        self.base = ConnectionBase(**data)
        self.__connection_id = None
        self.__connection_id_set = None


    @property
    def name(self):
        return self.base.name


    @property
    def connection_id(self):
        return self.__connection_id


    @connection_id.setter
    def connection_id(self, value: str):
        if self.__connection_id_set:
            raise ValueError('cannot reset connection ID')
        self.__connection_id_set = True
        self.__connection_id = value


    def open(self) -> ConnectionBase:
        raise NotImplementedError(f'open method not implemented for connection {self.name}')


    def push(self, message):
        raise NotImplementedError(f'push method not implemented for connection {self.name}')