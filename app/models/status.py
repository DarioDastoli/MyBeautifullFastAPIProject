from sqlalchemy import Column, Integer, String
from app.db import Base
from sqlalchemy.orm import relationship

class Status(Base):
    __tablename__ = "status"

    statusId = Column(Integer, primary_key=True)
    status = Column(String(255))

    results = relationship("Result", back_populates="status")