from sqlalchemy.orm import Mapped, mapped_column,relationship
from common import Base

class PriceCode(Base):
    __tablename__ = 'g_price_code'

    id: Mapped[int]= mapped_column(primary_key=True, nullable=False, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    sign: Mapped[str] = mapped_column(nullable=False, unique=True)

    def __init__(self, name:str = None, sign:str = None, id = None):
        self.name = name
        self.sign = sign
        self.id = id