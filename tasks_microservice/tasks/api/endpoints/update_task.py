from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject
from tasks.containers.core import Container
from tasks.domain import models
from tasks.domain.schemas import UpdateTaskInput
from tasks.domain.services.task_crud import TaskCrudService

router = APIRouter()


@router.patch("/tasks/{task_id}", response_model=models.Task)
@inject
async def update_task(
    task_id: int,
    data: UpdateTaskInput,
    service: TaskCrudService = Depends(Provide[Container.task_crud_service]),
):
    task = service.update_task(task_id, data)
    return task
