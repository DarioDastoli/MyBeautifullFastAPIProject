from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from app.db import Base

class User(Base):
    __tablename__ = "auth_user"

    id = Column(Integer, primary_key=True, index=True)
    password = Column(String(128), nullable=False)
    last_login = Column(DateTime, default=None)
    is_superuser = Column(Boolean, default=False)
    username = Column(String(150), unique=True, nullable=False, index=True)
    first_name = Column(String(150))
    last_name = Column(String(150))
    email = Column(String(254), unique=True, nullable=False, index=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    date_joined = Column(DateTime, default=None)
