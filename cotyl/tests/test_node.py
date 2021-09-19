# test_node.py

from cotyl.node.node import Node

def test_node_limited_construction():
    n = Node(name='testnode')
    assert n is not None
    assert type(n) == Node