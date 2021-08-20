.. _sphinx.ext.autosummary: https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html
.. _sphinx.ext.autodoc: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
.. _sphinx issue 6264: https://github.com/sphinx-doc/sphinx/issues/6264

=====
Usage
=====

**autodoc_pydantic** integrates seamlessly with sphinx' auto-documentation
utilities. You might not need to modify your code at all when
using :code:`automodule` or :code:`autosummary` directives.

automodule
==========

The :code:`automodule` directive of the `sphinx.ext.autodoc`_ extension
documents the content of an entire python module. All pydantic objects that
are encountered will be documented by *autodoc_pydantic*'s specialized
auto-documenters:

.. tabs::

   .. tab:: reST

      .. code-block:: rest

         .. automodule:: target.example_setting
            :members:

   .. tab:: *rendered output*

      .. automodule:: target.example_setting
         :members:
         :noindex:

   .. tab:: python

      .. autocodeblock:: target.example_setting

autosummary
===========

The :code:`autosummary` directive of the `sphinx.ext.autosummary`_
extension generates a table of references and short descriptions for a list of
python objects. Additionally, it can automatically generate individual
documentation pages (called stubs) for each entry. This makes it fairly easy to
sufficiently document several python objects at once:

.. tabs::

   .. tab:: reST

      .. code-block:: rest

         .. currentmodule:: target.example_autosummary

         .. autosummary::
            :toctree: _autosummary

            AutoSummaryModel
            AutoSummarySettings

   .. tab:: *rendered output*

      .. currentmodule:: target.example_autosummary

      .. autosummary::
         :toctree: _autosummary

         AutoSummaryModel
         AutoSummarySettings

   .. tab:: python

      .. autocodeblock:: target.example_autosummary

Please note, this example generates the autosummary table with hyperlinks to
the corresponding stub pages.

.. hint::

   To enable automatic stub generation, remember the following steps:

   - Add the :code:`sphinx.ext.autosummary` extension in *conf.py*.
   - Set :code:`autosummary_generate = True` in *conf.py*.
   - Add :code:`:toctree:` option to the autosummary directive.

   For more information, please visit the official documentation of
   `sphinx.ext.autosummary`_.

.. warning::

   The generated stub pages do not use the standard autosummary templates
   (e.g. the class template which lists all methods and attributes).
   As of sphinx version 3.5.4, this is not possible because autosummary does not support
   custom autodocumenters provided by extensions such as *autodoc_pydantic*
   (see `sphinx issue 6264`_). Instead, *autodoc_pydantic*'s
   autodocumenters are used to render the object's documentation in the
   generated stub pages of autosummary.


autopydantic
============

You may want to document pydantic objects explicitly. This is possible via the
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
like :code:`:members:` to show all members. Instead, **autodoc_pydantic** supplies
sensible default settings.

.. tabs::

   .. tab:: reST

      .. code-block:: rest

         .. autopydantic_model:: target.example_model.ExampleModel

   .. tab:: *rendered output*

      .. autopydantic_model:: target.example_model.ExampleModel
         :noindex:

   .. tab:: python

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

   .. tab:: *rendered output*

      .. autopydantic_settings:: target.example_setting.ExampleSettings
         :noindex:

   .. tab:: python

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

   .. tab:: *rendered output*

      .. autopydantic_field:: target.example_setting.ExampleSettings.field_with_constraints_and_description
         :noindex:

   .. tab:: python

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

   .. tab:: *rendered output*

      .. autopydantic_validator:: target.example_setting.ExampleSettings.check_max_length_ten
         :noindex:

   .. tab:: python

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

   .. tab:: *rendered output*

      .. autopydantic_config:: target.example_setting.ExampleSettings.Config
         :noindex:

   .. tab:: python

      .. autocodeblock:: target.example_setting

To overwrite global defaults, the following directive options can be supplied:

.. configtoc:: config
