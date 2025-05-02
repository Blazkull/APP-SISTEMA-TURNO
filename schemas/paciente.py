from typing import List, Optional
from sqlmodel import SQLModel, Field
from pydantic import EmailStr
from typing import TYPE_CHECKING



class PacienteBase(SQLModel):
    first_name: str = Field(max_length=30)
    last_name: str = Field(max_length=30)
    phone: str = Field(max_length=20)
    email: EmailStr = Field(max_length=100)
    number_identification: str = Field(max_length=30)
    active: bool = Field(default=True)

# Crear paciente
class PacienteCreate(PacienteBase):
    pass

# Leer paciente
class PacienteRead(PacienteBase):
    id: int

    model_config = {
    "from_attributes": True
    }

# Leer paciente con turnos relacionados
class PacienteReadWithTurnos(PacienteRead):
    turnos: List["TurnoRead"] = []

    model_config = {
    "from_attributes": True
    }

# Actualizar paciente
class PacienteUpdate(SQLModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    number_identification: Optional[str] = None
    active: Optional[bool] = None

#eliminar paciente
class PacienteDelete(PacienteRead):
    pass


#importar no globalmente
if TYPE_CHECKING:
    from schemas.turno import TurnoRead  