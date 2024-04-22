import pytest
import sphinx
from sphinx.ext.autosummary import FakeDirective

from sphinxcontrib.autodoc_pydantic.directives.autodocumenters import (
    PydanticFieldDocumenter,
    PydanticModelDocumenter,
    PydanticSettingsDocumenter,
    PydanticValidatorDocumenter,
)


@pytest.mark.parametrize(
    'klass',
    [
        PydanticModelDocumenter,
        PydanticSettingsDocumenter,
        PydanticFieldDocumenter,
        PydanticValidatorDocumenter,
    ],
)
def test_autosummary_fake_directive(klass):
    """Ensure that using autosummary's `FakeDirective` works with
    pydantic autodocumenters.

    This relates to issue #11.
    """

    klass(FakeDirective(), '')


def test_autosummary_imported_objects(parse_rst):
    """Make sure that autosummary also collects pydantic objects that are
    imported from other modules and which are documented by pydantic auto-
    documenters.

    This relates to issue #11.
    """

    input_rst = ['.. autosummary::', '', '   target.AutoSummaryModel', '']

    nodes = parse_rst(input_rst)
    node = nodes[1][0][0][2][0][0][0][0]

    if sphinx.version_info >= (4, 3):
        assert node['reftarget'] == 'target.AutoSummaryModel'
        assert node.astext() == 'target.AutoSummaryModel'
    else:
        assert node[0] == ':obj:`target.AutoSummaryModel <target.AutoSummaryModel>`'
