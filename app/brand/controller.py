from typing import List

from fastapi import APIRouter, HTTPException

from brand.schema import BrandSchema, UpdateBrandSchema
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

@brand_router.post(
    "/",
    response_model=BrandSchema,
    status_code=201
)
async def create_brand(brand:UpdateBrandSchema):
    brand = dict(brand)
    db_object = await db["brand"].insert_one(brand)
    brand["_id"] = str(db_object.inserted_id)
    
    return brand

@brand_router.delete(
    "/{_id}",
    status_code=204
)
async def delete_brand(_id:str):
    delete_result = await db["brand"].delete_one({"_id":_id})

    if delete_result.deleted_count == 1:
        return "success"

@brand_router.put(
    "/{_id}",
    status_code=204
)
async def patch_brand(_id:str, brand:UpdateBrandSchema):
    new_brand = dict(brand)
    update_result = await db["brand"].update_one({"_id": id}, {"$set": brand})
    
    if (
        (len(new_brand) > 0) and 
        (update_result.modified_count == 1) and 
        (updated_student := await db["brand"].find_one({"_id": id})) is not None
        ):
            return updated_student    

    raise HTTPException(satus_code=404, detail="Item not found")
    
