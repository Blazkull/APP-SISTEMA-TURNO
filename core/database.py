
from typing import Annotated
from fastapi import Depends
from sqlmodel import SQLModel, create_engine, Session
from core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=True)

def create_db_and_tables():
    from models.rol import Roles
    from models.usuario import Usuarios
    from models.categoria_turno import CategoriaTurno
    from models.estado_turno import EstadoTurno
    from models.paciente import Paciente
    from models.turno import Turno

    print("Creando tablas...")

    # Primero creas las tablas que no tienen claves foráneas
    SQLModel.metadata.create_all(engine, tables=[CategoriaTurno.__table__, EstadoTurno.__table__])

    # Luego creas las tablas que tienen claves foráneas pero no dependen de 'Turno'
    SQLModel.metadata.create_all(engine, tables=[Roles.__table__, Usuarios.__table__, Paciente.__table__])

    # Finalmente, creas la tabla 'Turno' que depende de las otras
    SQLModel.metadata.create_all(engine, tables=[Turno.__table__])

    print("Tablas creadas correctamente.")


def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]