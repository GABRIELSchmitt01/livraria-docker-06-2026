from fastapi import FastAPI, HTTPException

Livros = ["Hobbit", "O Senhor dos Aneis", "O Principe"]

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Bem-vindo à API de livros!"}


# listar-livros
@app.get("/livros")
async def listar_livros():
    return {"livros": Livros}


# adicionar-livro
@app.post("/livros")
async def adicionar_livro(livro: str):
    Livros.append(livro)
    return {
        "message": "Livro adicionado com sucesso",
        "livros": Livros
    }


# atualizar-livro
@app.put("/livros/{index}")
async def atualizar_livro(index: int, new_livro: str):

    if index >= len(Livros) or index < 0:
        raise HTTPException(
            status_code=404,
            detail="Livro não encontrado"
        )

    Livros[index] = new_livro

    return {
        "message": "Livro atualizado com sucesso!",
        "livros": Livros
    }


# deletar-livro
@app.delete("/livros/{index}")
async def deletar_livro(index: int):

    if index >= len(Livros) or index < 0:
        raise HTTPException(
            status_code=404,
            detail="Livro não encontrado"
        )

    Livros.pop(index)

    return {
        "message": "Livro deletado com sucesso!",
        "livros": Livros
    }

