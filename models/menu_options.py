from sqlalchemy import Boolean, Column, ForeignKey, Integer
from .common import Removable


class MenuOptions(Removable):
    __tablename__ = "menu_options"
    name = Column()
    optional = Column(Boolean(), nullable=False)
    priority = Column(Integer(), nullable=True)
    menu_id = Column(Integer(),ForeignKey("menu.id"), nullable = True)


class MenuOptionDetails(Removable):
    __tablename__ = "menu_option_details"
    name = Column()
    price = Column(Integer(100), nullable = False)
    priority = Column(Integer(), nullable=True)
    option_id = Column(Integer(),ForeignKey("menu_options.id"), nullable = True)