from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from common import Base
from typing import List

class Profile(Base):
    __tablename__ = 'g_profile'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, autoincrement=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(nullable=False, unique=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("g_user.id"), nullable=False)
    addresses: Mapped[List["Address"]] = relationship(back_populates='profile')
    user: Mapped["User"] = relationship(back_populates='profile')

    def __init__(self, email: str, phone: str, addresses: list["Address"]):
        self.email = email
        self.phone = phone
        self.addresses = addresses