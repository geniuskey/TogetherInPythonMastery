# schemas.py
from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    name: str
    age: int
    email: Optional[str] = None

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
