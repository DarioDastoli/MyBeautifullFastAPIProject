from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.db import Base
from sqlalchemy.orm import relationship

class Qualifying(Base):
    __tablename__ = "qualifying"

    qualifyId = Column(Integer, primary_key=True)
    raceId = Column(Integer, ForeignKey("races.raceId"))
    driverId = Column(Integer, ForeignKey("drivers.driverId"))
    constructorId = Column(Integer, ForeignKey("F1data_constructor.constructorId"))
    number = Column(Integer)
    position = Column(Integer)
    q1 = Column(String(255))
    q2 = Column(String(255))
    q3 = Column(String(255))

    race = relationship("Race", back_populates="qualifying")
    driver = relationship("Driver", back_populates="qualifying")
    constructor = relationship("Constructor", back_populates="qualifying")