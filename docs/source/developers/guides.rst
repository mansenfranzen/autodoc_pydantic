======
Guides
======

This page provides guides for developers regarding explanations and hands on
walkthroughs.

It contains lots of implementation details and builds upon previous knowledge
covered in the developers :ref:`design <expl_design>` explanation. It is
recommended to start there first before continuing here.

.. _understanding_autodocumenters:

------------------------------
Understanding auto-documenters
------------------------------

Auto-documenters typically inspect a python object and generate corresponding
reStructuredText (reST). The reST contains calls to sphinx directives, roles
and so on and is in turn converted docutils nodes. The docutil nodes are then
consumed by different builders to create the corresponding output (e.g. PDF, HTML).

An auto-documenter is not a sphinx directive in the first place because it does
not generate docutil nodes. Instead as mentioned above, it creates reST
(see auto-documenters |Documenter|_ base class and its |generate|_ method).
But how is the reST finally converted into docutil nodes?

When registering an auto-documenter to the sphinx application via
|app.add_autodocumenter|_, it is wrapped with the generic |AutodocDirective|_.
This directive executes the auto-documenter, retrieves its reST and then
converts the reST into docutils via the magic |parse_generated_content|_.

.. mermaid:: mermaid/autodocumenter.mmd

The interesting part is how a given reST is converted into docutils nodes
because this turns out to be very useful for different use cases when writing
custom directives.

Writing your own directives outputting docutil nodes is rather low level and
harder to learn in comparison to directives which can create arbitrary high
level reST that then will be converted to docutil nodes generically.

For example, part of **autodoc_pydantic**'s documentation is using this
functionality to handle repetitive and error prone tasks (see ``TabDocDirective``).


.. |Documenter| replace:: ``Documenter``
.. _Documenter: https://github.com/sphinx-doc/sphinx/blob/37730d0f8ed250b019f78701056308b25535e3c9/sphinx/ext/autodoc/__init__.py#L299

.. |generate| replace:: ``generate``
.. _generate: https://github.com/sphinx-doc/sphinx/blob/37730d0f8ed250b019f78701056308b25535e3c9/sphinx/ext/autodoc/__init__.py#L893

.. |app.add_autodocumenter| replace:: ``app.add_autodocumenter``
.. _app.add_autodocumenter: https://github.com/sphinx-doc/sphinx/blob/37730d0f8ed250b019f78701056308b25535e3c9/sphinx/application.py#L1085

.. |AutodocDirective| replace:: ``AutodocDirective``
.. _AutodocDirective: https://github.com/sphinx-doc/sphinx/blob/37730d0f8ed250b019f78701056308b25535e3c9/sphinx/ext/autodoc/directive.py#L125

.. |parse_generated_content| replace:: ``parse_generated_content``
.. _parse_generated_content: https://github.com/sphinx-doc/sphinx/blob/37730d0f8ed250b019f78701056308b25535e3c9/sphinx/ext/autodoc/directive.py#L108

-------------------
Adding new features
-------------------

This section describes how **autodoc_pydantic** can be extended to support new
features. As an example, we will cover the process of implementing an explicit
sort order for summary lists which was added in version 1.5.0.

Adding a new feature requires several related steps which are divided in the following topics:

1. **Provide rationale**: Shortly describe the feature. Reason why this feature
   should be added and what issue it solves. Compare the complexity and maintenance
   burden it adds in contrast to the value it provides.

2. **Specify the feature**: Depict the feature in very detail. Describe it's
   exact behaviour. Provide configuration names.

3. **Derive tests**: Translate the feature's specification into
   test cases to ensure that the implementation works as expected.

4. **Add configuration settings**: Register local and global configuration
   settings.

5. **Implement required behavior**: Finally add the actual implementation to the
   existing code base until tests pass.

6. **Update documentation**: Describe the new feature adding it to the
   :ref:`configuration <configuration>` page.

1. Provide rationale
====================

