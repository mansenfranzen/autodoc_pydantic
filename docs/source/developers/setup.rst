.. _main-1.x: https://github.com/mansenfranzen/autodoc_pydantic/tree/main-1.x
.. _main: https://github.com/mansenfranzen/autodoc_pydantic/tree/main

=====
Setup
=====

--------------------------------
Setting up developer environment
--------------------------------

**autodoc_pydantic** uses `poetry <https://python-poetry.org/>`__ for environment
and package management.

Cloning repository
------------------

.. code-block:: bash

   git clone https://github.com/mansenfranzen/autodoc_pydantic.git
   cd autodoc_pydantic


Creating environment
--------------------

.. code-block:: bash

   poetry install --all-extras

-----------------------
Running & writing tests
-----------------------

pytest
------

To quickly execute the test suite within your current developer environment
with pytest, run ``poetry run pytest``.

tox
---

For more sophisticated testing, use `tox <https://tox.wiki/en/latest>`_ 
for different test environments. Test environments are characterized 
by varying versions of python and *autodoc_pydantic*'s dependencies 
like pydantic and sphinx. This is critical for ensuring library 
compatibility across different versions of python and pydantic and 
sphinx.

**Usage:**

First, make sure you have tox installed globally via ``pipx`` or ``pip`` 
(see `here <https://tox.wiki/en/latest/installation.html>`_):

Second, to invoke the test suite with tox, run one of the following commands:

- Test a specific environment: ``tox -e py311-pydantic26-sphinx71``
- Test the latest stable versions from pypi: ``tox -e latest``
- Test the current developer versions from git repositories: ``tox -e development``
- Test all available environments: ``tox`` (not recommended)

Please visit the ``tox.ini`` for all available test environments.

.. note::

   Using tox has the benefit of completing the entire build-deploy-test-cycle:

   1. build source distribution from ``pyproject.toml``
   2. create specified virtual environment for test execution
   3. install source distribution in virtual environment
   4. run tests within virtual environment via pytest
   5. provide test coverage report

   This approach is chosen in the corresponding CI/CD pipeline.

-----------------------
Building & writing docs
-----------------------

**autodoc_pydantic**'s documentation is generated with `sphinx <https://www.sphinx-doc.org>`_ .
To generate the HTML documentation, please use the following:

.. code-block:: bash

   poetry shell
   cd docs
   make clean && make html

The generated documentation can be found under ``docs/build/html/index.html``.

.. show_versions::