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
