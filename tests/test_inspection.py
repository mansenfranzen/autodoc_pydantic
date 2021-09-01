"""This module contains tests regarding the `inspection` module.

"""
from typing import TypeVar

import pytest
from pydantic import BaseModel

from sphinxcontrib.autodoc_pydantic.inspection import (
    ModelWrapper, ModelInspector
)


@pytest.fixture(scope="session")
def serializable():
    class Serializable(BaseModel):
        field_one: str

    return ModelInspector(Serializable)


@pytest.fixture(scope="session")
def non_serializable():
    class Custom:
        def __init__(self):
            self.field = "foobar"

    new_type = TypeVar("Dummy")

    class NonSerializable(BaseModel):
        field_1: str
        field_2: object
        field_3: str = object()
        field_4: Custom = Custom()
        field_5: new_type
        field_6: int = 10

        class Config:
            arbitrary_types_allowed = True

    return ModelInspector(NonSerializable)


@pytest.mark.parametrize("field_test", [("field_1", True),
                                        ("field_2", False),
                                        ("field_3", False),
                                        ("field_4", False),
                                        ("field_5", True),
                                        ("field_6", True)])
def test_is_serializable(non_serializable, field_test):
    field_name, test_result = field_test
    result = non_serializable.fields.is_json_serializable(field_name)
    assert result is test_result


def test_find_non_json_serializable_fields(serializable,
                                           non_serializable):
    assert serializable.find_non_json_serializable_fields() == []
    assert non_serializable.find_non_json_serializable_fields() == ["field_2",
                                                                    "field_3",
                                                                    "field_4"]


def test_get_safe_schema_json_serializable(serializable):
    json_result, invalid = serializable.get_safe_schema_json()

    assert invalid == []
    assert "field_one" in json_result["properties"]


def test_get_safe_schema_json_non_serializable(non_serializable):
    json_result, invalid = non_serializable.get_safe_schema_json()

    invalid_expected = ["field_2", "field_3", "field_4"]
    assert invalid == invalid_expected
    for invalid_field in invalid_expected:
        assert "type" not in json_result["properties"][invalid_field]
