from model.profile import Profile
from model.address import Address
from model.group import Group
from model.item import Item
from model.price_code import PriceCode
from model.role import Role
from model.user import User
from model.user_role import UserRole
from model.order import Order
from sqlalchemy import create_engine
from config import Config
from log import Logger
from common import Base

from model import Address, Group, UserRole, Role, Profile, PriceCode, Item, User


engine = create_engine(Config.get_database_url(), echo=True)
Logger.info(f"Create schema for Database {engine}")
Base.metadata.create_all(engine, checkfirst=True)
