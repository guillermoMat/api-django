from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI()

app.title = "Doc. Dev. Mathieu"  # Cambiar titulo de la documentación


@app.get("/", tags=["GET base"])  # con "tags=["home"]" añadimos etiqueta a nuestra ruta
def initial():
    return "Hello word!"


@app.get("/saludo")
def mensajeBienvenida():
    return HTMLResponse("<h3>Hello words</h3>")


movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción",
    },
    {
        "id": 2,
        "title": "Duro de matar",
        "overview": "Mas duro que el roble, imposible de matar, nadie lo puede matar...",
        "year": "2015",
        "rating": 8.8,
        "category": "Acción",
    },
]


@app.get("/peliculas", tags=["GetMovies"])
def getPelis():
    return movies


@app.get("/pelicula/{id}", tags=["GetMovies"])
def get_Peli_ById(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return []


@app.get("/peliculas/", tags=["GetMovies"])
def get_Peli_ByCategory(category: str):
    listPelis = []
    for i in movies:
        if i["category"] == category:
            listPelis.append(i)
    if len(listPelis) == 0:
        return "No hay peliculas con esa categoria"
    else:
        return listPelis


# Creacion de pelicula
@app.post("/peliculas", tags=["CreateMovies"])
def create_movie(
    id: int = Body(),
    title: str = Body(),
    overview: str = Body(),
    year: str = Body(),
    rating: float = Body(),
    category: str = Body(),
):
    movies.append(
        {
            "id": id,
            "title": title,
            "overview": overview,
            "year": year,
            "rating": rating,
            "category": category,
        }
    )
    return movies


# actualizacion de elemento
@app.put("/peliculas/{id}", tags=["Update Movie"])
def update_movie(
    id: int,
    title: str = Body(),
    overview: str = Body(),
    year: str = Body(),
    rating: float = Body(),
    category: str = Body(),
):

    for item in movies:
        if item["id"] == id:
            item["title"] = title
            item["overview"] = overview
            item["year"] = year
            item["rating"] = rating
            item["category"] = category
            return movies


# eliminacion de pelicula
@app.delete("/pelicula/{id}", tags=["Delete Movie"])
def delete_movie(id: int):
    for i in movies:
        if i["id"] == id:
            movies.remove(i)
            return movies
    return "no se encontro la pelicula"
