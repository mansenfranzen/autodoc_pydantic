===========
Explanation
===========

The following sections are mainly intended for developers who want to contribute
or extend **autodoc_pydantic**. First, the design of **autodoc_pydantic** is
outlined guided by its actual goal.

Design of `autodoc_pydantic`
============================

This section aims at developers and contributors who want to understand the
design of `autodoc_pydantic` and how it integrates with sphinx and pydantic.
It intends to support a basic understanding of **autodoc_pydantic**'s code base.

Objective
---------

The main purpose of **autodoc_pydantic** is to improve auto-documentation for
pydantic models. The default sphinx autodoc is not very well suited for
pydantic models because it has no knowledge about pydantic specific concepts
like validators, fields and their possible constraints. **autodoc_pydantic**
leverages the additional knowledge about pydantic to provide a more
sophisticated documentation (e.g. see `this example <showcase>`_).

Inspection
----------

Before extending sphinx with new directives and generating reST, we first need
collect the relevant information to be documented from pydantic models.

While `sphinx.ext.autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_
already provides great tooling to inspect python
objects (e.g. class members, source name, imports), again it has no specific
knowledge about pydantic models. The auto-documenters need to extract relevant
information like pydantic fields and validators from pydantic models. This is
accomplished by the :ref:`inspection <api_inspection>` module which offers
several inspector classes for different aspects of pydantic models:

- :class:`FieldInspector <sphinxcontrib.autodoc_pydantic.inspection.FieldInspector>`
  -> field names, properties, JSON serializability and more
- :class:`ValidatorInspector <sphinxcontrib.autodoc_pydantic.inspection.ValidatorInspector>`
  -> validator names and types
- :class:`ConfigInspector <sphinxcontrib.autodoc_pydantic.inspection.ConfigInspector>`
  -> config usage and values
- :class:`ReferenceInspector <sphinxcontrib.autodoc_pydantic.inspection.ReferenceInspector>`
  -> reference mappings between fields and validators
- :class:`SchemaInspector <sphinxcontrib.autodoc_pydantic.inspection.SchemaInspector>`
  -> schema sanitizer
- :class:`StaticInspector <sphinxcontrib.autodoc_pydantic.inspection.StaticInspector>`
  -> static methods

All of these are composite classes which are wrapped under the main
:class:`ModelInspector <sphinxcontrib.autodoc_pydantic.inspection.ModelInspector>`
class which serves as the main entry point to inspect pydantic models:

.. code-block:: python

      from sphinxcontrib.autodoc_pydantic.inspection import ModelInspector
      from pydantic import BaseModel, validator, Field


      class TestModel(BaseModel):
          field_a: int = Field(1, min=0, max=10)
          field_b: str = "FooBar"

          @validator("field_a")
          def validate_field_a(cls, v):
              return v


      inspector = ModelInspector(TestModel)
      print("Show field names:", inspector.fields.names)
      # Show field names: ['field_a', 'field_b']
      print("Show field constraints:", inspector.fields.get_constraints("field_a"))
      # Show field constraints: {'min': 0, 'max': 10}


The :class:`ModelInspector <sphinxcontrib.autodoc_pydantic.inspection.ModelInspector>`
is primarily used by the autodocumenters which translate the additional pydantic
knowledge into actual reST.


Auto-Documenters
----------------

Once the relevant information about pydantic models is accessible via the
:class:`ModelInspector <sphinxcontrib.autodoc_pydantic.inspection.ModelInspector>`,
custom auto-documenters are necessary to translate the additional knowledge into
concrete reST documentation. For example, constraints could
be added to pydantic fields or the model `Config` class information could be
summarized in the model documentation.

From an implementation perspective, the sphinx documentation provides a great
`tutorial <https://www.sphinx-doc.org/en/master/development/tutorials/autodoc_ext.html>`_
as a starting point on how to write a custom auto-documenter. In fact, this was
also the initial step going forward with the development of **autodoc_pydantic**.
Please refer to this tutorial for a basic understanding on how auto-documenters
work.

