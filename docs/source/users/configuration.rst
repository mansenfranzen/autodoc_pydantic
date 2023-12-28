=============
Configuration
=============

.. _configuration:

One major strength of **autodoc_pydantic** is that every feature is completely
configurable to allow maximum customization. There are two ways to configure
how pydantic objects are displayed:

- **conf.py**: Globally define the default configuration via :code:`conf.py`
  which takes effect for all pydantic objects like:

   .. code-block:: python

      autodoc_pydantic_model_show_json = True
      autodoc_pydantic_model_show_config_summary = False

- **directive**: Locally define specific configurations via directive options.
  This overrides global configuration settings:

   .. code-block::

      .. autopydantic_model:: module.Model
         :model-show-json: True
         :model-show-config-summary: False


.. note::

   The following sections describe all available configurations in separation.
   Each configuration is activated in isolation while the remaining are disabled
   to highlight actual difference.

-----
Model
-----

Contains all modifications for pydantic `BaseModel`.


.. config_description:: autopydantic_model
   :title: Show Config Summary
   :path: target.configuration.ModelShowConfigSummary
   :confpy: autodoc_pydantic_model_show_config_summary
   :directive_option: model-show-config-summary
   :values: True, False

   Show model config summary within the class doc string. It may be meaningful
   when the class configuration carries some relevant information.


.. config_description:: autopydantic_model
   :title: Show Validator Summary
   :path: target.configuration.ModelShowValidatorsSummary
   :confpy: autodoc_pydantic_model_show_validator_summary
   :directive_option: model-show-validator-summary
   :values: True, False

   Show all validators along with corresponding fields within the class doc
   string. Hyperlinks are automatically created for validators and fields. This
   is especially useful when dealing with large models having a lot of
   validators. Please note, the sort order of summary items can be configured via
   :ref:`model-summary-list-order <autodoc_pydantic_model_summary_list_order>`.


.. config_description:: autopydantic_model
   :title: Show Validator Members
   :path: target.configuration.ModelShowValidatorMembers
   :confpy: autodoc_pydantic_model_show_validator_members
   :directive_option: model-show-validator-members
   :enable: members
   :values: True, False

   Show pydantic validator methods. They can be hidden if they are irrelevant.


.. config_description:: autopydantic_model
   :title: Show Field Summary
   :path: target.configuration.ModelShowFieldSummary
   :confpy: autodoc_pydantic_model_show_field_summary
   :directive_option: model-show-field-summary
   :values: True, False
   :version: 1.2.0

   Show all fields within the class doc string. Hyperlinks are automatically
   created. This is especially useful when dealing with large models having a
   lot of fields. Please note, the sort order of summary items can be configured via
   :ref:`model-summary-list-order <autodoc_pydantic_model_summary_list_order>`.


.. config_description:: autopydantic_model
   :title: Summary List Order
   :path: target.configuration.ModelSummaryListOrder
   :confpy: autodoc_pydantic_model_summary_list_order
   :directive_option: model-summary-list-order
   :enable: model-show-validator-summary, model-show-field-summary
   :values: alphabetical, bysource
   :version: 1.5.0

   Define the sort order within validator and field summaries (which can be
   activated via :ref:`model-show-validator-summary <autodoc_pydantic_model_show_validator_summary>`
   and :ref:`model-show-field-summary <autodoc_pydantic_model_show_field_summary>`,
   respectively).


.. config_description:: autopydantic_model
   :title: Show Undoc Members
   :path: target.configuration.ModelUndocMembers
   :confpy: autodoc_pydantic_model_undoc_members
   :directive_option: undoc-members
   :enable: members
   :values: True, False

   Show undocumented members. By default, undocumented members are hidden for
   standard :code:`auto` directives. For pydantic models, this is overwritten
   if enabled.

.. note::

   In order to show any members at all, you need to enable
   :ref:`autodoc_pydantic_model_members<autodoc_pydantic_model_members>`
   or set :code:`:members:`.


