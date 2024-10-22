#Modelos

from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#Llamado a la base para crear tablas

Base = declarative_base()

#Definición de las tablas de mi modelo

#tabla para usuario
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres = Column(String(50))
    fechaNacimiento = Column(Date)
    ubicacion = Column(String(100))
    metaAhorro = Column(Float)
# Tabla para gastos
class Gasto(Base):
    __tablename__ = 'gastos'
    id= Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Date)
    descripcion = Column(String(100))
    valorGasto = Column(Float)
    categoria = Column(String(100))

# Tabla para ingresos
class Ingreso(Base):
    __tablename__ = 'ingresos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Date)
    descripcion = Column(String(100))
    valorIngreso = Column(Float)

# Tabla para historial
class Historial(Base):
    __tablename__ = 'historial'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Date)
    totalIngresomensual = Column(Float)
    totalAhorroMensual = Column(Float)
    totalGastos = Column(Float)
