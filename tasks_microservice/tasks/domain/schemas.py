from typing import Optional

from pydantic import BaseModel

from tasks.domain.models import Status


class CreateTaskInput(BaseModel):
    title: str
    description: Optional[str] = ""
    status: Optional[str] = None


class UpdateTaskInput(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[Status]
