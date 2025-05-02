from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from pydantic import EmailStr
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.turno import Turno

class Paciente(SQLModel, table=True):
    __tablename__ = "paciente"

    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(max_length=30)
    last_name: str = Field(max_length=30)
    phone: str = Field(max_length=20, unique=True)
    email: EmailStr = Field(max_length=100, unique=True)
    number_identification: str = Field(max_length=30, unique=True)
    active: bool = Field(default=True)

    turnos: List["Turno"] = Relationship(back_populates="paciente")
