"""This module contains compatibility functions to abstract away implementation
differences between different sphinx versions.

"""

from typing import Tuple

import sphinx
from sphinx.addnodes import desc_sig_punctuation, desc_annotation, pending_xref


def desc_annotation_default_value(value: str):
    """Provides compatibility abstraction for `desc_annotation` for default
    values for sphinx version smaller and greater equal sphinx 4.3.

    """

    if sphinx.version_info < (4, 3):
        return [desc_annotation, f" = {value}"]
    from sphinx.addnodes import desc_sig_space
    return (desc_sig_space,
            [desc_sig_punctuation, "="],
            desc_sig_space,
            value)


def desc_annotation_type_annotation(type_str: str) -> Tuple:
    """Provides compatibility abstraction for `desc_annotation` for type
    annotation for sphinx version smaller and greater equal sphinx 4.3.

    """

    if sphinx.version_info < (4, 3):
        return (": ", [pending_xref, type_str])
    from sphinx.addnodes import desc_sig_space
    return ([desc_sig_punctuation, ":"],
            desc_sig_space,
            [pending_xref, type_str])


def desc_annotation_directive_prefix(prefix: str):
    """Provides compatibility abstraction for `desc_annotation` for directive
    prefix for sphinx version smaller and greater equal sphinx 4.3.

    """

    if sphinx.version_info >= (4, 3):
        from sphinx.addnodes import desc_sig_space
        return (prefix, desc_sig_space)
    return prefix + " "


def rst_alias_class_directive():
    """Provides compatibility abstraction for `class` directive when used with
    sphinx 4.3 or newer.

    """

    if sphinx.version_info >= (4, 3):
        return ":py:class:"
    return ":class:"
