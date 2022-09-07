from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from brand.controller import brand_router


app = FastAPI()
app.include_router(brand_router)


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
