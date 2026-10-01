from models import Employee
from models import Department
from models import Role
from models import Employee_role_mapping

def get_roles(db):
    return db.query(Role).all()

def get_role_by_id(id,db):
    print("e")
    return db.query(Role).filter(Role.role_id == id).first()


def create_roles(role,db):
    db.add(role)
    db.commit()
    db.refresh(role)
    return role

def save_role(current_roles, db):
    db.commit()
    db.refresh(current_roles)
    return current_roles


def delete_role(current_roles,db):
     db.delete(current_roles)
     db.commit()