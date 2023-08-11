from typing import  Generic, TypeVar
from abc import ABC

Repository = TypeVar("T")
Type = TypeVar("T")

class AbstractService(ABC):
    def get(id=None, name=None, limit=10):
        raise NotImplemented
    def put(obj=None, *arg, **kwarg):
        raise NotImplemented
    def upd(id):
        raise NotImplemented
    def dlt(id):
        raise NotImplemented