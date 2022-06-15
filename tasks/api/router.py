import asyncio
from typing import List

from fastapi import Depends, APIRouter

from tasks.containers.core import Container
from tasks.db.tasks_repository import HardCodedTasksRepository
from tasks import schemas
from tasks.domain import models
from dependency_injector.wiring import Provide, inject


router = APIRouter()


@router.get("/", tags=["tasks"])
async def home():
    return "I'm here"


@router.get("/tasks", tags=["tasks"], response_model=List[models.Task])
@inject
async def tasks(repo: HardCodedTasksRepository = Depends(Provide[Container.tasks_repo])):
    return repo.get_many()


@router.post("/tasks", tags=["tasks"], response_model=models.Task)
@inject
async def create_task(task_data: schemas.CreateTaskData, repo: HardCodedTasksRepository = Depends(Provide[Container.tasks_repo])):
    task = repo.create(task_data)
    return task
