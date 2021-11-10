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

    if sphinx.version_info >= (4, 3):
        from sphinx.addnodes import desc_sig_space
        return (desc_sig_space,
                [desc_sig_punctuation, "="],
                desc_sig_space,
                value)
    else:
        return [desc_annotation, f" = {value}"]


def desc_annotation_type_annotation(type_str: str) -> Tuple:
    """Provides compatibility abstraction for `desc_annotation` for type
    annotation for sphinx version smaller and greater equal sphinx 4.3.

    """

    if sphinx.version_info >= (4, 3):
        from sphinx.addnodes import desc_sig_space
        return ([desc_sig_punctuation, ":"],
                desc_sig_space,
                [pending_xref, type_str])
    else:
        return (": ", [pending_xref, type_str])
