from typing import List

from repository import AbstractRepository, T
from model import Item

class ItemRepository(AbstractRepository[Item]):

    def query(self, item, limit = 10) -> List[T]:
        return super().query(item, limit)

    def get(self, item) -> Item:
        return super().get(item)

    def put(self, item) -> bool:
        return super().put(item)

    def upd(self, item, field_name, value) -> bool:
        return super().upd(item, field_name, value)

    def dlt(self, item) -> bool:
        return super().dlt(item)