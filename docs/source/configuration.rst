=============
Configuration
=============

**autodoc_pydantic** is completely configurable. There are two ways to configure
how pydantic objects are displayed:

- **Package Level**: Globally define the default configuration via :code:`conf.py` which takes effect for all pydantic objects like:

   .. code-block:: python

      autodoc_pydantic_model_show_json = True
      autodoc_pydantic_model_show_config = False

- **Directive Level**: Locally define the specific configuration for individual directives. This overrides global configuration settings:

   .. code-block::

      .. autopydantic_model:: module.Model
         :model-show-json: True
         :model-show-config: False

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

      .. autopydantic_model:: target.configuration.ModelShowJson
         :model-show-json: True
         :hide-members:
         :noindex:

   .. tab:: disabled

      .. autopydantic_model:: target.configuration.ModelShowJson
         :model-show-json: False
         :hide-members:
         :noindex:

   .. tab:: example

      .. autocodeblock:: target.configuration.ModelShowJson

   .. tab:: rst

      .. code-block::

         .. autopydantic_model:: target.configuration.ModelShowJson
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

      .. autopydantic_model:: target.configuration.ModelShowConfig
         :model-show-config: True
         :model-show-json: False
         :hide-members:
         :noindex:

   .. tab:: disabled

      .. autopydantic_model:: target.configuration.ModelShowConfig
         :model-show-config: False
         :model-show-json: False
         :hide-members:
         :noindex:

   .. tab:: example

      .. autocodeblock:: target.configuration.ModelShowConfig

   .. tab:: rst

      .. code-block::

         .. autopydantic_model:: target.configuration.ModelShowConfig
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

      .. autopydantic_model:: target.configuration.ModelShowValidators
         :model-show-config: False
         :model-show-json: False
         :model-show-validators: True
         :hide-members:
         :noindex:

   .. tab:: disabled

      .. autopydantic_model:: target.configuration.ModelShowValidators
         :model-show-config: False
         :model-show-json: False
         :model-show-validators: False
         :hide-members:
         :noindex:

   .. tab:: example

      .. autocodeblock:: target.configuration.ModelShowValidators

   .. tab:: rst

      .. code-block::

         .. autopydantic_model:: target.configuration.ModelShowValidators
            :model-show-validators: True

   .. tab:: conf.py

      .. code-block:: python

         autodoc_pydantic_model_show_validators = True # False


Show ParamList
--------------

:Description: Show or hide parameter list of class signature. It usually becomes rather overloaded once a lot fields are present. Additionally, it is redundant since fields are documented anyway.

:Config: `autodoc_pydantic_model_show_paramlist`

:Option: `:model-show-paramlist:`

:Default: False

.. tabs::

   .. tab:: enabled

      .. autopydantic_model:: target.configuration.ModelShowParamList
         :model-show-config: True
         :model-show-json: False
         :model-show-paramlist: True
         :hide-members:
         :noindex:

   .. tab:: disabled

      .. autopydantic_model:: target.configuration.ModelShowParamList
         :model-show-config: False
         :model-show-json: False
         :model-show-paramlist: False
         :hide-members:
         :noindex:

   .. tab:: example

      .. autocodeblock:: target.configuration.ModelShowParamList

   .. tab:: rst

      .. code-block::

         .. autopydantic_model:: target.configuration.ModelShowParamList
            :model-show-paramlist: True

   .. tab:: conf.py

      .. code-block:: python

         autodoc_pydantic_model_show_paramlist = False # True


Show Undoc Members
------------------

:Description: Show undocumented members. By default, undocumented members are hidden for standard :code:`auto` directives. For pydantic models, this is overwritten if enabled.

:Config: `autodoc_pydantic_model_undoc_members`

:Option: `:undoc-members:`

:Default: True

.. tabs::

   .. tab:: enabled

      .. autopydantic_model:: target.configuration.ModelUndocMembers
         :model-show-json: False
         :undoc-members:
         :noindex:

   .. tab:: disabled

      .. autopydantic_model:: target.configuration.ModelUndocMembers
         :model-show-json: False
         :hide-members:
         :noindex:

   .. tab:: example

      .. autocodeblock:: target.configuration.ModelUndocMembers

   .. tab:: rst

      .. code-block::

         .. autopydantic_model:: target.configuration.ModelUndocMembers
            :undoc-members:

   .. tab:: conf.py

      .. code-block:: python

         autodoc_pydantic_model_undoc_members = True # False

.. note::

   In order to show any members at all, you need to enable :ref:`autodoc_pydantic_model_undoc_members<Show Members>`
   or set :code:`:members:`.


Show Members
------------

:Description: Show members. By default, members are hidden for standard :code:`auto` directives. For pydantic models, this is overwritten if enabled.

:Config: `autodoc_pydantic_model_members`

:Option: `:members:`

:Default: True

.. tabs::

   .. tab:: enabled

      .. autopydantic_model:: target.configuration.ModelMembers
         :model-show-json: False
         :noindex:

   .. tab:: disabled

      .. autopydantic_model:: target.configuration.ModelMembers
         :model-show-json: False
         :hide-members:
         :noindex:

   .. tab:: example

      .. autocodeblock:: target.configuration.ModelMembers

   .. tab:: rst

      .. code-block::

         .. autopydantic_model:: target.configuration.ModelMembers
            :members:

   .. tab:: conf.py

      .. code-block:: python

         autodoc_pydantic_model_members = True # False