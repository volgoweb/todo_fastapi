import asyncio
from icecream import ic

import aio_pika
import aio_pika.abc
from aiohttp import ClientSession, TCPConnector
from dependency_injector.wiring import Provide, inject
from fastapi import Depends, FastAPI, APIRouter

from tasks.containers.default import Container
from tasks.db.tasks_repository import HardCodedTasksRepository
from dependency_injector.wiring import Provide, inject


router = APIRouter()


@router.get("/", tags=["tasks"])
async def home():
    return "I'm here"


@router.get("/tasks", tags=["tasks"])
@inject
async def tasks(repo: HardCodedTasksRepository = Depends(Provide[Container.tasks_repo])):
    tasks = repo.get_many()
    return tasks
