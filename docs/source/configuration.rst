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


.. note::

   The following sections describe all available configurations in separation.
   Each configuration is activated in isolation while the remaining are disabled
   to highlight actual difference.

---------
BaseModel
---------

Contains all modifications for pydantic `BaseModel`.


.. tabdocconfig:: autopydantic_model
   :title: Show Config Summary
   :path: target.configuration.ModelShowConfigSummary
   :config: autodoc_pydantic_model_show_config_summary
   :option: model-show-config-summary
   :values: True, False

   Show model config summary within the class doc string. It may be meaningful
   when the class configuration carries some relevant information and you don't
   want to show the entire config class as an explicit member
   (see :ref:`model-show-config-member <autodoc_pydantic_model_show_config_member>`).


.. tabdocconfig:: autopydantic_model
   :title: Show Config Member
   :path: target.configuration.ModelShowConfigMember
   :config: autodoc_pydantic_model_show_config_member
   :option: model-show-config-member
   :option_additional: members
   :values: True, False*

   Show pydantic config class. It can be hidden if it is irrelevant or if
   replaced with :ref:`model-show-config-summary <autodoc_pydantic_model_show_config_summary>`.


.. tabdocconfig:: autopydantic_model
   :title: Show Validator Summary
   :path: target.configuration.ModelShowValidatorsSummary
   :config: autodoc_pydantic_model_show_validator_summary
   :option: model-show-validator-summary
   :values: True, False

   Show all validators along with corresponding fields within the class doc
   string. Hyperlinks are automatically created for validators and fields. This
   is especially useful when dealing with large models having a lot of
   validators.


.. tabdocconfig:: autopydantic_model
   :title: Show Validator Members
   :path: target.configuration.ModelShowValidatorMembers
   :config: autodoc_pydantic_model_show_validator_members
   :option: model-show-validator-members
   :option_additional: members
   :values: True, False

   Show pydantic validator methods. They can be hidden if they are irrelevant.


.. tabdocconfig:: autopydantic_model
   :title: Show Field Summary
   :path: target.configuration.ModelShowFieldSummary
   :config: autodoc_pydantic_model_show_field_summary
   :option: model-show-field-summary
   :values: True, False

   Show all fields within the class doc string. Hyperlinks are automatically
   created. This is especially useful when dealing with large models having a
   lot of fields.


.. tabdocconfig:: autopydantic_model
   :title: Show Undoc Members
   :path: target.configuration.ModelUndocMembers
   :config: autodoc_pydantic_model_undoc_members
   :option: undoc-members
   :option_additional: members
   :values: True, False

   Show undocumented members. By default, undocumented members are hidden for
   standard :code:`auto` directives. For pydantic models, this is overwritten
   if enabled.

.. note::

   In order to show any members at all, you need to enable
   :ref:`autodoc_pydantic_model_members<autodoc_pydantic_model_members>`
   or set :code:`:members:`.


.. tabdocconfig:: autopydantic_model
   :title: Show Members
   :path: target.configuration.ModelMembers
   :config: autodoc_pydantic_model_members
   :option: members
   :values: True, False

   Show members. By default, members are hidden for standard :code:`auto`
   directives. For pydantic models, this is overwritten if enabled.

.. tabdocconfig:: autopydantic_model
   :title: Member Order
   :path: target.configuration.ModelMemberOrder
   :config: autodoc_pydantic_model_member_order
   :option: member-order
   :option_additional: members, model-show-config-member, model-show-validator-members
   :values: groupwise, bysource, alphabetical

   Order members groupwise by default in the following order: fields,
   validators and config.


.. tabdocconfig:: autopydantic_model
   :title: Hide ParamList
   :path: target.configuration.ModelHideParamList
   :config: autodoc_pydantic_model_hide_paramlist
   :option: model-hide-paramlist
   :values: True, False

   Hide parameter list within class signature which usually becomes rather
   overloaded once a lot fields are present. Additionally, it is redundant
   since fields are documented anyway.


.. tabdocconfig:: autopydantic_model
   :title: Signature Prefix
   :path: target.configuration.ModelSignaturePrefix
   :config: autodoc_pydantic_model_signature_prefix
   :option: model-signature-prefix
   :values: pydantic model, class, foobar

   Define the signature prefix for pydantic models.


.. tabdocconfig:: autopydantic_model
   :title: Show Schema JSON
   :path: target.configuration.ModelShowJson
   :config: autodoc_pydantic_model_show_json
   :option: model-show-json
   :values: True, False

   Show the schema json representation of a pydantic model within in the class
   doc string as a collapsable code block.

.. warning::

   Fields containing custom objects may not be JSON serializable. This will break
   the schema generation by default. However, it can be handled via :ref:`Show Schema JSON Error Strategy <autodoc_pydantic_model_show_json_error_strategy>`.


.. _autodoc_pydantic_model_show_json_error_strategy:

Show Schema JSON Error Strategy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Define error handling in case a pydantic field breaks pydantic model schema
generation. This occurs if a pydantic field is not JSON serializable.

