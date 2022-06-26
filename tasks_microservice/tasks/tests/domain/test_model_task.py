import pytest
from tasks.domain.models import Task, Status
from tasks.domain.exceptions import StatusTransitionForbidden

BASE_TASK_DATA = {
    "id": 1,
    "title": "title",
    "description": "desc",
    "status": Status.DRAFT,
}


def test_creating():
    task = Task(
        **BASE_TASK_DATA
    )
    assert task.status == Status.DRAFT


def test_str_status_can_be_set():
    # GIVEN
    attrs = BASE_TASK_DATA.copy()
    del attrs["status"]

    # WHEN
    task = Task(
        **attrs,
        status=Status.DRAFT.value,
    )

    # THEN
    assert type(task.status) is Status


def test_raise_type_error_if_status_is_improper_type():
    # GIVEN
    attrs = BASE_TASK_DATA.copy()
    del attrs["status"]

    # THEN
    with pytest.raises(
        ValueError,
        match="value is not a valid enumeration member; permitted: 'draft', 'todo', 'in_progress', 'done'",
    ):
        # WHEN
        _ = Task(
            **attrs,
            status="bla",
        )


def test_transit_draft_to_done_status_fails():
    # GIVEN
    task = Task(**BASE_TASK_DATA)

    # # THEN
    with pytest.raises(StatusTransitionForbidden):
        # WHEN
        task.status = Status.DONE
