from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from common import Base

class Order(Base):
    __tablename__ = 'g_order'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, autoincrement=True)
    order_number: Mapped[int] = mapped_column(index=True)
    item_id: Mapped[int] = mapped_column(ForeignKey("g_item.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("g_user.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates='orders')

    def __init__(self, order_number, item_id):
        self.order_number = order_number
        self.item_id = item_id