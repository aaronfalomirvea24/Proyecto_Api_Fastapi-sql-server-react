from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# 1. Configuración de la cadena de conexión
# Reemplaza 'localhost' por el nombre de tu instancia si es diferente (ej. .\SQLEXPRESS)
params = urllib.parse.quote_plus(
    f"DRIVER={{{os.environ.get('DB_DRIVER')}}};"
    f"SERVER={os.environ.get('DB_SERVER')};"
    f"DATABASE={os.environ.get('DB_DATABASE')};"
    f"Trusted_Connection={os.environ.get('DB_TRUSTED_CONNECTION')};"
)

DATABASE_URL = f"mssql+pyodbc:///?odbc_connect={params}"

# 2. Creación del motor (Engine)
engine = create_engine(DATABASE_URL)

# 3. Creación de la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Clase base para los modelos
Base = declarative_base()

# Dependencia para obtener la DB en las rutas de FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()