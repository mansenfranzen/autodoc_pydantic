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

.. note::

   In June 2023, **pydantic v2** was released. This introduced backwards
   incompatible API and behavioral changes in comparison to pydantic v1. Hence,
   **autodoc_pydantic** required substantial adjustments, too. In order to keep
   the codebase clean and concise, separate versions for v1 and v2 were
   created. The v2 branch will eventually become the new `main`_ branch while
   the code for v1 remains in the `main-1.x`_ branch.

   In a nutshell, if you want to work on v1, please checkout the corresponding
   `main-1.x`_ branch. Otherwise, refer to the `main`_ branch.

Creating environment
--------------------

.. code-block:: bash

   poetry install -E dev -E erdantic

-----------------------
Running & writing tests
-----------------------

pytest
------

To quickly execute the test suite within your current developer environment
with pytest, run ``poetry run pytest``.

tox
---

For more sophisticated testing, you can use tox for different test
environments. A test environment is characterized by varying versions of
*autodoc_pydantic*'s dependencies like pydantic, sphinx and sphinx-tabs:

- Test a specific environment: ``poetry run tox -e py38-pydantic17-sphinx34``
- Test the latest stable versions from pypi: ``poetry run tox -e latest``
- Test the current developer versions from git repositories: ``poetry run tox -e development``
- Test all available environments: ``poetry run tox`` (not recommended)

Please visit the ``tox.ini`` for all available test environments.

.. note::

   Using tox has the benefit of completing the entire build-deploy-test-cycle:

   1. build source distribution from ``pyproject.toml``
   2. create specified virtual environment for test execution
   3. install source distribution in virtual environment
   4. run tests within virtual environment via pytest
   5. provide test coverage report


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