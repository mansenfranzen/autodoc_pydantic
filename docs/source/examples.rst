========
Examples
========

While the :doc:`configuration` documentation contains all available options in
detail, this page shows them in cooperation to provide different examples on how to
display pydantic models and settings.

.. _showcase:

Default configuration
=====================

This example shows the default out-of-the-box configuration of *autodoc_pydantic*.
In contrast, it also shows how standard sphinx autodoc displays the same code.

.. tabs::

   .. tab:: autodoc pydantic

      .. autopydantic_settings:: target.example_setting.ExampleSettings

   .. tab:: autodoc sphinx

      .. autopydantic_settings:: target.example_setting.ExampleSettings
         :members:
         :undoc-members:
         :__doc_disable_except__: members, undoc-members, settings-show-validator-members, settings-show-config-member, config-members
         :noindex:

   .. tab:: *example code*

      .. autocodeblock:: target.example_setting
