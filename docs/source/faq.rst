==========================
Frequently asked questions
==========================

Show inherited fields/validators
================================

Pydantic models can be subclassed to inherit fields and validators from base
classes. Naturally, **autodoc_pydantic** should also show these members.
Though, sphinx autodoc does not include any member from base classes by default.
However, sphinx autodoc offers a directive option named ``:inherited-members:``
which allows to include all members from all base classes except from `object`
(see docs `here <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#directives>`_).

Unfortunately, this will also include all members from ``pydantic.BaseModel``
(e.g. ``copy()``, ``schema()`` etc...) which is most likely not what one wants.
Luckily, ``:inherited-members:`` takes a parameter which allows to exclude base classes.
Hence, when supplying ``BaseModel`` as an argument for ``:inherited-members:``,
irrelevant members are ignored:

.. tabs::

   .. tab:: inherited_members.py

      .. autocodeblock:: target.faq.inherited_members

   .. tab:: inherited_members.rst

      .. code-block::

         .. automodule:: target.faq.inherited_members
            :inherited-members: BaseModel

   .. tab:: *rendered output*

      .. automodule:: target.faq.inherited_members
         :inherited-members: BaseModel
