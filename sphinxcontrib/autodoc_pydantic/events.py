from sphinx.addnodes import desc_content
from sphinx.application import Sphinx

OBJTYPES_CSS_FALLBACKS = {"pydantic_model": "class",
                          "pydantic_settings": "class",
                          "pydantic_validator": "method",
                          "pydantic_field": "attribute",
                          "pydantic_config": "class"}


def add_fallback_css_class(app: Sphinx,
                           domain: str,
                           objtype: str,
                           contentnode: desc_content):
    """Used as `object-description-transform` sphinx event to add default css
    classes to autodoc_pydantic's custom auto-documenter.

    """

    if not app.env.config["autodoc_pydantic_add_fallback_css_class"]:
        return

    if objtype in OBJTYPES_CSS_FALLBACKS:
        classes = contentnode.parent.attributes["classes"]
        idx = classes.index(objtype)
        fallback = OBJTYPES_CSS_FALLBACKS[objtype]
        classes.insert(idx, fallback)
