from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


# 사용자 데이터 모델 정의
class User(BaseModel):
    name: str
    age: int
    email: Optional[str] = None


# 사용자 데이터 저장소
users = {}


# 사용자 생성
@app.post("/users/{user_id}")
async def create_user(user_id: int, user: User):
    if user_id in users:
        return {"error": "User already exists"}
    users[user_id] = user
    return users[user_id]


# 사용자 조회
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id not in users:
        return {"error": "User not found"}
    return users[user_id]


# 사용자 업데이트
@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    if user_id not in users:
        return {"error": "User not found"}
    users[user_id] = user
    return users[user_id]


# 사용자 삭제
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    if user_id not in users:
        return {"error": "User not found"}
    del users[user_id]
    return {"message": "User deleted"}
