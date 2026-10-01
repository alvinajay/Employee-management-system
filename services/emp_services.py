from repositories import emp_repo as employee_repository
from models import Employee
from models import Department
from models import Role
from models import Employee_role_mapping
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError


def get_all_employees(db):
    print("three`")
    return employee_repository.get_all_employees(db)


def get_employee_by_id(id, db):
    print("two")
    employee = employee_repository.get_employee_by_id(id,db)
    if not employee:
        return {"message": "Employee not found"}
    return employee


def create_employee(employee, db):
    if employee.first_name.strip() == "":
        return {"message": "First name should not be empty"}
    if employee.last_name.strip() == "":
        return {"message": "Last name should not be empty"}
    if employee.role_id <= 0:
        return {"message": "Role ID should be greater than 0"}
    if employee.dept_id <= 0:
        return {"message": "Department ID should be greater than 0"}
    if employee.age < 18:
        return {"message": "Age should be greater than 18"}
    new_employee = Employee(
        first_name=employee.first_name,
        last_name=employee.last_name,
        age=employee.age,
        dept_id=employee.dept_id,
        role_id=employee.role_id
    )
    employee_repository.insert_employee(new_employee, db)
    return {
        "message": "Employee added successfully",
        "employee": new_employee
    }





def update_employee(id, employee, db):
    # Get the actual database model
    existing_employee = employee_repository.get_employee_model_by_id(id, db)

    if not existing_employee or existing_employee.deleted_at is not None:
        return {"message": "Employee not found"}

    if not employee.first_name.strip():
        return {"message": "First name should not be empty"}

    if not employee.last_name.strip():
        return {"message": "Last name should not be empty"}

    if employee.age < 18:
        return {"message": "Age must be at least 18"}

    try:
        existing_employee.first_name = employee.first_name.strip()
        existing_employee.last_name = employee.last_name.strip()
        existing_employee.age = employee.age
        existing_employee.dept_id = employee.dept_id
        existing_employee.role_id = employee.role_id

        # Commit changes to the database
        employee_repository.save_employee(existing_employee, db)

        return {
            "message": "Employee updated successfully",
            "employee": {
                "id": existing_employee.id,
                "first_name": existing_employee.first_name,
                "last_name": existing_employee.last_name,
                "age": existing_employee.age,
                "dept_id": existing_employee.dept_id,
                "role_id": existing_employee.role_id
            }
        }

    except Exception:
        db.rollback()
        raise

def patch_employee(id, employee, db):
    existing_employee = employee_repository.get_employee_by_id(id, db)
    if not existing_employee:
        return {"message": "Employee not found"}
    if employee.id is not None:
        existing_employee.id = employee.id
    if employee.first_name is not None:
        if employee.first_name.strip() == "":
            return {"message": "First name should not be empty"}
        existing_employee.first_name = employee.first_name
    if employee.last_name is not None:
        if employee.last_name.strip() == "":
            return {"message": "Last name should not be empty"}
        existing_employee.last_name = employee.last_name
    if employee.age is not None:
        if employee.age < 18:
            return {"message": "Age should be greater than or equal to 18"}
        existing_employee.age = employee.age
    if employee.dept_id is not None:
        if employee.dept_id <= 0:
            return {"message": "Department ID should be greater than 0"}
        existing_employee.dept_id = employee.dept_id
    if employee.role_id is not None:
        if employee.role_id <= 0:
            return {"message": "Role ID should be greater than 0"}
        existing_employee.role_id = employee.role_id
    try:
        employee_repository.save_employee(existing_employee, db)
    except IntegrityError:
        db.rollback()
        return {"message": "Employee ID already exists"}
    return {
        "message": "Employee updated successfully",
        "employee": existing_employee
    }

def delete_employee(id, db):
    employee = employee_repository.get_employee_model_by_id(id, db)
    if not employee:
        return {"message": "Employee does not exist"}
    employee_repository.delete_employee(employee, db)
    return {"message": "Employee deleted"}

def filter_by_role(role_id, db):
    employees = employee_repository.get_employee_by_role(role_id, db)
    if not employees:
        return {"message": "No employees found"}
    return employees