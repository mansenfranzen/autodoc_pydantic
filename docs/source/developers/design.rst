.. _expl_design:

======
Design
======

The following sections are mainly intended for developers or interested users
who want to contribute or who want to gain a deeper understanding about the
inner workings of **autodoc_pydantic**.

It aims to clarify the design of **autodoc_pydantic** and how it
integrates with sphinx and pydantic. Additionally, it intends to provide a
gentle introduction to the code base.

---------
Objective
---------

Before diving into any implementation details, let's take a high level
perspective first and focus on the issue that **autodoc_pydantic** solves.

The default sphinx autodoc extension is not very well suited for automatically
generated documentation of pydantic models because it has no domain knowledge
about pydantic specific concepts like validators and fields. As a result, the
default sphinx autodoc provides no information about field constraints, has
no references between fields and validators, shows overloaded or meaningless
signatures and does not even show default values for fields.

Hence, the main purpose of **autodoc_pydantic** is to improve auto-documentation
for pydantic models. It leverages the additional knowledge about pydantic to
provide a more sophisticated documentation (e.g. see :ref:`this example <showcase>`).
Moreover, every modification to the default sphinx auto-documentation should be
configurable to allow complete customization without enforcing any strict changes
to the existing documentation.

---------------
Core components
---------------

Guided by the objective to improve auto-documentation for pydantic models, three
mandatory core components can be derived.

1. :ref:`Inspection <expl_inspection>` - extract relevant information from pydantic models.
2. :ref:`Auto-documenters <expl_auto_documenters>` - translate pydantic specific knowledge into documentation pages.
3. :ref:`Configuration <expl_configuration>` - provide complete configurability of all modifications.

.. _expl_inspection:

Inspection
==========

Before extending sphinx with new directives and generating reST, we first need
collect the relevant information to be documented for pydantic models.

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

All of these are composite classes which are combined under the
:class:`ModelInspector <sphinxcontrib.autodoc_pydantic.inspection.ModelInspector>`
class which serves as the main entry point to inspect pydantic models:

.. mermaid:: mermaid/model_inspector.mmd

You may use the :class:`ModelInspector <sphinxcontrib.autodoc_pydantic.inspection.ModelInspector>`
programmatically to inspect pydantic models:

.. code-block:: python

   from sphinxcontrib.autodoc_pydantic.inspection import ModelInspector
   from pydantic import BaseModel, field_validator, Field


   class TestModel(BaseModel):
       field_a: int = Field(1, min=0, max=10)
       field_b: str = "FooBar"

       @field_validator("field_a")
       def validate_field_a(cls, v):
           return v


   inspector = ModelInspector(TestModel)

   print("Show field names:", inspector.fields.names)
   # Show field names: ['field_a', 'field_b']

   print("Show field constraints:", inspector.fields.get_constraints("field_a"))
   # Show field constraints: {'min': 0, 'max': 10}

.. _expl_auto_documenters:

Auto-Documenters
================

Once the relevant information about pydantic models is accessible via the
:class:`ModelInspector <sphinxcontrib.autodoc_pydantic.inspection.ModelInspector>`,
custom auto-documenters are necessary to translate the additional knowledge into
concrete reST documentation. For example, constraints could
be added to pydantic fields. Furthermore, the model `Config` class information
could be summarized in the model documentation.

From an implementation perspective, the sphinx documentation provides a great
`tutorial <https://www.sphinx-doc.org/en/master/development/tutorials/autodoc_ext.html>`_
as a starting point on how to write a custom auto-documenter. In fact, this was
also the initial step going forward with the development of **autodoc_pydantic**.
Please refer to this tutorial for a basic understanding on how to create your
own auto-documenters.

In a nutshell, an auto-documenter gets a python object as input, inspects it
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

