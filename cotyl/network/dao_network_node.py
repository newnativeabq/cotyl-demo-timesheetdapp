"""
DAO Network Node

Single point of egress for all nodes to automatically route to known
ingress connections via metadata, message type.
"""

from multiprocessing import Value
from cotyl.node.node import Node
from cotyl.node.router import Router
from cotyl.interface.interface import Interface
from cotyl.interface.connection import Connection
from cotyl.message.message import Message
from typing import Any, List




## Construct the interface ##
class DAONetworkInterface(Interface):
    
    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
    
    def _setup_connection(self, connection: Connection):
        connection.router = self.router
        return super()._setup_connection(connection)
    
    def setup(self, router: Router, host=None, port=None):
        return super().setup(router, host=host, port=port)

    def up(self):
        pass


## Construct the connections to the interface ##
class DAONetworkConnection(Connection):
    
    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        self._router = None

    @property
    def router(self):
        return self._router

    @router.setter
    def router(self, router: Router):
        if self._router is None:
            self._router = router
        else:
            raise ValueError('Router already assigned')
    
    def open(self):
        return self
    
    def push(self, m: Message) -> Message:
        assert type(m) == Message
        return self.router(m)





## Construct the Node ##

dao_interface = DAONetworkInterface(
    name='DAOInterface',
    connections=[
        DAONetworkConnection(name='DAOConnection')
    ]
)


def build_dao_network_node_from_connections(connections: List[Connection]):
    
    def _build_router_from_connections(connections) -> Router:
        r = Router()
        for connection in connections:
            route = _build_default_route(connection)

    return Node(
        name='DAO Network',
        interfaces=[dao_interface],
        router=_build_router_from_connections(connections)
    )