=============
Configuration
=============

One major strength of **autodoc_pydantic** is that every feature is completely
configurable to allow maximum customization. There are two ways to configure
how pydantic objects are displayed:

- **conf.py**: Globally define the default configuration via :code:`conf.py` which takes effect for all pydantic objects like:

   .. code-block:: python

      autodoc_pydantic_model_show_json = True
      autodoc_pydantic_model_show_config = False

- **option**: Locally define the specific configuration for individual directives. This overrides global configuration settings:

   .. code-block::

      .. autopydantic_model:: module.Model
         :model-show-json: True
         :model-show-config: False


-----
Model
-----

.. tabdocconfig:: autopydantic_model
   :title: Show JSON
   :path: target.configuration.ModelShowJson
   :config: autodoc_pydantic_model_show_json
   :option: model-show-json
   :values: True, False

   Show the json representation of a pydantic model within in the class doc string as a collapsable code block.


.. tabdocconfig:: autopydantic_model
   :title: Show Config
   :path: target.configuration.ModelShowConfig
   :config: autodoc_pydantic_model_show_config
   :option: model-show-config
   :values: True, False

   Show model config summary within the class doc string.


.. tabdocconfig:: autopydantic_model
   :title: Show Validators
   :path: target.configuration.ModelShowValidators
   :config: autodoc_pydantic_model_show_validators
   :option: model-show-validators
   :values: True, False

   Show all validators along with corresponding fields within the class doc string. Hyperlinks are automatically created for validators and fields.


.. tabdocconfig:: autopydantic_model
   :title: Hide ParamList
   :path: target.configuration.ModelHideParamList
   :config: autodoc_pydantic_model_hide_paramlist
   :option: model-hide-paramlist
   :values: True, False

   Hide parameter list of class signature. It usually becomes rather overloaded once a lot fields are present. Additionally, it is redundant since fields are documented anyway.


.. tabdocconfig:: autopydantic_model
   :title: Show Undoc Members
   :path: target.configuration.ModelUndocMembers
   :config: autodoc_pydantic_model_undoc_members
   :option: undoc-members
   :option_additional: members
   :values: True, False

   Show undocumented members. By default, undocumented members are hidden for standard :code:`auto` directives. For pydantic models, this is overwritten if enabled.

.. note::

   In order to show any members at all, you need to enable :ref:`autodoc_pydantic_model_undoc_members<Show Members>`
   or set :code:`:members:`.


.. tabdocconfig:: autopydantic_model
   :title: Show Members
   :path: target.configuration.ModelMembers
   :config: autodoc_pydantic_model_members
   :option: members
   :values: True, False

   Show members. By default, members are hidden for standard :code:`auto` directives. For pydantic models, this is overwritten if enabled.

.. tabdocconfig:: autopydantic_model
   :title: Member Order
   :path: target.configuration.ModelMemberOrder
   :config: autodoc_pydantic_model_member_order
   :option: member-order
   :option_additional: members, config-show, validator-show
   :values: groupwise, bysource, alphabetical

   Order members groupwise by default in the following order: fields, validators and config.