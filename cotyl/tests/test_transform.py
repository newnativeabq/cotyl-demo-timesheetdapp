# test_transform.py

from cotyl.node.transform import Transform


def test_make_transform():
    t = Transform(
        name='testtransform',
        fn=lambda x: x,
        validator=lambda x: x
    )
    assert t(1) == 1