.. config_description:: autopydantic_model
   :title: Show Members
   :path: target.configuration.ModelMembers
   :confpy: autodoc_pydantic_model_members
   :directive_option: members
   :values: True, False

   Show members. By default, members are hidden for standard :code:`auto`
   directives. For pydantic models, this is overwritten if enabled.

.. config_description:: autopydantic_model
   :title: Member Order
   :path: target.configuration.ModelMemberOrder
   :confpy: autodoc_pydantic_model_member_order
   :directive_option: member-order
   :enable: members, model-show-config-member, model-show-validator-members
   :values: groupwise, bysource, alphabetical

   Order members groupwise by default in the following order: fields,
   validators and config.


.. config_description:: autopydantic_model
   :title: Hide ParamList
   :path: target.configuration.ModelHideParamList
   :confpy: autodoc_pydantic_model_hide_paramlist
   :directive_option: model-hide-paramlist
   :values: True, False

   Hide parameter list within class signature which usually becomes rather
   overloaded once a lot fields are present. Additionally, it is redundant
   since fields are documented anyway.


.. config_description:: autopydantic_model
   :title: Hide Reused Validators
   :path: target.configuration_model_hide_reused_validator.ModelOne
   :example_path: target.configuration_model_hide_reused_validator
   :confpy: autodoc_pydantic_model_hide_reused_validator
   :directive_option: model-hide-reused-validator
   :values: True, False
   :version: 1.8.0

   Hide class methods that are created while declaring functions as reusable
   validators. For more information and a detailed example, please see
   :ref:`the example page for reused validators <example_reused_validators>`.


.. config_description:: autopydantic_model
   :title: Signature Prefix
   :path: target.configuration.ModelSignaturePrefix
   :confpy: autodoc_pydantic_model_signature_prefix
   :directive_option: model-signature-prefix
   :values: pydantic model, class, foobar

   Define the signature prefix for pydantic models.


.. config_description:: autopydantic_model
   :title: Show Erdantic figure
   :path: target.configuration.ModelErdanticFigure
   :confpy: autodoc_pydantic_model_erdantic_figure
   :directive_option: model-erdantic-figure
   :values: True, False

   Show the entity relationship diagram of the schemas using erdantic. To
   use this option, you need first to install
   `graphviz <https://graphviz.org/download/>`_ , then install
   **autodoc_pydantic** with the ``erdantic`` option:

   .. code-block:: bash

      pip install autodoc_pydantic[erdantic].


.. config_description:: autopydantic_model
   :title: Show Erdantic figure collapsed
   :path: target.configuration.ModelErdanticFigure
   :confpy: autodoc_pydantic_model_erdantic_figure_collapsed
   :directive_option: model-erdantic-figure-collapsed
   :enable: model-erdantic-figure
   :values: True, False

   Show the entity relationship diagram collapsed or not.
   :ref:`model-erdantic-figure <autodoc_pydantic_model_erdantic_figure>` must be True for this to have any effect.


.. config_description:: autopydantic_model
   :title: Show Schema JSON
   :path: target.configuration.ModelShowJson
   :confpy: autodoc_pydantic_model_show_json
   :directive_option: model-show-json
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

**Configuration** *(added in version 1.4.0)*

:conf.py: *autodoc_pydantic_model_show_json_error_strategy*

:directive_option: *model-show-json-error-strategy*

**Available values:**

- ``coerce``: Keep violating fields in resulting schema but only show the title. Do not
  provide a warning during doc building process.
- ``warn`` (default): Keep violating fields in resulting schema but only show the title. Provide
  a warning during the doc building process.
- ``raise``: Raises an ``sphinx.errors.ExtensionError`` during building process.


--------
Settings
--------

Contains all modifications for pydantic `BaseSettings`.

.. config_description:: autopydantic_settings
   :title: Show Config Summary
   :path: target.configuration.SettingsShowConfigSummary
   :confpy: autodoc_pydantic_settings_show_config_summary
   :directive_option: settings-show-config-summary
   :values: True, False

   Show model config summary within the class doc string. It may be meaningful
   when the class configuration carries some relevant information.


