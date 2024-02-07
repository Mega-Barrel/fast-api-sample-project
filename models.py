"""Pydantic Models"""

from pydantic import BaseModel #pylint: disable=E0401

class Todo(BaseModel):
    """
    Todo Parameters
    """
    id: int
    item: str
