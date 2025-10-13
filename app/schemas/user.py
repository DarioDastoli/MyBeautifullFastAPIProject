from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: int
    username: str
    email: str
    first_name: str | None = None
    last_name: str | None = None
    is_active: bool
    is_superuser: bool
    is_staff: bool
    password: str 
    last_login: datetime | None = None
    date_joined: datetime | None = None

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    first_name: str | None = None
    last_name: str | None = None
    is_active: bool = True
    is_superuser: bool = False
    is_staff: bool = False
    date_joined: datetime | None = None

class UserUpdate(BaseModel):
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    is_active: bool | None = None
    is_superuser: bool | None = None
    is_staff: bool | None = None
    password: str | None = None
    last_login: datetime | None = None
    date_joined: datetime | None = None
