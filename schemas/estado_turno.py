from typing import List, Optional
from sqlmodel import SQLModel, Field
from typing import TYPE_CHECKING



#base
class EstadoTurnoBase(SQLModel):
    name: str = Field(max_length=30, unique=True)
    description: str = Field(max_length=100)

#crear
class EstadoTurnoCreate(EstadoTurnoBase):
    pass

#leer
class EstadoTurnoRead(EstadoTurnoBase):
    id: int

    model_config = {
    "from_attributes": True
    }
#eliminar
class EstadoTurnoDelete(EstadoTurnoRead):
    pass

#actualizar
class EstadoTurnoUpdate(SQLModel):
    name: Optional[str] = None
    description: Optional[str] = None

#listar turnos por estado de turno    
class EstadoTurnoReadWithTurnos(EstadoTurnoRead):
    turnos: List["TurnoRead"] = []

    model_config = {
    "from_attributes": True
    }

#importar no globalmente
if TYPE_CHECKING:
    from schemas.turno import TurnoRead 