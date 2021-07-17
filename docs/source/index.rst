============================================
Welcome to autodoc_pydantic's documentation!
============================================
|PyPIBadge|_ |PythonBadge|_ |CIBadge|_ |QualityBadge|_ |CoverageBadge|_

**Seamlessly integrate pydantic models in your Sphinx documentation.**

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
- 📚 sorts fields, validators and model config within models by type
- 🍀 Supports `pydantic >= 1.5.0` and `sphinx >= 3.4.0`

To see those features in action, jump over to the :ref:`example <showcase>` section comparing
the appearance of standard sphinx autodoc with *autodoc_pydantic*.

.. toctree::
   :maxdepth: 1
   :caption: User guide

   installation
   usage
   configuration
   examples

.. toctree::
   :maxdepth: 1
   :caption: Developer guide

   developer_guide
   changelog


Acknowledgements
================

Thanks to great open source projects `sphinx`_,
`pydantic <https://pydantic-docs.helpmanual.io/>`_ and
`poetry <https://python-poetry.org/>`_ (and many more) ❤!


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _sphinx: https://www.sphinx-doc.org/en/master

.. |PyPIBadge| image:: https://badge.fury.io/py/autodoc-pydantic.svg
.. _PyPIBadge: https://pypi.org/project/autodoc-pydantic/

.. |CIBadge| image:: https://github.com/mansenfranzen/autodoc_pydantic/actions/workflows/tests.yml/badge.svg
.. _CIBadge: https://github.com/mansenfranzen/autodoc_pydantic/actions/workflows/tests.yml

.. |QualityBadge| image:: https://app.codacy.com/project/badge/Grade/30a083d784f245a98a0d5e6857708cc8
.. _QualityBadge: https://www.codacy.com/gh/mansenfranzen/autodoc_pydantic/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mansenfranzen/autodoc_pydantic&amp;utm_campaign=Badge_Grade

.. |CoverageBadge| image:: https://app.codacy.com/project/badge/Coverage/30a083d784f245a98a0d5e6857708cc8
.. _CoverageBadge: https://www.codacy.com/gh/mansenfranzen/autodoc_pydantic/dashboard?utm_source=github.com&utm_medium=referral&utm_content=mansenfranzen/autodoc_pydantic&utm_campaign=Badge_Coverage

.. |PythonBadge| image:: https://img.shields.io/badge/python-3.6+-blue.svg
.. _PythonBadge: http://www.python.org/