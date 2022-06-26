from tasks.domain.models import Status


def test_converting_str_to_status():
    # WHEN
    val = Status("todo")

    # THEN
    assert isinstance(val, Status)
    assert val.value == "todo"
