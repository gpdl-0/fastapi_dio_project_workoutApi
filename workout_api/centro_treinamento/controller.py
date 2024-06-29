from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy import select

from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.centro_treinamento.schemas import CentroTreinamentoIn, CentroTreinamentoOut
from workout_api.contrib.repository.dependencies import DatabaseDependency

router = APIRouter()

@router.post(path='/'
             ,summary='Criar nova categoria',
             status_code=status.HTTP_201_CREATED,
             response_model=CentroTreinamentoOut
             )
async def post(
    db_session: DatabaseDependency, 
    centro_treinamento_in: CentroTreinamentoIn = Body(...)
    ) -> CentroTreinamentoOut:
    centro_treinamento_out = CentroTreinamentoOut(id=uuid4(), **centro_treinamento_in.model_dump())
    centro_treinamento_model = CentroTreinamentoModel(**centro_treinamento_out.model_dump())
    db_session.add(centro_treinamento_model)
    await db_session.commit()
    return centro_treinamento_out

@router.get(path='/'
             ,summary='Consultar todas as categoria',
             status_code=status.HTTP_200_OK,
             response_model=list[CentroTreinamentoOut]
             )
async def query(db_session: DatabaseDependency) -> list[CentroTreinamentoOut]:
    categorias: list[CentroTreinamentoOut] = (
        await db_session.execute(select(CentroTreinamentoModel))).scalars().all()
    return categorias

@router.get(path='/{id}'
             ,summary='Consultar uma centro de treinamento pelo id',
             status_code=status.HTTP_200_OK,
             response_model=CentroTreinamentoOut
             )
async def query(id: UUID4, db_session: DatabaseDependency) -> CentroTreinamentoOut:
    centro_treinamento_out: CentroTreinamentoOut = (
        await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id))).scalars().first()
    if not centro_treinamento_out:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Centro de treinamento nao encontrada no id {id}'
            )
    return centro_treinamento_out