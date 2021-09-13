===========
Explanation
===========

The following sections are mainly intended for developers who want to contribute
or extend **autodoc_pydantic**. First, the design of **autodoc_pydantic** is
outlined guided by its actual goal.

--------------------------
Design of autodoc_pydantic
--------------------------

This section aims at developers and contributors who want to understand the
design of **autodoc_pydantic** and how it integrates with sphinx and pydantic.
It intends to support a basic understanding of **autodoc_pydantic**'s code base.

Objective
=========

The main purpose of **autodoc_pydantic** is to improve auto-documentation for
pydantic models. The default sphinx autodoc is not very well suited for
pydantic models because it has no knowledge about pydantic specific concepts
like validators, fields and their possible constraints. **autodoc_pydantic**
leverages the additional knowledge about pydantic to provide a more
sophisticated documentation (e.g. see :ref:`this example <showcase>`).

Inspection
==========

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

All of these are composite classes which are combined under the main
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



Auto-Documenters
================

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
Please refer to this tutorial for a basic understanding on how to create your
own auto-documenters.

In a nutshell, an auto-documenter gets an python object as input, inspects it
and generates reST as output.

.. note::

   If you want to know more about why auto-documenters are no sphinx directives
   and how their generated reST is eventually converted into actual documentation
   pages, please read :ref:`understanding auto-documenters <understanding_autodocumenters>`.

The following auto-documenters exist in the :ref:`autodocumenters <api_autodocumenters>` module:

- :class:`PydanticModelDocumenter <sphinxcontrib.autodoc_pydantic.directives.autodocumenters.PydanticModelDocumenter>`
- :class:`PydanticSettingsDocumenter <sphinxcontrib.autodoc_pydantic.directives.autodocumenters.PydanticSettingsDocumenter>`
- :class:`PydanticFieldDocumenter <sphinxcontrib.autodoc_pydantic.directives.autodocumenters.PydanticFieldDocumenter>`
- :class:`PydanticValidatorDocumenter <sphinxcontrib.autodoc_pydantic.directives.autodocumenters.PydanticValidatorDocumenter>`
- :class:`PydanticConfigClassDocumenter <sphinxcontrib.autodoc_pydantic.directives.autodocumenters.PydanticConfigClassDocumenter>`

Configuration settings
----------------------

An important aspect is how **autodoc_pydantic** handles configuration settings.
Since all features are completely configurable (globally via ``conf.py`` and
locally via directive options), they have to be represented in code.

Global settings are defined in the ``__init__`` module and are directly
added when **autodoc_pydantic** is registered as an sphinx extension:

.. code-block:: python
   :caption: __init__.py

   # ...

   def add_configuration_values(app: Sphinx):
       """Adds all configuration values to sphinx application.

       """

       stem = "autodoc_pydantic_"
       add = app.add_config_value

       # ...

       add(f'{stem}field_list_validators', True, True, bool)
       add(f'{stem}field_doc_policy', OptionsFieldDocPolicy.BOTH, True, str)
       add(f'{stem}field_show_constraints', True, True, bool)
       add(f'{stem}field_show_alias', True, True, bool)
       add(f'{stem}field_show_default', True, True, bool)
       add(f'{stem}field_show_required', True, True, bool)
       add(f'{stem}field_signature_prefix', "field", True, str)

   # ...

   def setup(app: Sphinx) -> Dict[str, Any]:
       add_configuration_values(app)

Local settings are defined in the separate :ref:`options.definitions <api_options>`
module containing all directive options for auto-documenters, e.g:

.. code-block:: python
   :caption: directives/options/definition.py

   # ...

   OPTIONS_FIELD = {
       "field-show-default": option_default_true,
       "field-show-required": option_default_true,
       "field-signature-prefix": unchanged,
       "field-show-alias": option_default_true,
       "field-show-constraints": option_default_true,
       "field-list-validators": option_default_true,
       "field-doc-policy": option_one_of_factory(OptionsFieldDocPolicy.values()),
       "__doc_disable_except__": option_list_like}

   # ...

These directive options are then registered by the corresponding
auto-documenters:

.. code-block:: python
   :caption: directives/autodocumenters.py

   # ...

   class PydanticFieldDocumenter(AttributeDocumenter):
       """Represents specialized Documenter subclass for pydantic fields.

       """

       # ...

       option_spec = dict(AttributeDocumenter.option_spec)
       option_spec.update(OPTIONS_FIELD)

       # ...