A summary list is an enumeration with references to all available fields or
validators. If enabled, it is appended to the doc string of the model
(see examples for :ref:`model-show-validator-summary <autodoc_pydantic_model_show_validator_summary>`
and :ref:`model-show-field-summary <autodoc_pydantic_model_show_field_summary>`).

Prior to version 1.5.0, summary lists for validators and fields were already
supported. However, their sort order was not explicitly defined and could not be
configured. Even worse, the sort order was arbitrary and may have varied between
python versions (e.g. dicts being ordered vs. unordered).

Depending on one's requirement, sort order should be either alphabetically or
given by source. This is analogous to how ``member_order`` can be configured in
sphinx.

2. Specify the feature
======================

- Summary list order applies to pydantic models and pydantic settings.

- Two configurations are added accordingly:

    - ``model-show-field-summary``
    - ``settings-show-field-summary``

- Configurations accept two possible values:

    - ``alphabetical`` - sort items alphabetically
    - ``bysource`` - use order given in source code

- It affects both the sort order for field and validator summary lists.

3. Derive tests
===============

With the above specification, test cases can be formulated.

Example model
-------------

In order to test the feature, there needs to be a pydantic model to generate
testable reST from in the first place. Therefore, let's create an exemplary model
which allows to check for the correct implementation of summary list orders.
This requires at least two pydantic fields and validators to be sortable.

.. code-block:: python
   :caption: tests/roots/test-base/target/configuration.py

   class ModelSummaryListOrder(BaseModel):
       """ModelSummaryListOrder."""

       field_b: int = 1
       field_a: int = 1

       @field_validator("field_b")
       def validate_b(cls, v):
           return v

       @field_validator("field_a")
       def validate_a(cls, v):
           return v

Test implementation
-------------------

Testing auto-documenters in sphinx comes with some complexity. An auto-documenter
generates reST. Hence, the generated reST has to be tested. Manually creating the correct
reST output is far from being easy and requires some practice. As an example, let's
assume we test for alphabetical order. The correct reST for the above exemplary
model is as follows:

.. code-block:: python
   :caption: tests/test_configuration_model.py

   result = [
   '',
   '.. py:pydantic_model:: ModelSummaryListOrder',
   '   :module: target.configuration',
   '',
   '   ModelSummaryListOrder.',
   '',
   '   :Fields:',
   '      - :py:obj:`field_a (int) <target.configuration.ModelSummaryListOrder.field_a>`',
   '      - :py:obj:`field_b (int) <target.configuration.ModelSummaryListOrder.field_b>`',
   '',
   '   :Validators:',
   '      - :py:obj:`validate_a <target.configuration.ModelSummaryListOrder.validate_a>` » :py:obj:`field_a <target.configuration.ModelSummaryListOrder.field_a>`',
   '      - :py:obj:`validate_b <target.configuration.ModelSummaryListOrder.validate_b>` » :py:obj:`field_b <target.configuration.ModelSummaryListOrder.field_b>`',
   ''
   ]

.. tip::

   In most cases it's a reasonable approach to generate the reST with the
   ``autodocument`` fixture (as described below) in the first place and then
   confirm it's validity manually afterwards.

Next, we need to instantiate and invoke the auto-documenter on the exemplary model
to retrieve the generated reST from the auto-documenter. Unfortunately, this requires
a sophisticated test setup. This includes running a sphinx test application
while loading an exemplary sphinx source directory containing the
examplary model. Luckily, sphinx' test suite and its adoption in **autodoc_pydantic**
provides a pytest fixture named ``autodocument`` to abstract away all of this
complexity. Consider the following test invocation:

.. code-block:: python
   :caption: tests/test_configuration_model.py

   def test_autodoc_pydantic_model_summary_list_order_alphabetical(autodocument):

       # explict global
       actual = autodocument(
           documenter='pydantic_model',
           object_path='target.configuration.ModelSummaryListOrder',
           options_app={
               "autodoc_pydantic_model_show_validator_summary": True,
               "autodoc_pydantic_model_show_field_summary": True,
               "autodoc_pydantic_model_summary_list_order": "alphabetical"},
           deactivate_all=True)
       assert result == actual

