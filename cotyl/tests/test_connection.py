# test_connection.py

from cotyl.interface.connection import Connection

def test_make_simple_connection():
    c = Connection(
        name='test',
        schema_name='testschema',
        destination='testloc',
        protocol='testprot'
    )