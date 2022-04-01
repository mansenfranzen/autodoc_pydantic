"""This module is relates to `test_inspection` with future annotations enabled.

"""

import sys
import pytest

if sys.version_info < (3, 7):
    pytest.skip("future annotations not available", allow_module_level=True)

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

    if requires_forward_ref():
        Foo.update_forward_refs()

    return ModelInspector(Foo)


def test_is_serializable_self_reference(serializable_self_reference):
    """Ensure that pydantic models containing self references without forward
    references are properly JSON serializable.

    """

    assert serializable_self_reference.fields.non_json_serializable == []