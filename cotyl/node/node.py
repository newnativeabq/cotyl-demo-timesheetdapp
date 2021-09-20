"""
Node

Main class for constructing DAO nodes.
Here, nodes are defined as a set of ingress and egress
interfaces, a router, and routes.  A user will define routes
in terms of named interfaces and transforms and the node will handle
orchestration of message transforms and responses through the 
ingresses.
"""

from pydantic import BaseModel
from typing import List, Optional, Any
from cotyl.node.router import Router
from cotyl.node.route import Route
from cotyl.interface.interface import Interface

import logging
logger = logging.getLogger(__name__)


class NodeBase(BaseModel):
    name: str
    router: Optional[Router]
    interfaces: Optional[List[Interface]]
    routes: Optional[List[Route]]

    class Config:
        arbitrary_types_allowed = True
    
    

class Node():
    def __init__(self, **data: Any) -> None:
        self.base = NodeBase(**data)
        self.__node_id = None
        self.__node_id_set = False


    @property
    def name(self):
        return self.base.name


    @property
    def router(self):
        return self.base.router


    @property
    def interfaces(self):
        return self.base.interfaces


    @property
    def routes(self):
        return self.base.routes


    @property 
    def node_id(self):
        if self.__node_id_set:
            return self.__node_id


    @node_id.setter
    def node_id(self, value: str):
        if self.__node_id_set:
            raise ValueError('Cannot reset node ID')
        self.__node_id_set = True
        self.__node_id = value