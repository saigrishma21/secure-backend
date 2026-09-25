import logging

from fastapi import FastAPI

from .database import engine, Base
from . import models
from .routers import auth, files


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Secure Backend API",
    description="Secure backend using FastAPI",
    version="1.0.0"
)


app.include_router(auth.router)
app.include_router(files.router)


@app.get("/")
def home():
    logger.info("Home endpoint accessed")

    return {
        "message": "Secure Backend API is running"
    }