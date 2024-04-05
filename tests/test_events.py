from pathlib import Path
from typing import List

import pytest
from sphinx.addnodes import document

from sphinxcontrib.autodoc_pydantic.events import OBJTYPES_CSS_FALLBACKS

PARAMS_FALLBACK_CSS_CLASS = dict(
    argnames=['objtype', 'fallback_css_class'],
    argvalues=OBJTYPES_CSS_FALLBACKS.items(),
    ids=OBJTYPES_CSS_FALLBACKS.keys(),
)

APP_OVERWRITE_FALLBACK_CSS_CLASS = dict(
    autodoc_pydantic_settings_show_config_member=True,
    autodoc_pydantic_model_show_config_member=True,
)


@pytest.fixture(scope='function')
def path_fallback_css_class():
    current = Path(__file__).parent
    return current.joinpath('roots', 'test-events-add-css-fallback')


@pytest.fixture(scope='function')
def doctree_css_fallback_false(prod_app, path_fallback_css_class) -> document:
    result = prod_app(
        source_dir=path_fallback_css_class,
        docnames=['add_css_fallback'],
        confoverrides={
            'autodoc_pydantic_add_fallback_css_class': False,
            **APP_OVERWRITE_FALLBACK_CSS_CLASS,
        },
    )

    return result.doctree['add_css_fallback']


@pytest.fixture(scope='function')
def doctree_css_fallback_true(prod_app, path_fallback_css_class) -> document:
    result = prod_app(
        source_dir=path_fallback_css_class,
        docnames=['add_css_fallback'],
        confoverrides={
            'autodoc_pydantic_add_fallback_css_class': True,
            **APP_OVERWRITE_FALLBACK_CSS_CLASS,
        },
    )

    return result.doctree['add_css_fallback']


def filter_doctree_by_objtype(node: document, objtype: str) -> List[document]:
    """Returns all elements of a doctree which equal to given `objtype`."""

    result = []

    try:
        if objtype == node.attributes['objtype']:
            result.append(node)
    except (AttributeError, KeyError):
        pass

    for children in node.children:
        result.extend(filter_doctree_by_objtype(children, objtype))

    return result


@pytest.mark.parametrize(**PARAMS_FALLBACK_CSS_CLASS)
def test_add_fallback_css_class_false(
    doctree_css_fallback_false, objtype, fallback_css_class
):
    """Ensure that fallback css class is not added to autodoc_pydantic
    generated nodes per objtype.

    This relates to #77.

    """
    nodes = filter_doctree_by_objtype(doctree_css_fallback_false, objtype)

    assert len(nodes) > 0

    for node in nodes:
        css_classes = node.attributes['classes']
        assert css_classes[-1] == objtype
        assert css_classes[-2] != fallback_css_class


@pytest.mark.parametrize(**PARAMS_FALLBACK_CSS_CLASS)
def test_add_fallback_css_class_true(
    doctree_css_fallback_true, objtype, fallback_css_class
):
    """Ensure that fallback css class is added to autodoc_pydantic generated
    nodes per objtype.

    This relates to #77.

    """
    nodes = filter_doctree_by_objtype(doctree_css_fallback_true, objtype)
    # ensure that there is at lease one node with relevant objtype
    assert len(nodes) > 0

    for node in nodes:
        css_classes = node.attributes['classes']
        assert css_classes[-1] == objtype
        assert css_classes[-2] == fallback_css_class
