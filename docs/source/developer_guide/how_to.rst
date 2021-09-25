======
Guides
======

-------------------
Adding new features
-------------------

This section describes how **autodoc_pydantic** can be extended to support new features. As an example, we will cover the process of implementing an explicit sort order for summary lists. A summary list is an enumeration with references to all available fields or validators which is appended to the doc string  of the model (see examples for ``model_show_validator_summary`` and ``model_show_field_summary``). Prior to version 1.5.0, summary lists for validators and fields were already supported. However, their sort order was not explicitly defined and could not be configured. 

One of **autodoc_pydantic** main strengths is its configurability. Each feature can be globally (affecting all pydantic objects via ``conf.py``) and locally (affecting only single directive via directive options) enabled or disabled. Hence, new features that change the default appearence or content of standard sphinx autodoc should be configurable, too.

This section describes how to add an explicit sort order for summary lists of pydantic models and settings. It serves as an example on how to add new feature.

More concretely, **autodoc_pydantic** may add summary lists for pydantic validators and fields via ``model_show_validator_summary`` and ``model_show_field_summary``, respectively. Those summary lists require a specific sort order. Intuitively, there are two main choices. First, sort fields or validators alphabetically. Second, keep the order given by source.

The following steps are required:

1. Add global configuration option to ``__init__.py``

First, we need to register a new global configuration option which will be configurable from the ``conf.py``. For our case, we are going to add the following to the function ``add_configuration_values``:

.. code-block:: python

   add(f'{stem}settings_summary_list_order', summary_list_order, True, str)
   add(f'{stem}model_summary_list_order', summary_list_order, True, str)

2. Add local configuruation option to ``autodoc.py``

Second, we want to allow our pydantic auto-documenters to accept directive options to overwrite globally set options. In this example, we need to modify ``OPTION_SPEC_MODEL`` and ``OPTION_SPEC_SETTINGS`` since pydantic models and settings are the configuration target. The ``OPTION_SPEC`` dictionaries contain all available directive options and their corresponding option validator functions:

.. code-block:: python

   OPTION_SPEC_SETTINGS = {

      # ...

      "settings-summary-list-order": option_one_of_factory(
         OptionsSummaryListOrder.values()
      ),

      # ...

   }


   OPTION_SPEC_MODEL = {

      # ...

      "model-summary-list-order": option_one_of_factory(
         OptionsSummaryListOrder.values()
      ),

      # ...

   }

3. Add test-cases
