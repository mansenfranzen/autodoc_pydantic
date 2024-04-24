========
Examples
========

Configurations
==============

While the :doc:`configuration` documentation contains all available options in
detail, this page shows them in conjunction to provide different examples on how to
display pydantic models and settings.

.. _showcase:

-------
Default
-------

This example shows the default out-of-the-box configuration of **autodoc_pydantic**.
In contrast, it also shows how standard sphinx autodoc displays the same example code.

.. tabs::

   .. tab:: *output autodoc_pydantic*

      .. autopydantic_settings:: target.example_setting.ExampleSettings

   .. tab:: *output default sphinx*

      .. autopydantic_settings:: target.example_setting.ExampleSettings
         :members:
         :undoc-members:
         :__doc_disable_except__: members, undoc-members, settings-show-validator-members
         :noindex:

   .. tab:: python

      .. autocodeblock:: target.example_setting

   .. tab:: reST

      .. code-block::

         .. autopydantic_settings:: target.example_setting.ExampleSettings


----------------------------
Entity-Relationship Diagram
----------------------------

This example shows the rendered output of a pydantic model including an Entity-Relationship Diagram.


.. tabs::

   .. tab:: *rendered output*

      .. autopydantic_model:: target.example_erdantic.Order
         :noindex:
         :model-erdantic-figure: True
         :model-erdantic-figure-collapsed: False

   .. tab:: reST

      .. code-block::

         .. autopydantic_model:: target.example_erdantic.Order
            :model-erdantic-figure: True
            :model-erdantic-figure-collapsed: False

   .. tab:: python

      .. autocodeblock:: target.example_erdantic


-----------
Fields only
-----------

In this scenario everything is hidden except actual pydantic fields. Validators
and model/setting config is hidden.

.. tabs::

   .. tab:: *rendered output*

      .. autopydantic_settings:: target.example_setting.ExampleSettings
         :noindex:
         :settings-show-json: False
         :settings-show-config-summary: False
         :settings-show-validator-members: False
         :settings-show-validator-summary: False
         :field-list-validators: False


   .. tab:: reST

      .. code-block::

         .. autopydantic_settings:: target.example_setting.ExampleSettings
            :settings-show-json: False
            :settings-show-config-summary: False
            :settings-show-validator-members: False
            :settings-show-validator-summary: False
            :field-list-validators: False

   .. tab:: python

      .. autocodeblock:: target.example_setting


Specifics
=========

This section focuses rendered documentation examples of pydantic specific
concepts such as model validators, required/optional fields or generic models.

----------------
Model validators
----------------

This example highlights how `model validators <https://docs.pydantic.dev/latest/usage/validators/#model-validators>`_
(``@model_validator`` or ``@field_validator('*')``) are represented. Since they
validate all fields, their corresponding field reference is replaced with a
simple ``all fields`` marker which hyperlinks to the related model itself.

.. tabs::

   .. tab:: *rendered output*

      .. autopydantic_model:: target.example_validators.ExampleValidators

   .. tab:: reST

      .. code-block::

         .. autopydantic_model:: target.example_validators.ExampleValidators

   .. tab:: python

      .. autocodeblock:: target.example_validators


.. note::

   By default the function signature of validators is replaced with hyperlinks
   to validated fields by **autodoc_pydantic**. You can disable this behaviour
   via :ref:`validator-replace-signature <autodoc_pydantic_validator_replace_signature>`.


------------------------
Required/Optional fields
------------------------

Pydantic has different ways to represent required or optional fields as
described in the `official documentation <https://pydantic-docs.helpmanual.io/usage/models/#required-optional-fields>`_ .
The following example outlines all available combinations with the default
**autodoc_pydantic** settings:

.. tabs::

   .. tab:: *rendered output*

      .. autopydantic_model:: target.example_required_optional_fields.RequiredOptionalField
         :member-order: bysource
         :model-summary-list-order: bysource

   .. tab:: reST

      .. code-block::

         .. autopydantic_model:: target.example_required_optional_fields.RequiredOptionalField
            :member-order: bysource
            :model-summary-list-order: bysource

   .. tab:: python

      .. autocodeblock:: target.example_required_optional_fields

.. _example_swap_name_with_alias:

--------------------------
Swap field name with alias
--------------------------

It is possible to completely replace the field name with the provided field
alias when :ref:`field-swap-name-and-alias <autodoc_pydantic_field_swap_name_and_alias>`
is enabled:

.. tabs::

   .. tab:: *rendered output with swap*

      .. autopydantic_model:: target.example_swap_name_with_alias.SwapFieldWithAlias
         :field-swap-name-and-alias:
         :validator-list-fields:

   .. tab:: *rendered output without swap*

      .. autopydantic_model:: target.example_swap_name_with_alias.SwapFieldWithAlias
         :validator-list-fields:
         :noindex:

   .. tab:: reST

      .. code-block::

         .. autopydantic_model:: target.example_swap_name_with_alias.SwapFieldWithAlias
            :field-swap-name-and-alias:
            :validator-list-fields:

   .. tab:: python

      .. autocodeblock:: target.example_swap_name_with_alias

--------------
Generic Models
--------------

Generic pydantic models can be documented just as normal models, too. The
following example is borrowed from the official pydantic documentation for
`generic models <https://pydantic-docs.helpmanual.io/usage/models/#generic-models>`_ :

.. tabs::

   .. tab:: *rendered output*

      .. automodule:: target.example_generics
         :members:

   .. tab:: reST

      .. code-block::

         .. automodule:: target.example_generics
            :members:

   .. tab:: python

      .. autocodeblock:: target.example_generics


.. _example_reused_validators:

-----------------
Reused Validators
-----------------

Functions can be declared as
`reusable validators <https://pydantic-docs.helpmanual.io/usage/validators/#reuse-validators>`_
for pydantic models. Unlike normal validators which are bound methods, a
reusable validator is an actual function. Therefore, the function should be
referenced and linked with corresponding pydantic fields in the generated
documentation.

While declaring a reusable validator, a class method is automatically created
for the pydantic model that conveys no meaningful information. Hence it can be
hidden in the documentation via
:ref:`model-hide-resued-validator <autodoc_pydantic_model_hide_reused_validator>`.

The following example is borrowed from the official pydantic documentation for
`reused validators <https://pydantic-docs.helpmanual.io/usage/validators/#reuse-validators>`_
which shows how the reused function is correctly linked within the
:ref:`model's validator summary <autodoc_pydantic_model_show_validator_summary>`
and the
:ref:`fields validator's list <autodoc_pydantic_field_list_validators>`:

.. tabs::

   .. tab:: *rendered output with hiding*

      .. autofunction:: target.example_reused_validators.normalize

      .. autopydantic_model:: target.example_reused_validators.Consumer

      .. autopydantic_model:: target.example_reused_validators.Producer



   .. tab:: *rendered output without hiding*

      .. autofunction:: target.example_reused_validators.normalize
         :noindex:

      .. autopydantic_model:: target.example_reused_validators.Consumer
         :model-hide-reused-validator: false
         :noindex:

      .. autopydantic_model:: target.example_reused_validators.Producer
         :model-hide-reused-validator: false
         :noindex:

   .. tab:: reST

      .. code-block::

         .. automodule:: target.example_reused_validators
            :members:
            :undoc-members:

   .. tab:: python

      .. autocodeblock:: target.example_reused_validators