:conf.py: *autodoc_pydantic_model_show_json_error_strategy*

:option: *model-show-json-error-strategy*

**Available values:**

- ``coerce``: Keep violating fields in resulting schema but only show the title. Do not
  provide a warning during doc building process.
- ``warn`` (default): Keep violating fields in resulting schema but only show the title. Provide
  a warning during the doc building process.
- ``raise``: Raises an ``sphinx.errors.ExtensionError`` during building process.


------------
BaseSettings
------------

Contains all modifications for pydantic `BaseSettings`.

.. tabdocconfig:: autopydantic_settings
   :title: Show Config Summary
   :path: target.configuration.SettingsShowConfigSummary
   :config: autodoc_pydantic_settings_show_config_summary
   :option: settings-show-config-summary
   :values: True, False

   Show model config summary within the class doc string. It may be meaningful
   when the class configuration carries some relevant information and you don't
   want to show the entire config class as an explicit member
   (see :ref:`settings-show-config-member <autodoc_pydantic_settings_show_config_member>`).


.. tabdocconfig:: autopydantic_settings
   :title: Show Config Member
   :path: target.configuration.SettingsShowConfigMember
   :config: autodoc_pydantic_settings_show_config_member
   :option: settings-show-config-member
   :option_additional: members
   :values: True, False*

   Show pydantic config class. It can be hidden if it is irrelevant or if
   replaced with :ref:`settings-show-config-summary <autodoc_pydantic_settings_show_config_summary>`.


.. tabdocconfig:: autopydantic_settings
   :title: Show Validator Summary
   :path: target.configuration.SettingsShowValidatorsSummary
   :config: autodoc_pydantic_settings_show_validator_summary
   :option: settings-show-validator-summary
   :values: True, False

   Show all validators along with corresponding fields within the class doc
   string. Hyperlinks are automatically created for validators and fields. This
   is especially useful when dealing with large models having a lot of
   validators.


.. tabdocconfig:: autopydantic_settings
   :title: Show Validator Members
   :path: target.configuration.SettingsShowValidatorMembers
   :config: autodoc_pydantic_settings_show_validator_members
   :option: settings-show-validator-members
   :option_additional: members
   :values: True, False

   Show pydantic validator methods. They can be hidden if they are irrelevant.


.. tabdocconfig:: autopydantic_settings
   :title: Show Field Summary
   :path: target.configuration.SettingsShowFieldSummary
   :config: autodoc_pydantic_settings_show_field_summary
   :option: settings-show-field-summary
   :values: True, False

   Show all fields within the class doc string. Hyperlinks are automatically
   created. This is especially useful when dealing with large models having a
   lot of fields.

.. tabdocconfig:: autopydantic_settings
   :title: Show Undoc Members
   :path: target.configuration.SettingsUndocMembers
   :config: autodoc_pydantic_settings_undoc_members
   :option: undoc-members
   :option_additional: members
   :values: True, False

   Show undocumented members. By default, undocumented members are hidden for
   standard :code:`auto` directives. For pydantic settings, this is overwritten
   if enabled.

.. note::

   In order to show any members at all, you need to enable
   :ref:`autodoc_pydantic_settings_members<autodoc_pydantic_settings_members>`
   or set :code:`:members:`.


.. tabdocconfig:: autopydantic_settings
   :title: Show Members
   :path: target.configuration.SettingsMembers
   :config: autodoc_pydantic_settings_members
   :option: members
   :values: True, False

   Show members. By default, members are hidden for standard :code:`auto`
   directives. For pydantic settingss, this is overwritten if enabled.

.. tabdocconfig:: autopydantic_settings
   :title: Member Order
   :path: target.configuration.SettingsMemberOrder
   :config: autodoc_pydantic_settings_member_order
   :option: member-order
   :option_additional: members, settings-show-config-member, settings-show-validator-members
   :values: groupwise, bysource, alphabetical

   Order members groupwise by default in the following order: fields,
   validators and config.


.. tabdocconfig:: autopydantic_settings
   :title: Hide ParamList
   :path: target.configuration.SettingsHideParamList
   :config: autodoc_pydantic_settings_hide_paramlist
   :option: settings-hide-paramlist
   :values: True, False

   Hide parameter list within class signature which usually becomes rather
   overloaded once a lot fields are present. Additionally, it is redundant
   since fields are documented anyway.


.. tabdocconfig:: autopydantic_settings
   :title: Signature Prefix
   :path: target.configuration.SettingsSignaturePrefix
   :config: autodoc_pydantic_settings_signature_prefix
   :option: settings-signature-prefix
   :values: pydantic settings, class, foobar

   Define the signature prefix for pydantic settings.


.. tabdocconfig:: autopydantic_settings
   :title: Show Schema JSON
   :path: target.configuration.SettingsShowJson
   :config: autodoc_pydantic_settings_show_json
   :option: settings-show-json
   :values: True, False

   Show the schema json representation of pydantic settings within in the class
   doc string as a collapsable code block.

