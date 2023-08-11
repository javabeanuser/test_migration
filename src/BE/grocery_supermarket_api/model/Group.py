from sqlalchemy.orm import Mapped, mapped_column, relationship
from common import Base

class Group(Base):
    __tablename__ = 'g_group'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)

    def __init__(self, name= None, id = None):
        self.name = name
        self.id = id