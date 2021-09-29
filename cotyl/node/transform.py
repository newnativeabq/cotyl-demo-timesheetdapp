"""
Transform

base class for protected function caller and metadata updates.
"""

from pydantic import BaseModel
from typing import Any


class Transform(BaseModel):
    
    name: str
    validator: Any
    fn: Any

    def __call__(self, m):
        return self.fn(self.validator(m))



null_transform = Transform(
    name = 'NullTransform',
    validator = lambda x: x,
    fn = lambda x: x,
)