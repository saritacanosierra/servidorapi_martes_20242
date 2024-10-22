from pydantic import BaseModel, Field, ConfigDict  # Paquete del api que permite crear un modelo base del DTO
from datetime import date  # Paquete para fechas y horas.
from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import sessionmaker

# Los DTO son clases que establecen el modelo de transferencia de datos.

class UsuarioDTOPeticion(BaseModel):  # Petición para guardar los datos en la BD
    nombres: str
    fechaNacimiento: date
    ubicacion: str
    metaAhorro: float

    class Config:
        orm_mode = True
        from_attributes = True

class UsuarioDTORespuesta(BaseModel):  # Petición para traer los datos de la BD
    id: int
    nombres: str
    fechaNacimiento: date
    ubicacion: str
    metaAhorro: float
    class Config:
        orm_mode = True
        from_attributes = True

class GastoDTOPeticion(BaseModel):
    fecha: date
    descripcion: str
    valorGasto: float
    categoria: str

    class Config:
        orm_mode = True
        from_attributes = True 

class GastoDTORespuesta(BaseModel):
    id: int
    fecha: date
    descripcion: str
    valorGasto: float
    categoria: str

    class Config:
        orm_mode = True
        from_attributes = True  

class IngresoDTOPeticion(BaseModel):
    fecha: date
    descripcion: str
    valorIngreso: float

    class Config:
        orm_mode = True
        from_attributes = True  

class IngresoDTORespuesta(BaseModel):
    id: int
    fecha: date
    descripcion: str
    valorIngreso: float

    class Config:
        orm_mode = True
        from_attributes = True  

class historialDTOPeticion(BaseModel):
    fecha: date
    totalIngresomensual: float
    totalAhorroMensual: float
    totalGastos: float 

    class Config:
        orm_mode = True
        from_attributes = True  

class historialDTORespuesta(BaseModel):
    id: int
    fecha: date
    totalIngresomensual: float
    totalAhorroMensual: float
    totalGastos: float  

    class Config:
        orm_mode = True
        from_attributes = True 




