from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.routers.gpu_router import router as gpu_router
from app.database.connection import engine, Base
from app.database import models
from init_db import init_database

# Inicializar banco e popular se vazio
init_database()

app = FastAPI(title="GPU API")

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).resolve().parent / "static"),
    name="static",
)

app.include_router(gpu_router)

@app.get("/")
def home():
    return FileResponse(Path(__file__).resolve().parent / "static" / "index.html")


@app.get("/health")
def health():
    return {"status": "ok"}