.. warning::

   Fields containing custom objects may not be JSON serializable. This will break
   the schema generation by default. However, it can be handled via  :ref:`Show Schema JSON Error Strategy <autodoc_pydantic_settings_show_json_error_strategy>`.

.. _autodoc_pydantic_settings_show_json_error_strategy:

Show Schema JSON Error Strategy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Define error handling in case a pydantic field breaks pydantic settings schema
generation. This occurs if a pydantic field is not JSON serializable.

:conf.py: *autodoc_pydantic_settings_show_json_error_strategy*

:option: *settings-show-json-error-strategy*

**Available values:**

- ``coerce``: Keep violating fields in resulting schema but only show the title. Do not
  provide a warning during doc building process.
- ``warn`` (default): Keep violating fields in resulting schema but only show the title. Provide
  a warning during the doc building process.
- ``raise``: Raises an ``sphinx.errors.ExtensionError`` during building process.


------
Fields
------

.. tabdocconfig:: autopydantic_model
   :title: List Validators
   :path: target.configuration.FieldListValidators
   :config: autodoc_pydantic_field_list_validators
   :option: field-list-validators
   :option_additional: members, field-doc-policy=docstring
   :values: True, False

   List all linked validators within doc string that process the current field.
   Hyperlinks to corresponding validators are automatically provided.


.. tabdocconfig:: autopydantic_model
   :title: Docstring Policy
   :path: target.configuration.FieldDocPolicy
   :config: autodoc_pydantic_field_doc_policy
   :option: field-doc-policy
   :option_additional: members
   :values: docstring, description, both*

   Define what content is displayed in the main field docstring. The following
   values are possible:

   - **docstring** shows the exact docstring of the python attribute.
   - **description** displays the information provided via the pydantic field's description.
   - **both** will output the attribute's docstring together with the pydantic field's description.


.. tabdocconfig:: autopydantic_model
   :title: Show Constraints
   :path: target.configuration.FieldShowConstraints
   :config: autodoc_pydantic_field_show_constraints
   :option: field-show-constraints
   :option_additional: members, field-doc-policy=docstring
   :values: True, False

   Displays all constraints that are associated with the given pydantic field.


.. tabdocconfig:: autopydantic_model
   :title: Show Alias
   :path: target.configuration.FieldShowAlias
   :config: autodoc_pydantic_field_show_alias
   :option: field-show-alias
   :option_additional: members, field-doc-policy=docstring
   :values: True, False

   Provides the pydantic field's alias in the signature.


.. tabdocconfig:: autopydantic_model
   :title: Show Default Value
   :path: target.configuration.FieldShowDefault
   :config: autodoc_pydantic_field_show_default
   :option: field-show-default
   :option_additional: members, field-doc-policy=docstring
   :values: True, False

   Provides the pydantic field's default value in the signature. Unfortunately
   this is not provided by standard autodoc (as of version 3.5.4).


.. tabdocconfig:: autopydantic_model
   :title: Signature Prefix
   :path: target.configuration.FieldSignaturePrefix
   :config: autodoc_pydantic_field_signature_prefix
   :option: field-signature-prefix
   :option_additional: members, field-doc-policy=docstring
   :values: field, attribute, foobar

   Define the signature prefix for pydantic field.


----------
Validators
----------

.. tabdocconfig:: autopydantic_model
   :title: Replace Signature
   :path: target.configuration.ValidatorReplaceSignature
   :config: autodoc_pydantic_validator_replace_signature
   :option: validator-replace-signature
   :option_additional: members, model-show-validator-members, undoc-members
   :values: True, False

   Replaces the validator signature with custom links to corresponding fields.
   Pydantic validator signatures usually do not carry important information and
   hence may be replaced. However, you may want to keep the signature patterns
   constant across methods. In this scenario, you may list the associated
   fields within the doc string via
   :ref:`validator-list-fields <autodoc_pydantic_validator_list_fields>`.


.. tabdocconfig:: autopydantic_model
   :title: List Fields
   :path: target.configuration.ValidatorListFields
   :config: autodoc_pydantic_validator_list_fields
   :option: validator-list-fields
   :option_additional: members, model-show-validator-members, undoc-members
   :values: True, False*

   List all fields that are processed by current validator.
   This provides the same information as
   :ref:`validator-replace-signature <autodoc_pydantic_validator_replace_signature>`,
   however it does not change the signature but adds the links in the doc
   string.


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

   Show members. By default, members are hidden for standard :code:`auto`
   directives. For pydantic class config, this is overwritten if enabled.

.. note::

   By default, all undocumented members are shown for the `Config` class.
   The directive option :code:`:undoc-members:` is added automatically.


.. tabdocconfig:: autopydantic_config
   :title: Signature Prefix
   :path: target.configuration.ConfigSignaturePrefix.Config
   :config: autodoc_pydantic_config_signature_prefix
   :option: config-signature-prefix
   :values: model, class, foobar

   Define the signature prefix for config class.
