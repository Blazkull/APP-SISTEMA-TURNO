from typing import List, Optional
from sqlmodel import SQLModel, Field
from typing import TYPE_CHECKING


class RolBase(SQLModel):
    name: str = Field(max_length=30, unique=True)
    description: str = Field(max_length=100)

# Crear
class RolCreate(RolBase):
    pass

# Leer básico
class RolRead(RolBase):
    id: int

    model_config = {
    "from_attributes": True
    }
# Leer con usuarios relacionados
class RolReadWithUsuarios(RolRead):
    usuarios: List["UsuarioRead"] = []

    model_config = {
    "from_attributes": True
    }
# Actualizar
class RolUpdate(SQLModel):
    name: Optional[str] = None
    description: Optional[str] = None

#eliminar
class RolDelete(RolRead):
    pass


#importar no globalmente

if TYPE_CHECKING:
    from schemas.usuario import UsuarioRead