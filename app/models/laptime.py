from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.db import Base
from sqlalchemy.orm import relationship

class LapTime(Base):
    __tablename__ = "lapTimes"

    raceId = Column(Integer, ForeignKey("races.raceId"), primary_key=True)
    driverId = Column(Integer, ForeignKey("drivers.driverId"), primary_key=True)
    lap = Column(Integer, primary_key=True)
    position = Column(Integer)
    time = Column(String(255))
    milliseconds = Column(Integer)

    race = relationship("Race", back_populates="laptimes")
    driver = relationship("Driver", back_populates="laptimes")