from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from common import Base
from typing import List

class User(Base):
    __tablename__ = 'g_user'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("g_role.id"), nullable=False, default=2)
    password: Mapped[str] = mapped_column(nullable=False)
    orders: Mapped[List["Order"]] = relationship(back_populates='user')
    profile: Mapped["Profile"] = relationship(back_populates='user')
    role: Mapped["Role"] = relationship(back_populates='user')

    def __init__(self, name, role_id, password, orders: list, profile):
        self.name = name
        self.role_id = role_id
        self.password = password
        self.orders = orders
        self.profile = profile