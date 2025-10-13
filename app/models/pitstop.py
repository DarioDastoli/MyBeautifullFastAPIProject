from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base

class PitStop(Base):
    __tablename__ = "pitstops"

    raceId = Column(Integer, ForeignKey("races.raceId"), primary_key=True)
    driverId = Column(Integer, ForeignKey("drivers.driverId"), primary_key=True)
    stop = Column(Integer, primary_key=True)
    lap = Column(Integer)
    time = Column(String(20))
    duration = Column(Float)
    milliseconds = Column(Integer)

    driver = relationship("Driver", back_populates="pitstops")
    race = relationship("Race", back_populates="pitstops")