from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

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

@app.get("/admin/brand")
async def get_brand(response:Response):
  response.headers["Access-Control-Allow-Origin"] = "*"
  return   {"data":[{
  "name" : "스타벅스",
  "banner_url" : "https://www.naver.com",
  "banner_link" : "https://www.naver.com"
  },
  {
    "name" : "한솥도시락",
    "banner_url" : "https://www.naver.com",
    "banner_link" : "https://www.naver.com"
    }]
    }