Local directive options overwrite global settings. Checking for both global and
local settings while also handling precedence is abstracted away via
:class:`PydanticDocumenterOptions <sphinxcontrib.autodoc_pydantic.directives.options.composites.PydanticDocumenterOptions>`
which provides many convenience methods for interacting with options.

Pydantic Composite
------------------

Essentially, auto-documenters need to employ the
:class:`ModelInspector <sphinxcontrib.autodoc_pydantic.inspection.ModelInspector>`
for retrieving the relevant information to be documented and
:class:`PydanticDocumenterOptions <sphinxcontrib.autodoc_pydantic.directives.options.composites.PydanticDocumenterOptions>`
for accessing configuration settings. Both are combined in the
:class:`PydanticDocumenterNamespace <sphinxcontrib.autodoc_pydantic.directives.autodocumenters.PydanticDocumenterNamespace>`
composite class via ``inspect`` and ``options`` attributes, respectively. This
provides a single entry point for all mandatory functionality that is required
to populate auto-documenter's content.

The :class:`PydanticDocumenterNamespace <sphinxcontrib.autodoc_pydantic.directives.autodocumenters.PydanticDocumenterNamespace>`
is added to every auto-documenter during it's initialization as the `pydantic`
attribute and is then used within methods as follows:

.. code-block::
   :caption: directives/autodocumenters.py

   # ...

   class PydanticFieldDocumenter(AttributeDocumenter):
       """Represents specialized Documenter subclass for pydantic fields.

       """

       # ...

       def __init__(self, *args):
           super().__init__(*args)
           self.pydantic = PydanticDocumenterNamespace(self, is_child=True)

       # ...

       def add_default_value_or_required(self):
           """Adds default value or required marker.

           """

           field_name = self.pydantic_field_name
           is_required = self.pydantic.inspect.fields.is_required(field_name)
           show_default = self.pydantic.options.is_true("field-show-default")
           show_required = self.pydantic.options.is_true("field-show-required")

           # ...

Directives
==========

Using customized auto-documenters already allows for a great amount of
modification regarding the content that can be represented by the default
sphinx directives. For example, **autodoc_pydantic** could simply use the
existing ``py:method`` directive to document pydantic validators. However,
the default signature of pydantic validators does not convey valuable
information because it most often just shows a single argument without letting
us know which pydantic field is validated. Instead, we might want to put
references to the validated fields directly into the header since this more
relevant. This is not possible while relying on the default directives.

Therefore, **autodoc_pydantic** additionally provides the following
directives in :ref:`directives <api_directives>` module to allow more advanced
customization:

- :class:`PydanticModel <sphinxcontrib.autodoc_pydantic.directives.directives.PydanticModel>`
- :class:`PydanticSettings <sphinxcontrib.autodoc_pydantic.directives.directives.PydanticSettings>`
- :class:`PydanticField <sphinxcontrib.autodoc_pydantic.directives.directives.PydanticField>`
- :class:`PydanticValidator <sphinxcontrib.autodoc_pydantic.directives.directives.PydanticValidator>`
- :class:`PydanticConfigClass <sphinxcontrib.autodoc_pydantic.directives.directives.PydanticConfigClass>`


------------------
Specialized topics
------------------

This section describes some specifics about the inner workings of sphinx and pydantic which became of importance while implementing certain features or fixing bugs. It captures knowledge which otherwise might get lost if not written down.

.. _understanding_autodocumenters:

Understanding auto-documenters
==============================

Auto-documenters typically inspect a python object and generate corresponding
reStructuredText (reST). The reST contains calls to sphinx directives, roles
and so on and is in turn converted docutils nodes. The docutil nodes are then
consumed by different builders to create the corresponding output (e.g. PDF, HTML).

An auto-documenter is not a sphinx directive in the first place because it does
not generate docutil nodes. Instead as mentioned above, it creates reST
(see `Documenter` base class for autodocumenters and its `generate` method).
But how is the reST finally converted into docutil nodes?

When registering a auto-documenter via `app.add_autodocumenter(PydanticFieldDocumenter)`,
it is wrapped with the generic `AutodocDirective`. This directive executes
the auto-documenter, retrieves its reST and then converts the reST into docutils.

The interesting part is how a given reST is converted into docutils nodes
because this turns out to be very useful for different use cases when writing
custom directives.

Writing your own directives outputting docutil nodes is rather low level and
harder to learn in comparison to directives which can create arbitrary high
level reST that then will be converted to docutil nodes generically.

For example, part of `autodoc_pydantic`'s documentation is using this
functionality to handle repetitive and error prone tasks (see `TabDocDirective`).
More specifically, the actual conversion from reST to docutil nodes is done in
`parse_generated_content`.