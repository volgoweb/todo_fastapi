from typing import Dict, Set, NoReturn, Iterable, Tuple, List, DefaultDict, Optional
from collections import defaultdict
from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
from icecream import ic  # type: ignore


app = FastAPI()


class User(BaseModel):
    id: int
    name: str


class Reminder(BaseModel):
    id: int
    name: str
    task_id: int


class Task(BaseModel):
    id: int
    title: str
    author_id: int
    author: Optional[User]
    assignee_id: int
    assignee: Optional[User]
    reminders: Optional[List[Reminder]]


class TaskCollection:
    async def get_many(self) -> List[Task]:
        await asyncio.sleep(1)
        return [
            Task(
                id=1,
                title="task-1",
                assignee_id=1,
                author_id=2,
            ),
            Task(
                id=2,
                title="task-2",
                assignee_id=2,
                author_id=1,
            ),
            Task(
                id=3,
                title="task-3",
                assignee_id=1,
                author_id=1,
            ),
        ]


class UserCollection:
    async def get_many_by_ids(self, ids: Iterable) -> List[User]:
        await asyncio.sleep(1)
        return [
            User(
                id=1,
                name="User-1",
            ),
            User(
                id=2,
                name="User-2",
            ),
        ]


class ReminderCollection:
    async def get_many_by_tasks_ids(self, tasks_ids: Iterable) -> List[Reminder]:
        await asyncio.sleep(1)
        return [
            Reminder(
                id=1,
                name="reminder-1 for task-1",
                task_id=1,
            ),
            Reminder(
                id=2,
                name="reminder-2 for task-1",
                task_id=1,
            ),
            Reminder(
                id=3,
                name="reminder-1 for task-2",
                task_id=2,
            ),
        ]


async def _extend_with_users_data(tasks_by_id: Dict, user_task_map: DefaultDict[int, Set]) -> None:
    ic("_extend_with_users_data START")
    users_ids = set(user_task_map.keys())
    users = await UserCollection().get_many_by_ids(users_ids)
    users_by_id = {user.id: user for user in users}
    for user_id, tasks_info in user_task_map.items():
        user = users_by_id[user_id]
        for task_id, source_field in tasks_info:
            setattr(tasks_by_id[task_id], source_field, user)
    ic("_extend_with_users_data END")


async def _extend_with_reminders_data(tasks_by_id: Dict, tasks_ids: Set) -> None:
    ic("_extend_with_reminders_data START")
    reminders = await ReminderCollection().get_many_by_tasks_ids(tasks_ids)
    for reminder in reminders:
        task = tasks_by_id[reminder.task_id]
        if getattr(task, "reminders", None) is None:
            task.reminders = []
        task.reminders.append(reminder)
    ic("_extend_with_reminders_data END")


@app.get("/tasks")
async def get_tasks():
    tasks = await TaskCollection().get_many()
    tasks_by_id = {}
    tasks_ids = set()
    user_task_map = defaultdict(set)
    for task in tasks:
        tasks_by_id[task.id] = task
        tasks_ids.add(task.id)
        user_task_map[task.assignee_id].add(
            (task.id, "assignee")
        )
        user_task_map[task.author_id].add(
            (task.id, "author")
        )

    await asyncio.gather(
        _extend_with_users_data(tasks_by_id, user_task_map),
        _extend_with_reminders_data(tasks_by_id, tasks_ids),
    )
    return list(tasks_by_id.values())
