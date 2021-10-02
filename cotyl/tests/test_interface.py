# test_interface.py

import pytest

from cotyl.interface.interface import Interface, LogInterface
from cotyl.interface.connection import LogConnection
from cotyl.node.router import Router
from cotyl.message.message import Message

import logging
logger = logging.getLogger(__name__)

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


def test_connection_push():
    connection = LogConnection()
    message = Message(schema_name='test', data='test_message', destination='log')
    connection.push(message)
    logger.info('test message log')


def test_log_interface_all_actions():
    r = Router()
    i = LogInterface()
    i.setup(router=r)
    i.up()
    log_connection = i.expose()[0]
    message = Message(schema_name='test', data='log_test_message', destination='log')
    log_connection.push(message)