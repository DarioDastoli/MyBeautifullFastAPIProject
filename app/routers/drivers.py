from warnings import filters
from fastapi import APIRouter, Depends, HTTPException, Path
from typing import Optional, Annotated
from sqlalchemy.orm import Session
from app.models import Driver
from app.schemas import DriverUpdate, Driver as DriverSchema
from app.db import get_db

router = APIRouter(
    prefix="/api",
    tags=["Drivers"]
)

@router.get('/search')
def search_drivers(
    limit: int = 50,
    nationality: Annotated[Optional[str], Path(title="Driver nationality")] = None,
    surname: Annotated[Optional[str], Path(title="Driver surname")] = None,
    number: Annotated[Optional[int], Path(title="Driver number")] = None,
    db: Session = Depends(get_db)
):
    filters = []
    print(db.query(Driver).count())
    if nationality is not None:
        filters.append(Driver.nationality == nationality)
    from sqlalchemy import func
    if surname is not None:
        filters.append(func.lower(Driver.surname).like(f"%{surname.lower()}%"))
    if number is not None:
        filters.append(Driver.number == number)
    print("Filters:", filters)


    drivers = db.query(Driver).filter(*filters).limit(limit).all()
    return drivers

@router.get("/drivers")
def get_drivers(limit: int=50, offset:int=0, db:Session=Depends(get_db)):
    drivers = db.query(Driver).offset(offset).limit(limit).all()
    return drivers

@router.get('/drivers/{driver_id}')
def get_drivers_by_id(
    driver_id:Annotated[int, Path(title="The ID of the driver to get", ge=1)],
    db:Session=Depends(get_db)
):
    driver = db.query(Driver).filter(Driver.driverId == driver_id).first()
    return driver


@router.patch('/driver/{driver_id}', response_model=DriverSchema)
def update_driver_number(
    driver_id: Annotated[int, Path(title="The ID of the driver to update", ge=1)],
    driver_update: DriverUpdate,
    db: Session = Depends(get_db)
):
    driver = db.query(Driver).filter(Driver.driverId == driver_id).first()
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    driver.number = driver_update.number
    db.commit()
    db.refresh(driver)
    return driver

