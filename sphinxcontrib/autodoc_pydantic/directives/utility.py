"""This module contains various utility functions which are relevant for
autodocumenters and directives.

"""

from __future__ import annotations

import re
from typing import TYPE_CHECKING

from docutils.nodes import emphasis
from sphinx.addnodes import pending_xref

if TYPE_CHECKING:
    from sphinx.environment import BuildEnvironment

REGEX_TYPE_ANNOT = re.compile(
    r'\s+:type:\s([a-zA-Z1-9\._\[]+\]?)\[([a-zA-Z1-9\._\[\]]+)\]'
)


class NullType:
    """Helper class to present a Null value which is not the same
    as python's `None`. This represents a missing value, or no
    value at all by convention. It should be used as a singleton.

    """

    def __bool__(self) -> bool:
        return False


NONE = NullType()


def create_field_href(name: str, ref: str, env: BuildEnvironment) -> pending_xref:
    """Create `pending_xref` node with link to given `reference`."""

    options = {
        'refdoc': env.docname,
        'refdomain': 'py',
        'reftype': 'obj',
        'reftarget': ref,
    }

    refnode = pending_xref(name, **options)
    classes = ['xref', 'py', 'py-obj']
    refnode += emphasis(name, name, classes=classes)
    return refnode


def remove_node_by_tagname(nodes: list, tagname: str) -> None:
    """Removes node from list of `nodes` with given `tagname` in place."""

    for remove in [node for node in nodes if node.tagname == tagname]:
        nodes.remove(remove)


def intercept_type_annotations_py_gt_39(line: str) -> str:
    """Helper function to modify string representation of annotated types for
    python < 3.9. Without modification, an annotated int will result in
    `int[int]` instead of `int`.

    """

    contains_type = ':type:' in line
    contains_bracket = '[' in line

    if contains_type and contains_bracket:
        match = REGEX_TYPE_ANNOT.match(line)
        if match:
            t1, t2 = match.groups()
            if t1 == t2:
                return line.replace(f'{t1}[{t1}]', t1)

    return line
