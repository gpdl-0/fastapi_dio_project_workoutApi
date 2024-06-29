from pydantic import Field, PositiveFloat
from typing import Annotated, Optional

from workout_api.categorias.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta
from workout_api.contrib.schemas import BaseSchema, OutMixin

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Atleta', examples='Giovanni',max_length=50)]
    cpf: Annotated[str, Field(description='CPF do Atleta', examples='12345678900',max_length=11)]
    idade: Annotated[int, Field(description='Idade do Atleta', examples=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do Atleta', examples=77.9)]
    altura: Annotated[PositiveFloat, Field(description='Altura do Atleta', examples=1.70)]
    sexo: Annotated[str, Field(description='Sexo do Atleta', examples='M',max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do atleta')]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description='Centro de treinamento do atleta')]
    
class AtletaIn(Atleta):
    pass
class AtletaOut(Atleta, OutMixin):
    pass

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description='Nome do Atleta', examples='Giovanni',max_length=50)]
    idade: Annotated[Optional[int], Field(None, description='Idade do Atleta', examples=25)]
