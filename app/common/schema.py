from pydantic import BaseModel
from datetime import datetime

class RemovableSchema(BaseModel):
    created_at : datetime
    removed_at : datetime | None
