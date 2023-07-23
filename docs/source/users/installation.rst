============
Installation
============

**autodoc_pydantic** is a sphinx extension and works well with
:code:`pydantic >= 1.5.0` and :code:`sphinx >= 3.5.0`.

.. note::

   In June 2023, pydantic v2 was released. This introduced backwards
   incompatible API and behavioral semantic changes in comparison to pydantic
   v1. Hence, **autodoc_pydantic** required substantial changes, too. In order
   to keep the codebase clean and concise, a separate branch for v2 was created
   while the original code remains in the v1 branch.

   In a nutshell, support for pydantic v2 is provided via
   ``autodoc_pydantic >= 2.0.0`` whereas pydantic v1 will required
   ``autodoc_pydantic < 2.0.0``. By default, your dependency resolver should
   automatically select the correct version depending on the given pydantic
   version.


1. Install with pip
===================

**autodoc_pydantic** needs to be installed just like any other python package
into your documentation building environment:

.. code-block:: bash

   pip install autodoc_pydantic

.. warning::
   If you wish to use the
   :ref:`model-erdantic-figure <autodoc_pydantic_model_erdantic_figure>`
   feature to visualize ERD, you will need to install
   `graphviz <https://graphviz.org/download/>`_ first, then install
   **autodoc_pydantic** with the erdantic option:

   .. code-block:: bash

      pip install autodoc_pydantic[erdantic]

2. Enable extension
===================

Once installed, you'll need to enable it within sphinx' :code:`conf.py`:

.. code-block:: python

   extensions = ['sphinxcontrib.autodoc_pydantic']

3. Configuration
================

**autodoc_pydantic** can be completely customized to meet your individual requirements.
As an example, to display the collapsible JSON schema for pydantic models but to hide them for
pydantic settings, add the following to sphinx' :code:`conf.py`:

.. code-block:: python

   autodoc_pydantic_model_show_json = True
   autodoc_pydantic_settings_show_json = False

All available options are covered in detail with examples in the :doc:`configuration` documentation.

The default configuration already takes effect as soon as you enable **autodoc_pydantic**.
More concretely, sphinx' autodoc directives like :code:`automodule` will already use the
newly added pydantic documenters. To explicitly use the **autodoc_pydantic** directives,
please visit the :doc:`usage` documentation.