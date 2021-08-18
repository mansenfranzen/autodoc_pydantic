Changelog
=========

v1.4.0 - 2021-XX-XX
-------------------

This is a feature and bug release.

Added
~~~~~

- Include ``show-json-error-strategy`` for pydantic models and settings to define
  error handling in case a pydantic field breaks the JSON schema generation
  `#8 <https://github.com/mansenfranzen/autodoc_pydantic/issues/8>`__.

Bugfix
~~~~~~

- Improve handling of non serializable pydantic fields for JSON model generation.
  Using ``pd.DataFrame`` as a type annotation raised an exception instead of being
  handled appropriately `#28 <https://github.com/mansenfranzen/autodoc_pydantic/issues/28>`__.
- Allow typed fields within doc strings to successfully reference pydantic models
  and settings `#27 <https://github.com/mansenfranzen/autodoc_pydantic/issues/27>`__.

Testing
~~~~~~~

- Add explicit tests for references originating from typed fields.
- Add more diverse tests for handling non serializable fields breaking JSON model
  generation.
- Add tests for different error handling strategies regarding ``show-json-error-strategy``.

Documentation
~~~~~~~~~~~~~

- Add sections in configuration page for describing ``show-json-error-strategy``.

Contributors
~~~~~~~~~~~~

- Thanks to `tahoward <https://github.com/tahoward>`__ for reporting a bug related to
  missing references in typed fields `#27 <https://github.com/mansenfranzen/autodoc_pydantic/issues/27>`__.
- Thanks to `thomas-pedot <https://github.com/thomas-pedot>`__ for reporting a bug related to
  error handling of pydantic fields breaking JSON schema generation `#28 <https://github.com/mansenfranzen/autodoc_pydantic/issues/28>`__.


v1.3.1 - 2021-07-21
-------------------

This is a minor release including the following:

- Providing support for ``root_validator`` `#20 <https://github.com/mansenfranzen/autodoc_pydantic/issues/20>`__ .
- Fixing a bug concerning overwriting ``member-order`` `#21 <https://github.com/mansenfranzen/autodoc_pydantic/issues/21>`__ .
- Integrating flake8 for static code analysis.

Bugfix
~~~~~~

- Fix ``member-order`` being overwritten by autodoc pydantic's autodocumenters `#21 <https://github.com/mansenfranzen/autodoc_pydantic/issues/21>`__.

Documentation
~~~~~~~~~~~~~

- Add example showing representation of asterisk and root validators.
- Add `sphinx-copybutton` extension.

Testing
~~~~~~~

- Add explicit tests for asterisk and root validators.
- Add test case ensuring that ``member-order`` is not affected by other auto-documenters.
- Fix several tests which in fact tested wrong behaviour.

Internal
~~~~~~~~

- Refactor and simplify field validator mapping generation of ``inspection.ModelWrapper``.
- Replace ``set_default_option_with_value`` with specific ``set_members_all``.
- Create separate copy for every auto-documenters ``option`` object to prevent shared options.

Contributors
~~~~~~~~~~~~

- Thanks to `roguh <https://github.com/roguh>`__ for submitting a feature request
  for ``root_validators`` `#20 <https://github.com/mansenfranzen/autodoc_pydantic/issues/20>`__.
- Thanks to `ybnd <https://github.com/ybnd>`__ for submitting a bug report concerning
  incorrect behaviour for ``member-order`` `#21 <https://github.com/mansenfranzen/autodoc_pydantic/issues/21>`__


v1.3.0 - 2021-05-10
-------------------

This is a release focusing on testing and packaging. It includes tests for
sphinx 4.0 support. Additionally, it moves all test invocation specifications
to ``tox.ini``.

Documentation
~~~~~~~~~~~~~

- Add acknowledgements to index.
- Add detailed description for running tests with pytest and tox.
- Convert changelog page from markdown to reST.

Testing
~~~~~~~

- Use tox for defining different test environments (specific stable, latest
  stable and development). Remove test environment specifications from github
  ci and move it to ``tox.ini`` addressing #\ `7 <https://github.com/mansenfranzen/autodoc_pydantic/issues/7>`__.
- Add sphinx 4.0 to test environments addressing #\ `16 <https://github.com/mansenfranzen/autodoc_pydantic/issues/16>`__.
- Define specific test environments instead of testing all matrix combinations.
- Provide version information about *autdoc_pydantic* and relevant
  dependencies.

Packaging
~~~~~~~~~

