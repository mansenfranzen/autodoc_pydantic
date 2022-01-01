"""This module contains tests regarding the `inspection` module.

"""
from typing import TypeVar

import pydantic
import pytest
from pydantic import BaseModel

from sphinxcontrib.autodoc_pydantic.inspection import ModelInspector, \
    StaticInspector
from tests.compatability import object_is_serializable


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


@pytest.mark.parametrize(
    "field_test",
    [
        ("field_1", True),
        ("field_2", object_is_serializable()),
        ("field_3", False),
        ("field_4", False),
        ("field_5", True),
        ("field_6", True),
    ],
)
def test_is_serializable(non_serializable, field_test):
    field_name, test_result = field_test
    result = non_serializable.fields.is_json_serializable(field_name)
    assert result is test_result


def test_find_non_json_serializable_fields(serializable, non_serializable):
    assert serializable.fields.non_json_serializable == []

    non_serial_fields = ["field_2", "field_3", "field_4"]
    if pydantic.version.VERSION[:3] >= "1.9":
        non_serial_fields.remove("field_2")

    assert non_serializable.fields.non_json_serializable == non_serial_fields


def test_get_safe_schema_json_serializable(serializable):
    json_result = serializable.schema.sanitized

    assert "field_one" in json_result["properties"]


def test_get_safe_schema_json_non_serializable(non_serializable):
    json_result = non_serializable.schema.sanitized
    invalid_fields = non_serializable.fields.non_json_serializable

    for invalid_field in invalid_fields:
        assert "type" not in json_result["properties"][invalid_field]


def test_is_pydantic_model_true():
    """Test is_pydantic_model with a simple subclass of BaseModel"""

    class IsAModel(BaseModel):
        ...

    assert StaticInspector.is_pydantic_model(IsAModel)


def test_is_pydantic_model_false():
    """Test is_pydantic_model with items that are not
    a subclass of BaseModel"""

    class IsNotAModel:
        ...

    assert not StaticInspector.is_pydantic_model(IsNotAModel)
    assert not StaticInspector.is_pydantic_model("NotEvenAClass")


def test_is_pydantic_model_edge_case():
    """Tests bugfix for issue #57, which seems to be related
    to https://bugs.python.org/issue45326"""

    try:
        EdgeCase = dict[str, str]
    except TypeError:
        # older version of python, use typing module instead
        from typing import Dict

        EdgeCase = Dict[str, str]

    assert not StaticInspector.is_pydantic_model(EdgeCase)
