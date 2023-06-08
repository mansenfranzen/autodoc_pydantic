"""This module contains reST templates used by autodocumenters and directives.

"""

TPL_COLLAPSE = """
.. raw:: html

   <p><details  class="{details_class}">
   <summary>{summary}</summary>

{lines}

.. raw:: html

   </details></p>

"""


def to_collapsable(lines: list[str], title, css_class) -> list[str]:
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

    lines = "\n".join(lines)
    lines = TPL_COLLAPSE.format(
        lines=lines,
        summary=title,
        details_class=css_class
    )
    return lines.split("\n")