- Replace ``pytest-cov`` with ``coverage``.
- Remove ``myst-parser`` dependency addressing #\ `16 <https://github.com/mansenfranzen/autodoc_pydantic/issues/16>`__.
- Add ``tox`` for executing tests in CI.
- Remove poetry development dependencies and replace it with explicit
  ``extras`` for *docs*, *test* and *dev*.

Internal
~~~~~~~~

- Rename ``util`` module to ``composites`` to improve naming convention.

Added
~~~~~

- ``show_versions`` function to show important dependency information which are
  relevant for tracking down bugs as part of the new ``utility`` module.

v1.2.0 - 2021-05-09
-------------------

This is a feature release adding the field summary for pydantic
models/settings.

Documentation
~~~~~~~~~~~~~

-  Refactor and simplify sphinx extension ``helper`` module for better
   maintainability and readability.
-  Improve many of the available descriptions in the ``configuration``
   section.
-  Provide correct markers for the actual default values in the
   ``configuration`` section.

Added
~~~~~

-  Introduce ``model-show-field-summary`` and
   ``settings-show-field-summary`` which partially addresses
   #\ `14 <https://github.com/mansenfranzen/autodoc_pydantic/issues/14>`__.

Internal
~~~~~~~~

-  Add ``get_fields`` to ``inspection`` module.

v1.1.3 - 2021-05-08
-------------------

This is a patch release addressing missing cross reference ability and
minor refactorings.

Internal
~~~~~~~~

-  Add ``add_domain_object_types`` to extension ``setup``.
-  Add version and extension meta data to ``setup``.
-  Refactor rather complex ``setup`` into separate functions.

Testing
~~~~~~~

-  Rename test directory ``test-ext-autodoc-pydantic`` to ``test-base``
   to streamline naming convention.
-  Add test directory ``test-edgecase-any-reference`` to mock issue with
   failing ``:any:`` reference to pydantic objects including
   ``test_any_reference`` test.
-  Add ``test_sphinx_build`` test module to check that the sphinx docs
   build without error and warning which can be seen as an end to end
   test because *autodoc\_pydantic*'s documentation is built with sphinx
   and contains an entire collection of usage examples for
   *autodoc\_pydantic* itself.

Bugfix
~~~~~~

-  Enable cross referencing of pydantic objects which are documented
   with *autodoc\_pydantic* directives and linked via ``:any:`` role
   #\ `3 <https://github.com/mansenfranzen/autodoc_pydantic/issues/3>`__.

Documentation
~~~~~~~~~~~~~

-  Add *complete configuration* and *fields only* example to
   documentation.

v1.1.2 - 2021-05-06
-------------------

This is a bugfix release on compatibility issues with sphinx
autosummary.

Internal
~~~~~~~~

-  Remove custom object import and use autodoc's provided functionality.
-  Add ``option_is_true`` and ``option_is_false`` for
   ``PydanticAutoDirective`` respecting missing values via custom
   ``NONE`` object.
-  Move member option processing from ``__init__`` to
   ``document_members`` for ``PydanticModelDocumenter``.
-  Introduce ``PydanticDirectiveBase`` base class for all pydantic
   directives to remove code redundancies.

Bugfix
~~~~~~

-  Respect ``.. currentmodule::`` directive for object imports
   `#12 <https://github.com/mansenfranzen/autodoc_pydantic/issues/12>`__.
-  Make ``autosummary``'s ``FakeDirective`` work with pydantic
   autodocumenters
   `#11 <https://github.com/mansenfranzen/autodoc_pydantic/issues/11>`__.
-  Allow ``AutoSummary.get_items`` to successfully list pydantic
   autodocumenters which wrap objects imported to external modules
   `#11 <https://github.com/mansenfranzen/autodoc_pydantic/issues/11>`__.

Documentation
~~~~~~~~~~~~~

-  Add ``autosummary`` explanation to usage section.

Testing
~~~~~~~

-  Add test module for ensuring ``autosummary`` interoperability.

Contributors
~~~~~~~~~~~~

-  Thanks to `antvig <https://github.com/antvig>`__ for reporting and
   testing an issue related to autosummary
   `#11 <https://github.com/mansenfranzen/autodoc_pydantic/issues/11>`__.

v1.1.1 - 2021-04-26
-------------------

This is a minor release with focus on refactoring and doc strings.

Internal
~~~~~~~~

-  Several minor readability refactorings.

Documentation
~~~~~~~~~~~~~

-  Add changelog and ``myst_parser`` for parsing markdown files.

Project
~~~~~~~

-  Add animated example to showcase difference between standard sphinx
   autodoc and pydantic autodoc.
-  Add project logo.
-  Add changelog.

v1.1.0 - 2021-04-24
-------------------

This is small feature release enabling ``autodoc_pydantic`` to handle
non JSON serializable fields properly.

