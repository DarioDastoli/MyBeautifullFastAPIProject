from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import drivers, login, constructors, races, results

app = FastAPI(
    title="ErgastDB API Wrapper",
    description="Un'API FastAPI che espone i dati di ErgastDB (F1).",
    version="1.0.0"
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