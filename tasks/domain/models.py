from typing import Set, Optional, Dict
from enum import Enum
from pydantic import BaseModel


class Status(Enum):
    DRAFT = "draft"
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class StatusMixin:
    __TRANSITIONS_MAP: Dict[Status, Set[Status]] = {
        Status.DRAFT: {
            Status.TODO,
            Status.IN_PROGRESS,
            Status.DONE,
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

    def __init__(self, status: Status, **kwargs):
        print("---status", status)
        self.status = status
        super().__init__(**kwargs)

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: Status):
        self.__status = Status(status)

    def transit_status(self, new_value: Status) -> None:
        if new_value in self._get_allowed_statuses():
            self.__status = new_value

    def _get_allowed_statuses(self) -> Set[Status]:
        status_from: Status = self.__status
        statuses: Set[Status] = self.__TRANSITIONS_MAP.get(status_from, set())
        statuses.add(status_from)
        return statuses


class Task(BaseModel, StatusMixin):
    id: int
    title: str
    description: Optional[str] = ""


