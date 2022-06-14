from dependency_injector.containers import DeclarativeContainer
from dependency_injector import providers

from tasks.db.tasks_repository import HardCodedTasksRepository


class Container(DeclarativeContainer):
    config = providers.Configuration()
    tasks_repo = providers.Factory(HardCodedTasksRepository)
