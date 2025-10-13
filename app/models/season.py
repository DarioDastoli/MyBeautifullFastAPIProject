from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.db import Base
from sqlalchemy.orm import relationship

class Season(Base):
    __tablename__ = "seasons"

    year = Column(Integer, primary_key=True)
    url = Column(String(255))