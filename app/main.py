from fastapi import Depends, FastAPI

app = FastAPI()

from franchise.model import Franchise


@app.get("/")
async def root():
    return {"message": "Hello World"}
