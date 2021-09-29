======
Guides
======

The following sections are specific to **autodoc_pydantic**'s implementation details and build upon previous understanding covered in the developers :ref:`explanation`. It is recommended to start there first before continuing here.

-------------------
Adding new features
-------------------

This section describes how **autodoc_pydantic** can be extended to support new features. As an example, we will cover the process of implementing an explicit sort order for summary lists which was added in version 1.5.0.

Adding a new feature requires several related steps which are divided in the following topics:

1. Provide rationale
2. Specify the feature
2. Derive and create tests
3. Add configuration settings
4. Implement required behavior
5. Update documentation

1. Provide rationale
====================

A summary list is an enumeration with references to all available fields or validators. If enabled, it is appended to the doc string of the model (see examples for ``model_show_validator_summary`` and ``model_show_field_summary``). 

Prior to version 1.5.0, summary lists for validators and fields were already supported. However, their sort order was not explicitly defined and could not be configured. Even worse, the sort order was arbitrary and may have varied between python versions (e.g. dicts being ordered vs. unordered). 

Depending on one's requirement, sort order should be either alphabetically or given by source. This is analogous to how ``member_order`` can be configured in sphinx.

2. Specify the feature
======================

- Summary list order applies to pydantic models and pydantic settings. 
- It affects the sort order of both field and validator summary lists. 
- Two sort options are available:
    1. Alphabetically - use alphabetical order
    2. By source - use order given in source code
- Define option names

1. Add global configuration option to ``__init__.py``


One of **autodoc_pydantic** main strengths is its configurability. Each feature can be globally (affecting all pydantic objects via ``conf.py``) and locally (affecting only single directive via directive options) enabled or disabled. Hence, new features that change the default appearence or content of standard sphinx autodoc should be configurable, too.

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
