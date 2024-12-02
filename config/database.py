import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

"""
Este código configura una conexión a una base de datos MySQL utilizando SQLAlchemy,
una biblioteca en Python para interactuar con bases de datos.
"""
database_name = "../movies.sqlite"
"""
Aquí se define el nombre de la base de datos a la que se conectará la aplicación. En este caso, database.moviesapp
parece referirse a una base de datos llamada moviesapp dentro de un esquema o contenedor database. Si el esquema no existe,
puede que el nombre sea simplemente un nombre arbitrario.
"""

base_dir = os.path.dirname(os.path.realpath(__file__))
"""
Esta línea obtiene el directorio base donde se encuentra el archivo Python que se está ejecutando.
Es útil si necesitas hacer referencia a rutas relativas dentro del proyecto.
"""

database_url = f"sqlite:///{os.path.join(base_dir,database_name)}"
#   Esta es la cadena de conexión (URL) para acceder a la base de datos MySQL.

engine = create_engine(database_url, echo=True)
# es una función de SQLAlchemy que crea una instancia de un "motor de base de datos" a partir de la URL proporcionada.

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# es una fábrica de SQLAlchemy que crea sesiones. Las sesiones son responsables de las transacciones y las operaciones con la base de datos.
base = declarative_base()
# es una función que devuelve una clase base a partir de la cual todos los modelos de base de datos deben heredar.
