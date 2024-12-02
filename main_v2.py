from typing import Optional
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field

# VAMOS A UTILIZAR Pydantic EN ESTE ARCHIVO
# tambien podemos utilizar validaciones que nos proporciona "pydantic", especificamente "Field"

app2 = FastAPI()

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


@app2.get("/movies", tags=["Get Movies"])
def getMovies():
    return movies


# Creando una pelicula utilizando el modelo BaseModel
@app2.post("/movies", tags=["createMovie"])
def createMovie(peli: Movie):
    movies.append(peli)
    return movies


# Actualizando una pelicula utilizando el modelo BaseModel
@app2.put("/movie/{id}", tags=["UpdateMovie"])
def updateMovie(id: int, peli: Movie):
    for item in movies:
        if item["id"] == id:
            item["title"] = peli.title
            item["overview"] = peli.overview
            item["year"] = peli.year
            item["rating"] = peli.rating
            item["category"] = peli.category
            return movies


# Obteniendo una pelicula por id y poniendole un rango de 1 a 200 con Path
@app2.get("/peli_by_id/{id}", tags=["Get Movies"])
def get_movie_byID(id: int = Path(ge=1, le=200)):
    for i in movies:
        if i["id"] == id:
            return i
    return []


# Obteniendo una pelicula por categoria y poniendo parametro con Query
@app2.get("/movies_by_category/", tags=["Get Movies"])
def get_movie_byCategory(category: str = Query(min_length=5, max_length=15)):
    listMovies = []
    for item in movies:
        if item["category"] == category:
            listMovies.append(item)

    if len(listMovies) > 0:
        return listMovies
    else:
        return "No se encontro esa categoria"
