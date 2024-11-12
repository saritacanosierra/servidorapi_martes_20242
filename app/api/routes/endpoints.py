# Importaciones necesarias
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.api.DTO.dtos import (UsuarioDTOPeticion, UsuarioDTORespuesta, GastoDTOPeticion, GastoDTORespuesta, IngresoDTOPeticion, IngresoDTORespuesta, 
                              historialDTOPeticion, historialDTORespuesta)
from app.api.models.tablasSQL import Usuario, Gasto, Ingreso, Historial
from app.database.configuration import SessionLocal

# Crear el router
rutas = APIRouter()

# Función para conectar con la base de datos
def conectarConBD():
    try:
        basedatos = SessionLocal()
        yield basedatos

    except Exception as error:
        basedatos.rollback()
        raise error
    finally:
        basedatos.close()

# Endpoint para guardar un usuario__________________________________________________________________________________________________

@rutas.post("/usuario", response_model=UsuarioDTORespuesta, summary="Registrar un usuario en la base de datos")
def guardarUsuario(datosUsuario: UsuarioDTOPeticion, database: Session = Depends(conectarConBD)):
    try:
        usuario = Usuario(**datosUsuario.dict())
        database.add(usuario)
        database.commit()
        database.refresh(usuario)
        return UsuarioDTORespuesta.from_orm(usuario) 
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Error al guardar el usuario: {(error)}")

# Endpoint para obtener todos los usuarios
@rutas.get("/usuarios", response_model=List[UsuarioDTORespuesta], summary="Obtener todos los usuarios")
def obtenerUsuarios(database: Session = Depends(conectarConBD)):
    return database.query(Usuario).all()

# Endpoint para obtener un usuario por ID
@rutas.get("/usuario/{usuario_id}", response_model=UsuarioDTORespuesta, summary="Obtener un usuario por ID")
def obtenerUsuario(usuario_id: int, database: Session = Depends(conectarConBD)):
    usuario = database.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return UsuarioDTORespuesta.from_orm(usuario)

# Endpoint para actualizar un usuario
@rutas.put("/usuario/{usuario_id}", response_model=UsuarioDTORespuesta, summary="Actualizar un usuario")
def actualizarUsuario(usuario_id: int, datosUsuario: UsuarioDTOPeticion, database: Session = Depends(conectarConBD)):
    usuario = database.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    for key, value in datosUsuario.dict().items():
        setattr(usuario, key, value)
    database.commit()
    database.refresh(usuario)
    return UsuarioDTORespuesta.from_orm(usuario)

# Endpoint para eliminar un usuario
@rutas.delete("/usuario/{usuario_id}", summary="Eliminar un usuario")
def eliminarUsuario(usuario_id: int, database: Session = Depends(conectarConBD)):
    usuario = database.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    database.delete(usuario)
    database.commit()
    return {"detail": "Usuario eliminado"}

# Endpoint para guardar un gasto___________________________________________________________________________________________________
@rutas.post("/gasto", response_model=GastoDTORespuesta, summary="Registrar un gasto en la base de datos")
def guardarGasto(datosGasto: GastoDTOPeticion, database: Session = Depends(conectarConBD)):
    try:
        gasto = Gasto(**datosGasto.dict())
        database.add(gasto)
        database.commit()
        database.refresh(gasto)
        return GastoDTORespuesta.from_orm(gasto)
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Error al guardar el gasto: {(error)}")

# Endpoint para obtener todos los gastos
@rutas.get("/gastos", response_model=List[GastoDTORespuesta], summary="Obtener todos los gastos")
def obtenerGastos(database: Session = Depends(conectarConBD)):
    return database.query(Gasto).all()

# Endpoint para obtener un gasto por ID
@rutas.get("/gasto/{gasto_id}", response_model=GastoDTORespuesta, summary="Obtener un gasto por ID")
def obtenerGasto(gasto_id: int, database: Session = Depends(conectarConBD)):
    try:
        gasto = database.query(Gasto).filter(Gasto.id == gasto_id).first()
        if not gasto:
            raise HTTPException(status_code=404, detail="Gasto no encontrado")
        return GastoDTORespuesta.from_orm(gasto)
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Error al obtener el gasto: {error}")

# Endpoint para actualizar un gasto
@rutas.put("/gasto/{gasto_id}", response_model=GastoDTORespuesta, summary="Actualizar un gasto")
def actualizarGasto(gasto_id: int, datosGasto: GastoDTOPeticion, database: Session = Depends(conectarConBD)):
    gasto = database.query(Gasto).filter(Gasto.id == gasto_id).first()
    if not gasto:
        raise HTTPException(status_code=404, detail="Gasto no encontrado")
    for key, value in datosGasto.dict().items():
        setattr(gasto, key, value)
    database.commit()
    database.refresh(gasto)
    return GastoDTORespuesta.from_orm(gasto)

# Endpoint para eliminar un gasto
@rutas.delete("/gasto/{gasto_id}", summary="Eliminar un gasto")
def eliminarGasto(gasto_id: int, database: Session = Depends(conectarConBD)):
    gasto = database.query(Gasto).filter(Gasto.id == gasto_id).first()
    if not gasto:
        raise HTTPException(status_code=404, detail="Gasto no encontrado")
    database.delete(gasto)
    database.commit()
    return {"detail": "Gasto eliminado"}


