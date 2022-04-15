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

   .. tab:: *rendered output pydantic*

      .. autopydantic_settings:: target.example_setting.ExampleSettings

   .. tab:: *rendered output sphinx*

      .. autopydantic_settings:: target.example_setting.ExampleSettings
         :members:
         :undoc-members:
         :__doc_disable_except__: members, undoc-members, settings-show-validator-members, settings-show-config-member, config-members
         :noindex:

   .. tab:: python

      .. autocodeblock:: target.example_setting

   .. tab:: reST

      .. code-block::

         .. autopydantic_settings:: target.example_setting.ExampleSettings


--------
Complete
--------

This example represents a rendered output for which all features are enabled.
It deviates from the default configuration above because it contains redundant
information which is most likely not required. However, for demonstration purposes,
this scenario covers all available display options for pydantic models/settings.


.. tabs::

   .. tab:: *rendered output*

      .. autopydantic_settings:: target.example_setting.ExampleSettings
         :noindex:
         :settings-show-config-member: True
         :validator-list-fields: True

   .. tab:: reST

      .. code-block::

         .. autopydantic_settings:: target.example_setting.ExampleSettings
            :noindex:
            :settings-show-config-member: True
            :validator-list-fields: True

   .. tab:: python

      .. autocodeblock:: target.example_setting


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
         :settings-show-config-member: False
         :settings-show-config-summary: False
         :settings-show-validator-members: False
         :settings-show-validator-summary: False
         :field-list-validators: False


   .. tab:: reST

      .. code-block::

         .. autopydantic_settings:: target.example_setting.ExampleSettings
            :settings-show-json: False
            :settings-show-config-member: False
            :settings-show-config-summary: False
            :settings-show-validator-members: False
            :settings-show-validator-summary: False
            :field-list-validators: False

   .. tab:: python

      .. autocodeblock:: target.example_setting


Specifics
=========

This section focuses rendered documentation examples of pydantic specific
concepts such as root validators, required/optional fields or generic models.

----------------------------
Asterisk and root validators
----------------------------

This example highlights how `asterisk <https://pydantic-docs.helpmanual.io/usage/validators/#pre-and-per-item-validators>`_
(``@validator('*')``) and `root validators <https://pydantic-docs.helpmanual.io/usage/validators/#root-validators>`_ (``@root_validator``)
are represented. Since they validate all fields, their corresponding field reference is replaced
with a simple ``all fields`` marker which hyperlinks to the related model itself.

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
The following example outlines all available combinations:

.. tabs::

   .. tab:: *rendered output*

      .. automodule:: target.example_required_optional_fields
         :members:

   .. tab:: reST

      .. code-block::

         .. automodule:: target.example_required_optional_fields
            :members:

   .. tab:: python

      .. autocodeblock:: target.example_required_optional_fields

--------------
Generic Models
--------------

Generic pydantic models can be documented just as normal models, too. The
following example is borrowed from the official
`pydantic documentation <https://pydantic-docs.helpmanual.io/usage/models/#generic-models>`_ :

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