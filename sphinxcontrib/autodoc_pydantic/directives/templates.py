"""This module contains reST templates used by autodocumenters and directives.

"""

TPL_COLLAPSE = """
.. raw:: html

   <p><details  class="autodoc_pydantic_collapsable_json">
   <summary>Show JSON schema</summary>

.. code-block:: json

{}

.. raw:: html

   </details></p>

"""
