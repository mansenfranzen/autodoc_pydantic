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
