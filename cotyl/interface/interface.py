"""
Interface Base

Interfaces handle ingress and egress through nodes via network and local OS messaging.
"""

from pydantic import BaseModel
from typing import List, Any

from cotyl.interface.connection import Connection
from cotyl.node.router import Router


class InterfaceBase(BaseModel):
    name: str
    connections: List[Connection]


class Interface(InterfaceBase):
    def __init__(self, **data: Any) -> None:
        self.base = InterfaceBase(**data)
        self.__interface_id = None
        self.__interface_id_set = False
        self.__router = None
        self.__router_set = None
        self.__setup = False


    @property
    def name(self):
        return self.base.name


    @property
    def connections(self):
        return self.base.connections


    @property 
    def interface_id(self):
        return self.__interface_id


    @interface_id.setter
    def interface_id(self, value: str):
        if self.__interface_id_set:
            raise ValueError('cannot reset interface ID')
        self.__interface_id_set = True
        self.__interface_id = value


    @property
    def router(self):
        return self.__router

    
    @router.setter
    def router(self, value: Router):
        if self.__router_set:
            raise ValueError('cannot reset router')
        self.__router_set = True
        self.__router = value        


    def _setup_connection(self, connection: Connection):
        connection.connection_id = hash(connection)


    def expose(self) -> List[Connection]:
        assert self.__setup == True, 'setup interface before exposing connections with interface.setup()'
        ready_connections = []
        for connection in self.connections:
            ready_connections.append(connection.open())
        return ready_connections


    def setup(self):
        for connection in self.connections:
            self._setup_connection(connection)
