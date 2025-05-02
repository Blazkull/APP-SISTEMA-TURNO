from typing import List, Optional
from sqlmodel import SQLModel, Field
from typing import TYPE_CHECKING



class CategoriaTurnoBase(SQLModel):
    name: str = Field(max_length=30, unique=True)
    description: str = Field(max_length=100)

#crear
class CategoriaTurnoCreate(CategoriaTurnoBase):
    pass

#leer
class CategoriaTurnoRead(CategoriaTurnoBase):
    id: int

    model_config = {
    "from_attributes": True
    }
#eliminar
class CategoriaTurnoDelete(CategoriaTurnoRead):
    pass

#actualizar
class CategoriaTurnoUpdate(SQLModel):
    name: Optional[str] = None
    description: Optional[str] = None


#leer todos los tengan un turno con una categoria especifica
class CategoriaTurnoReadWithTurnos(CategoriaTurnoRead):
    turnos: List["TurnoRead"] = []

    model_config = {
    "from_attributes": True
    }

if TYPE_CHECKING:
    from schemas.turno import TurnoRead 