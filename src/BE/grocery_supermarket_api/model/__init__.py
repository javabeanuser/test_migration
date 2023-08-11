from model.Profile import Profile
from model.Address import Address
from model.Group import Group
from model.Item import Item
from model.PriceCode import PriceCode
from model.Role import Role
from model.User import User
from model.UserRole import UserRole
from model.OrderStatus import OrderStatus
from model.Order import Order
from model.Status import Status
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from config import Config
from log import Logger
from common import Base

engine = create_engine(Config.get_database_url(), echo=False)
Logger.info(f"Create schema for Database {engine}...")
Base.metadata.create_all(engine, checkfirst=True)
Logger.info(f"Created schema for Database {engine}")

session = Session(engine)

try:
    admin = Role("admin", 'ADMIN')
    moderator = Role("moderator", 'MODERATOR')
    user = Role("user", 'USER')

    session.add_all([admin, moderator, user])
    session.commit()
    Logger.info("Added roles in g_role")
except Exception as e:
    session.rollback()
    Logger.warn(f"Roles exist in the table g_role")
    Logger.debug(f"Roles exist in the table g_role: {e}")

try:
    dollar = PriceCode("dollar", "$")
    session.add_all([dollar])
    session.commit()
    Logger.info("Added price codes in g_price_code")
except Exception as e:
    session.rollback()
    Logger.warn(f"Price Codes exist in the table g_price_code")
    Logger.debug(f"Price Codes exist in the table g_price_code: {e}")


try:
    session.add_all([Group("Grocery"),
                     Group("Home"),
                     Group("Car"),
                     Group("Meat")
                     ])
    session.commit()
    Logger.info("Added groups in g_group")
except Exception as e:
    session.rollback()
    Logger.warn(f"Groups exist in the table g_group")
    Logger.debug(f"Groups exist in the table g_group: {e}")


try:
    session.add_all([Item(group_id=1, name="Apple", description="An Apple", price_code_id=1, price=10),
                     Item(group_id=1, name="Kiwi", description="A Kiwi", price_code_id=1, price=12),
                     Item(group_id=1, name="Carrot", description="A Carrot", price_code_id=1, price=5),
                     Item(group_id=1, name="Watermelon", description="A Watermelon", price_code_id=1, price=2)
                     ])
    session.commit()
    Logger.info("Added base items in g_item")
except Exception as e:
    session.rollback()
    Logger.warn(f"Items exist in the table g_item")
    Logger.debug(f"Items exist in the table g_item: {e}")

