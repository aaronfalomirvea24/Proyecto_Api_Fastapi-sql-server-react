from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta


# Configuración básica
SECRET_KEY = "AaronFifa2013********"  # Cambia esto por una clave secreta fuerte
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def verificar_password(password_plano, password_hasheado):
    return pwd_context.verify(password_plano, password_hasheado)

def crear_token_acceso(data: dict):
    para_encriptar = data.copy()
    expiracion = datetime.utcnow() + timedelta(minutes=60)
    para_encriptar.update({"exp": expiracion})
    return jwt.encode(para_encriptar, SECRET_KEY, algorithm=ALGORITHM)
def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.JWTError:
        return None