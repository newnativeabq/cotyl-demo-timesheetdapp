# test_node.py

from cotyl.node.node import Node
from cotyl.interface.interface import Interface
from cotyl.interface.connection import NullConnection


def test_node_limited_construction():
    n = Node(name='testnode')
    assert n is not None
    assert type(n) == Node


def test_node_connections():
    con = NullConnection()
    ifc = Interface(connections=[con])
    node = Node(name='test', interfaces=[ifc])
    node.setup()
    assert len(node.connections) == 1