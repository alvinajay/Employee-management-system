from models import Department
from datetime import datetime

from repositories import emp_repo


def get_departments(db):
    return (
        db.query(Department)
        .filter(Department.deleted_at == None)
        .order_by(Department.dept_id)
        .all()
    )

def get_departments_by_id(id, db):
    return (
        db.query(Department)
        .filter(
            Department.dept_id == id,
            Department.deleted_at == None
        )
        .first()
    )


def insert_department(department, db):
    db.add(department)
    db.commit()
    db.refresh(department)
    return department


def change_department(department, db):
    db.commit()
    db.refresh(department)
    return department

def delete_employee(id, db):
    employee = emp_repo.get_employee_model_by_id(id, db)

    if not employee:
        return {"message": "Employee not found"}

    employee.deleted_at = datetime.now()

    db.commit()

    return {"message": "Employee soft deleted successfully"}