from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.usuario import Usuarios  # Importación segura para evitar ciclos

class Roles(SQLModel, table=True):
    __tablename__ = "rol"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=30, unique=True)
    description: str = Field(max_length=100)

    usuarios: List["Usuarios"] = Relationship(back_populates="roles")
