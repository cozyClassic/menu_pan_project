from pydantic import BaseModel, Field
from bson.objectid import ObjectId

from db.db import PyObjectId

class BrandSchema(BaseModel):
    id: PyObjectId = Field(
        default_factory=PyObjectId,
        alias="_id")
    name:str
    banner_url:str|None
    banner_link:str|None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "스타벅스",
                "banner_url": "https://www.naver.com",
                "banner_link": "https://www.naver.com",
            }
        }

class UpdateBrandSchema(BaseModel):
    name:str|None
    banner_url:str|None
    banner_link:str|None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "스타벅스",
                "banner_url": "https://www.naver.com",
                "banner_link": "https://www.naver.com",
            }
        }
