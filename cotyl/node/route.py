"""
Route

Constructor for building node routes
"""

from pydantic import BaseModel
from cotyl.node.transform import Transform
from cotyl.interface.connection import Connection


class Route(BaseModel):
    
    transform: Transform
    egress: Connection

    class Config:
        arbitrary_types_allowed = True

    @property
    def destination(self):
        return self.egress.destination

    @property
    def schema_name(self):
        return self.egress.schema_name

    class Config:
        arbitrary_types_allowed = True

    def __call__(self, m):
        return self.egress(self.transform(m))