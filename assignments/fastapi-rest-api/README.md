# 📘 Tarefa: Construindo REST APIs com FastAPI

## 🎯 Objetivo

Os alunos aprenderão a construir uma REST API usando o framework FastAPI. Eles irão criar endpoints para gerenciar uma biblioteca de livros, evoluindo de rotas simples de leitura até um CRUD completo com validação de dados.

## 📝 Tarefas

### 🛠️ Primeiros Endpoints de Leitura

#### Descrição
Comece com o básico! Use o starter code fornecido para criar seus primeiros endpoints GET que retornam a lista de livros da biblioteca. Rode o servidor com `uvicorn` e explore a documentação interativa automática em `/docs`.

#### Requisitos
O programa concluído deve:

- Criar um endpoint `GET /books` que retorna a lista completa de livros
- Criar um endpoint `GET /books/{book_id}` que retorna um livro específico pelo seu `id`
- Retornar o status HTTP `404` com uma mensagem amigável quando o livro não for encontrado


### 🛠️ Criando Livros com Validação

#### Descrição
Agora vamos permitir adicionar novos livros! Use um modelo Pydantic para validar os dados recebidos e crie um endpoint POST. Experimente enviar dados inválidos pela documentação em `/docs` e observe como o FastAPI responde automaticamente.

#### Requisitos
O programa concluído deve:

- Definir um modelo Pydantic `Book` com os campos `title` (str), `author` (str) e `year` (int)
- Criar um endpoint `POST /books` que adiciona um novo livro à lista, gerando um `id` automaticamente
- Retornar o status HTTP `201` com o livro criado (incluindo o `id`) na resposta


### 🛠️ Atualizando e Removendo Livros

#### Descrição
Complete o CRUD! Adicione endpoints para atualizar e remover livros existentes. Lembre-se de tratar os casos em que o livro não existe.

#### Requisitos
O programa concluído deve:

- Criar um endpoint `PUT /books/{book_id}` que atualiza os dados de um livro existente
- Criar um endpoint `DELETE /books/{book_id}` que remove um livro da lista
- Retornar o status HTTP `404` quando o `book_id` não existir em ambos os endpoints


### 🛠️ Desafio: Busca e Filtros

#### Descrição
Deixe sua API ainda mais poderosa! Adicione query parameters ao endpoint de listagem para permitir buscas e filtros. Este é um desafio extra — use a criatividade!

#### Requisitos
O programa concluído deve:

- Permitir filtrar livros por autor com `GET /books?author=<nome>`
- Permitir buscar livros cujo título contenha um termo com `GET /books?search=<termo>` (sem diferenciar maiúsculas de minúsculas)
- Permitir combinar os dois filtros na mesma requisição
