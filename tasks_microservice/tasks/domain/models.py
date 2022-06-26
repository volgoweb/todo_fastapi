from typing import Set, Dict
from enum import Enum
from pydantic import BaseModel
from tasks.domain.exceptions import StatusTransitionForbidden


class CustomBase(BaseModel):
    class Config:
        validate_assignment = True

    def __setattr__(self, key, value):
        field_setter = getattr(self, f"_set_{key}")
        if field_setter:
            return field_setter(value)
        return super().__setattr__(key, value)


class Status(Enum):
    DRAFT = "draft"
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class StatusMixin(CustomBase):
    __TRANSITIONS_MAP: Dict[Status, Set[Status]] = {
        Status.DRAFT: {
            Status.TODO,
        },
        Status.TODO: {
            Status.IN_PROGRESS,
            Status.DONE,
        },
        Status.IN_PROGRESS: {
            Status.TODO,
            Status.DONE,
        },
    }

    status: Status

    def _set_status(self, status: Status):
        if not isinstance(status, Status):
            status = Status(status)

        print(self._get_allowed_statuses())
        if status in self._get_allowed_statuses():
            self.status = status
        else:
            raise StatusTransitionForbidden

    def _get_allowed_statuses(self) -> Set[Status]:
        statuses: Set[Status] = self.__TRANSITIONS_MAP.get(self.status, set())
        statuses.add(self.status)
        return statuses


class Task(StatusMixin, CustomBase):
    id: int
    title: str
    description: str
