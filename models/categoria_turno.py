from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.turno import Turno

class CategoriaTurno(SQLModel, table=True):
    __tablename__ = "categoriaTurno"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=30, unique=True)
    description: str = Field(max_length=100)

    turnos: List["Turno"] = Relationship(back_populates="categoria_turno")
