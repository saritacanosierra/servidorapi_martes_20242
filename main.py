from fastapi import FastAPI
from app.database.configuration import engine
from app.api.models.tablasSQL import Base
from app.api.routes.endpoints import rutas  # Corregido 'endpoindts' a 'endpoints'
from starlette.responses import RedirectResponse
import uvicorn

from starlette.responses import RedirectResponse
from starlette.middlewere.cors import CORSMiddleware

# Crear las tablas de SQL desde Python
Base.metadata.create_all(bind=engine)

# Variable para administrar la aplicación
app = FastAPI()


#configurar el protocolo CORS
app.add_middleware(
    CORSMiddleware(
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
))

# Raíz de los endpoints
@app.get("/")
# Activar la API
def main():
    return RedirectResponse(url="/docs")

app.include_router(rutas)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)