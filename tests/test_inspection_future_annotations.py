from __future__ import annotations

import pytest
from pydantic import BaseModel
from sphinxcontrib.autodoc_pydantic.inspection import ModelInspector
from tests.compatibility import requires_forward_ref


@pytest.fixture(scope="session")
def serializable_self_reference():
    class Foo(BaseModel):
        a: int = 123
        b: Foo = None
        c: "Foo" = None

    if requires_forward_ref():
        Foo.update_forward_refs()

    return ModelInspector(Foo)


def test_is_serializable_self_reference(serializable_self_reference):
    """Ensure that pydantic models containing self references without forward
    references are properly JSON serializable.

    """

    assert serializable_self_reference.fields.non_json_serializable == []