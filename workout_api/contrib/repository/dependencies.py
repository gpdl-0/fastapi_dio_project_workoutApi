from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from workout_api.configs.db import get_session

DatabaseDependency = Annotated[AsyncSession,Depends(get_session)]