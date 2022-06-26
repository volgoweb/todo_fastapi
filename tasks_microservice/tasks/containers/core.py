from dependency_injector.containers import DeclarativeContainer
from dependency_injector import providers

from tasks.db.tasks_repository import HardCodedTasksRepository
from tasks.domain.services.task_crud import TaskCrudService


class Container(DeclarativeContainer):
    config = providers.Configuration()
    tasks_repo = providers.Factory(HardCodedTasksRepository)
    task_crud_service = providers.Factory(
        TaskCrudService,
        repo=tasks_repo,
    )
