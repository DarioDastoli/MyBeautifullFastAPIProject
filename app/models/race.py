from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from app.db import Base
from sqlalchemy.orm import relationship

class Race(Base):
    __tablename__ = "races"

    raceId = Column(Integer, primary_key=True)
    year = Column(Integer)
    round = Column(Integer)
    circuitId = Column(Integer, ForeignKey("circuits.circuitId"))
    name = Column(String(255))
    date = Column(Date)
    time = Column(Time)
    url = Column(String(255))

    circuit = relationship("Circuit", back_populates="races")
    results = relationship("Result", back_populates="race")
    qualifying = relationship("Qualifying", back_populates="race")
    pitstops = relationship("PitStop", back_populates="race")
    laptimes = relationship("LapTime", back_populates="race")
    constructor_results = relationship("ConstructorResult", back_populates="race")
    driver_standings = relationship("DriverStanding", back_populates="race")
    constructor_standings = relationship("ConstructorStanding", back_populates="race")
