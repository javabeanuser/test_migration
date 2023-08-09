from typing import  Generic, TypeVar
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from config import Config
from abc import ABC, abstractmethod
from typing import List
from log import Logger

T = TypeVar("T")

class AbstractRepository(ABC, Generic[T]):
    def __init__(self, debug = False):
        engine = create_engine(Config.get_database_url(), echo=debug)
        self.session = Session(engine)
    @abstractmethod
    def query(self,obj, limit: int = 10) -> List[T]:
        """
        Gets list of the objects from the table
        @object - object
        @limit - maximum List size to fetch
        """
        Logger.debug(f"Query for type {type(obj)}")
        if obj.id or obj.name:
            return self.session.query(type(obj)).where((type(obj).id == obj.id) | (type(obj).name == obj.name)).limit(limit).all()
        else:
            return self.session.query(type(obj)).limit(limit).all()
    @abstractmethod
    def get(self,obj) -> T:
        """
        Gets one object from the table
        @object - object
        """
        Logger.debug(f"Get for id={obj.id} with type {type(obj)}")
        return self.session.get(type(obj), obj.id)
    @abstractmethod
    def put(self,obj) -> bool:
        """
        Puts an object in table
        @object - object
        """
        try:
            self.session.add(obj)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            Logger.error(f"Error on putting object into the table {type(obj)}: {e}")
            return False
    @abstractmethod
    def upd(self, obj, field_name, value) -> bool:
        """
        Updates an object in table by id to avoid batch update, the object field id is required to be set
        @object - object
        @field_name - name of the field to be updated
        @value - new value
        """
        try:
            print(1)
            self.session.query(type(obj)).\
                filter(type(obj).id == obj.id).\
                update({f'{field_name}': value})
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            Logger.error(f"Error on updating object from the table {type(obj)}: {e}")
            return False
    @abstractmethod
    def dlt(self, obj) -> bool:
        """
        Deletes an object in table by id to avoid batch delete, the object field id is required to be set
        @object - object
        """
        try:
            self.session.filter(type(obj).id == obj.id).delete(obj)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            Logger.error(f"Error on deleting object from the table {type(obj)}: {e}")
            return False