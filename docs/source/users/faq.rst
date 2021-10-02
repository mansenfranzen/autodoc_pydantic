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
