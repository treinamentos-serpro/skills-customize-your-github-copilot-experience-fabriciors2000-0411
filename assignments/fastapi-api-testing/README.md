# 📘 Assignment: Testes Automatizados para APIs FastAPI

## 🎯 Objective

Aprenda a verificar automaticamente o comportamento de uma API FastAPI com `pytest` e `TestClient`. Você vai testar respostas de sucesso, validações e erros sem precisar iniciar um servidor web separado.

## 📝 Tasks

### 🛠️ Configure o cliente de testes

#### Descrição
Use a API da biblioteca criada na atividade anterior. Instale `pytest` e `httpx`, crie um arquivo `test_api.py` e configure nele o `TestClient` apontando para a aplicação FastAPI. Ajuste o import para o nome do módulo da sua aplicação.

#### Requisitos
O programa concluído deve:

- Criar um cliente de testes usando `fastapi.testclient.TestClient`
- Testar `GET /books` e confirmar que a resposta tem status `200` e contém uma lista
- Testar `GET /books/{book_id}` com um livro existente e confirmar os dados retornados


### 🛠️ Verifique validações e respostas de erro

#### Descrição
Escreva testes para os dados enviados à API e para os casos em que um livro não existe. Use as respostas HTTP para confirmar se a aplicação trata cada situação como esperado.

#### Requisitos
O programa concluído deve:

- Testar `POST /books` com dados válidos e confirmar o status `201` e o livro criado
- Testar `POST /books` com dados inválidos ou campos obrigatórios ausentes e confirmar o status `422`
- Testar a busca de um `book_id` inexistente e confirmar o status `404`


### 🛠️ Teste atualizações, remoções e isolamento

#### Descrição
Complete a cobertura dos endpoints de escrita. Como os dados da API podem ficar em memória entre chamadas, prepare dados conhecidos para cada teste para que a ordem de execução não altere os resultados.

#### Requisitos
O programa concluído deve:

- Testar `PUT /books/{book_id}` com um livro existente e confirmar o status `200` e os dados atualizados
- Testar `DELETE /books/{book_id}` com um livro existente e confirmar que ele não aparece mais na listagem
- Testar `PUT` e `DELETE` com um `book_id` inexistente e confirmar o status `404`
- Executar todos os testes com `pytest -q` e obter aprovação sem depender da ordem em que são executados