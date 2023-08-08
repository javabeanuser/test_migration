from sqlalchemy.orm import Mapped, mapped_column,relationship
from common import Base
from model.user_role import UserRole

class Role(Base):
    __tablename__ = 'g_role'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    role: Mapped[UserRole] = mapped_column(nullable=False, unique=True)
    user: Mapped["User"] = relationship(back_populates='role')

    def __init__(self, name:str, role: UserRole):
        self.name = name
        self.role = role