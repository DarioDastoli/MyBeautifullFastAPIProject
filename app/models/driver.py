from sqlalchemy import Column, Integer, String, Date
from app.db import Base
from sqlalchemy.orm import relationship
from pydantic import BaseModel

class Driver(Base):
    __tablename__ = "drivers"

    driverId = Column(Integer, primary_key=True)
    driverRef = Column(String(255))
    number = Column(Integer)
    code = Column(String(3))
    forename = Column(String(255))
    surname = Column(String(255))
    dob = Column(Date)
    nationality = Column(String(255))
    url = Column(String(255))

    results = relationship("Result", back_populates="driver")
    qualifying = relationship("Qualifying", back_populates="driver")
    pitstops = relationship("PitStop", back_populates="driver")
    laptimes = relationship("LapTime", back_populates="driver")
    standings = relationship("DriverStanding", back_populates="driver")
