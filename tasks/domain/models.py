from typing import Set, NoReturn
from enum import Enum


class Status(Enum):
    DRAFT = "draft"
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class StatusMixin:
    __TRANSITIONS_MAP = {
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

    def __init__(self, status: Status):
        self.status = status

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: Status):
        self.__status = Status(status)

    def transit_status(self, new_value: Status) -> NoReturn:
        if new_value in self._get_allowed_statuses():
            self.__status = new_value

    def _get_allowed_statuses(self) -> Set[Status]:
        status_from = self.__status
        statuses = self.__TRANSITIONS_MAP.get(status_from, {})
        statuses.add(status_from)
        return statuses


class Task(StatusMixin):
    pass
