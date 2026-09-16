from pydantic import BaseModel, Field

class LivroSchema(BaseModel):
    id: int
    titulo: str = Field(
        min_length=3,
        max_lenght=100,
    )
    autor: str = Field(
        min_lenght=3,
        max_length=100,
    )
    ano_publicacao: int
    