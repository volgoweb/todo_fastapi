from tasks.domain.interfaces.repo_interfaces import ITaskRepo
from tasks.domain.models import Task
from tasks.domain.schemas import CreateTaskInput, UpdateTaskInput


class TaskCrudService:
    def __init__(self, repo: ITaskRepo):
        self._repo = repo

    def create_task(self, data: CreateTaskInput) -> Task:
        task = self._repo.create_task(data)
        return task

    def update_task(self, task_id: int, data: UpdateTaskInput) -> Task:
        task = self._repo.get_by_id(task_id)
        for field, value in data.dict().items():
            # ?? do something if some field is changed
            setattr(task, field, value)
        self._repo.save_task(task)
        return task
