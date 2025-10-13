from sqlalchemy import Column, Integer, String, Float
from app.db import Base
from sqlalchemy.orm import relationship

class Circuit(Base):
    __tablename__ = "circuits"

    circuitId = Column(Integer, primary_key=True)
    circuitRef = Column(String(255))
    name = Column(String(255))
    location = Column(String(255))
    country = Column(String(255))
    lat = Column(Float)
    lng = Column(Float)
    alt = Column(Integer)
    url = Column(String(255))

    races = relationship("Race", back_populates="circuit")