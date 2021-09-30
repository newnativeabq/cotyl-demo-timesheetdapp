# test_router.py

from cotyl.message.message import Message
from cotyl.node.router import Router
from cotyl.node.route import Route
from cotyl.node.transform import null_transform
from cotyl.interface.connection import NullConnection

import pytest 


@pytest.fixture
def null_route():
    return Route(
        transform=null_transform,
        egress=NullConnection()
    )

@pytest.fixture
def simple_message():
    return Message(
        schema_name='any',
        destination='return',
        data={'testkey': 'testval'}
    )



def test_make_simple_router(null_route, simple_message):
    rt = Router()
    rt.add_route(null_route)
    assert rt(simple_message).data == simple_message.data

