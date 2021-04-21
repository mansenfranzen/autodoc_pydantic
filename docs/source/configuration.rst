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

---------------------
Default configuration
---------------------

.. tabs::

   .. tab:: autodoc pydantic

      .. autopydantic_settings:: target.ExampleSettings

   .. tab:: autodoc sphinx

      .. autopydantic_settings:: target.ExampleSettings
         :members:
         :__doc_disable_except__: members
         :noindex:

   .. tab:: *example code*

      .. autocodeblock:: target.ExampleSettings


---------
BaseModel
---------

Contains all modifications for pydantic `BaseModel`.

.. tabdocconfig:: autopydantic_model
   :title: Show JSON
   :path: target.configuration.ModelShowJson
   :config: autodoc_pydantic_model_show_json
   :option: model-show-json
   :values: True, False

   Show the json representation of a pydantic model within in the class doc string as a collapsable code block.


.. tabdocconfig:: autopydantic_model
   :title: Show Config Summary
   :path: target.configuration.ModelShowConfigSummary
   :config: autodoc_pydantic_model_show_config_summary
   :option: model-show-config-summary
   :values: True, False

   Show model config summary within the class doc string.


.. tabdocconfig:: autopydantic_model
   :title: Show Config Member
   :path: target.configuration.ModelShowConfigMember
   :config: autodoc_pydantic_model_show_config_member
   :option: model-show-config-member
   :option_additional: members
   :values: True, False

   Show pydantic config class. It can be hidden if it is irrelevant.


.. tabdocconfig:: autopydantic_model
   :title: Show Validator Summary
   :path: target.configuration.ModelShowValidatorsSummary
   :config: autodoc_pydantic_model_show_validator_summary
   :option: model-show-validator-summary
   :values: True, False

   Show all validators along with corresponding fields within the class doc string. Hyperlinks are automatically created for validators and fields.


.. tabdocconfig:: autopydantic_model
   :title: Show Validator Members
   :path: target.configuration.ModelShowValidatorMembers
   :config: autodoc_pydantic_model_show_validator_members
   :option: model-show-validator-members
   :option_additional: members
   :values: True, False

   Show pydantic validator methods. They can be hidden if they are irrelevant.


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
   :option_additional: members, model-show-config-member, model-show-validator-members
   :values: groupwise, bysource, alphabetical

   Order members groupwise by default in the following order: fields, validators and config.


.. tabdocconfig:: autopydantic_model
   :title: Hide ParamList
   :path: target.configuration.ModelHideParamList
   :config: autodoc_pydantic_model_hide_paramlist
   :option: model-hide-paramlist
   :values: True, False

   Hide parameter list of class signature. It usually becomes rather overloaded once a lot fields are present. Additionally, it is redundant since fields are documented anyway.


.. tabdocconfig:: autopydantic_model
   :title: Signature Prefix
   :path: target.configuration.ModelSignaturePrefix
   :config: autodoc_pydantic_model_signature_prefix
   :option: model-signature-prefix
   :values: pydantic model, class, foobar

   Define the signature prefix for pydantic models.


------------
BaseSettings
------------

Contains all modifications for pydantic `BaseSettings`.

.. tabdocconfig:: autopydantic_settings
   :title: Show JSON
   :path: target.configuration.SettingsShowJson
   :config: autodoc_pydantic_settings_show_json
   :option: settings-show-json
   :values: True, False

   Show the json representation of a pydantic settings within in the class doc string as a collapsable code block.


.. tabdocconfig:: autopydantic_settings
   :title: Show Config Summary
   :path: target.configuration.SettingsShowConfigSummary
   :config: autodoc_pydantic_settings_show_config_summary
   :option: settings-show-config-summary
   :values: True, False

   Show settings config summary within the class doc string.


.. tabdocconfig:: autopydantic_settings
   :title: Show Config Member
   :path: target.configuration.SettingsShowConfigMember
   :config: autodoc_pydantic_settings_show_config_member
   :option: settings-show-config-member
   :option_additional: members
   :values: True, False

   Show pydantic config class. It can be hidden if it is irrelevant.


.. tabdocconfig:: autopydantic_settings
   :title: Show Validator Summary
   :path: target.configuration.SettingsShowValidatorsSummary
   :config: autodoc_pydantic_settings_show_validator_summary
   :option: settings-show-validator-summary
   :values: True, False

   Show all validators along with corresponding fields within the class doc string. Hyperlinks are automatically created for validators and fields.


