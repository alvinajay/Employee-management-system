from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from services import role_service as role_service
from schemas.role import (
    Rolecreate,
    roleupdate
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/roles")
def get_roles(db: Session = Depends (get_db)):
    return role_service.get_roles(db)


@router.get("/roles/filter")
def get_role_by_id(id: int,db : Session = Depends (get_db)):
    return role_service.get_role_by_id(id,db)


@router.post("/roles")
def post_roles(role: Rolecreate,db: Session = Depends(get_db)):
    return role_service.create_role(role, db)

@router.put("/roles/filter")
def change_role(id: int, role: roleupdate, db: Session = Depends(get_db)):
    return role_service.change_role(id, role, db)


@router.delete("/roles/filter")
def delete_role(id: int,db : Session = Depends(get_db)):
    return role_service.delete_role(id,db)