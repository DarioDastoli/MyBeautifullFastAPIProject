from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Result
from app.db import get_db



router = APIRouter(
    prefix="/api",
    tags=["Results"]
)


@router.get("/results")
def get_results(race_id: int | None = None, driver_id: int | None = None, db: Session = Depends(get_db)):
    query = db.query(Result)
    if race_id:
        query = query.filter(Result.raceId == race_id)
    if driver_id:
        query = query.filter(Result.driverId == driver_id)
    results = query.limit(100).all()
    return results