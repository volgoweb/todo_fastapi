import pytest
from pydantic import BaseModel, ValidationError, Field


def test_setter_validation():
    class Model(BaseModel):
        status: int

        class Config:
            validate_assigment = True

    m = Model(status=1)
    with pytest.raises(ValidationError):
        m.status = "text"


def test_immutable_fields():
    class My(BaseModel):
        title: str
        status: int = Field(allow_mutation=False)

        class Config:
            validate_assignment = True

    m = My(status=1, title="bla")
    m.title = "bla2"
    with pytest.raises(TypeError):
        m.status = 4


def test_setter():
    class My(BaseModel):
        status: int

        class Config:
            validate_assignment = True

        def __setattr__(self, key, value):
            field_setter = getattr(self, f"__set_status")
            if field_setter:
                return field_setter(value)
            return super().__setattr__(key, value)

        def __set_status(self, status):
            if status == 5:
                raise ValueError("Forbidden status transition")
            self.status = status

    m = My(status=1)
    m.status = 4
    with pytest.raises(ValueError, match="Forbidden status transition"):
        m.status = 5
