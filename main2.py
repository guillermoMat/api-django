from config.database import engine, base
from fastapi import FastAPI
from routers.movie_router import movie_router
from routers.user_router import user_router


app = FastAPI()
base.metadata.create_all(bind=engine)

# El contenido de estos esta en la carpeta routers
app.include_router(movie_router)
app.include_router(user_router)
