===
API
===

---------
Structure
---------

The following API documentation does not include all modules of **autodoc_pydantic**.
Instead, it focuses only on modules that are relevant for documentation purposes:

.. parsed-literal::

   autodoc_pydantic
   |
   \|- __init__.py
   \|- :ref:`inspection.py <api_inspection>`
   \|- utility.py
   |
   +--directives
      \|- __init__.py
      \|- :ref:`autodocumenters.py <api_autodocumenters>`
      \|- :ref:`directives.py <api_directives>`
      \|- templates.py
      \|- utility.py
      \|
      \\--options
         \|- __init__.py
         \|- :ref:`composites.py <api_composites>`
         \|- :ref:`definition.py <api_definition>`
         \|- enums.py
         \\- validators.py

For everything else, please refer to the `source code <https://github.com/mansenfranzen/autodoc_pydantic>`_
directly.

-------
Modules
-------

.. _api_inspection:

inspection.py
=============

This module is located at ``sphinxcontrib/autodoc_pydantic/inspection.py``.

.. automodule:: sphinxcontrib.autodoc_pydantic.inspection
   :members:
   :show-inheritance:
   :member-order: bysource

.. _api_autodocumenters:

autodocumenters.py
==================

This module is located at ``sphinxcontrib/autodoc_pydantic/directives/autodocumenters.py``.

.. automodule:: sphinxcontrib.autodoc_pydantic.directives.autodocumenters
   :members:
   :show-inheritance:
   :member-order: bysource

.. _api_definition:

definition.py
=============

This module is located at ``sphinxcontrib/autodoc_pydantic/directives/options/definition.py``.

.. automodule:: sphinxcontrib.autodoc_pydantic.directives.options.definition
   :members:
   :member-order: bysource
   :undoc-members:

.. _api_composites:

composites.py
=============

This module is located at ``sphinxcontrib/autodoc_pydantic/directives/options/composites.py``.

.. automodule:: sphinxcontrib.autodoc_pydantic.directives.options.composites
   :members:
   :member-order: bysource
   :show-inheritance:

.. _api_directives:

directives.py
=============

This module is located at ``sphinxcontrib/autodoc_pydantic/directives/directives.py``.

.. automodule:: sphinxcontrib.autodoc_pydantic.directives.directives
   :members:
   :show-inheritance:
   :member-order: bysource