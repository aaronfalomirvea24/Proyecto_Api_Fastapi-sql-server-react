from pyclbr import Class
from typing import Optional
from pydantic import BaseModel
from datetime import datetime
# Esquema base para pedidos
class PedidoBase(BaseModel):
    MesaID: int
    ProductoID: int
    Cantidad: int
    EstadoPedido: str
# Esquema para crear un nuevo pedido
class PedidoCreate(PedidoBase):
    pass
# Esquema para actualizar el estado de un pedido
class PedidoUpdate(BaseModel):
    EstadoPedido: str

# Esquema para eliminar un pedido
class PedidoDelete(BaseModel):
    PedidoID: int
    # Esquema para mostrar un pedido
class PedidoResponse(PedidoBase):
    PedidoID: int
    FechaHora: datetime
    class Config:
        from_attributes = True
    #Esquema base para mesas
class MesaBase(BaseModel):
    Numero: int
    EstadoMesa: str
    # Esquema para crear una nueva mesa
class MesaCreate(MesaBase):
    pass
# Esquema para actualizar el estado de una mesa
class MesaUpdate(BaseModel):
    EstadoMesa: str
    # Esquema para eliminar una mesa
class MesaDelete(BaseModel):
    MesaID: int
    # Esquema para mostrar una mesa
class MostrarMesa(BaseModel):
    MesaID: int
    Numero: int
    EstadoMesa: str
    # Esquema para mostrar una mesa
class MesaResponse(MesaBase):
    pass
class Config:
    from_attributes = True
    # Esquema base para productos 
class ProductoBase(BaseModel):
    ProductoID: int
    Nombre: str
    Precio: float
    Categoria: Optional[str] = None 
    ImagenURL: Optional[str] = None
    Disponible: Optional[bool] = None
    # Esquema para mostrar un producto
class ProductoResponse(ProductoBase):
    pass
class ProductoCreate(ProductoBase):
    pass
class ProductoUpdate(BaseModel):
    Nombre: Optional[str] = None
    Precio: float
    Categori: Optional[str] = None
    Disponible: Optional[bool] = None

class ProductoDelete(BaseModel):
    ProductoID: int
class Config:
    from_attributes = True
    populate_by_name = True
