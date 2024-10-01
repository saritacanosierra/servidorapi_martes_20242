from fastapi import APIRouter, HTTPException #Librería para los servicios que necesito en la base de datos (Actualizar, Guardar, etc)
from sqlalchemy.orm import Session #Comunicación con la base de datos.
from typing import List
from fastapi.params import Depends #Utilizar dependencias del api para comunicación interna.
from app.api.DTO.dtos import UsuarioDTOPeticion, UsuarioDTORespuesta
from app.api.models.tablasSQL import Usuario
from app.database.configuration import SessionLocal,engine

rutas = APIRouter()

def conectarConBD():
    try:
        basedatos = SessionLocal()
        yield basedatos #Activar la base de datos
           
    except Exception as error:
        basedatos.rollback()
        raise error
    finally:
        basedatos.close()