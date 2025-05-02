from fastapi import APIRouter, status, HTTPException
from pydantic import ValidationError
from sqlmodel import select

from schemas.rol import RolCreate, RolUpdate, RolRead, RolReadWithUsuarios
from models.rol import Roles
from core.database import SessionDep

router = APIRouter()

# Listar todos los roles
@router.get("/api/roles", response_model=list[RolRead], tags=["ROLES"])
def list_roles(session: SessionDep):
    try:
        return session.exec(select(Roles)).all()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al listar roles: {str(e)}",
        )

# Obtener un rol por ID
@router.get("/api/roles/{rol_id}", response_model=RolRead, tags=["ROLES"])
def read_rol(rol_id: int, session: SessionDep):
    try:
        rol_db = session.get(Roles, rol_id)
        if not rol_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Rol no encontrado"
            )
        return rol_db
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener el rol: {str(e)}",
        )
    
# obtener rol con usuarios relacionados
@router.get("/api/roles/{rol_id}/usuarios", response_model=RolReadWithUsuarios, tags=["ROLES"])
def read_rol_with_usuarios(rol_id: int, session: SessionDep):
    try:
        rol_db = session.get(Roles, rol_id)
        if not rol_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Role not found"
            )
        return rol_db
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while retrieving the role: {str(e)}"
        )


# Crear nuevo rol
@router.post("/api/roles", response_model=RolRead, status_code=status.HTTP_201_CREATED, tags=["ROLES"])
def create_rol(rol_data: RolCreate, session: SessionDep):
    try:
        rol = Roles.model_validate(rol_data.model_dump())
        existing_rol = session.exec(select(Roles).where(Roles.name == rol.name)).first()
        if existing_rol:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Rol ya registrado"
            )
        session.add(rol)
        session.commit()
        session.refresh(rol)
        return rol
    except HTTPException as http_exc:
        raise http_exc
    except ValidationError as ve:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Datos inválidos: {str(ve)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al crear rol: {str(e)}"
        )

# Eliminar un rol
@router.delete("/api/roles/{rol_id}", status_code=status.HTTP_200_OK, tags=["ROLES"])
def delete_rol(rol_id: int, session: SessionDep):
    try:
        rol_db = session.get(Roles, rol_id)
        if not rol_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Rol no encontrado"
            )
        session.delete(rol_db)
        session.commit()
        return {"detail": "Rol eliminado correctamente"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al eliminar rol: {str(e)}"
        )

# Actualizar un rol
@router.patch("/api/roles/{rol_id}", response_model=RolRead, tags=["ROLES"])
def update_rol(rol_id: int, rol_data: RolUpdate, session: SessionDep):
    try:
        rol_db = session.get(Roles, rol_id)
        if not rol_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Rol no encontrado"
            )
        rol_data_dict = rol_data.model_dump(exclude_unset=True)

        if "name" in rol_data_dict and rol_data_dict["name"] != rol_db.name:
            existing_rol = session.exec(select(Roles).where(Roles.name == rol_data_dict["name"])).first()
            if existing_rol and existing_rol.id != rol_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Nombre de rol ya registrado"
                )

        rol_db.sqlmodel_update(rol_data_dict)
        session.add(rol_db)
        session.commit()
        session.refresh(rol_db)
        return rol_db
    except HTTPException as http_exc:
        raise http_exc
    except ValidationError as ve:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Datos inválidos: {str(ve)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al actualizar rol: {str(e)}"
        )
