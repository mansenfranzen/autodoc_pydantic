===
FAQ
===

Show inherited fields/validators
================================

Pydantic models can be subclassed to inherit fields and validators from base
classes. Naturally, **autodoc_pydantic** should also show these members.
By default, sphinx autodoc does not include any member from base classes, though.
However, sphinx autodoc provides a directive option named ``:inherited-members:``
which allows to include all members from all base classes except `object`
(see docs `here <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#directives>`_).

Unfortunately, this will also include all members from ``pydantic.BaseModel``
(e.g. ``copy()``, ``schema()`` etc...) which is most likely not what one wants.
Luckily, ``:inherited-members:`` takes a parameter which allows to exclude base classes.
Hence, when supplying ``BaseModel`` as an argument for ``:inherited-members:``,
irrelevant members are ignored:

.. tabs::

   .. tab:: python

      .. autocodeblock:: target.faq.inherited_members

   .. tab:: reST

      .. code-block::

         .. automodule:: target.faq.inherited_members
            :inherited-members: BaseModel

   .. tab:: *rendered output*

      .. automodule:: target.faq.inherited_members
         :inherited-members: BaseModel

.. note::

   For more, please see the corresponding
   `github issue #32 <https://github.com/mansenfranzen/autodoc_pydantic/issues/32>`_.


Exclude ``__init__`` docstring
==============================

If a pydantic model's documentation rendered by **autodoc_pydantic** 
includes the docstring from the pydantic base class or from the model's 
``__init__`` method, it may be due to autodoc's ``autoclass_content`` 
setting in sphinx's ``conf.py``. 

The configuration below tells Sphinx to include both the class docstring
*and* that of ``__init__`` for auto-documented classes::

   autoclass_content = "both"

This behavior does also apply to **autodoc_pydantic**'s
auto-documenters. If you haven't overwritten the ``__init__`` 
method in your model, this will look exactly like it has 
inherited the Pydantic base class docstring. In order to only 
show the class docstring, change this setting back to "class"::

   autoclass_content = "class"

.. note::

   For more, please see the corresponding
   `github issue #58 <https://github.com/mansenfranzen/autodoc_pydantic/issues/58>`_.


Document models as an attribute
===============================

Pydantic models/settings can be also used and documented as class attributes,
as in the following example:

.. code-block:: python

   from pydantic import BaseModel, validator


   class Model(BaseModel):
       """Model Doc String."""

       field: int
       """Field Doc String"""

       field2: str
       """Field2 Doc String"""

       @validator("field")
       def validate(cls, v):
           """Dummy validator"""
           return v


   class Container:
       """Container Doc String"""

       TEST_MODEL = Model

If you auto-document this code via ``automodule`` for example, then the pydantic model
``Model`` gets both documented as a standalone class and as an class attribute
of ``Container``. In the ladder case, plain sphinx autodoc adds an alias note
with reference to the main documentation section of ``Model`` by default. It
does not provide more documentation related to ``Model`` to prevent duplication
with the main class documentation.

However until version ``1.5.1``, **autodoc_pydantic** added content like json
schema, field and validator summaries when models/settings were documented
as class attributes. This was removed in version ``1.6.0`` to be in line with
the default sphinx autodoc behaviour.

.. note::

   For more, please see the corresponding
   `github issue #78 <https://github.com/mansenfranzen/autodoc_pydantic/issues/78>`_.
