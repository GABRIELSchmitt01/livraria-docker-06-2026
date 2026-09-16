from fasapi import APIRouter, HTTPException
from app.schemas.livro import LivroSchema

router = APIRouter(
    prefixe="/livros",
    tags=["livros"],
)
