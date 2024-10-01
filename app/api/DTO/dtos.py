from pydantic import BaseModel,Field  #Paquete del api que permite crear un modelo base del DTO
from datetime import date  #Paquete para fechas y horas.

#Los DTO son clases que establecen el modelo de transferencia de datos.

class UsuarioDTOPeticion(BaseModel): #Petición para guardar los datos en la BD
    nombres: str
    fechaNacimiento:date
    ubicacion: str
    metaAhorro: float
    class config:
        orm_mode = True

class UsuarioDTORespuesta(BaseModel): #Petición para traer los datos de la BD
    id: int
    nombres: str
    metaAhorro: float
    class config:
        orm_mode = True
        
