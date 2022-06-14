from typing import List
from tasks.domain.models import Task, Status

FAKE_TASKS_DATA = {
    1: Task(
        id=1,
        title="Task-1",
        description="Task-1 Description",
        status=Status.IN_PROGRESS,
    ),
    2: Task(
        id=2,
        title="Task-2",
        description="Task-2 Description",
        status=Status.IN_PROGRESS,
    ),
    3: Task(
        id=3,
        title="Task-3",
        description="Task-3 Description",
        status=Status.TODO,
    ),
    4: Task(
        id=4,
        title="Task-4",
        description="Task-4 Description",
        status=Status.DONE,
    ),
}


class HardCodedTasksRepository:
    def get_many(self) -> List[Task]:
        return list(FAKE_TASKS_DATA.values())

    def get_by_id(self, id_: int) -> Task:
        return FAKE_TASKS_DATA[id_]

