from fastapi import APIRouter, Depends, HTTPException
from fastapi import Request, status
from sqlalchemy.orm import Session
from app.models import Race
from app.db import get_db

router = APIRouter(
    prefix="/api",
    tags=["Races"]
)


@router.get("/races")
def get_races(year: int | None = None, limit: int = 50, offset: int = 0, db: Session = Depends(get_db)):
    query = db.query(Race)
    if year:
        query = query.filter(Race.year == year)
    races = query.offset(offset).limit(limit).all()
    return races

@router.get("/races/{race_id}")
def get_race(race_id: int, db: Session = Depends(get_db)):
    race = db.query(Race).filter(Race.raceId == race_id).first()
    if not race:
        raise HTTPException(status_code=404, detail="Race not found")
    return race