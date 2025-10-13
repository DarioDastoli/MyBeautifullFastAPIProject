from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.db import Base
from sqlalchemy.orm import relationship

class ConstructorStanding(Base):
    __tablename__ = "constructorStandings"

    constructorStandingsId = Column(Integer, primary_key=True)
    raceId = Column(Integer, ForeignKey("races.raceId"))
    constructorId = Column(Integer, ForeignKey("F1data_constructor.constructorId"))
    points = Column(Float)
    position = Column(Integer)
    positionText = Column(String(255))
    wins = Column(Integer)

    race = relationship("Race", back_populates="constructor_standings")
    constructor = relationship("Constructor", back_populates="standings")