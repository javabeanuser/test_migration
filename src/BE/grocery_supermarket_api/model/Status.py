from common import Base
from model import OrderStatus
from sqlalchemy.orm import Mapped, mapped_column,relationship

class Status(Base):
    __tablename__ = 'g_status'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, autoincrement=True)
    description: Mapped[str] = mapped_column(nullable=False, unique=True)
    status: Mapped[OrderStatus] = mapped_column(nullable=False, unique=True)

    def __init__(self, description:str, status: OrderStatus):
        self.description = description
        self.status = status