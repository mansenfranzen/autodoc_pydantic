from sphinx.addnodes import desc_content
from sphinx.application import Sphinx

OBJTYPES_CSS_FALLBACKS = {
    'pydantic_model': 'class',
    'pydantic_settings': 'class',
    'pydantic_validator': 'method',
    'pydantic_field': 'attribute',
}


def add_fallback_css_class(
    app: Sphinx,
    domain: str,  # noqa: ARG001
    objtype: str,
    contentnode: desc_content,
) -> None:
    """Used as `object-description-transform` sphinx event to add default css
    classes to autodoc_pydantic's custom auto-documenter.

    """

    if objtype not in OBJTYPES_CSS_FALLBACKS:
        return

    classes = contentnode.parent.attributes['classes']

    if not app.env.config['autodoc_pydantic_add_fallback_css_class']:
        return

    idx = classes.index(objtype)
    fallback = OBJTYPES_CSS_FALLBACKS[objtype]
    classes.insert(idx, fallback)
