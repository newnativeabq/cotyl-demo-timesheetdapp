"""
Router - node

Introspects messages and calls appropriate route.
"""

from cotyl.node.route import Route
from cotyl.message.message import Message


class Router():

    def __init__(self) -> None:
        self.__routes = {}


    def add_route(self, route: Route):
        ckey = route.destination+route.schema_name
        assert ckey not in self.__routes.keys(), 'only one route per schema allowed per router'
        self.__routes[ckey] = route


    def __call__(self, m: Message) -> Message:
        ckey = m.destination+m.schema_name
        route = self.__routes[ckey]
        return route(m)