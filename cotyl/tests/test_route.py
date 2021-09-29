# test_route.py


from cotyl.node.route import Route
from cotyl.node.transform import null_transform
from cotyl.interface.connection import NullConnection


def test_make_null_route():
    r = Route(
        transform=null_transform,
        egress=NullConnection()
    )
    assert r(1) == 1