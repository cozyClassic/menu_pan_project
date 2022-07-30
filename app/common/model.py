from sqlalchemy import *
from datetime import datetime
from ...db.db import Base

class Removable(Base):
    created_at = Column(DateTime(), default=datetime.now, nullable=False)
    removed_at = Column(DateTime())

    def remove(self):
        self.removed_at = datetime.now()