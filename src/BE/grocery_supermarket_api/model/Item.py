from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from common import Base
from model.Group import Group
from model.PriceCode import PriceCode

class Item(Base):
    __tablename__ = 'g_item'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    group_id: Mapped[int] = mapped_column(ForeignKey(Group.id), nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    price_code_id: Mapped[int] = mapped_column(ForeignKey(PriceCode.id))
    price: Mapped[float] = mapped_column(nullable=False, default=0)
    image_bytes: Mapped[bytes] = mapped_column(nullable=True)
    price_code: Mapped["PriceCode"] = relationship(backref="price_code_id")
    group: Mapped["Group"] = relationship(backref="group_id")
    def __init__(self,
                 id = None,
                 group_id: str = 1,
                 name: str = None,
                 description: str = None,
                 price_code_id: int = 1,
                 price: int = 0,
                 image_bytes = None):
        if id != None: self.id = id
        self.group_id = group_id
        self.name = name
        self.description = description
        self.price_code_id = price_code_id
        self.price = price
        self.image_bytes = image_bytes