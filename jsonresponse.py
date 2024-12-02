from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse


app = FastAPI()

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": 2009,
        "rating": 7.8,
        "category": "Acción",
    },
    {
        "id": 2,
        "title": "Duro de matar",
        "overview": "Mas duro que el roble, imposible de matar, nadie lo puede matar...",
        "year": 2012,
        "rating": 8.8,
        "category": "Acción",
    },
    {
        "id": 4,
        "title": "La leyenda de aang",
        "overview": "El maestro de los cuatro elementos",
        "year": 2009,
        "rating": 4.8,
        "category": "Drama",
    },
]


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(max_length=30)
    overview: str = Field(default="Agregar descripción")
    year: int
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=5, max_length=15)


# Utilizamos JsonResponse para devolver el listado
# Funciona para todas las veces que debamos retornoar un listado o algo
@app.get("/movies", tags=["Get Movies"])
def getMovies():
    return JSONResponse(content=movies)


# retornamos todas las peliculas pero indicamos que devolvemos una lista
@app.get("/movies/", tags=["Get Movies"], response_model=List[Movie])
def getMovies() -> List[Movie]:
    return JSONResponse(content=movies)


# aca retornamos una pelicula en particular e indicamos que retornamos solo una pelicula
@app.get("/movies/{id}", tags=["Get Movies"], response_model=Movie)
def getMovie_ByID(id: int) -> Movie:
    for item in movies:
        if item["id"] == id:
            return item
    return []


# creacion de pelicula y retornamos un diccionario
@app.post("/pelicula", tags=["Create Movie"])
def create_movie(movie: Movie):
    movies.append(movie.model_dump())
    return JSONResponse(content={"message": "Pelicula guardada"})


# lo mismo para actualización
@app.put("/pelicula", tags=["Actualizar Peli"])
def update_movie(id: int, peli: Movie):
    for item in movies:
        if item["id"] == id:
            item["title"] = peli.title
            item["overview"] = peli.overview
            item["year"] = peli.year
            item["rating"] = peli.rating
            item["category"] = peli.category
            return JSONResponse(content={"message": "Contenido actualizado"})


# en el calo de creación o modificación, en el cual retornamos un diccionario
# podemos indicarlo tambien
@app.post("/pelicula/", tags=["Create Movie"], response_model=dict)
def create_movie(movie: Movie) -> dict:
    movies.append(movie.model_dump())
    return JSONResponse(content={"message": "Pelicula guardada"})
