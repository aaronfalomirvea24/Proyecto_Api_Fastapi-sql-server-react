import datetime
from sqlalchemy.orm import Session
from app import auth, database
import app.models as models
import app.schemas as schemas
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# ✅ Función para obtener el usuario actual desde el token
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar el token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = auth.verificar_token(token)  # debes tener esta función en auth.py
    if payload is None:
        raise credentials_exception
    username: str = payload.get("sub")
    if username is None:
        raise credentials_exception
    usuario = db.query(models.usuarios).filter(models.usuarios.username == username).first()
    if usuario is None:
        raise credentials_exception
    return usuario

# ──────────────────────────────────────────
# PEDIDOS
# ──────────────────────────────────────────

@router.post("/pedidos/", response_model=schemas.PedidoResponse)
def create_pedido(
    pedido: schemas.PedidoCreate,
    db: Session = Depends(database.get_db),
    current_user: models.usuarios = Depends(get_current_user)  # 🔒 protegido
):
    db_pedido = models.Pedidos(**pedido.dict())

    if db_pedido.FechaHora:
        db_pedido.FechaHora = db_pedido.FechaHora.replace(tzinfo=None)
    else:
        db_pedido.FechaHora = datetime.datetime.now().replace(tzinfo=None)
        
    try:
        db.add(db_pedido)
        db.commit()
        db.refresh(db_pedido)
        return db_pedido
    except Exception as e:
        db.rollback()
        print(f"Error al insertar pedido: {e}")
        raise e
    
@router.get("/pedidos/", response_model=list[schemas.PedidoResponse])
def read_pedidos(
    db: Session = Depends(database.get_db),
    current_user: models.usuarios = Depends(get_current_user)  # 🔒 protegido
):
    return db.query(models.Pedidos).all()

@router.get("/pedidos/{pedido_id}", response_model=schemas.PedidoResponse)
def read_pedido(
    pedido_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.usuarios = Depends(get_current_user)  # 🔒 protegido
):
    return db.query(models.Pedidos).filter(models.Pedidos.PedidoID == pedido_id).first()

@router.put("/pedidos/{pedido_id}", response_model=schemas.PedidoResponse)
def update_pedido(
    pedido_id: int,
    pedido: schemas.PedidoUpdate,
    db: Session = Depends(database.get_db),
    current_user: models.usuarios = Depends(get_current_user)  # 🔒 protegido
):
    db_pedido = db.query(models.Pedidos).filter(models.Pedidos.PedidoID == pedido_id).first()
    if not db_pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    for key, value in pedido.dict().items():
        setattr(db_pedido, key, value)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido

@router.delete("/pedidos/{pedido_id}", response_model=schemas.PedidoResponse)
def delete_pedido(
    pedido_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.usuarios = Depends(get_current_user)  # 🔒 protegido
):
    db_pedido = db.query(models.Pedidos).filter(models.Pedidos.PedidoID == pedido_id).first()
    if not db_pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    db.delete(db_pedido)
    db.commit()
    return db_pedido

# ──────────────────────────────────────────
# MESAS
# ──────────────────────────────────────────

@router.post("/mesas/", response_model=schemas.MostrarMesa)
def create_mesa(
    mesa: schemas.MesaCreate,
    db: Session = Depends(database.get_db),
    current_user: models.usuarios = Depends(get_current_user)  # 🔒 protegido
):
    db_mesa = models.Mesas(**mesa.dict())
    db.add(db_mesa)
    db.commit()
    db.refresh(db_mesa)
    return db_mesa

@router.get("/mesas/", response_model=list[schemas.MostrarMesa])
def read_mesas(
    db: Session = Depends(database.get_db),
    current_user: models.usuarios = Depends(get_current_user)  # 🔒 protegido
):
    return db.query(models.Mesas).all()

