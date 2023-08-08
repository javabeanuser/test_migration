from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from common import Base
from model.group import Group
from model.price_code import PriceCode

class Item(Base):
    __tablename__ = 'g_item'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    group: Mapped[int] = mapped_column(ForeignKey(Group.id), nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column()
    price_code_id: Mapped[int] = mapped_column(ForeignKey(PriceCode.id))
    price: Mapped[float] = mapped_column(nullable=False, default=0)
    image_bytes: Mapped[bytes] = mapped_column()
    price_code: Mapped["PriceCode"] = relationship(back_populates="item")

    def __init__(self, group:str, name:str, description: str, price_code_id: int, price: int, image_bytes):
        self.group = group
        self.name = name
        self.description = description
        self.price_code_id = price_code_id
        self.price = price
        self.image_bytes = image_bytes