.. tabdocconfig:: autopydantic_settings
   :title: Show Validator Members
   :path: target.configuration.SettingsShowValidatorMembers
   :config: autodoc_pydantic_settings_show_validator_members
   :option: settings-show-validator-members
   :option_additional: members
   :values: True, False

   Show pydantic validator methods. They can be hidden if they are irrelevant.


.. tabdocconfig:: autopydantic_settings
   :title: Show Undoc Members
   :path: target.configuration.SettingsUndocMembers
   :config: autodoc_pydantic_settings_undoc_members
   :option: undoc-members
   :option_additional: members
   :values: True, False

   Show undocumented members. By default, undocumented members are hidden for standard :code:`auto` directives. For pydantic settingss, this is overwritten if enabled.

.. note::

   In order to show any members at all, you need to enable :ref:`autodoc_pydantic_settings_undoc_members<Show Members>`
   or set :code:`:members:`.


.. tabdocconfig:: autopydantic_settings
   :title: Show Members
   :path: target.configuration.SettingsMembers
   :config: autodoc_pydantic_settings_members
   :option: members
   :values: True, False

   Show members. By default, members are hidden for standard :code:`auto` directives. For pydantic settingss, this is overwritten if enabled.

.. tabdocconfig:: autopydantic_settings
   :title: Member Order
   :path: target.configuration.SettingsMemberOrder
   :config: autodoc_pydantic_settings_member_order
   :option: member-order
   :option_additional: members, settings-show-config-member, settings-show-validator-members
   :values: groupwise, bysource, alphabetical

   Order members groupwise by default in the following order: fields, validators and config.


.. tabdocconfig:: autopydantic_settings
   :title: Hide ParamList
   :path: target.configuration.SettingsHideParamList
   :config: autodoc_pydantic_settings_hide_paramlist
   :option: settings-hide-paramlist
   :values: True, False

   Hide parameter list of class signature. It usually becomes rather overloaded once a lot fields are present. Additionally, it is redundant since fields are documented anyway.


.. tabdocconfig:: autopydantic_settings
   :title: Signature Prefix
   :path: target.configuration.SettingsSignaturePrefix
   :config: autodoc_pydantic_settings_signature_prefix
   :option: settings-signature-prefix
   :values: pydantic settings, class, foobar

   Define the signature prefix for pydantic settings.


----------
Validators
----------

.. tabdocconfig:: autopydantic_model
   :title: Replace signature
   :path: target.configuration.ValidatorReplaceSignature
   :config: autodoc_pydantic_validator_replace_signature
   :option: validator-replace-signature
   :option_additional: members, model-show-validator-members, undoc-members
   :values: True, False

   Replaces the validator signature with custom link to corresponding field.


.. tabdocconfig:: autopydantic_model
   :title: List fields
   :path: target.configuration.ValidatorListFields
   :config: autodoc_pydantic_validator_list_fields
   :option: validator-list-fields
   :option_additional: members, model-show-validator-members, undoc-members
   :values: True, False

   List all fields that are validated by given method.


.. tabdocconfig:: autopydantic_model
   :title: Signature Prefix
   :path: target.configuration.ValidatorSignaturePrefix
   :config: autodoc_pydantic_validator_signature_prefix
   :option: validator-signature-prefix
   :option_additional: members, model-show-validator-members, undoc-members
   :values: validator, classmethod, foobar

   Define the signature prefix for pydantic validator.

------------
Config Class
------------

.. tabdocconfig:: autopydantic_model
   :title: Show Members
   :path: target.configuration.ConfigMembers
   :config: autodoc_pydantic_config_members
   :option: members
   :option_additional: model-show-config-member, undoc-members
   :values: True, False

   Show members. By default, members are hidden for standard :code:`auto` directives. For pydantic class config, this is overwritten if enabled.

.. note::

   By default, all undocumented members are shown for the `Config` class. The directive option :code:`:undoc-members:` is added automatically.


.. tabdocconfig:: autopydantic_config
   :title: Signature Prefix
   :path: target.configuration.ConfigSignaturePrefix.Config
   :config: autodoc_pydantic_config_signature_prefix
   :option: config-signature-prefix
   :values: model, class, foobar

   Define the signature prefix for config class.