.. note::

   Auto-documenters generate reST and are independent of sphinx directives in
   the first place. However, once they are registered to the sphinx
   application via ``app.add_autodocumenter``, they are wrapped via the
   ``AutodocDirective`` which in turn finally converts reST into docutil nodes.

The following auto-documenters exist in the :ref:`autodocumenters <api_autodocumenters>` module:

- :class:`PydanticModelDocumenter <sphinxcontrib.autodoc_pydantic.directives.autodocumenters.PydanticModelDocumenter>`
- :class:`PydanticSettingsDocumenter <sphinxcontrib.autodoc_pydantic.directives.autodocumenters.PydanticSettingsDocumenter>`
- :class:`PydanticFieldDocumenter <sphinxcontrib.autodoc_pydantic.directives.autodocumenters.PydanticFieldDocumenter>`
- :class:`PydanticValidatorDocumenter <sphinxcontrib.autodoc_pydantic.directives.autodocumenters.PydanticValidatorDocumenter>`
- :class:`PydanticConfigClassDocumenter <sphinxcontrib.autodoc_pydantic.directives.autodocumenters.PydanticConfigClassDocumenter>`


**autodoc_pydantic**'s flexibility to be completely customizable requires
many directive options to be available. Hence, there is the separate module
:ref:`options.definitions <api_options>` containing all options for the
auto-documenters. These option definitions are then registered by the corresponding
auto-documenters:

.. code-block:: python
   :emphasize-lines: 9, 10
   :caption: directives/autodocumenters.py

      class PydanticFieldDocumenter(AttributeDocumenter):
          """Represents specialized Documenter subclass for pydantic fields.

          """

          objtype = 'pydantic_field'
          directivetype = 'pydantic_field'
          priority = 10 + AttributeDocumenter.priority
          option_spec = dict(AttributeDocumenter.option_spec)
          option_spec.update(OPTIONS_FIELD)

Directives
----------

Using customized auto-documenters already allows for a great amount of modification regarding the content that can be represented by the default sphinx directives. For example, `autodoc_pydantic` could simply use the existing `py:method` directive to document pydantic validators. However, the default signature of pydantic validators does not convey valueable information because it most often just shows a single argument without letting us know which pydantic field is validated. Instead, we might want to put refrences to the validated fields directly into the header since this more relevant. This is not possible while relying on the default directives. Therefore, `autodoc_pydantic` additionally provides the following directives in `sphinxcontrib.autodoc_pydantic.directives` to further customize the documentation:

- pydantic_model
- pydantic_settings
- pydantic_field
- pydantic_validator
- pydantic_config

Adding new features
===================

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



Specialized topics
==================

This section describes some specifics about the inner workings of sphinx and pydantic which became of importance while implementing certain features or fixing bugs. It captures knowledge which otherwise might get lost if not written down.

Understanding auto-documenters
------------------------------

Autodocumenters typically inspect a python object and generate corresponding reStructuredText (reST). The reST contains calls to sphinx directives, roles and so on and is in turn converted docutils nodes. The docutil nodes are then consumed by different builders to create the corresponding output (e.g. PDF, HTML).

An autodocumenter is not a sphinx directive in the first place because it does not generate docutil nodes. Instead as mentioned above, it creates reST (see `Documenter` base class for autodocumenters and its `generate` method). But how is the reST finally converted into docutil nodes?

When registering a autodocumenter via `app.add_autodocumenter(PydanticFieldDocumenter)`, it is wrapped with the generic `AutodocDirective`. This directive executes the autodocumenter, retrieves its reST and then converts the reST into docutils.

The interesting part is how a given reST is converted into docutils nodes because this turns out to be very useful for different use cases when writing custom directives.
Writing your own directives outputting docutil nodes is rather low level and harder to learn in comparison to directives which can create arbitrary high level reST that then will be converted to docutil nodes generically.
For example, part of `autodoc_pydantic`'s documentation is using this functionality to handle repetitive and error prone tasks (see `TabDocDirective`). More specifically, the actual conversion from reST to docutil nodes is done in `parse_generated_content`.