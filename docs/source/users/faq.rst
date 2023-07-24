.. _sphinx.ext.autodoc: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
.. _autoapi: https://sphinx-autoapi.readthedocs.io/en/latest/index.html
.. _config-class: https://autodoc-pydantic.readthedocs.io/en/main-1.x/users/configuration.html#config-class
.. _show-config-member: https://autodoc-pydantic.readthedocs.io/en/main-1.x/users/configuration.html#show-config-member

===
FAQ
===

.. _faq_migration_guide:

Migration guide from v1 to v2
=============================

In June 2023, pydantic v2 was released while introducing backwards incompatible
API and behavioral changes in comparison to pydantic v1. Supporting pydantic v2
required substantial adjustments to the codebase leading to a new major release
of **autodoc_pydantic** (v1.9.0 -> v2.0.0), too.

Do I need to migrate existing sphinx code?
------------------------------------------

Maybe 😋. **autodoc_pydantic**'s API remained stable, execpt for removing a
redundant and rather exotic feature.

Specifically, the following global ``conf.py`` configurations and their
corresponding local directive options are no longer available:

- ``autodoc_pydantic_model_show_config_member``
- ``autodoc_pydantic_settings_show_config_member``
- ``autodoc_pydantic_config_members``
- ``autodoc_pydantic_config_signature_prefix``

These enabled documenting pydantic model configurations in isolation or as a
separate member of the pydantic model (see `config-class`_ and
`show-config-member`_). However, they are redundant and less concise in
contrast to ``autodoc_pydantic_model_show_config_summary`` and
``autodoc_pydantic_settings_show_config_summary``. Please use these instead
in order to document your model configurations.

Does autodoc_pydantic modify pydantic's v2 semantics?
-----------------------------------------------------

No, **autodoc_pydantic** does not modify the underlying behavior of pydantic in
any way. Instead, it only documents whatever pydantic exposes. Hence, all
behavioral changes such as the new default strict mode are preserved in v2.

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

.. tabs::

   .. tab:: python

      .. autocodeblock:: target.faq.model_as_attr

   .. tab:: reST

      .. code-block::

         .. automodule:: target.faq.model_as_attr
            :members:

   .. tab:: *rendered output*

      .. automodule:: target.faq.model_as_attr
         :members:

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


.. _faq_add_fallback_css_class:

Broken layout for ``autodoc_pydantic``
======================================

Depending on the theme you're using (e.g. Jupyter-Book), you may experience a
broken CSS/HTML layout for content generated by **autodoc_pydantic**.

This occurs because the auto-documenter's ``objtype`` is used as the standard
CSS class in their corresponding HTML output. For example, standard python
classes have objtype ``class`` when being documented with sphinx autodoc.
Hence, the resulting css class is ``class`` in the corresponding HTML output.

However, sphinx extensions with custom object types (e.g. ``pydantic_model``)
will replace the css class ``class`` with ``pydantic_model``. If a theme relies
on standard css classes like ``class``, it will break.

Since version ``1.6.0`` this is fixed by default via
:ref:`autodoc_pydantic_add_fallback_css_class<autodoc_pydantic_add_fallback_css_class>`
which automatically adds the default css classes that **autodoc_pydantic**
replaces.

.. note::

   For more, please see the corresponding
   `github issue #77 <https://github.com/mansenfranzen/autodoc_pydantic/issues/77>`_.

Interoperability with ``autoapi``
=================================

The `autoapi`_ package is an alternative to `sphinx.ext.autodoc`_. It solely
relies on static code analysis while ``sphinx.ext.autodoc`` actually imports the
python code to be documented. Moreover, ``autoapi`` leverages custom jinja
templates to generate rst files.

Essentially, ``autoapi`` does not rely on ``sphinx.ext.autodoc`` whereas
**autodoc_pydantic** is based on it. Hence, **autodoc_pydantic** is not
compatible with ``autoapi``. In consequence, documentation generated by
``autoapi`` ignores **autodoc_pydantic**.

.. note::

   For more, please see the corresponding
   `github issue #138 <https://github.com/mansenfranzen/autodoc_pydantic/issues/138>`_.
