"""
Connection Object

Contains information about accessing an interface by describing
the message schema, destination, and protocol of the connection and 
push/open methods to send data to the interface.
"""

from pydantic import BaseModel
from typing import Any, Optional

from cotyl.message.message import Message

import logging 
logger = logging.getLogger(__name__)



class ConnectionBase(BaseModel):
    name: Optional[str]
    schema_name: Optional[str] = 'None'
    destination: Optional[str]
    protocol: Optional[str]

    def __repr__(self):
        return f"<Connection> {self.name}: destination {self.destination}"



class Connection():
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

    @property
    def destination(self):
        return self.base.destination

    @property
    def schema_name(self):
        return self.base.schema_name


    @connection_id.setter
    def connection_id(self, value: str):
        if self.__connection_id_set:
            raise ValueError('cannot reset connection ID')
        self.__connection_id_set = True
        self.__connection_id = value


    def __call__(self, message: Message):
        return self.push(message)


    def open(self) -> ConnectionBase:
        raise NotImplementedError(f'open method not implemented for connection {self.name}')


    def push(self, message: Message):
        raise NotImplementedError(f'push method not implemented for connection {self.name}')






########################
### Test Connections ###
########################

class LogConnection(Connection):
    def __init__(self) -> None:
        """Log Connection
            Log messages. Primarily for debugging
        """
        data = {
            'name':'print_connection',
            'schema_name':'NULL_SCHEMA',
            'destination':'logger',
            'protocol':'logging',
        }
        super().__init__(**data)
        self.logger = logging.getLogger(__name__)

    def open(self) -> Connection:
        return self

    def push(self, message: Message):
        self.logger.info(message)


class NullConnection(Connection):
    """Null Connection
        Primarily for tests.  Overrides required methods with minimal returns.
    """
    destination: Optional[str] = 'return'
    schema_name: str = 'any'

    def open(self) -> Connection:
        return self

    def push(self, message: Message):
        return message