from pprint import pprint
from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from brand.schema import BrandSchema
from db.db import db

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/x")
async def test():
    data = []
    cursor = db.brand.find()
    for document in await cursor.to_list(length=100) :
        data.extend([document])
    print(data)
    return

@app.get(
    "/admin/brand",
    response_model=List[BrandSchema])
async def get_brand():
    brands = await db["brand"].find().to_list(100)

    return brands