Internal
~~~~~~~~

-  Replace inspection methods that use models JSON schema with methods
   that directly access relevant pydantic object attributes.
-  Intercept non JSON serializable fields and overwrite types and
   default values indicating serialization error.

Documentation
~~~~~~~~~~~~~

-  Add explicit note about how non JSON serializable fields are handled
   for ``model-show-json`` and ``settings-show-json``.

v1.0.0 - 2021-04-23
-------------------

This is a major release providing API stability with main focus on
extensive tests and documentation.

Added
~~~~~

-  Add custom css for ``autodoc_pydantic`` extension.

Internal
~~~~~~~~

-  Add ``PydanticAutoDirective`` as composite class to mainly manage
   option/configuration management for directives.
-  Add ``PydanticAutoDoc`` as composite class to mainly manage
   option/configuration management for autodocumenters.
-  Unify directive options and global configuration settings via
   composite classes.
-  Add option validators ``option_members``, ``option_one_of_factory``,
   ``option_default_true``, ``option_list_like``.

Documentation
~~~~~~~~~~~~~

-  Add extensions to automate documentation generation:
-  ``ConfigurationToc`` to generate options/conf toc mappings from usage
   to configuration section
-  ``TabDocDirective`` to generate rendered examples in configuration
   section
-  ``AutoCodeBlock`` to generate code block from object path

-  Add user guide:
-  Installation
-  Usage
-  Configuration
-  Examples

-  Add developer guide:
-  Setting up development environment
-  Running tests
-  Building docs

-  Add ``.readthedocs.yaml``.

Testing
~~~~~~~

-  Add test python package with code examples for test execution (same
   structure as sphinx tests).
-  Add fixture ``test_app`` to instantiate test app with settable
   configuration settings.
-  Add fixture ``autodocument`` to handle restructured text generation
   tests (autodocumenter tests).
-  Add fixture ``parse_rst`` to handle node generation tests from
   restructured text (directive tests).
-  Add autodoc/directive tests for all available configuration settings
-  Include sourcery in CI pipeline.

Packaging
~~~~~~~~~

-  Modify package dependencies to ``sphinx >=3.4`` and
   ``pydantic >= 1.5``.

v0.1.1 - 2021-04-04
-------------------

This release adds the sphinx documentation skeleton.

Documentation
~~~~~~~~~~~~~

-  Add initial sphinx documentation.

v0.1.0 - 2021-03-30
-------------------

This is the initial of autodoc\_pydantic.

Added
~~~~~

-  Autodocumenter ``PydanticModelDocumenter`` with configurations:
-  ``model_show_json``
-  ``model_show_config_member``
-  ``model_show_config_summary``
-  ``model_show_validator_members``
-  ``model_show_validator_summary``
-  ``model_hide_paramlist``
-  ``model_undoc_members``
-  ``model_members``
-  ``model_member_order``
-  ``model_signature_prefix``

-  Autodocumenter ``PydanticSettingsDocumenter`` with configurations:
-  ``settings_show_json``
-  ``settings_show_config_member``
-  ``settings_show_config_summary``
-  ``settings_show_validator_members``
-  ``settings_show_validator_summary``
-  ``settings_hide_paramlist``
-  ``settings_undoc_members``
-  ``settings_members``
-  ``settings_member_order``
-  ``settings_signature_prefix``

-  Autodocumenter ``PydanticFieldDocumenter`` with configurations:
-  ``field_list_validators``
-  ``field_doc_policy``
-  ``field_show_constraints``
-  ``field_show_alias``
-  ``field_show_default``
-  ``field_signature_prefix``

-  Autodocumenter ``PydanticValidatorDocumenter`` with configurations:
-  ``validator_signature_prefix``
-  ``validator_replace_signature``
-  ``validator_list_fields``

-  Autodocumenter ``PydanticConfigClassDocumenter`` with configurations:
-  ``config_signature_prefix``
-  ``config_members``

-  Directives ``PydanticModel``, ``PydanticSettings``,
   ``PydanticField``, ``PydanticValidator``, ``PydanticConfigClass``

Internal
~~~~~~~~

-  Add ``inspection`` along with ``ModelWrapper`` module providing
   functionality to inspect pydantic objects to retrieve relevant
   informations for documentation.

Testing
~~~~~~~

-  Add end to end tests for autodocumenters and directives.
-  Setup github actions for CI.
-  Add codacy integration.
-  Add code coverage.

Packaging
~~~~~~~~~

-  Use poetry for package management.
-  Add ``pyproject.toml``.
-  Add github action to upload to PyPI upon version tags on main branch.

