import pytest
from sphinx.ext.autosummary import FakeDirective

from sphinxcontrib.autodoc_pydantic import (
    PydanticModelDocumenter,
    PydanticSettingsDocumenter,
    PydanticFieldDocumenter,
    PydanticValidatorDocumenter,
    PydanticConfigClassDocumenter
)


@pytest.mark.parametrize("klass", [PydanticModelDocumenter,
                                   PydanticSettingsDocumenter,
                                   PydanticFieldDocumenter,
                                   PydanticValidatorDocumenter,
                                   PydanticConfigClassDocumenter])
def test_autosummary_fake_directive(klass):
    """Ensure that using autosummary's `FakeDirective` works with
    pydantic autodocumenters.

    This relates to issue #11.
    """

    klass(FakeDirective(), "")


def test_autosummary_imported_objects(parse_rst):
    """Make sure that autosummary also collects pydantic objects that are
    imported from other modules and which are documented by pydantic auto-
    documenters.

    This relates to issue #11.
    """

    input_rst = [
        '.. autosummary::',
        '',
        '   target.AutoSummaryModel',
        ''
    ]

    nodes = parse_rst(input_rst)
    ref = nodes[1][0][0][2][0][0][0][0][0]

    assert ref == ':obj:`target.AutoSummaryModel <target.AutoSummaryModel>`'
