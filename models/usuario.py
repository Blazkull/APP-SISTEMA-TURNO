from typing import Optional, List
from pydantic import EmailStr
from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.rol import Roles
    from models.turno import Turno

class Usuarios(SQLModel, table=True):
    __tablename__ = "usuarios"

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(max_length=30, unique=True)
    email: EmailStr = Field(max_length=100, unique=True)
    password: str = Field(max_length=100)
    rol_id: int = Field(foreign_key="rol.id")
    active: bool = Field(default=True)

    roles: Optional["Roles"] = Relationship(back_populates="usuarios")
    turnos: List["Turno"] = Relationship(back_populates="usuario")
