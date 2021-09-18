"""
Interface Base

Interfaces handle ingress and egress through nodes via network and local OS messaging.
"""

from pydantic import BaseModel


class Interface(BaseModel):
    name: str