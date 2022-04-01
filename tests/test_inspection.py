"""This module contains tests regarding the `inspection` module.

"""
from typing import TypeVar, Union

try:
    from typing import ForwardRef
except ImportError:
    from typing import _ForwardRef as ForwardRef

import pydantic
import pytest
from pydantic import BaseModel

from sphinxcontrib.autodoc_pydantic.inspection import ModelInspector, \
    StaticInspector
from tests.compatibility import object_is_serializable, requires_forward_ref


@pytest.fixture(scope="session")
def serializable():
    class Serializable(BaseModel):
        field_one: str

    return ModelInspector(Serializable)


@pytest.fixture(scope="session")
def serializable_mix():
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


@pytest.fixture(scope="session")
def serializable_forward_ref():
    Foo = ForwardRef('Foo')

    class Foo(BaseModel):
        a: int = 123
        b: Foo = None
        c: "Foo" = None

    if requires_forward_ref():
        Foo.update_forward_refs()

    return ModelInspector(Foo)


@pytest.fixture(scope="session")
def serializable_self_reference():
    class Foo(BaseModel):
        a: int = 123
        b: Foo = None
        c: "Foo" = None

    if requires_forward_ref():
        Foo.update_forward_refs()

    return ModelInspector(Foo)


@pytest.fixture(scope="session")
def serializable_forward_ref_union():
    Foo = ForwardRef('Foo')

    class Foo(BaseModel):
        a: int = 123
        b: Union[Foo, int] = 2
        c: Union["Foo", str] = "foobar"

    if requires_forward_ref():
        Foo.update_forward_refs()

    return ModelInspector(Foo)


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
def test_is_serializable(serializable_mix, field_test):
    """Test different scenarios of serializable and non-serializable fields.

    """

    field_name, test_result = field_test
    result = serializable_mix.fields.is_json_serializable(field_name)
    assert result is test_result


def test_is_serializable_forward_ref(serializable_forward_ref):
    """Ensure that pydantic models containing forward refs are properly
    JSON serializable.

    """

    assert serializable_forward_ref.fields.non_json_serializable == []


def test_is_serializable_self_reference(serializable_self_reference):
    """Ensure that pydantic models containing self references without forward
    references are properly JSON serializable.

    """

    assert serializable_self_reference.fields.non_json_serializable == []


def test_is_serializable_forward_ref_union(serializable_forward_ref_union):
    """Ensure that pydantic models containing forward refs with unions are
    properly JSON serializable.

    This relates to #98.

    """
    assert serializable_forward_ref_union.fields.non_json_serializable == []


def test_find_non_json_serializable_fields(serializable, serializable_mix):
    assert serializable.fields.non_json_serializable == []

    non_serial_fields = ["field_2", "field_3", "field_4"]
    if pydantic.version.VERSION[:3] >= "1.9":
        non_serial_fields.remove("field_2")

    assert serializable_mix.fields.non_json_serializable == non_serial_fields


def test_get_safe_schema_json_serializable(serializable):
    json_result = serializable.schema.sanitized

    assert "field_one" in json_result["properties"]


def test_get_safe_schema_json_non_serializable(serializable_mix):
    json_result = serializable_mix.schema.sanitized
    invalid_fields = serializable_mix.fields.non_json_serializable

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
