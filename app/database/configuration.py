#Conexión con la base de datos

#Importación de las librerías

from sqlalchemy import create_engine,event #Llamar la librería para la comunicación con la base de datos
from sqlalchemy.orm import sessionmaker #abrir un canal hacia la base de datos
from sqlalchemy.engine import Engine
from sqlalchemy.orm import declarative_base

#Datos para la conexión a base de datos

dataBaseName = "gestordb"
userName = "root"
userPassword = ""
connectionPort = 3306
server = "localhost"

#Creando la conexión

dataBaseConnection = f"mysql+mysqlconnector://{userName}:{userPassword}@{server}:{connectionPort}/{dataBaseName}"

#Creo el motor de conexión

engine = create_engine(dataBaseConnection)

#Abrir la sesión con la base de datos

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

#Declaración de la Base

Base = declarative_base()

#Función para crear las tablas en la base de datos

def crear_tablas():
    Base.metadata.create_all(bind=engine)

