from typing import List

from fastapi import APIRouter

from brand.schema import BrandSchema
from db.db import db

brand_router = APIRouter(
    prefix="/admin/brand"
)

@brand_router.get(
    "/",
    response_model=List[BrandSchema])
async def get_brand():
    brands = await db["brand"].find().to_list(100)

    return brands
