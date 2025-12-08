import os
from  app.env import load_env

load_env()

class Settings:
    DB_USER: str = os.environ.get("DB_USER", "root")
    DB_PASSWORD: str = os.environ.get("DB_PASSWORD")
    DB_HOST: str = os.environ.get("DB_HOST", "localhost")
    DB_PORT: str = os.environ.get("DB_PORT", "3306")
    DB_NAME: str = os.environ.get("DB_NAME", "ergastdb")

    
    SQL_ECHO: bool = os.getenv("SQL_ECHO", "false").lower() == "true"

    SECRET_KEY: str = os.environ.get("SECRET_KEY", "your-default-secret-key")
    JWT_SECRET_KEY: str = os.environ.get("JWT_SECRET_KEY", "your-jwt-secret-key")
    JWT_ALGORITHM: str = os.environ.get("JWT_ALGORITHM", "HS256")
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.environ.get("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", "30")) 

    PROJECT_NAME: str = os.environ.get("PROJECT_NAME", "My FastAPI Project")
    DESCRIPTION: str = os.environ.get("DESCRIPTION", "An API to expose ErgastDB (F1) data.")    
    VERSION: str = os.environ.get("VERSION", "0.0.0")

    BACKEND_CORS_ORIGINS: list = os.environ.get("BACKEND_CORS_ORIGINS", "*").split(",")
    ALLOWED_METHODS: list = os.environ.get("ALLOWED_METHODS", "*").split(",")
    ALLOWED_HEADERS: list = os.environ.get("ALLOWED_HEADERS", "*").split(",")


settings = Settings()