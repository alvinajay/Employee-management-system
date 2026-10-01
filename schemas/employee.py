from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    age: int
    dept_id: int
    role_id: int


class EmployeePut(BaseModel):
    first_name: str
    last_name: str
    age: int
    dept_id:int
    role_id:int

class EmployeePatch(BaseModel):
    id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[int] = None
    dept_id:Optional[int] = None
    role_id:Optional[int] = None


class DepartmentCreate(BaseModel):
    dept_id: int
    dept_name: str
    created_at: datetime
    deleted_at: datetime

class Departmentupdate(BaseModel):
    dept_id: int
    dept_name: str
    created_at: datetime
    deleted_at: datetime


    
class Rolecreate(BaseModel):
    role_id : int
    role_name: str
    created_at: datetime
    deleted_at: datetime

class roleupdate(BaseModel):
    role_id : int
    role_name: str
    created_at: datetime
    deleted_at: datetime