from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.db import Base
from sqlalchemy.orm import relationship

class ConstructorResult(Base):
    __tablename__ = "constructorResults"

    constructorResultsId = Column(Integer, primary_key=True)
    raceId = Column(Integer, ForeignKey("races.raceId"))
    constructorId = Column(Integer, ForeignKey("F1data_constructor.constructorId"))
    points = Column(Float)
    status = Column(String(255))

    race = relationship("Race", back_populates="constructor_results")
    constructor = relationship("Constructor", back_populates="constructor_results")