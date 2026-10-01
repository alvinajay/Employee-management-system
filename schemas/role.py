from pydantic import BaseModel
from typing import Optional
from datetime import datetime

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