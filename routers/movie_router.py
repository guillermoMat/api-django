from typing import Optional
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from config.database import session
from models.movie import Movie as MovieModel
from fastapi import APIRouter
from fastapi.responses import JSONResponse

movie_router = APIRouter()

# UTILIZAMOS ESTE ROUTER EN MAIN2


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(max_length=30)
    overview: str = Field(default="Agregar descripción")
    year: int
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=5, max_length=15)


# class Movie(BaseModel):
#     id: Optional[int] = None
#     title: str = Field(max_length=30)
#     overview: str = Field(default="Agregar descripción")
#     year: int
#     rating: float = Field(ge=1, le=10)
#     category: str = Field(min_length=5, max_length=15)


# Utilizamos JsonResponse para devolver el listado
# Funciona para todas las veces que debamos retornoar un listado o algo
@movie_router.get("/movies", tags=["Get Movies"])
def getMovies():
    db = session()
    result = db.query(MovieModel).all()
    return JSONResponse(content=jsonable_encoder(result))


@movie_router.get("/moviesByID", tags=["Get Movies"])
def getMovieByID(id: int):
    db = session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()

    if not result:
        return JSONResponse(content={"result": "Pelicula no encontrada"})
    return JSONResponse(content=jsonable_encoder(result))


# Actualización de pelicula
@movie_router.put("/movies", tags=["Update movie"])
def update_movie(id: int, movie: Movie):
    db = session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()

    if not result:
        return JSONResponse(content={"result": "elemento2 no encontrado"})
    result.title = movie.title
    result.overview = movie.overview
    result.year = movie.year
    result.rating = movie.rating
    result.category = movie.category
    db.commit()
    return JSONResponse(content={"result": "Pelicula actualizada"})


# Eliminacion movie
@movie_router.delete("/delete", tags=["Eliminación pelicula"])
def delete_movie(id: int):
    db = session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()

    if not result:
        return JSONResponse(content={"result": "elemento2 no encontrado"})

    db.delete(result)
    db.commit()
    return JSONResponse(content={"result": "Pelicula eliminada"})


# creacion de pelicula y retornamos un diccionario
@movie_router.post("/pelicula", tags=["Create Movie"])
def create_movie(movie: Movie):
    db = session()
    new_movie = MovieModel(**movie.dict())
    db.add(new_movie)
    db.commit()
    return JSONResponse(content={"message": "Pelicula guardada"})


"""
En tu código, cuando defines la función create_movie, primero se valida la entrada con el modelo de Pydantic y
luego se convierte en un objeto del modelo SQLAlchemy para guardarlo en la base de datos.

movie: Movie: Hace referencia al modelo de Pydantic.
new_movie = MovieModel(**movie.dict()): movie.dict() convierte el modelo Pydantic en un diccionario.
"""
