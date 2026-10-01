
from models import Employee
from models import Department
from models import Role
from models import Employee_role_mapping
from datetime import datetime
from sqlalchemy.orm import declarative_base, relationship

def get_all_employees(db):
    print("two")
    employees = (db.query(Employee).filter(Employee.deleted_at == None).order_by(Employee.id).all())
    result = []
    for emp in employees:
        result.append({
            "id": emp.id,
            "first_name": emp.first_name,
            "last_name": emp.last_name,
            "age": emp.age,
            "dept_name": emp.department.dept_name,
            "role_name": emp.role.role_name
        })

    return result


def get_employee_by_id(id, db):
    emp = (db.query(Employee).filter(Employee.deleted_at == None,Employee.id == id).first())

    if not emp:
        return None

    return {
        "id": emp.id,
        "first_name": emp.first_name,
        "last_name": emp.last_name,
        "age": emp.age,
        "dept_id": emp.dept_id,
        "role_id": emp.role_id,
        "dept_name": emp.department.dept_name,
        "role_name": emp.role.role_name
    }
def get_employee_model_by_id(id, db):
    return db.query(Employee).filter(Employee.id == id).first()

def get_employee_by_role(role_id, db):
    return db.query(Employee)\
        .filter(Employee.role_id == role_id)\
        .all()

def get_employee_by_name(name, db):
    return db.query(Employee)\
        .filter(Employee.first_name == name)\
        .all()

def get_employee_by_age(age, db):
    return db.query(Employee)\
        .filter(Employee.age == age)\
        .all()

def insert_employee(employee, db):
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

def save_employee(employee, db):
    db.commit()
    db.refresh(employee)
    return employee

def delete_employee(employee, db):
    employee.deleted_at = datetime.now()
    db.commit()
    db.refresh(employee)

def get_employee_by_letter(letter,db):
    print("g")
    return[
        {"name":name,"role":role}
     for name,role in (db.query(Employee.first_name)
     .filter(Employee.name.like(f"{letter}%"))
     .all())
    ]
