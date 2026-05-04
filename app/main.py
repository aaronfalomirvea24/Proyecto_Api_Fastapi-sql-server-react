from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from app import  database
from app import models,endpoints
from fastapi.middleware.cors import CORSMiddleware
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
app = FastAPI(
    swagger_ui_parameters = {"persistAuthorization": True}
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#token endpoint para autenticación
@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API del Restaurante Ficticio!"}
models.Base.metadata.create_all(bind=database.engine)
app.include_router(endpoints.router)
