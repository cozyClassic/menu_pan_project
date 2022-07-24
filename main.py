import os

from fastapi import Depends, FastAPI

from config import Settings

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/subway/category")
async def subway_cateogry():
    category = [
    "프로모션",
    "샌드위치",
    "샐러드",
    "랩, 기타",
    "사이드, 음료"
    ]
    return {"category":category}
# 서브웨이 로고 이미지 : https://www.subway.co.kr/images/common/logo_w.png
@app.get("/subway/category")
async def subway_cateogry():
    sandwich=[
    "스파이시 쉬림프",
    "스파이시 쉬림프 아보카도",
    "쉬림프",
    "터키 베이컨 아보카도",
    "로티세리 바비큐 치킨",
    "스테이크 & 치즈",
    "K-바비큐",
    "풀드 포크 바비큐",
    "써브웨이 클럽",
    "스파이시 이탈리안",
    "치킨 데리야끼",
    "비엘티",
    "이탈리안비엠티",
    "미트볼",
    "터키",
    "참치",
    "햄",
    "에그마요",
    "베지",
    "로스트 치킨"
    ]
    return {"sandwich":sandwich}