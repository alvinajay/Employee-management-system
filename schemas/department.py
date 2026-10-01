from pydantic import BaseModel
from typing import Optional
from datetime import datetime

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
