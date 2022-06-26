from typing import List

from fastapi import Depends, APIRouter

from tasks.containers.core import Container
from tasks.db.tasks_repository import HardCodedTasksRepository
from tasks.domain import models
from tasks.api.endpoints import create_task, update_task, healthcheck
from dependency_injector.wiring import Provide, inject


router = APIRouter()
router.include_router(create_task.router)
router.include_router(update_task.router)
router.include_router(healthcheck.router)


@router.get("/", tags=["tasks"])
async def home():
    return "I'm here"


@router.get("/tasks", tags=["tasks"], response_model=List[models.Task])
@inject
async def tasks(repo: HardCodedTasksRepository = Depends(Provide[Container.tasks_repo])):
    return repo.get_many()
