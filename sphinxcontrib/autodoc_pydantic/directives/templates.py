"""This module contains reST templates used by autodocumenters and directives."""

from __future__ import annotations

TPL_COLLAPSE = """
.. raw:: html

   <p><details  class="{details_class}">
   <summary>{summary}</summary>

{lines}

.. raw:: html

   </details></p>

"""


def to_collapsable(lines: list[str], title: str, css_class: str) -> list[str]:
    """Place given lines into a collapsable HTML block.

    Parameters
    ----------
    lines: list
        The actual content, that should be placed into a collapsable block.
    title: str
        The name of the collapsable block title.
    css_class: str
        Name of the css class for the collapsable block.

    """

    lines_joined = '\n'.join(lines)
    lines_formatted = TPL_COLLAPSE.format(
        lines=lines_joined,
        summary=title,
        details_class=css_class,
    )
    return lines_formatted.split('\n')
