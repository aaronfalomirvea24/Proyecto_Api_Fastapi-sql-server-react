from sqlalchemy.orm import Session
from app import database
import app.models as models
import app.schemas as schemas
from app  import database
from fastapi import  APIRouter, Depends
router = APIRouter()
@router.post("/pedidos/", response_model=schemas.PedidoResponse)

def create_pedido(pedido: schemas.PedidoCreate, db: Session = Depends(database.get_db)):
    db_pedido = models.Pedidos(**pedido.dict())
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido

#obtenemos todos los pedidos
@router.get("/pedidos/", response_model=list[schemas.PedidoResponse])

def read_pedidos(db: Session = Depends(database.get_db)):
    return db.query(models.Pedidos).all()

#obtenemos un pedido por su ID
@router.get("/pedidos/{pedido_id}", response_model=schemas.PedidoResponse)

def read_pedido(pedido_id: int, db: Session = Depends(database.get_db)):
    return db.query(models.Pedidos).filter(models.Pedidos.PedidoID == pedido_id).first()

#actualizamos el estado de un pedido
@router.put("/pedidos/{pedido_id}", response_model=schemas.PedidoResponse)

def update_pedido(pedido_id: int, pedido: schemas.PedidoUpdate, db: Session = Depends(database.get_db)):
    db_pedido = db.query(models.Pedidos).filter(models.Pedidos.PedidoID == pedido_id).first()
    if not db_pedido:
        return {"error": "Pedido no encontrado"}
    for key, value in pedido.dict().items():
        setattr(db_pedido, key, value)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido

#eliminamos un pedido por su ID
@router.delete("/pedidos/{pedido_id}", response_model=schemas.PedidoResponse)

def delete_pedido(pedido_id: int, db: Session = Depends(database.get_db)):
    db_pedido = db.query(models.Pedidos).filter(models.Pedidos.PedidoID == pedido_id).first()
    if not db_pedido:
        return {" Message": "Pedido no encontrado"}
    db.delete(db_pedido)
    db.commit()
    return db_pedido

# Crear endpoints para CRUD de Mesas
#crear una nueva mesa
@router.post("/mesas/", response_model=schemas.MostrarMesa)

def create_mesa(mesa: schemas.MesaCreate, db: Session = Depends(database.get_db)):
    db_mesa = models.Mesas(**mesa.dict())
    db.add(db_mesa)
    db.commit()
    db.refresh(db_mesa)
    return db_mesa

#Mostrar todas las mesas
@router.get("/mesas/", response_model=list[schemas.MostrarMesa])

def read_mesas(db: Session = Depends(database.get_db)):
    return db.query(models.Mesas).all()

#Mostrar una mesa por su ID
@router.get("/mesas/{mesa_id}", response_model=schemas.MostrarMesa)

def read_mesa(mesa_id: int, db: Session = Depends(database.get_db)):
    return db.query(models.Mesas).filter(models.Mesas.MesaID == mesa_id).first()

#Actualizar el estado de una mesa
@router.put("/mesas/{mesa_id}", response_model=schemas.MostrarMesa)
def update_mesa(mesa_id: int, mesa: schemas.MesaUpdate, db: Session = Depends(database.get_db)):
    db_mesa = db.query(models.Mesas).filter(models.Mesas.MesaID == mesa_id).first()
    if not db_mesa:
        return {"error": "Mesa no encontrada"}
    for key, value in mesa.dict().items():
        setattr(db_mesa, key, value)
    db.commit()
    db.refresh(db_mesa)
    return db_mesa
#Eliminar una mesa por su ID
@router.delete("/mesas/{mesa_id}", response_model=schemas.MostrarMesa)
def delete_mesa(mesa_id: int, db: Session = Depends(database.get_db)):
    db_mesa = db.query(models.Mesas).filter(models.Mesas.MesaID == mesa_id).first()
    if not db_mesa:
        return {"error": "Mesa no encontrada"}
    db.delete(db_mesa)
    db.commit()
    return db_mesa
# Crear endpoints para CRUD de Productos
#crear un nuevo producto
@router.post("/productos/", response_model=schemas.ProductoResponse)  
def create_producto(producto: schemas.ProductoCreate, db: Session = Depends(database.get_db)):
    db_producto = models.Productos(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto
#Mostrar todos los productos
@router.get("/productos/", response_model=list[schemas.ProductoResponse])
def read_productos(db: Session = Depends(database.get_db)):
    return db.query(models.Productos).all()
#Mostrar un producto por su ID
@router.get("/productos/{producto_id}", response_model=schemas.ProductoResponse)
def read_producto(producto_id: int, db: Session = Depends(database.get_db)):
    return db.query(models.Productos).filter(models.Productos.ProductoID == producto_id).first()
#Actualizar un producto
@router.put("/productos/{producto_id}", response_model=schemas.ProductoResponse)
def update_producto(producto_id: int, producto: schemas.ProductoUpdate, db: Session = Depends(database.get_db)):
    db_producto = db.query(models.Productos).filter(models.Productos.ProductoID == producto_id).first()
    if not db_producto:
        return {"error": "Producto no encontrado"}
    for key, value in producto.dict().items():
        setattr(db_producto, key, value)
    db.commit()
    db.refresh(db_producto)
    return db_producto
#Eliminar un producto por su ID
@router.delete("/productos/{producto_id}", response_model=schemas.ProductoResponse)
def delete_producto(producto_id: int, db: Session = Depends(database.get_db)):
    db_producto = db.query(models.Productos).filter(models.Productos.ProductoID == producto_id).first()
    if not db_producto:
        return {"error": "Producto no encontrado"}
    db.delete(db_producto)
    db.commit()
    return db_producto