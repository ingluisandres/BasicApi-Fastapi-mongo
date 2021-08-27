from pydantic import BaseModel
from typing import Optional


class Athletes(BaseModel):
    _id: Optional[str]
    Name: str
    NOC: str
    Discipline: str


class User(BaseModel):
    email: str
    password: str

class Login(BaseModel):
    email: str
    password: str
    class Config():
        orm_mode = True

class Token(BaseModel):
    access_token: str
    tocken_type: str

class TokenData(BaseModel):
    admin_name: Optional[str] = None    