All auto-documenters are not written from scratch but inherit from
the default auto-documenters to borrow most of the main functionality provided
by `sphinx.ext.autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_
Moreover, new methods with separate logic are added and existing methods are
overloaded to inject custom content.

.. _expl_configuration:

Configuration
=============

Another important aspect is how **autodoc_pydantic** handles configuration settings.
Since all features are completely configurable (globally via ``conf.py`` and
locally via directive options), they have to be represented in code.

Global
------

Global settings are defined in the ``__init__`` module and are directly
added when **autodoc_pydantic** is registered as an sphinx extension:

.. code-block:: python
   :caption: sphinxcontrib/autodoc_pydantic/__init__.py

   def add_configuration_values(app: Sphinx):
       """Adds all configuration values to sphinx application.

       """

       stem = "autodoc_pydantic_"
       add = app.add_config_value

       add(f'{stem}field_list_validators', True, True, bool)
       add(f'{stem}field_doc_policy', OptionsFieldDocPolicy.BOTH, True, str)
       add(f'{stem}field_show_constraints', True, True, bool)
       add(f'{stem}field_show_alias', True, True, bool)
       add(f'{stem}field_show_default', True, True, bool)
       add(f'{stem}field_show_required', True, True, bool)
       add(f'{stem}field_signature_prefix', "field", True, str)

   def setup(app: Sphinx) -> Dict[str, Any]:
       add_configuration_values(app)

Local
-----

Local settings are defined in the separate :ref:`definition <api_definition>`
module containing all directive options for auto-documenters, e.g:

.. code-block:: python
   :caption: sphinxcontrib/autodoc_pydantic/directives/options/definition.py

   OPTIONS_FIELD = {
       "field-show-default": option_default_true,
       "field-show-required": option_default_true,
       "field-signature-prefix": unchanged,
       "field-show-alias": option_default_true,
       "field-show-constraints": option_default_true,
       "field-list-validators": option_default_true,
       "field-doc-policy": option_one_of_factory(OptionsFieldDocPolicy.values()),
       "__doc_disable_except__": option_list_like}

These directive options are then registered by the corresponding
auto-documenters:

.. code-block:: python
   :caption: directives/autodocumenters.py

   # ...

   class PydanticFieldDocumenter(AttributeDocumenter):
       """Represents specialized Documenter subclass for pydantic fields.

       """

       option_spec = dict(AttributeDocumenter.option_spec)
       option_spec.update(OPTIONS_FIELD)

Local directive options overwrite global settings. Checking for both global and
local settings while also handling precedence is abstracted away via
:class:`PydanticDocumenterOptions <sphinxcontrib.autodoc_pydantic.directives.options.composites.PydanticDocumenterOptions>`
which provides many convenience methods for interacting with options.

----------------------
Implementation details
----------------------

This section is a continuation of the previous :ref:`design <expl_design>`
section. It is highly recommended to start there first if you haven't read it.

Otherwise, feel free to explore more of the implementation details.

Pydantic Composite
==================

Essentially, auto-documenters need to employ the
:class:`ModelInspector <sphinxcontrib.autodoc_pydantic.inspection.ModelInspector>`
for retrieving the relevant information to be documented and
:class:`AutoDocOptions <sphinxcontrib.autodoc_pydantic.directives.options.composites.AutoDocOptions>`
for accessing configuration settings.

Both are combined in the
:class:`PydanticAutoDoc <sphinxcontrib.autodoc_pydantic.directives.autodocumenters.PydanticAutoDoc>`
composite class via ``inspect`` and ``options`` attributes, respectively. This
provides a single entry point for all mandatory functionality that is required
to populate auto-documenter's content.

.. mermaid:: mermaid/pydantic_composite.mmd

The :class:`PydanticAutoDoc <sphinxcontrib.autodoc_pydantic.directives.autodocumenters.PydanticAutoDoc>`
is added to every auto-documenter during it's initialization as the `pydantic`
attribute and is then used within methods as follows:

.. code-block::
   :caption: directives/autodocumenters.py

   class PydanticFieldDocumenter(AttributeDocumenter):
       """Represents specialized Documenter subclass for pydantic fields.

       """

       def __init__(self, *args):
           super().__init__(*args)
           self.pydantic = PydanticAutoDoc(self, is_child=True)


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
the user know which pydantic field is validated. Instead, one might want to put
references to the validated fields directly into the header since this more
relevant. This is not possible while relying on the default directives.

Therefore, **autodoc_pydantic** additionally provides the following
directives in :ref:`directives <api_directives>` module to allow more advanced
customization:

- :class:`PydanticModel <sphinxcontrib.autodoc_pydantic.directives.directives.PydanticModel>`
- :class:`PydanticSettings <sphinxcontrib.autodoc_pydantic.directives.directives.PydanticSettings>`
- :class:`PydanticField <sphinxcontrib.autodoc_pydantic.directives.directives.PydanticField>`
- :class:`PydanticValidator <sphinxcontrib.autodoc_pydantic.directives.directives.PydanticValidator>`
