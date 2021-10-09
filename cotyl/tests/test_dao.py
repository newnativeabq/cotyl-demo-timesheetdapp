# test_dao.py

from cotyl.network.dao_network_node import build_dao_network_node_from_connections
from cotyl.interface.connection import NullConnection
from cotyl.interface.interface import LogInterface
from cotyl.node.node import Router, Route

import logging

from cotyl.node import router 
logger = logging.getLogger(__name__)


def test_dao_network_node():
    node = build_dao_network_node_from_connections([NullConnection()])
    node.setup()


def test_simple_dao():
    intc = LogInterface()
    intc.connections.append(NullConnection())
    router = Router()