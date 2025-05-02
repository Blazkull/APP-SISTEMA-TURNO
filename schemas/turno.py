from typing import Optional
from datetime import datetime
from pydantic import BaseModel


# Base
class TurnoBase(BaseModel):
    paciente_id: int
    categorias_id: int
    estado_turno_id: int
    usuario_id: int
    note: Optional[str] = None
    numero_turno: Optional[int] = None

# Crear
class TurnoCreate(TurnoBase):
    pass

# Actualizar
class TurnoUpdate(BaseModel):
    paciente_id: Optional[int] = None
    categorias_id: Optional[int] = None
    estado_turno_id: Optional[int] = None
    usuario_id: Optional[int] = None
    note: Optional[str] = None
    numero_turno: Optional[int] = None

# Leer
class TurnoRead(TurnoBase):
    id: int
    fecha_solicitud: datetime
    model_config = {
    "from_attributes": True
    }

    

#Eliminar
class TurnoDelete(TurnoBase):
    id:int
    model_config = {
    "from_attributes": True
    }