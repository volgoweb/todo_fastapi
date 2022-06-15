from typing import Optional
from pydantic import BaseModel


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = ""
    status: Optional[str] = None


class CreateTaskData(BaseModel):
    title: str
    description: Optional[str] = ""
    status: Optional[str] = None
