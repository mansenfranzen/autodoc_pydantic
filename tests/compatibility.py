"""This module contains compatibility functions to abstract away implementation
differences between different sphinx versions.

"""
from typing import Tuple, List
from sys import version_info
import re

import pydantic
import sphinx
from sphinx.addnodes import desc_sig_punctuation, desc_annotation, pending_xref


def get_pydantic_version() -> Tuple:
    """Helper function to get major and minor pydantic version.

    """

    version_strings = pydantic.version.VERSION.split(".")[:2]
    version_numbers = [int(x) for x in version_strings]
    return tuple(version_numbers)


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
    return f'{prefix} '


def rst_alias_class_directive() -> str:
    """Provides compatibility abstraction for `class` directive when used with
    sphinx 4.3 or newer.

    """

    return ":py:class:" if sphinx.version_info >= (4, 3) else ":class:"


def object_is_serializable() -> bool:
    """Provides compatibility abstraction to define whether type object is
    serializable or not.

    """

    return get_pydantic_version() >= (1, 9)


def requires_forward_ref() -> bool:
    """Provides compatibility abstraction to define whether forward references
    require `model.update_forward_refs()` in pydantic.

    """

    return get_pydantic_version() < (1, 9)


def convert_ellipsis_to_none(result: List[str]) -> List[str]:
    """Eliminate subtle differences in default values of required pydantic
    fields between various pydantic versions.

    """

    return [x.replace("Ellipsis", "None") for x in result]


def typing_module_prefix() -> str:
    """Provides compatibility abstraction to account for changed behaviour of
    `autodoc_typehints_format` in sphinx 5.0 from fully qualified to short
    which requires types of typing module to prefixed with `~typing.`.

    """

    if (5,) <= sphinx.version_info < (6, 1):
        return "~typing."

    return ""


def typehints_prefix() -> str:
    """Provides compatibility abstraction to account for changed behaviour of
    `autodoc_typehints_format` in sphinx 5.0 from fully qualified to short
    which requires `~`.

    """

    if sphinx.version_info >= (5,):
        return "~"

    return ""


def module_doc_string_tab() -> str:
    """Provides compatibility abstraction to account for changed behaviour of
    python module doc string in sphinx 5.2 that gains an additional whitespace
    tab at the start.

    """

    if sphinx.version_info >= (5, 2):
        return "   "

    return ""


def get_type_expected(field_type: str):
    if sphinx.version_info >= (6, 1):
        optional_match = re.findall(r'Optional\[(\w*)\]', field_type)
        if optional_match is not None and len(optional_match) > 0:
            return optional_match[0] + ' | None'  # int | None
    return field_type  # 'Optional[int]'


TYPING_MODULE_PREFIX = typing_module_prefix()
TYPEHINTS_PREFIX = typehints_prefix()
OPTIONAL_INT = TYPING_MODULE_PREFIX + get_type_expected('Optional[int]')