.. config_description:: autopydantic_settings
   :title: Show Validator Summary
   :path: target.configuration.SettingsShowValidatorsSummary
   :confpy: autodoc_pydantic_settings_show_validator_summary
   :directive_option: settings-show-validator-summary
   :values: True, False

   Show all validators along with corresponding fields within the class doc
   string. Hyperlinks are automatically created for validators and fields. This
   is especially useful when dealing with large models having a lot of
   validators. Please note, the sort order of summary items can be configured via
   :ref:`settings-summary-list-order <autodoc_pydantic_settings_summary_list_order>`.


.. config_description:: autopydantic_settings
   :title: Show Validator Members
   :path: target.configuration.SettingsShowValidatorMembers
   :confpy: autodoc_pydantic_settings_show_validator_members
   :directive_option: settings-show-validator-members
   :enable: members
   :values: True, False

   Show pydantic validator methods. They can be hidden if they are irrelevant.


.. config_description:: autopydantic_settings
   :title: Show Field Summary
   :path: target.configuration.SettingsShowFieldSummary
   :confpy: autodoc_pydantic_settings_show_field_summary
   :directive_option: settings-show-field-summary
   :values: True, False
   :version: 1.2.0

   Show all fields within the class doc string. Hyperlinks are automatically
   created. This is especially useful when dealing with large models having a
   lot of fields. Please note, the sort order of summary items can be configured via
   :ref:`settings-summary-list-order <autodoc_pydantic_settings_summary_list_order>`.


.. config_description:: autopydantic_settings
   :title: Summary List Order
   :path: target.configuration.SettingsSummaryListOrder
   :confpy: autodoc_pydantic_settings_summary_list_order
   :directive_option: settings-summary-list-order
   :enable: settings-show-validator-summary, settings-show-field-summary
   :values: alphabetical, bysource
   :version: 1.5.0

   Define the sort order within validator and field summaries (which can be
   activated via :ref:`settings-show-validator-summary <autodoc_pydantic_settings_show_validator_summary>`
   and :ref:`settings-show-field-summary <autodoc_pydantic_settings_show_field_summary>`,
   respectively).


.. config_description:: autopydantic_settings
   :title: Show Undoc Members
   :path: target.configuration.SettingsUndocMembers
   :confpy: autodoc_pydantic_settings_undoc_members
   :directive_option: undoc-members
   :enable: members
   :values: True, False

   Show undocumented members. By default, undocumented members are hidden for
   standard :code:`auto` directives. For pydantic settings, this is overwritten
   if enabled.

.. note::

   In order to show any members at all, you need to enable
   :ref:`autodoc_pydantic_settings_members<autodoc_pydantic_settings_members>`
   or set :code:`:members:`.


.. config_description:: autopydantic_settings
   :title: Show Members
   :path: target.configuration.SettingsMembers
   :confpy: autodoc_pydantic_settings_members
   :directive_option: members
   :values: True, False

   Show members. By default, members are hidden for standard :code:`auto`
   directives. For pydantic settingss, this is overwritten if enabled.

.. config_description:: autopydantic_settings
   :title: Member Order
   :path: target.configuration.SettingsMemberOrder
   :confpy: autodoc_pydantic_settings_member_order
   :directive_option: member-order
   :enable: members, settings-show-config-member, settings-show-validator-members
   :values: groupwise, bysource, alphabetical

   Order members groupwise by default in the following order: fields,
   validators and config.


.. config_description:: autopydantic_settings
   :title: Hide ParamList
   :path: target.configuration.SettingsHideParamList
   :confpy: autodoc_pydantic_settings_hide_paramlist
   :directive_option: settings-hide-paramlist
   :values: True, False

   Hide parameter list within class signature which usually becomes rather
   overloaded once a lot fields are present. Additionally, it is redundant
   since fields are documented anyway.

.. config_description:: autopydantic_settings
   :title: Hide Reused Validators
   :path: target.configuration_settings_hide_reused_validator.SettingOne
   :example_path: target.configuration_settings_hide_reused_validator
   :confpy: autodoc_pydantic_settings_hide_reused_validator
   :directive_option: settings-hide-reused-validator
   :values: True, False
   :version: 1.8.0

   Hide class methods that are created while declaring functions as reusable
   validators. For more information and a detailed example, please see
   :ref:`the example page for reused validators <example_reused_validators>`.


