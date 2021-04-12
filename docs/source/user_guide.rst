============
Installation
============

=====
Usage
=====

=============
Configuration
=============

Summary
=======

**autodoc_pydantic** is completely configurable to meet your custom requirements.
There are two ways to configure how pydantic objects are displayed:

- **Package Level**: Globally define the default configuration via :code:`conf.py` like:

   .. code-block:: python

      autodoc_pydantic_model_show_json = True
      autodoc_pydantic_model_show_config = False

- **Directive Level**: Locally define the specific configuration for individual directives via options like:

   .. code-block::

      .. autopydantic_model:: module.Model
         :model-show-json: True
         :model-show-config: False

Reference
=========

:Model:

  - :ref:`Show JSON - autodoc_pydantic_model_show_json<Show JSON>`
  - :ref:`Show Config - autodoc_pydantic_model_show_config<Show Config>`

-----
Model
-----

Show JSON
---------

:Description: Show the json representation of a pydantic model within in the class doc string as a collapsable code block.

:Config: `autodoc_pydantic_model_show_json`

:Option: `:model-show-json:`

:Default: True

.. tabs::

   .. tab:: enabled

      .. autopydantic_model:: package.cfg.ShowJson
         :model-show-json: True
         :hide-members:
         :noindex:

   .. tab:: disabled

      .. autopydantic_model:: package.cfg.ShowJson
         :model-show-json: False
         :hide-members:
         :noindex:

   .. tab:: example

      .. code-block:: python

         class ShowJson(BaseModel):
             """Exmaple showing json representation."""

             field: int = 5

   .. tab:: rst

      .. code-block::

         .. autopydantic_model:: package.cfg.ShowJson
            :model-show-json: True

   .. tab:: conf.py

      .. code-block:: python

         autodoc_pydantic_model_show_json = True # False


Show Config
-----------

:Description: Show model config summary within the class doc string.

:Config: `autodoc_pydantic_model_show_config`

:Option: `:model-show-config:`

:Default: True

.. tabs::

   .. tab:: enabled

      .. autopydantic_model:: package.cfg.ShowConfig
         :model-show-config: True
         :model-show-json: False
         :hide-members:
         :noindex:

   .. tab:: disabled

      .. autopydantic_model:: package.cfg.ShowConfig
         :model-show-config: False
         :model-show-json: False
         :hide-members:
         :noindex:

   .. tab:: example

      .. code-block:: python

         class ShowConfig(BaseModel):
             """Example showing model configuration."""

             class Config:
                 title = "FooBar"
                 allow_mutation = True

   .. tab:: rst

      .. code-block::

         .. autopydantic_model:: package.cfg.ShowConfig
            :model-show-config: True

   .. tab:: conf.py

      .. code-block:: python

         autodoc_pydantic_model_show_config = True # False


Show Validators
---------------

:Description: Show all validators along with corresponding fields within the class doc string. Hyperlinks are automatically created for validators and fields.

:Config: `autodoc_pydantic_model_show_validators`

:Option: `:model-show-validators:`

:Default: True

.. tabs::

   .. tab:: enabled

      .. autopydantic_model:: package.cfg.ShowValidators
         :model-show-config: False
         :model-show-json: False
         :model-show-validators: True
         :hide-members:
         :noindex:

   .. tab:: disabled

      .. autopydantic_model:: package.cfg.ShowValidators
         :model-show-config: False
         :model-show-json: False
         :model-show-validators: False
         :hide-members:
         :noindex:

   .. tab:: example

      .. code-block:: python

         class ShowValidators(BaseModel):
             """Exmaple showing validators."""

             field1: int = 5
             field2: str = "FooBar"

             @validator("field1")
             def check1(cls, v):
                 return v

             @validator("field2")
             def check2(cls, v):
                 return v

   .. tab:: rst

      .. code-block::

         .. autopydantic_model:: package.cfg.ShowValidators
            :model-show-validators: True

   .. tab:: conf.py

      .. code-block:: python

         autodoc_pydantic_model_show_validators = True # False