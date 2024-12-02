from fastapi import FastAPI

app = FastAPI()

"""
class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(max_length=30)
    overview: str = Field(default="Agregar descripción")
    year: int
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=5, max_length=15)
    """
