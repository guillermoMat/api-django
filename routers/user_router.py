from typing import Optional
from fastapi import Depends, APIRouter, HTTPException, Request
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer
from jwt_manager import create_token, validate_token

user_router = APIRouter()

# UTILIZAMOS ESTE ROUTER EN MAIN2


class User(BaseModel):
    email: str
    passw: str


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


class JWTBearer(HTTPBearer):
    async def __call__(
        self, request: Request
    ):  # tiene que ser async por la llamada al super()
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data["email"] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="Credenciales incorrectas")


"""
Cuando defines una función como async def, indicas que esa función será una "función asíncrona".
Esto significa que puede contener llamadas a otras funciones asíncronas y puede utilizar la palabra clave await para esperar
a que se completen estas llamadas de forma asíncrona, sin bloquear la ejecución del programa principal.

Cuando se llama a una función asíncrona, esta devuelve un "objeto awaitable". Este objeto se puede esperar utilizando la palabra clave await.
Al hacerlo, el control se devuelve al bucle de eventos (event loop) de Python, que puede continuar ejecutando otras tareas mientras espera
a que la operación asíncrona se complete
"""


@user_router.post("/path", tags=["Autenticación"])
def auth(usuario: User):
    if usuario.email == "admin@gmail.com" and usuario.passw == "admin123":
        token = create_token(usuario.model_dump())
        return JSONResponse(content=token)
    return JSONResponse(content={"error": "Credenciales inválidas"}, status_code=401)


@user_router.get("/movies", tags=["All movies"], dependencies=[Depends(JWTBearer)])
def get_movies():
    return JSONResponse(content=movies)


"""
{
  "email": "admin@gmail.com",
  "passw": "admin123"
}
"""
