from service import AbstractService
from repository import ItemRepository
from model import Item


class FakeService(AbstractService):
    def get(id=None, name=None, limit=10):
        return super().get(name, limit)

    def put(obj=None, *arg, **kwarg):
        return super().put(*arg, **kwarg)

    def upd(id):
        return super().upd()

    def dlt(id):
        return super().dlt()

    def get_grocery_init_data(self):
        items = []
        for item in ItemRepository().query(Item()):
            items.append(item.__repr__())
        rsdata = {
            'status': 'Success',
            'data': [
                {
                    'name': "Grocery",
                    'items': items
                }
            ]
        }
        return rsdata