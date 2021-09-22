"""
Interface Base

Interfaces handle ingress and egress through nodes via network and local OS messaging.
"""

from cotyl.message.message import Message
from pydantic import BaseModel
from typing import List, Any, Optional

from cotyl.interface.connection import Connection
from cotyl.node.router import Router

import logging


class InterfaceBase(BaseModel):
    name: Optional[str]
    connections: Optional[List[Connection]]

    class Config:
        arbitrary_types_allowed = True


class Interface():
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


    def setup(self, router:Router, **kwargs):
        self.router = router
        for connection in self.connections:
            self._setup_connection(connection, **kwargs)
        self.__setup = True


    def up(self, **kwargs):
        raise NotImplementedError(f'Up not implemented for interface {self.name}')



#######################
### Dummy Interface ###
#######################
# Example of creating an interface with connection to router
from functools import partial


def log(m, logger=logging.getLogger(__name__), router=None):
    logger.info(m)
    

class LogInterfaceConnection(Connection):
    def __init__(self, **data: Any) -> None:
        data = {
            'name':'log_connection',
            'schema_name':'NULL_SCHEMA',
            'destination':'logger',
            'protocol':'logging',
        }
        super().__init__(**data)
        self.interface_fn = None

    def open(self):
        return self

    def push(self, m: Message):
        print(m.data)
        return self.interface_fn(m.data)



class LogInterface(Interface):
    def __init__(self, **data: Any) -> None:
        super().__init__(name='log_interface', connections=[LogInterfaceConnection()])

    def up(self):
        pass

    def setup(self, router: Router):
        super().setup(router)
        for connection in self.connections:
            connection.interface_fn = partial(log, router=router)   # Interface will not hold the transform function.
                                                                    # The router is being passed to the log function 
                                                                    # to demonstrate router availability in building
                                                                    # endpoints, etc.
