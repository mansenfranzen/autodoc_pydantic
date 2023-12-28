============================================
Welcome to autodoc_pydantic's documentation!
============================================

**Seamlessly integrate pydantic models in your Sphinx documentation.**

|PyPIBadge|_ |PythonBadge|_ |CIBadge|_ |CoverageBadge|_ |ContributersBadge|_ |DownloadsBadge|_

You love `pydantic <https://pydantic-docs.helpmanual.io/>`_ 💖 and you want to
document your models and configuration settings with `sphinx`_?
Perfect, let's go. But wait, sphinx' `autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_
does not integrate too well with pydantic models 😕.
Don't worry - just :code:`pip install autodoc_pydantic` 😉.

Features
--------

- 💬 provides default values, alias and constraints for model fields
- 🔗 adds hyperlinks between validators and corresponding fields
- 📃 includes collapsable model json schema
- 🏄 natively integrates with autodoc and autosummary extensions
- 📎 defines explicit pydantic prefixes for models, settings, fields, validators and model config
- 📋 shows summary section for model configuration, fields and validators
- 👀 hides overloaded and redundant model class signature
- 🔱 visualizes entity-relationship-diagrams for class hierarchies
- 🍀 Supports `pydantic >= 1.5.0` and `sphinx >= 4.0.0`

To see those features in action, jump over to the :ref:`example <showcase>` section comparing
the appearance of standard sphinx autodoc with **autodoc_pydantic**.

.. note::

   This documentation is based on ``autodoc_pydantic >= 2.0.1``. If you are
   using pydantic v1 along with ``autodoc_pydantic < 2.0.0``, please find the
   latest v1 documentation `here <https://autodoc-pydantic.readthedocs.io/en/main-1.x/>`_ .

.. toctree::
   :maxdepth: 1
   :caption: Users

   users/installation
   users/usage
   users/configuration
   users/examples
   users/faq

.. toctree::
   :maxdepth: 1
   :caption: Developers

   developers/setup
   developers/design
   developers/guides


.. toctree::
   :maxdepth: 1
   :caption: Reference

   reference/api
   reference/changelog


Acknowledgements
----------------

Thanks to great open source projects

- `sphinx`_
- `pydantic <https://pydantic-docs.helpmanual.io/>`_
- `poetry <https://python-poetry.org/>`_
- `mermaid.js <https://mermaid-js.github.io/mermaid/#/>`_
- and many more involved

and all `contributors <https://github.com/mansenfranzen/autodoc_pydantic/tree/refactor_inspection#acknowledgements>`_ to **autodoc_pydantic** ❤!


.. _sphinx: https://www.sphinx-doc.org/en/master

.. |PyPIBadge| image:: https://img.shields.io/pypi/v/autodoc_pydantic?style=flat
.. _PyPIBadge: https://pypi.org/project/autodoc-pydantic/

.. |CIBadge| image:: https://img.shields.io/github/actions/workflow/status/mansenfranzen/autodoc_pydantic/tests.yml?branch=main&style=flat
.. _CIBadge: https://github.com/mansenfranzen/autodoc_pydantic/actions/workflows/tests.yml

.. |DownloadsBadge| image:: https://img.shields.io/pypi/dm/autodoc_pydantic?color=fe7d37&style=flat
.. _DownloadsBadge: https://pypistats.org/packages/autodoc-pydantic

.. |ContributersBadge| image:: https://img.shields.io/badge/all_contributors-41-orange.svg?style=flat
.. _ContributersBadge: https://github.com/mansenfranzen/autodoc_pydantic/tree/refactor_inspection#acknowledgements

.. |CoverageBadge| image:: https://img.shields.io/codecov/c/gh/mansenfranzen/autodoc_pydantic?style=flat
.. _CoverageBadge: https://app.codecov.io/gh/mansenfranzen/autodoc_pydantic

.. |PythonBadge| image:: https://img.shields.io/badge/python-3.8+-blue.svg?style=flat
.. _PythonBadge: http://www.python.org/