@router.get("/mesas/{mesa_id}", response_model=schemas.MostrarMesa)
def read_mesa(
    mesa_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.usuarios = Depends(get_current_user)  # 🔒 protegido
):
    return db.query(models.Mesas).filter(models.Mesas.MesaID == mesa_id).first()

@router.put("/mesas/{mesa_id}", response_model=schemas.MostrarMesa)
def update_mesa(
    mesa_id: int,
    mesa: schemas.MesaUpdate,
    db: Session = Depends(database.get_db),
    current_user: models.usuarios = Depends(get_current_user)  # 🔒 protegido
):
    db_mesa = db.query(models.Mesas).filter(models.Mesas.MesaID == mesa_id).first()
    if not db_mesa:
        raise HTTPException(status_code=404, detail="Mesa no encontrada")
    for key, value in mesa.dict().items():
        setattr(db_mesa, key, value)
    db.commit()
    db.refresh(db_mesa)
    return db_mesa

@router.delete("/mesas/{mesa_id}", response_model=schemas.MostrarMesa)
def delete_mesa(
    mesa_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.usuarios = Depends(get_current_user)  # 🔒 protegido
):
    db_mesa = db.query(models.Mesas).filter(models.Mesas.MesaID == mesa_id).first()
    if not db_mesa:
        raise HTTPException(status_code=404, detail="Mesa no encontrada")
    db.delete(db_mesa)
    db.commit()
    return db_mesa

# ──────────────────────────────────────────
# PRODUCTOS
# ──────────────────────────────────────────

@router.post("/productos/", response_model=schemas.ProductoResponse)
def create_producto(
    producto: schemas.ProductoCreate,
    db: Session = Depends(database.get_db),
    current_user: models.usuarios = Depends(get_current_user)  # 🔒 protegido
):
    db_producto = models.Productos(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

@router.get("/productos/", response_model=list[schemas.ProductoResponse])
def read_productos(db: Session = Depends(database.get_db)):  # público, sin candado
    return db.query(models.Productos).all()

@router.get("/productos/{producto_id}", response_model=schemas.ProductoResponse)
def read_producto(producto_id: int, db: Session = Depends(database.get_db)):  # público
    return db.query(models.Productos).filter(models.Productos.ProductoID == producto_id).first()

@router.put("/productos/{producto_id}", response_model=schemas.ProductoResponse)
def update_producto(
    producto_id: int,
    producto: schemas.ProductoUpdate,
    db: Session = Depends(database.get_db),
    current_user: models.usuarios = Depends(get_current_user)  # 🔒 protegido
):
    db_producto = db.query(models.Productos).filter(models.Productos.ProductoID == producto_id).first()
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    for key, value in producto.dict().items():
        setattr(db_producto, key, value)
    db.commit()
    db.refresh(db_producto)
    return db_producto

@router.delete("/productos/{producto_id}", response_model=schemas.ProductoResponse)
def delete_producto(
    producto_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.usuarios = Depends(get_current_user)  # 🔒 protegido
):
    db_producto = db.query(models.Productos).filter(models.Productos.ProductoID == producto_id).first()
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(db_producto)
    db.commit()
    return db_producto
# ──────────────────────────────────────────
# REGISTRO DE USUARIOS
# ──────────────────────────────────────────

@router.post("/usuarios/register")
def register(username: str, password: str, db: Session = Depends(database.get_db)):
    # Verificar si el usuario ya existe
    existing = db.query(models.usuarios).filter(models.usuarios.username == username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    # Hashear password y crear usuario
    import bcrypt
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    nuevo_usuario = models.usuarios(username=username, hashed_password=hashed)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return {"message": "User created successfully", "username": nuevo_usuario.username}
# ──────────────────────────────────────────
# AUTH
# ──────────────────────────────────────────
@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    usuario = db.query(models.usuarios).filter(models.usuarios.username == form_data.username).first()
    if not usuario or not auth.verificar_password(form_data.password, usuario.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = auth.crear_token_acceso(data={"sub": usuario.username})
    return {"access_token": token, "token_type": "bearer"}
