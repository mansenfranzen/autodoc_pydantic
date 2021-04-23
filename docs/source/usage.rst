=====
Usage
=====

Autodoc Sphinx
==============

*autodoc_pydantic* integrates seamlessly with sphinx' autodoc. Therefore, you
might not need to modify your code at all when using :code:`automodule`.

automodule
----------

In this case, autodoc passes the documentation of all pydantic objects directly to
*autodoc_pydantic*:

.. tabs::

   .. tab:: reST

      .. code-block:: rest

         .. automodule:: target.example_setting
            :members:

   .. tab:: rendered output

      .. automodule:: target.example_setting
         :members:
         :noindex:

   .. tab:: source code

      .. autocodeblock:: target.example_setting


Autodoc Pydantic
================

If you don't want to rely on the :code:`automodule` directive, *autodoc_pydantic*
adds custom directives for pydantic models, settings, fields, validators and config class.

To completely customize a specific directive, you can use all available directive
options, as explained in detail in the :doc:`configuration` section.

autopydantic_model
------------------

In comparison the :code:`automodule`, you don't need to add directive options
like :code:`:members:` to show all members. Instead, *autodoc_pydantic* supplies
sensible default settings.

.. tabs::

   .. tab:: reST

      .. code-block:: rest

         .. autopydantic_model:: target.example_model.ExampleModel

   .. tab:: rendered output

      .. autopydantic_model:: target.example_model.ExampleModel
         :noindex:

   .. tab:: source code

      .. autocodeblock:: target.example_setting

To overwrite global defaults, the following directive options can be supplied:

.. configtoc:: model


autopydantic_settings
---------------------

Documenting pydantic models behaves exactly like :code:`autopydantic_model`.

.. tabs::

   .. tab:: reST

      .. code-block:: rest

         .. autopydantic_settings:: target.example_setting.ExampleSettings

   .. tab:: rendered output

      .. autopydantic_settings:: target.example_setting.ExampleSettings
         :noindex:

   .. tab:: source code

      .. autocodeblock:: target.example_setting

To overwrite global defaults, the following directive options can be supplied:

.. configtoc:: settings


autopydantic_field
------------------

In some rare cases, you may want to document individual pydantic fields. In most cases,
pydantic fields are documented along with its corresponding pydantic model/setting.

.. tabs::

   .. tab:: reST

      .. code-block:: rest

         .. autopydantic_field:: target.example_setting.ExampleSettings.field_with_constraints_and_description

   .. tab:: rendered output

      .. autopydantic_field:: target.example_setting.ExampleSettings.field_with_constraints_and_description
         :noindex:

   .. tab:: source code

      .. autocodeblock:: target.example_setting

To overwrite global defaults, the following directive options can be supplied:

.. configtoc:: field


autopydantic_validator
-------------------------

As with pydantic validators, one usually does not document validators separately
from its corresponding pydantic model/settings but it is still possible.

.. tabs::

   .. tab:: reST

      .. code-block:: rest

         .. autopydantic_validator:: target.example_setting.ExampleSettings.check_max_length_ten

   .. tab:: rendered output

      .. autopydantic_validator:: target.example_setting.ExampleSettings.check_max_length_ten
         :noindex:

   .. tab:: source code

      .. autocodeblock:: target.example_setting

To overwrite global defaults, the following directive options can be supplied:

.. configtoc:: validator


autopydantic_config
----------------------

Very rarely, you may want to document a pydantic config class without the corresponding
pydantic model/setting. However, technically it's possible since the :code:`autopydantic_config`
directive is used by the :code:`autopydantic_model` and :code:`autopydantic_settings`.

.. tabs::

   .. tab:: reST

      .. code-block:: rest

         .. autopydantic_config:: target.example_setting.ExampleSettings.Config

   .. tab:: rendered output

      .. autopydantic_config:: target.example_setting.ExampleSettings.Config
         :noindex:

   .. tab:: source code

      .. autocodeblock:: target.example_setting

To overwrite global defaults, the following directive options can be supplied:

.. configtoc:: config