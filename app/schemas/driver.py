from pydantic import BaseModel

class Driver(BaseModel):
    driverRef: str
    number: int
    code: str
    forename: str
    surname: str
    dob: str  # ISO format date
    nationality: str
    url: str

class DriverUpdate(BaseModel):
    number: int