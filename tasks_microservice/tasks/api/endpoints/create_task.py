from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status
from tasks.containers.core import Container
from tasks.domain import models
from tasks.domain.schemas import CreateTaskInput
from tasks.domain.services.task_crud import TaskCrudService

router = APIRouter()


@router.post("/tasks", tags=["tasks"], status_code=status.HTTP_201_CREATED, response_model=models.Task)
@inject
async def create_task(
    data: CreateTaskInput,
    service: TaskCrudService = Depends(Provide[Container.task_crud_service]),
):
    task = service.create_task(data)
    return task
