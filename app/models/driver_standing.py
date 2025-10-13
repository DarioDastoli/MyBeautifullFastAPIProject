from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.db import Base
from sqlalchemy.orm import relationship

class DriverStanding(Base):
    __tablename__ = "driverStandings"

    driverStandingsId = Column(Integer, primary_key=True)
    raceId = Column(Integer, ForeignKey("races.raceId"))
    driverId = Column(Integer, ForeignKey("drivers.driverId"))
    points = Column(Float)
    position = Column(Integer)
    positionText = Column(String(255))
    wins = Column(Integer)

    race = relationship("Race", back_populates="driver_standings")
    driver = relationship("Driver", back_populates="standings")