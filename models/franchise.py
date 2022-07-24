from sqlalchemy import Column, Integer, String
from .common import Removable


class Franchise(Removable):
    __tablename__ = "franchise"

    id = Column(Integer(), primay_key=True)
    name = Column(String(100), nullable = False)
    group_id = Column(Integer(), nullable = True)

    def __repr__(self):
        return f"Brand {self.name}"