Essentially, the ``autodocument`` fixture invokes the ``pydantic_model``
auto-documenter on the example model ``target.configuration.ModelSummaryListOrder``
while injecting global and local configuration settings. Finally, it returns the
generated reST ``actual`` which is compared to the manually created ``result`` reST from
above.

Please notice how the ``autodocument`` fixture is used with its various parameters:

:documenter: Identifies the auto-documenter used to generate reST.
:object_path: Defines the path to the mocked model to be tested.
:options_app: Injects global configuration settings to ``conf.py``.
:options_doc: Provides local configuration settings as directive options.
:deactivate_all: If enabled, it deactivates all of **autodoc_pydantic**'s
  features to simplify the complexity of the resulting reST and to isolate
  the tested feature.

Using the fixture allows to test for more scenarios within the same test case.
For example, we want to check for providing local settings only or check for
local settings to overwrite global settings:

.. code-block:: python
   :caption: tests/test_configuration_model.py

   def test_autodoc_pydantic_model_summary_list_order_alphabetical(autodocument):

       # explict local
       actual = autodocument(
           documenter='pydantic_model',
           object_path='target.configuration.ModelSummaryListOrder',
           options_app={"autodoc_pydantic_model_show_validator_summary": True,
                        "autodoc_pydantic_model_show_field_summary": True},
           options_doc={"model-summary-list-order": "alphabetical"},
           deactivate_all=True)
       assert result == actual

       # explicit local overwrite global
       actual = autodocument(
           documenter='pydantic_model',
           object_path='target.configuration.ModelSummaryListOrder',
           options_app={"autodoc_pydantic_model_show_validator_summary": True,
                        "autodoc_pydantic_model_show_field_summary": True,
                        "autodoc_pydantic_model_summary_list_order": "bysource"},
           options_doc={"model-summary-list-order": "alphabetical"},
           deactivate_all=True)
       assert result == actual

Don't worry if several things still remain unclear. It takes some time to get
your head around. It's best to test around with some dummy class and see how
``autodocument`` generates reST.

.. note::

   The ``options_app`` parameter of the ``autodocument`` fixture activates the
   ``autodoc_pydantic_model_show_validator_summary`` and
   ``autodoc_pydantic_model_show_field_summary`` options. This is required
   because the summary lists would not show up otherwise which in turn would
   prevent testing the summary list order in the first place.

4. Add configuration settings
=============================

One of **autodoc_pydantic** main strengths is its configurability. Each feature
can be enabled/disabled on two levels:

- **globally**: affecting all pydantic objects via ``conf.py``
- **locally**: affecting only a single directive via directive options

Hence, new features that change the default appearance of standard sphinx
autodoc should be configurable, too.

.. hint::

   The developer's explanation section contains more useful information on
   :ref:`configuration <expl_configuration>`.

1. Global configuration
-----------------------

First, let's register the new global configuration options which will be
configurable from sphinx' ``conf.py``. Global settings are added in the
``__init__`` module via ``add_configuration_values`` function:

.. code-block:: python
   :caption: sphinxcontrib/autodoc_pydantic/__init__.py

   def add_configuration_values(app: Sphinx):
       """Adds all configuration values to sphinx application.

       """

       stem = "autodoc_pydantic_"
       add = app.add_config_value

       summary_list_order = OptionsSummaryListOrder.ALPHABETICAL

       # ...

       add(f'{stem}settings_summary_list_order', summary_list_order, True, str)
       add(f'{stem}model_summary_list_order', summary_list_order, True, str)

2. Local configuration
----------------------

Second, we want to allow our pydantic auto-documenters to accept directive
options to overwrite globally set options. In this example, we need to modify
``OPTION_SPEC_MODEL`` and ``OPTION_SPEC_SETTINGS``:

