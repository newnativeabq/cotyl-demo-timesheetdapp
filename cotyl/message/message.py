"""
Message wrapper class.  Contains message metadata for routing and
type introspection as well as serialization/deserialization methods
where requried.
"""

from typing import Any


class Message():
    def __init__(self, schema_name: str, data: Any) -> None:
        self.schema_name = schema_name
        self.data = data

    def serialize(self, data: Any):
        raise NotImplementedError(f'serialization method not defined for {self.schema_name}')

    def deserialize(self):
        raise NotImplementedError(f'deserialize method not defined for {self.schema_name}')