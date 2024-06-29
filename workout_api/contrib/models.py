from sqlalchemy.orm import DeclarativeBase,Mapped, mapped_column
from sqlalchemy import UUID
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from uuid import uuid4

# Parent class to declare a base model for all other child models
class BaseModel(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True),default=uuid4,nullable=False)