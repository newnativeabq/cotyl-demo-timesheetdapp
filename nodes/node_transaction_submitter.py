# Transaction Submission Node
# Interacts with cardano CLI/cardano node where needed


from cotyl.node.node import Node


transaction_submitter = Node(
    name='node_transaction_submitter'
)