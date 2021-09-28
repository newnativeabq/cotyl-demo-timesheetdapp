# Building the TimeSheet DAO

from cotyl.dao.dao import DAO

from nodes.node_webserver import webnode
from nodes.node_transaction_builder import transaction_builder
from nodes.node_querychain import querychain
from nodes.node_transaction_submitter import transaction_submitter


dao = DAO(
    nodes = [
        webnode,
        transaction_builder,
        querychain,
        transaction_submitter,
        ]
)


if __name__ == "__main__":
    print('Hello DAO')
    dao.visualize()