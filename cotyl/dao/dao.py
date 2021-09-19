"""
DAO base class

The DAO object handles:
    Register/identify nodes
    Visualize the DAO (draw graph)
    Run the DAO (Starts all interfaces)
"""

from cotyl.node.node import Node
from cotyl.dao.graph import DGraph

class DAO():
    def __init__(self) -> None:
        self.graph = DGraph()

    def register(self, node: Node):
        pass