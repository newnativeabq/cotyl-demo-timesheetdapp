# WebServer Node
# Entrypoint into this dApp


from requests.sessions import Request
from cotyl.node.node import Node
from cotyl.node.router import Router
from cotyl.interface.interface import Interface
from cotyl.interface.connection import Connection
from cotyl.utils import filter_dict

from typing import Any

from nodes.node_webserver_webapp import build_app, serve_app

import requests

# Define Ingress Interface
class WebNodeWebInterface(Interface):
    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        

    def _setup_connection(self, connection: Connection, **kwargs):
        fkwargs = filter_dict(kwargs, ['host', 'port'])
        connection.base.protocol = 'http'
        connection.url = ':'.join(['http://'+fkwargs['host'], fkwargs['port']])
        return super()._setup_connection(connection)

    def setup(self, router: Router, host='127.0.0.1', port='8080'):
        return super().setup(router, host=host, port=port)

    def up(self, **kwargs):
        web_kwargs = filter_dict(
            kwargs, 
            [
                'host',
                'port',
            ])
        app = build_app()
        process = serve_app(app, **web_kwargs)


# Define the flavor of connections we expect from the webserver
class WebNodeWebConnection(Connection):
    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        assert 'request' in data, 'Must pass in request function'
        self.request = data['request']

    def open(self):
        return self
    
    def push(self, *args, **kwargs):
        if hasattr(self, 'request'):
            return self.request(self.url, *args, **kwargs)  ## return alows arbitrary chain through DAO


def simple_get(url, *args, **kwargs):
    return requests.get(url)


# Construct the node
web_interface = WebNodeWebInterface(
    name='WebInterface',
    connections=[WebNodeWebConnection(name='get_root', request=simple_get)]
)

webnode = Node(
    name='node_webserver',
    interfaces=[web_interface],
    router=Router()
)