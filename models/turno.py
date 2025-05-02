from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.categoria_turno import CategoriaTurno
    from models.estado_turno import EstadoTurno
    from models.paciente import Paciente
    from models.usuario import Usuarios

# Definir el modelo de la tabla Turno
class Turno(SQLModel, table=True):
    __tablename__ = "turnos"

    id: Optional[int] = Field(default=None, primary_key=True)
    paciente_id: int = Field(foreign_key="paciente.id")
    categorias_id: int = Field(foreign_key="categoria_turno.id")
    estado_turno_id: int = Field(foreign_key="estado_turno.id")
    usuario_id: int = Field(foreign_key="usuarios.id")
    fecha_solicitud: datetime = Field(default_factory=datetime.now)
    note: Optional[str] = Field(max_length=40)
    numero_turno: Optional[int] = None

    # Relaciones
    usuario: Optional["Usuarios"] = Relationship(back_populates="turnos")
    paciente: Optional["Paciente"] = Relationship(back_populates="turnos")
    categoria_turno: Optional["CategoriaTurno"] = Relationship(back_populates="turnos")
    estado_turno: Optional["EstadoTurno"] = Relationship(back_populates="turnos")
