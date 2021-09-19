"""
Router - node

Introspects messages and calls appropriate route.
"""

from pydantic import BaseModel
from cotyl.node.route import Route
from cotyl.message.message import Message


class Router(BaseModel):
    def __init__(self) -> None:
        self.__routes = {}

    def add_route(self, route: Route, schema: str):
        assert schema not in self.__routes.keys(), 'only one route per schema allowed per router'
        self.__routes[schema] = route

    def __call__(self, m: Message):
        route = self.__routes[m.schema]
        route(m)