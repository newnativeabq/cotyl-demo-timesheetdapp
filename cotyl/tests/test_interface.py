# test_interface.py

import pytest

from cotyl.interface.interface import Interface
from cotyl.interface.connection import LogConnection, Connection
from cotyl.node.router import Router
from cotyl.message.message import Message

import logging


def test_interface_limited_construction():
    i = Interface(name='testinterface', connections=[LogConnection()])


def test_interface_setup():
    i = Interface(name='testinterface', connections=[LogConnection()])
    r = Router()
    i.setup(router=r)


def test_interface_expose_first_fail():
    i = Interface(name='testinterface', connections=[LogConnection()])
    try:
        connections = i.expose()
    except:
        r = Router()
        i.setup(router=r)
        connections = i.expose()
        assert type(connections[0]) == LogConnection


def test_connection_push(caplog):
    caplog.set_level(logging.DEBUG, logger=__name__)
    connection = LogConnection()
    message = Message(schema_name='test', data='test_message')
    connection.push(message)