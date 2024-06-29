# Projeto DIO
## WorkoutAPI

Esta é uma API CRUD sobre crossfit chamada WorkoutAPI idealizada pela Expert Nayanna da DIO. 
É uma API simples e completa, seu intuito é ser hands-on, mas com o necessário para você aprender como utilizar o FastAPI e banco de dados.

## Stack da API

A API foi desenvolvida utilizando o `fastapi` (async), junto das seguintes libs: `alembic`, `SQLAlchemy`, `pydantic`. Para salvar os dados está sendo utilizando o `postgres`, por meio do `docker`.

## Execução da API

Para executar o projeto, crie um venv, ative-o e instale as dependencias.

```bash
python -m venv .venv
source activate
pip install -r requirements.txt
```
Para subir o banco de dados, caso não tenha o [docker-compose](https://docs.docker.com/compose/install/linux/) instalado, faça a instalação e logo em seguida, execute:

```bash
make run-docker
```
Para criar uma migration nova, execute:

```bash
make create-migrations d="nome_da_migration"
```

Para criar o banco de dados, execute:

```bash
make run-migrations
```

## API

Para subir a API, execute:
```bash
make run
```
e acesse: http://127.0.0.1:8000/docs

# Referências

FastAPI: https://fastapi.tiangolo.com/

Este repositório foi feito como estudo e inspirado no repositório original abaixo:
https://github.com/digitalinnovationone/workout_api 