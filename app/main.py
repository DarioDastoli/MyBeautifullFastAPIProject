from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import drivers, login, constructors, races, results
import os
from dotenv import load_dotenv

load_dotenv()


app = FastAPI(
    title=os.getenv("PROJECT_NAME", "F1-FASTAPI"),
    description="An API to expose ErgastDB (F1) data.",
    version=os.getenv("VERSION","1.0.0")
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login.router)
app.include_router(drivers.router)
app.include_router(constructors.router)
app.include_router(races.router)
app.include_router(results.router)