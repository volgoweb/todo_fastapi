import pytest
from tasks.domain.models import Task, Status


def test_creating():
    _ = Task(
        status=Status.DRAFT,
    )


def test_str_status_can_be_set():
    task = Task(status=Status.DRAFT.value)
    assert type(task.status) is Status


def test_raise_type_error_if_status_is_inproper_type():
    with pytest.raises(ValueError, match="'bla' is not a valid Status"):
        _ = Task(status="bla")
