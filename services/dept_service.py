from repositories import dept_repo as dept_repo
from models import Employee
from models import Department
from models import Role
from models import Employee_role_mapping
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError

def get_departments(db):
    return dept_repo.get_departments(db)

def get_departments_by_id(id,db):
    print("w")
    return dept_repo.get_departments_by_id(id,db)


def create_Department(department, db):
    current_department = dept_repo.get_departments_by_id(department.dept_id,db)
    if current_department:
        return {"message": "Department already exists"}
    if department.dept_name.strip() == "":
        return {"message": "Name should not be empty"}
    new_department = Department(
        dept_id=department.dept_id,
        dept_name=department.dept_name,
        created_at=department.created_at
    )
    dept_repo.insert_department(new_department, db)
    return {
        "message": "Department added successfully",
        "Department": new_department
    }


def update_department(id, department, db):
    current_department = dept_repo.get_departments_by_id(id,db)
    if not current_department:
        return {"message": "department not found"}
    current_department.dept_id = department.dept_id
    current_department.dept_name = department.dept_name
    current_department.created_at = department.created_at
    try:
        dept_repo.change_department(current_department,db)
    except IntegrityError:
        db.rollback()
        return {"message": "department nalready exists"}
    return {
        "message": "department updated successfully",
        "employee": current_department
    }


def delete_department(id, db):
    current_department = dept_repo.get_departments_by_id(id, db)

    if not current_department:
        return {"message": "Department does not exist"}

    dept_repo.delete_department(current_department, db)

    return {"message": "Department deleted"}