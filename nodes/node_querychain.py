# Query Chain Node
# Interfaces with exterior Dandelion API services


from cotyl.node.node import Node
from cotyl.node.router import Router
from cotyl.interface.interface import Interface
from cotyl.interface.connection import Connection


## Define Ingress Interface ##


## Define Ingress Connections ##


## Define Egress Connections ##

# Egress connections from the query node will leave the DAO.
# The DAO is 'aware' of this boundary as the egress connections
# are not being used exposed as ingress connections elsewhere.





querychain = Node(
    name='node_querychain'
)