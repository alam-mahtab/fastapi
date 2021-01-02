from datetime import date
from typing import List, Optional

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class User(BaseModel):
    username: str
    email: Optional[str] = None
    phone: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserInDB(User):
    hashed_password: str

class UserCreate(User):
    password: str
    confirm_password : str
    email: str
    first_name :str
    last_name : str
    phone : str
    dateofbirth : date

class UserDB(User):
    pass