.. config_description:: autopydantic_settings
   :title: Signature Prefix
   :path: target.configuration.SettingsSignaturePrefix
   :confpy: autodoc_pydantic_settings_signature_prefix
   :directive_option: settings-signature-prefix
   :values: pydantic settings, class, foobar

   Define the signature prefix for pydantic settings.


.. config_description:: autopydantic_settings
   :title: Show Schema JSON
   :path: target.configuration.SettingsShowJson
   :confpy: autodoc_pydantic_settings_show_json
   :directive_option: settings-show-json
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

**Configuration** *(added in version 1.4.0)*

:conf.py: *autodoc_pydantic_settings_show_json_error_strategy*

:directive_option: *settings-show-json-error-strategy*

**Available values:**

- ``coerce``: Keep violating fields in resulting schema but only show the title. Do not
  provide a warning during doc building process.
- ``warn`` (default): Keep violating fields in resulting schema but only show the title. Provide
  a warning during the doc building process.
- ``raise``: Raises an ``sphinx.errors.ExtensionError`` during building process.


------
Fields
------

.. config_description:: autopydantic_model
   :title: List Validators
   :path: target.configuration.FieldListValidators
   :confpy: autodoc_pydantic_field_list_validators
   :directive_option: field-list-validators
   :enable: members, field-doc-policy=docstring
   :values: True, False

   List all linked validators within doc string that process the current field.
   Hyperlinks to corresponding validators are automatically provided.


.. config_description:: autopydantic_model
   :title: Docstring Policy
   :path: target.configuration.FieldDocPolicy
   :confpy: autodoc_pydantic_field_doc_policy
   :directive_option: field-doc-policy
   :enable: members
   :values: docstring, description, both*

   Define what content is displayed in the main field docstring. The following
   values are possible:

   - **docstring** shows the exact docstring of the python attribute.
   - **description** displays the information provided via the pydantic field's description.
   - **both** will output the attribute's docstring together with the pydantic field's description.


.. config_description:: autopydantic_model
   :title: Show Constraints
   :path: target.configuration.FieldShowConstraints
   :confpy: autodoc_pydantic_field_show_constraints
   :directive_option: field-show-constraints
   :enable: members, field-doc-policy=docstring
   :values: True, False

   Displays all constraints that are associated with the given pydantic field.


.. config_description:: autopydantic_model
   :title: Show Alias
   :path: target.configuration.FieldShowAlias
   :confpy: autodoc_pydantic_field_show_alias
   :directive_option: field-show-alias
   :enable: members, field-doc-policy=docstring
   :values: True, False

   Provides the pydantic field's alias in the signature.


.. config_description:: autopydantic_model
   :title: Show Default Value
   :path: target.configuration.FieldShowDefault
   :confpy: autodoc_pydantic_field_show_default
   :directive_option: field-show-default
   :enable: members, field-doc-policy=docstring
   :values: True, False
   :version: 1.4.0

   Provides the pydantic field's default value in the signature. Unfortunately
   this is not provided by standard sphinx autodoc (as of version 4.5.0).


.. config_description:: autopydantic_model
   :title: Show Required
   :path: target.configuration.FieldShowRequired
   :confpy: autodoc_pydantic_field_show_required
   :directive_option: field-show-required
   :enable: members, field-show-default
   :values: True, False

   Add ``[Required]`` marker for all pydantic fields that do not have a default
   value. Otherwise, misleading ``None`` is displayed when
   :ref:`field-show-default <autodoc_pydantic_field_show_default>` is enabled.


.. config_description:: autopydantic_model
   :title: Show Optional
   :path: target.configuration.FieldShowOptional
   :confpy: autodoc_pydantic_field_show_optional
   :directive_option: field-show-optional
   :enable: members, field-show-default
   :values: True, False
   :version: 1.7.0

   Add ``[Optional]`` marker for all pydantic fields that have a
   ``default_factory``. Otherwise, misleading ``None`` is  displayed when
   :ref:`field-show-default <autodoc_pydantic_field_show_default>` is enabled.


