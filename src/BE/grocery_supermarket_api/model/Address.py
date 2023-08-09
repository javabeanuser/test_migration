from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from common import Base


class Address(Base):
    __tablename__ = 'g_address'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, autoincrement=True)
    country: Mapped[str] = mapped_column(nullable=False, unique=False)
    city: Mapped[str] = mapped_column(nullable=False, unique=False)
    street: Mapped[str] = mapped_column(nullable=False, unique=False)
    profile_id: Mapped[int] = mapped_column(ForeignKey("g_profile.id"), nullable=False)
    profile: Mapped["Profile"] = relationship(back_populates='addresses')

    def __init__(self, country: str, city: str, street: str):
        self.country = country
        self.city = city
        self.street = street
