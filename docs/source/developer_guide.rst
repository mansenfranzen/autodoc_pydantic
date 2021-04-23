--------------------------------
Setting up developer environment
--------------------------------

*autodoc_pydantic* uses poetry for environment and package management.

Cloning repository
------------------

.. code-block:: bash

   git clone https://github.com/mansenfranzen/autodoc_pydantic.git
   cd autodoc_pydantic

Creating environment
--------------------

.. code-block:: bash

   poetry install

-----------------------
Running & writing tests
-----------------------

.. code-block:: bash

   poetry run pytest

-----------------------
Building & writing docs
-----------------------

.. code-block:: bash

   poetry shell
   cd docs
   make clean && make html
