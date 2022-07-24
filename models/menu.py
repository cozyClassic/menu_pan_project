from sqlalchemy import Column, ForeignKey, Integer, String

from .common import Removable


class Category1(Removable):
    __tablename__ = "category1"

    id = Column(Integer(), primay_key=True)
    name = Column(String(100), nullable = False)
    franchise_id = Column(Integer(), ForeignKey("franchise.id"), nullable = True)

    def __repr__(self):
        return f"Category1 {self.name}"

class Category2(Removable):
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

