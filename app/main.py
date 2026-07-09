from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from app import database
from app import models, endpoints
from fastapi.middleware.cors import CORSMiddleware

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(
    swagger_ui_parameters={"persistAuthorization": True}
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    models.Base.metadata.create_all(bind=database.engine)
    print("✅ Tablas creadas correctamente", flush=True)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API del Restaurante!"}

app.include_router(endpoints.router)