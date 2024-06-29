from pydantic import UUID4, Field
from typing import Annotated

from workout_api.contrib.schemas import BaseSchema

class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', examples='CT King',max_length=20)]
    endereco: Annotated[str, Field(description='Endereco', examples='Rua 10, n 137',max_length=60)]
    proprietario: Annotated[int, Field(description='Marcos da Rocha', examples=30)]

class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', examples='CT King',max_length=20)]

class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description='Identificador do centro de treinamento')]
    