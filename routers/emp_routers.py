from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from services import emp_services as employee_service
from schemas.employee import (
    EmployeeCreate,
    EmployeePut,
    EmployeePatch
)
from schemas.department import(
    DepartmentCreate,
    Departmentupdate
)
from schemas.role import(
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

@router.get("/employees")
def employees(db: Session = Depends(get_db)):
    print("one")
    return employee_service.get_all_employees(db)

@router.get("/employees/filter")
def get_employee(id: int, db: Session = Depends(get_db)):
    return employee_service.get_employee_by_id(id, db)

@router.post("/employeeinput")
def create_employee(employee: EmployeeCreate,db: Session = Depends(get_db)):
    print("POST RECEIVED")
    return employee_service.create_employee(employee, db)

@router.put("/employees/filter")
def update_employee(id: int,employee: EmployeePut,db: Session = Depends(get_db)):
    return employee_service.update_employee(id, employee, db)

@router.patch("/employees/filter")
def patch_employee(id: int,employee: EmployeePatch,db: Session = Depends(get_db)):
    return employee_service.patch_employee(id, employee, db)

@router.delete("/employees/filter")
def delete_employee(id: int,db: Session = Depends(get_db)):
    return employee_service.delete_employee(id, db)

@router.get("/employeesbyrole/filter")
def department(role_id: int,db: Session = Depends(get_db)):
    return employee_service.filter_by_role(role_id, db)

@router.get("/search/filter")
def searchname(name: str,db: Session = Depends(get_db)):
    return employee_service.filter_by_name(name, db)

@router.get("/employeesbyage/filter")
def age(age: int,db: Session = Depends(get_db)):
    return employee_service.filter_by_age(age, db)

@router.get("/welcome/filter")
def welcome(name: str,db: Session = Depends(get_db)):
    return employee_service.welcome_employee(name, db)

@router.get("/role")
def departments(db: Session = Depends(get_db)):
    return employee_service.role_statistics(db)

@router.get("/salary")
def salary(db: Session = Depends(get_db)):
    return employee_service.salary_statistics(db)

@router.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):
    return employee_service.dashboard_statistics(db)

@router.get("/employee/count")
def employee_count(db: Session = Depends(get_db)):
    return employee_service.employee_count(db)

@router.get("/employeessalary/highest-salary")
def highest_salary(db: Session = Depends(get_db)):
    return employee_service.highest_salary(db)

@router.get("/employeessalary/lowest-salary")
def lowest_salary(db: Session = Depends(get_db)):
    return employee_service.lowest_salary(db)

@router.get("/employeebyalphabet/filter")
def employee_by_letter(letter: str,db: Session = Depends(get_db)):
    return employee_service.get_employee_by_letter(letter,db)