.. code-block:: python
   :caption: sphinxcontrib/autodoc_pydantic/directives/options/definition.py

   OPTION_SPEC_SETTINGS = {
      "settings-summary-list-order": option_one_of_factory(
         OptionsSummaryListOrder.values()
      ),
   }

   OPTION_SPEC_MODEL = {
      "model-summary-list-order": option_one_of_factory(
         OptionsSummaryListOrder.values()
      ),
   }

.. hint::

   The ``OPTION_SPEC_X`` dictionaries contain all available directive options and
   their corresponding option validator functions for all available auto-documenters


5. Implement required behavior
==============================

The actual implementation is rather simple in contrast to the previous steps.
A single method is required that is able to sort both fields and validators in
alphabetical order or by source:

.. code-block:: python
   :caption: sphinxcontrib/autodoc_pydantic/directives/autodocumenters.py

   class PydanticModelDocumenter(ClassDocumenter):

       def _sort_summary_list(self, names: Iterable[str]) -> List[str]:
           """Sort member names according to given sort order
           `OptionsSummaryListOrder`.

           """

           sort_order = self.pydantic.options.get_value(name="summary-list-order",
                                                        prefix=True,
                                                        force_availability=True)

           if sort_order == OptionsSummaryListOrder.ALPHABETICAL:
               def sort_func(name: str):
                   return name
           elif sort_order == OptionsSummaryListOrder.BYSOURCE:
               def sort_func(name: str):
                   name_with_class = f"{self.object_name}.{name}"
                   return self.analyzer.tagorder.get(name_with_class)
           else:
               raise ValueError(
                   f"Invalid value `{sort_order}` provided for "
                   f"`summary_list_order`. Valid options are: "
                   f"{OptionsSummaryListOrder.values()}")

           return sorted(names, key=sort_func)

This method is called within the ``add_validators_summary`` and
``add_field_summary`` methods to provide the correct summary list ordering, e.g.:

.. code-block:: python
   :caption: sphinxcontrib/autodoc_pydantic/directives/autodocumenters.py

   class PydanticModelDocumenter(ClassDocumenter):

       def add_validators_summary(self):
           """Adds summary section describing all validators with corresponding
           fields.

           """
           # ...

           # get correct sort order
           validator_names = filtered_references.keys()
           sorted_validator_names = self._sort_summary_list(validator_names)

           # ...

The previously created tests determine the correctness of the newly added
implementation while the existing tests ensure that no regressions occur.

6. Update documentation
=======================

If you have made it thus far, congratulations! Let's reward ourselves by updating
the documentation to let others know about the new feature.

**autodoc_pydantic** provides a custom directive named ``config_description`` to
simplify the process of adding documentation for new features:

.. code-block:: rest
   :caption: docs/source/user_guide/configuration.rst

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

You can see how this renders in the corresponding configuration section
:ref:`here <autodoc_pydantic_model_summary_list_order>`. Importantly, the ``config_description``
directive generates rendered output for all provided configuration values which
greatly helps to understand how the feature changes the resulting documentation.

The ``config_description`` directive takes the following parameters:

:directive header: Represents the argument of the directive. Define the
  auto-documenter to be used and documented.
:title: Set the title of resulting section.
:path: Provide a path to a pydantic object which is used to render
  exemplary output for provided configuration values.
:example_path: Optionally provide explicit path to example code if ``path`` is
  not sufficient for example code.
:confpy: Represents the name of the global configuration setting that
  can be modified in ``conf.py``.
:directive_option: Represents the name of the local configuration setting that
  is can be used as a directive option.
:enable: You may need to enable additional configuration
  settings for the output to render properly. In this case, showing the
  summary list order requires to show summary lists in the first place. Hence,
  this is enabled via ``model-show-validator-summary`` and
  ``model-show-field-summary``.
:values: Contains a list of available configuration values for this
  feature which each will be used to render the output.
:version: Set the version when this configuration was added.
:directive body: Represents the content of the directive. Provide reST
  describing the feature.

.. note::

   You have may recognized that ``:path:`` points at the mocked model we have
   created earlier to test against. Essentially, we are using the same model
   not just for testing but also for showcasing the new feature.
