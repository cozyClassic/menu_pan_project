from sqlalchemy import Column, ForeignKey, Integer, String

from ..common.model import Removable
from db.db import Base


class Category1(Removable, Base):
    __tablename__ = "category1"

    id = Column(Integer(), primay_key=True)
    name = Column(String(100), nullable = False)
    franchise_id = Column(Integer(), ForeignKey("franchise.id"), nullable = True)

    def __repr__(self):
        return f"Category1 {self.name}"

class Category2(Removable, Base):
    __tablename__ = "category2"

    id = Column(Integer(), primay_key=True)
    name = Column(String(100), nullable = False)
    category1_id = Column(Integer(), ForeignKey("category1.id"), nullable = True)

    def __repr__(self):
        return f"Category2 {self.name}"

class Menu(Removable):
    __tablename__ = "menu"
    name = Column(String(100), nullable=False)
    category2_id = Column(Integer(),ForeignKey("category2.id"), nullable = True)
    price = Column(Integer(100), nullable = False)
    menu_image_url = Column(String(255), nullable = True)

class MenuDetail(Removable, Base):
    __tablename__ = "menu_detail"
    calorie = Column()
    sodiume = Column()
    protein = Column()
    s_fat = Column()
    un_s_fat= Column()
    caffein = Column()
    sugars = Column()
    allegry = Column()
