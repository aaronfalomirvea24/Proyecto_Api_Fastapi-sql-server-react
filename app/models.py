from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Numeric, String, Float, func
from .database import Base
# Definición de los modelos de la base de datos,en este caso, las tablas Mesas, Productos y Pedidos,de mi base de datos SQL Server utilizando SQLAlchemy ORM.
class Mesas(Base):
    __tablename__ = "mesas"
    MesaID = Column(Integer, primary_key=True, index=True)
    Numero = Column(Integer, unique=True, nullable=False)
    EstadoMesa = Column(String(20), default="LIBRE") # 'LIBRE', 'OCUPADA'
class Productos(Base):
    __tablename__ = "productos"
    ProductoID = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(100), nullable=False)
    Precio = Column(Float, nullable=False)
    Categoria = Column(String(50), nullable=True)
    ImagenURL = Column(String(255), nullable=True)
    Disponible = Column(Boolean, default=True)
class Pedidos(Base):
    __tablename__ = "pedidos"
    PedidoID = Column(Integer, primary_key=True, index=True)
    MesaID = Column(Integer, ForeignKey("mesas.MesaID"), primary_key=True, nullable=False)
    ProductoID = Column(Integer, ForeignKey("productos.ProductoID"), primary_key=True, nullable=False)
    Cantidad = Column(Integer, nullable=False)
    EstadoPedido = Column(String(20), default="PENDIENTE") # 'PENDIENTE', 'EN PREPARACION', 'LISTO', 'ENTREGADO'
    FechaHora = Column(DateTime(timezone=True), server_default=func.now())
class usuarios(Base):
    __tablename__ = "Usuarios"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String(50),unique=True,nullable=False)
    hashed_password=Column(String(255),nullable=False)
