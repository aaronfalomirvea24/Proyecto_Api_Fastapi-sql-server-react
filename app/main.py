import http

from fastapi import Depends, FastAPI
from app import  database
from . import models,endpoints
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API del Restaurante Ficticio!"}
models.Base.metadata.create_all(bind=database.engine)
app.include_router(endpoints.router)