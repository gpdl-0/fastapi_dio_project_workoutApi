from datetime import datetime
from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy import select

from workout_api.atleta.schemas import AtletaIn,AtletaOut, AtletaUpdate
from workout_api.categorias.models import CategoriaModel
from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.contrib.repository.dependencies import DatabaseDependency
from workout_api.atleta.models import AtletaModel

router = APIRouter()

@router.post(path='/'
             ,summary='Criar novo atleta',
             status_code=status.HTTP_201_CREATED,
             response_model=AtletaOut
             )

async def post(
    db_session: DatabaseDependency, 
    atleta_in: AtletaIn = Body(...)
    ):

    categoria_name = atleta_in.categoria.nome
    centro_treinamento_nome = atleta_in.centro_treinamento.nome

    categoria = (await db_session.execute(
        select(CategoriaModel).filter_by(nome=categoria_name))
        ).scalars().first()
    
    if not categoria:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'Categoria {categoria_name} nao foi encontrada')
    
    centro_treinamento = (await db_session.execute(
        select(CentroTreinamentoModel).filter_by(nome=categoria_name))
        ).scalars().first()
    
    if not centro_treinamento:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'O {centro_treinamento_nome} nao foi encontrado')
    
    atleta_out = AtletaOut(id=uuid4(),created_at=datetime.utcnow(), **atleta_in.model_dump())
    atleta_model = AtletaModel(**atleta_out.model_dump(exclude={'categoria', 'centro_treinamento'}))
    atleta_model.categoria_id = categoria.pk_id

    db_session.add(atleta_model)
    await db_session.commit()
    
    return atleta_out

@router.get(path='/'
             ,summary='Consultar todos os atletas',
             status_code=status.HTTP_200_OK,
             response_model=list[AtletaOut]
             )
async def query(db_session: DatabaseDependency) -> list[AtletaOut]:
    atletas: list[AtletaOut] = (
        await db_session.execute(select(AtletaModel))).scalars().all()
    
    return [AtletaOut.model_validate(atleta) for atleta in atletas]

@router.get(path='/{id}'
             ,summary='Consultar um atleta pelo id',
             status_code=status.HTTP_200_OK,
             response_model=AtletaOut
             )
async def get(id: UUID4, db_session: DatabaseDependency) -> AtletaOut:
    atleta: AtletaOut = (
        await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()
    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Categoria nao encontrada no id {id}'
            )
    return atleta

@router.patch(path='/{id}'
             ,summary='Editar um atleta pelo id',
             status_code=status.HTTP_200_OK,
             response_model=AtletaOut
             )
async def get(id: UUID4, db_session: DatabaseDependency, atleta_up: AtletaUpdate = Body(...)) -> AtletaOut:
    atleta: AtletaOut = (
        await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()
    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Categoria nao encontrada no id {id}'
            )
    atleta_update = atleta_up.model_dump(exclude_unset=True)
    for key,value in atleta_update.items():
        setattr(atleta, key, value)
    await db_session.commit()
    await db_session.refresh(atleta)
    return atleta

@router.dekete(path='/{id}'
             ,summary='Deletar um atleta pelo id',
             status_code=status.HTTP_204_NO_CONTENT,
             )
async def get(id: UUID4, db_session: DatabaseDependency) -> None:
    atleta: AtletaOut = (
        await db_session.execute(select(AtletaModel).filter_by(id=id))).scalars().first()
    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Categoria nao encontrada no id {id}'
            )
    await db_session.delete(atleta)
    await db_session.commit(atleta)
