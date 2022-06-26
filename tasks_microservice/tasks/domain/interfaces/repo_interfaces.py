from typing import List

from tasks.domain.models import Task
from tasks.domain.schemas import CreateTaskInput, UpdateTaskInput


class ITaskRepo:
    def get_many(self) -> List[Task]:
        raise NotImplementedError()

    def get_by_id(self, task_id: int) -> Task:
        raise NotImplementedError()

    def create_task(self, data: CreateTaskInput) -> Task:
        raise NotImplementedError()

    def update_task(self, data: UpdateTaskInput) -> Task:
        raise NotImplementedError()

    def save_task(self, task: Task) -> Task:
        raise NotImplementedError()