# Endpoint para guardar un ingreso_____________________________________________________________________________________________________
@rutas.post("/ingreso", response_model=IngresoDTORespuesta, summary="Registrar un ingreso en la base de datos")
def guardarIngreso(datosIngreso: IngresoDTOPeticion, database: Session = Depends(conectarConBD)):
    try:
        ingreso = Ingreso(**datosIngreso.dict())
        database.add(ingreso)
        database.commit()
        database.refresh(ingreso)
        return IngresoDTORespuesta.from_orm(ingreso)
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Error al guardar el ingreso: {(error)}")

# Endpoint para obtener todos los ingresos
@rutas.get("/ingresos", response_model=List[IngresoDTORespuesta], summary="Obtener todos los ingresos")
def obtenerIngresos(database: Session = Depends(conectarConBD)):
    return database.query(Ingreso).all()

# Endpoint para obtener un ingreso por ID
@rutas.get("/ingreso/{ingreso_id}", response_model=IngresoDTORespuesta, summary="Obtener un ingreso por ID")
def obtenerIngreso(ingreso_id: int, database: Session = Depends(conectarConBD)):
    try:
        ingreso = database.query(Ingreso).filter(Ingreso.id == ingreso_id).first()
        if not ingreso:
            raise HTTPException(status_code=404, detail="Ingreso no encontrado")
        return IngresoDTORespuesta.from_orm(ingreso)
    except Exception as error:
        raise HTTPException(status_code=500, detail=f"Error al obtener el ingreso: {error}")

# Endpoint para actualizar un ingreso
@rutas.put("/ingreso/{ingreso_id}", response_model=IngresoDTORespuesta, summary="Actualizar un ingreso")
def actualizarIngreso(ingreso_id: int, datosIngreso: IngresoDTOPeticion, database: Session = Depends(conectarConBD)):
    ingreso = database.query(Ingreso).filter(Ingreso.id == ingreso_id).first()
    if not ingreso:
        raise HTTPException(status_code=404, detail="Ingreso no encontrado")
    for key, value in datosIngreso.dict().items():
        setattr(ingreso, key, value)
    database.commit()
    database.refresh(ingreso)
    return IngresoDTORespuesta.from_orm(ingreso)

# Endpoint para eliminar un ingreso
@rutas.delete("/ingreso/{ingreso_id}", summary="Eliminar un ingreso")
def eliminarIngreso(ingreso_id: int, database: Session = Depends(conectarConBD)):
    ingreso = database.query(Ingreso).filter(Ingreso.id == ingreso_id).first()
    if not ingreso:
        raise HTTPException(status_code=404, detail="Ingreso no encontrado")
    database.delete(ingreso)
    database.commit()
    return {"detail": "Ingreso eliminado"}

# Endpoint para obtener el historial de transacciones____________________________________________________________________________________
@rutas.get("/historial", response_model=List[historialDTORespuesta], summary="Obtener historial de transacciones")
def obtenerHistorial(database: Session = Depends(conectarConBD)):
    historial = database.query(Historial).all()  # Usar la tabla Historial
    return historial

# Endpoint para guardar un historial de transacciones (gasto o ingreso) utilizando DTOs
@rutas.post("/historial", response_model=historialDTORespuesta, summary="Registrar una transacción en el historial")
def guardarHistorial(datosTransaccion: historialDTOPeticion, database: Session = Depends(conectarConBD)):
    try:
        transaccion = Historial(**datosTransaccion.dict())  # Guardar en la tabla Historial
        database.add(transaccion)
        database.commit()
        database.refresh(transaccion)
        return historialDTORespuesta(tipo=datosTransaccion.tipo, detalle=transaccion)
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Error al guardar la transacción: {(error)}")

# Endpoint para actualizar una transacción en el historial
@rutas.put("/historial/{transaccion_id}", response_model=historialDTORespuesta, summary="Actualizar una transacción en el historial")
def actualizarHistorial(transaccion_id: int, datosTransaccion: historialDTOPeticion, database: Session = Depends(conectarConBD)):
    if datosTransaccion.tipo == "gasto":
        transaccion = database.query(Gasto).filter(Gasto.id == transaccion_id).first()
    elif datosTransaccion.tipo == "ingreso":
        transaccion = database.query(Ingreso).filter(Ingreso.id == transaccion_id).first()
    else:
        raise HTTPException(status_code=400, detail="Tipo de transacción no válido")

    if not transaccion:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")

    for key, value in datosTransaccion.detalle.items():
        setattr(transaccion, key, value)
    
    database.commit()
    database.refresh(transaccion)
    return historialDTORespuesta(tipo=datosTransaccion.tipo, detalle=transaccion)

# Endpoint para eliminar una transacción del historial
@rutas.delete("/historial/{transaccion_id}", summary="Eliminar una transacción del historial")
def eliminarHistorial(transaccion_id: int, tipo: str, database: Session = Depends(conectarConBD)):
    if tipo == "gasto":
        transaccion = database.query(Gasto).filter(Gasto.id == transaccion_id).first()
    elif tipo == "ingreso":
        transaccion = database.query(Ingreso).filter(Ingreso.id == transaccion_id).first()
    else:
        raise HTTPException(status_code=400, detail="Tipo de transacción no válido")

    if not transaccion:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")

    database.delete(transaccion)
    database.commit()
    return {"detail": "Transacción eliminada"}
