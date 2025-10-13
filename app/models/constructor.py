from sqlalchemy import Column, Integer, String
from app.db import Base
from sqlalchemy.orm import relationship

class Constructor(Base):
    __tablename__ = "F1data_constructor"

    constructorId = Column(Integer, primary_key=True)
    constructorRef = Column(String(255))
    name = Column(String(255))
    nationality = Column(String(255))
    url = Column(String(255))

    results = relationship("Result", back_populates="constructor")
    standings = relationship("ConstructorStanding", back_populates="constructor")
    qualifying = relationship("Qualifying", back_populates="constructor")
    constructor_results = relationship("ConstructorResult", back_populates="constructor")