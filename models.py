from sqlalchemy import Column, Integer, String ,ForeignKey,DateTime
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Department(Base):
    __tablename__ = "departments"

    dept_id = Column(Integer,primary_key = True)
    dept_name = Column(String)
    deleted_at = Column(DateTime)

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    dept_id = Column(Integer, ForeignKey("departments.dept_id"))
    role_id = Column(Integer, ForeignKey("roles.role_id"))
    deleted_at = Column(DateTime)
    department = relationship("Department")
    role = relationship("Role")


class Role(Base):
    __tablename__ = "roles"

    role_id = Column(Integer,primary_key = True)
    role_name = Column(String)
    deleted_at = Column(DateTime)

class Employee_role_mapping(Base):
    __tablename__ = "employee_role_mapping"
    mapping_id = Column(Integer,primary_key = True)
    employee_id = Column(Integer , ForeignKey('employees.id'))
    role_id = Column(Integer , ForeignKey('roles.role_id'))  