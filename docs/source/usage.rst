.. _sphinx.ext.autosummary: https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html
.. _sphinx.ext.autodoc: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
.. _sphinx issue 6264: https://github.com/sphinx-doc/sphinx/issues/6264

=====
Usage
=====

*autodoc_pydantic* integrates seamlessly with sphinx' auto documentation
utilities. Therefore, you might not need to modify your code at all when
using :code:`autosummary` and :code:`automodule` directives.

autosummary
===========

Using the :code:`autosummary` directive of the `sphinx.ext.autosummary`_
extension allows to create a table of contents. Each entry corresponds to a
python object to be documented (including pydantic models/settings) for which
individual documentation pages (called stubs) can be automatically generated:

.. tabs::

   .. tab:: reST

      .. code-block:: rest

         .. autosummary::
            :toctree: _autosummary

            target.example_autosummary.AutoSummaryModel
            target.example_autosummary.AutoSummarySettings

   .. tab:: rendered output

      .. autosummary::
         :toctree: _autosummary

         target.example_autosummary.AutoSummaryModel
         target.example_autosummary.AutoSummarySettings

   .. tab:: source code

      .. autocodeblock:: target.example_autosummary

.. hint::

   To automatically generate stubs for all autosummary entries, a few things
   have to be done:

   - Add the :code:`sphinx.ext.autosummary` extension in :code:`conf.py`.
   - Set :code:`autosummary_generate = True` in :code:`conf.py`.
   - Add :code:`:toctree:` option to the autosummary directive.

   For more information, please visit the official documentation of
   `sphinx.ext.autosummary`_.

.. warning::

   The generated stub pages do not follow the standard autosummary templates
   (e.g. the class template which lists all methods and attributes). Currently
   as of Sphinx 3.5.4, this is not possible because autosummary does not support
   custom autodocumenters provided by extensions such as *autodoc_pydantic*
   (see also `sphinx issue 6264`_). Instead, *autodoc_pydantic*'s
   autodocumenters are used to render the object's documentation in the
   generated stub pages of autosummary.

automodule
==========

One may wants to document the content of an entire module via the
:code:`automodule` directive of the `sphinx.ext.autodoc`_ extension. The
documentation of all pydantic objects is directly passed to
*autodoc_pydantic*'s auto documenters:

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


autopydantic
============

You may want to document pydantic objects directly. This is possible via the
specialized directives provided by *autodoc_pydantic*:

- :ref:`autopydantic_model`
- :ref:`autopydantic_settings`
- :ref:`autopydantic_field`
- :ref:`autopydantic_validator`
- :ref:`autopydantic_config`

.. _autopydantic_model:

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

      .. autocodeblock:: target.example_model

To overwrite global defaults, the following directive options can be supplied:

.. configtoc:: model

.. _autopydantic_settings:

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

.. _autopydantic_field:

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


.. _autopydantic_validator:

autopydantic_validator
----------------------

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

.. _autopydantic_config:

autopydantic_config
-------------------

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
