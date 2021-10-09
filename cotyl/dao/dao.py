"""
DAO base class

The DAO object handles:
    Register/identify nodes
    Visualize the DAO (draw graph)
    Run the DAO (Starts all interfaces)
"""

from cotyl.node.node import Node
from cotyl.network.dao_network_node import build_dao_network_node_from_connections
from cotyl.dao.graph import DGraph
from cotyl.utils import coalesce, filter_dict

from typing import List

class DAO():
    
    def __init__(self, nodes: List[Node], **kwargs) -> None:
        self.graph = DGraph()
        self.nodes = tuple(nodes)
        self.__registry_hist = {}
        self.connections = []
        self.kwargs = kwargs

        self.register_all(**kwargs)
        

    def __index_node(self, node: Node):
        # Index the node in a registration history for future lookup and to prevent
        # repeated registrations.
        try:
            max_node_index = max(self.__registry_hist.values())
        except:
            max_node_index = None
        self.__registry_hist[node.node_id] = (coalesce(max_node_index, 0), node)


    def register(self, node: Node, **kwargs):
        # Setup node and assign unique identifiers, parameters
        node = self.setup_node(node, **kwargs)

        # Check registration status is false
        if node.node_id in self.__registry_hist.keys():
            raise ValueError("Node already registered")
        
        # Register the Node and index its position 
        self.graph.register_node(node)
        self.__index_node(node)

        # Dump node connections
        self.connections.extend(node.connections)
        
    
    def register_all(self, **kwargs):
        def _register_node(node, **kwargs):
            self.register(node=node, **kwargs)
        list(map(_register_node, self.nodes))
        self._inject_runtime_nodes()



    def setup_node(self, node: Node) -> Node:
        # Setup DAO controlled node parameters.
        node.node_id = hash(node)
        node.setup()
        return node


    def _inject_runtime_nodes(self):
        # Build central networking node and add to network
        dao_network_node = build_dao_network_node_from_connections(self.connections)
        self.setup_node(dao_network_node)
        self.graph.register_node(dao_network_node)
        

    def visualize(self):
        viz_kwargs = filter_dict(
            self.kwargs,
            [
                'with_labels'
            ]
            )
        self.graph.draw(**viz_kwargs)


    def run(self):
        raise NotImplementedError("Run Not Ready Yet")
