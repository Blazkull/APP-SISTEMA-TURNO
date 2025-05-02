from typing import Optional
from sqlmodel import SQLModel
from pydantic import EmailStr
from typing import TYPE_CHECKING

class UsuarioBase(SQLModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    active: Optional[bool] = None

# Crear
class UsuarioCreate(UsuarioBase):
    password: str
    rol_id: int

# Leer básico
class UsuarioRead(UsuarioBase):
    id: int

    class Config:
        orm_mode = True

# Leer con rol_id
class UsuarioReadRol(UsuarioBase):
    id: int
    rol_id: int

    model_config = {
    "from_attributes": True
    }

# Leer con relación a Roles
class UsuarioReadWithRol(UsuarioRead):
    roles: Optional["Roles"]

    model_config = {
    "from_attributes": True
    }

# Actualizar
class UsuarioUpdate(SQLModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    rol_id: Optional[int] = None
    active: Optional[bool] = None

#eliminar
class UsuarioDelete(UsuarioRead):
    pass



#importar no globalmente si no cuando se necesite
if TYPE_CHECKING:
    from models.rol import Roles
