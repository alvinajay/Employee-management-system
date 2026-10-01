from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from services import dept_service
from schemas.department import (
    DepartmentCreate,
    Departmentupdate
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/departments")
def get_departments(db: Session = Depends (get_db)):
    return dept_service.get_departments(db)


@router.get("/departments/filter")
def get_departments_by_id(id: int,db: Session = Depends(get_db)):
    print("d")
    return dept_service.get_departments_by_id(id,db)

@router.post("/department")
def post_department(department: DepartmentCreate,db: Session = Depends(get_db)):
    return dept_service.create_Department(department, db)


@router.put("/department/filter")
def update_department(id: int,department: Departmentupdate,db: Session = Depends(get_db)):
    return dept_service.update_department(id,department,db)


@router.delete("/department/filter")
def delete_department(id: int, db: Session = Depends(get_db)):
    return dept_service.delete_department(id, db)