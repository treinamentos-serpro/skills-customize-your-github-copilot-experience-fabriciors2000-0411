# Código Inicial: Construindo REST APIs com FastAPI
#
# Para instalar as dependências:
#   pip install fastapi uvicorn
#
# Para rodar o servidor:
#   uvicorn starter-code:app --reload
#
# Depois acesse a documentação interativa em: http://127.0.0.1:8000/docs

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API da Biblioteca", version="1.0.0")

# "Banco de dados" em memória para começar
books = [
    {"id": 1, "title": "O Pequeno Príncipe", "author": "Antoine de Saint-Exupéry", "year": 1943},
    {"id": 2, "title": "Dom Casmurro", "author": "Machado de Assis", "year": 1899},
    {"id": 3, "title": "Harry Potter e a Pedra Filosofal", "author": "J.K. Rowling", "year": 1997},
]


# Tarefa 2: Defina aqui o modelo Pydantic Book
# class Book(BaseModel):
#     ...


@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API da Biblioteca! Acesse /docs para explorar."}


# Tarefa 1: Crie o endpoint GET /books


# Tarefa 1: Crie o endpoint GET /books/{book_id}
# Dica: use HTTPException(status_code=404, detail="...") quando o livro não existir


# Tarefa 2: Crie o endpoint POST /books


# Tarefa 3: Crie o endpoint PUT /books/{book_id}


# Tarefa 3: Crie o endpoint DELETE /books/{book_id}