.. config_description:: autopydantic_model
   :title: Swap Name and Alias
   :path: target.configuration.FieldSwapNameAndAlias
   :confpy: autodoc_pydantic_field_swap_name_and_alias
   :directive_option: field-swap-name-and-alias
   :enable: members, field-show-alias
   :values: False, True
   :version: 1.7.0

   Swaps field name with field alias. If
   :ref:`field-show-alias <autodoc_pydantic_field_show_alias>` is enabled,
   the original alias shows the actual field name instead.

   .. hint::

      Enabling this option will automatically interact with the following
      configurations by replacing the field name with the field alias:

      - :ref:`model-show-field-summary <autodoc_pydantic_model_show_field_summary>`
      - :ref:`model-show-validator-summary <autodoc_pydantic_model_show_validator_summary>`
      - :ref:`validator-replace-signature <autodoc_pydantic_validator_replace_signature>`
      - :ref:`validator-list-fields <autodoc_pydantic_validator_list_fields>`

      A complete example is provided :ref:`here <example_swap_name_with_alias>`.


.. config_description:: autopydantic_model
   :title: Signature Prefix
   :path: target.configuration.FieldSignaturePrefix
   :confpy: autodoc_pydantic_field_signature_prefix
   :directive_option: field-signature-prefix
   :enable: members, field-doc-policy=docstring
   :values: field, attribute, foobar

   Define the signature prefix for pydantic field.


----------
Validators
----------

.. config_description:: autopydantic_model
   :title: Replace Signature
   :path: target.configuration.ValidatorReplaceSignature
   :confpy: autodoc_pydantic_validator_replace_signature
   :directive_option: validator-replace-signature
   :enable: members, model-show-validator-members, undoc-members
   :values: True, False

   Replaces the validator signature with custom links to corresponding fields.
   Pydantic validator signatures usually do not carry important information and
   hence may be replaced. However, you may want to keep the signature patterns
   constant across methods. In this scenario, you may list the associated
   fields within the doc string via
   :ref:`validator-list-fields <autodoc_pydantic_validator_list_fields>`.


.. config_description:: autopydantic_model
   :title: List Fields
   :path: target.configuration.ValidatorListFields
   :confpy: autodoc_pydantic_validator_list_fields
   :directive_option: validator-list-fields
   :enable: members, model-show-validator-members, undoc-members
   :values: True, False*

   List all fields that are processed by current validator.
   This provides the same information as
   :ref:`validator-replace-signature <autodoc_pydantic_validator_replace_signature>`,
   however it does not change the signature but adds the links in the doc
   string.


.. config_description:: autopydantic_model
   :title: Signature Prefix
   :path: target.configuration.ValidatorSignaturePrefix
   :confpy: autodoc_pydantic_validator_signature_prefix
   :directive_option: validator-signature-prefix
   :enable: members, model-show-validator-members, undoc-members
   :values: validator, classmethod, foobar

   Define the signature prefix for pydantic validator.


-------
General
-------

.. _autodoc_pydantic_add_fallback_css_class:

Add Fallback CSS Class
~~~~~~~~~~~~~~~~~~~~~~

Adds fallback css classes for HTML content generated by **autodoc_pydantic**
to prevent breaking themes which rely on the standard sphinx autodoc
``objtype`` css classes.

More concretely, the following auto-documenter directives gain the following
css fallback classes:

- pydantic_model -> class
- pydantic_settings -> class
- pydantic_field -> attribute
- pydantic_validator -> method
- pydantic_config -> class

For more, please see the corresponding :ref:`FAQ<faq_add_fallback_css_class>`
section.

**Configuration** *(added in version 1.6.0)*

:conf.py: *autodoc_pydantic_add_fallback_css_class*

**Available values:**

- ``True`` (default): Add fallback CSS classes.
- ``False``: Do not add fallback CSS classes.

.. note::

   Sphinx versions prior ``4.0.0`` did not include the ``objtype`` as a default
   css class for the corresponding docutil nodes. **autodoc_pydantic** will
   add the ``objtype`` as a css class for its generated output for older sphinx
   versions, too.
