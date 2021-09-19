"""
DAO Graph

Handles construction and visualization of graph representation.
"""

import networkx as nx
from cotyl.node.node import Node

import logging
logger = logging.getLogger(__name__)


class DGraph():
    def __init__(self):
        self.__g = nx.MultiDiGraph()
        
    def register_node(self, node: Node):
        def _get_edges_from_routes(node: Node):
            logger.warn("Not Implemented.  Unable to introspect edges from node just yet.")

        self.__g.add_node(node.node_id)
        # self.__g.add_edges_from(_get_edges_from_routes(node))  ## TODO: Get Edges from routes
        logging.debug(f"added {node.name}:{node.node_id}, {_get_edges_from_routes(node.routes)}")
        
    @property
    def num_nodes(self):
        return self.__g.number_of_nodes()
    
    @property
    def num_edges(self):
        return self.__g.number_of_edges()
    
    @property
    def nodes(self):
        return self.__g.nodes
    
    @property
    def edges(self):
        return self.__g.edges
    
    def get_edge(self, a, b):
        return self.__g[a][b]
    
    def draw(self, *args, **kwargs):
        logger.warn("visualization not fully integrated.  Only outputting dot format")
        pydot = nx.nx_pydot.write_dot(self.__g, 'viz.dot')