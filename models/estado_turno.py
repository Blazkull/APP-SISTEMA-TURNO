from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.turno import Turno

class EstadoTurno(SQLModel, table=True):
    __tablename__ = "estado_turno"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=30, unique=True)
    description: str = Field(max_length=100)

    turnos: List["Turno"] = Relationship(back_populates="estado_turno")
