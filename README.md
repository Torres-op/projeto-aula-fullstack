# Biblioteca

Projeto da aula de FullStack feito com Django e PostgreSQL.

Permite cadastrar livros e organizá-los em acervos. Cada acervo tem:

- **Tipo:** Digital ou Físico.
- **Categoria:** segue a Classificação Decimal de Dewey (000 a 900).

| Código | Categoria |
|---|---|
| 000 | Generalidades e Informação |
| 100 | Filosofia e Psicologia |
| 200 | Religião e Teologia |
| 300 | Ciências Sociais e Direito |
| 400 | Linguística e Idiomas |
| 500 | Ciências Puras (Exatas e Naturais) |
| 600 | Ciências Aplicadas (Tecnologia) |
| 700 | Artes e Recreação |
| 800 | Literatura |
| 900 | História e Geografia |

Os acervos podem ser pesquisados por nome do livro, tipo e categoria.

## Requisitos

- Python 3.12 ou mais recente
- PostgreSQL

## Como rodar

1. Crie e ative o ambiente virtual:

   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Instale as dependências:

   ```powershell
   pip install -r requirements.txt
   ```

3. Crie um banco de dados vazio no PostgreSQL.

4. Copie o arquivo de exemplo e preencha com os dados do banco:

   ```powershell
   copy .env.example .env
   ```

5. Crie as tabelas no banco:

   ```powershell
   python manage.py migrate
   ```

6. Crie um usuário para acessar o admin:

   ```powershell
   python manage.py createsuperuser
   ```

7. Inicie o servidor:

   ```powershell
   python manage.py runserver
   ```

## Como rodar com Docker

Com o Docker não é preciso instalar o Python nem o PostgreSQL: o `docker-compose.yml` sobe o banco e o projeto juntos.

1. Crie o arquivo `.env` como no passo 4 acima. O banco é criado com esses dados na primeira vez que o projeto sobe.

2. Suba o projeto. As tabelas são criadas automaticamente:

   ```powershell
   docker compose up --build
   ```

3. Para criar um usuário do admin, abra outro terminal e rode:

   ```powershell
   docker compose exec web python manage.py createsuperuser
   ```

4. Para parar, aperte `Ctrl+C` ou rode `docker compose down`. Os dados do banco continuam salvos para a próxima vez. Para apagar o banco também, rode `docker compose down -v`.

As alterações no código aparecem sem precisar subir o projeto de novo.

## Páginas

| Endereço | O que faz |
|---|---|
| http://127.0.0.1:8000/livros/ | Lista os livros |
| http://127.0.0.1:8000/livros/novo/ | Cadastra um livro |
| http://127.0.0.1:8000/acervos/ | Pesquisa acervos por nome, tipo e categoria |
| http://127.0.0.1:8000/admin/ | Cadastra livros e acervos |

Para montar um acervo, entre no admin, cadastre os livros e depois crie o acervo escolhendo o tipo, a categoria e os livros.
