from fastapi import APIRouter, Depends, HTTPException, status
from app.models.constructor import Constructor
from app.db import get_db
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/api",
    tags=["Constructors"]
)

@router.get("/constructors/{constructor_id}")
def get_constructor(constructor_id: int, db: Session = Depends(get_db)):
    constructor = db.query(Constructor).filter(Constructor.constructorId == constructor_id).first()
    if not constructor:
        raise HTTPException(status_code=404, detail="Constructor not found")
    return constructor

@router.get("/constructors")
def get_constructors(limit: int = 50, offset: int = 0, db: Session = Depends(get_db)):
    constructors = db.query(Constructor).offset(offset).limit(limit).all()
    return constructors