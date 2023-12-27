Changelog
=========

v2.1.0 - 2024-01-XX
-------------------

This is a maintenance and bugfix release extending support to pydantic v2.5, 
sphinx v7.2 and python 3.12. Python 3.7 is removed from the test matrix and 
will be no longer supported.

Testing
~~~~~~~

- Add pydantic 2.2/2.3/2.4/2.5 to test matrix.
- Add python 3.12 to test matrix.
- Add sphinx 7.1/7.2 to test matrix.
- Remove obsolete `skip ci` condition from github actions.
- Update ``conftest`` to use ``pathlib`` instead of older Sphinx 
  ``sphinx.testing.path`` module that is being deprecated for 
  forward-compatibility with newer Sphinx versions.

Bugfix
~~~~~~

- Fix incompatibity with sphinx 7.2 due to changed usage of path objects.
  For more, see `#11606 <https://github.com/sphinx-doc/sphinx/issues/11605>`__.
- `#176 <https://github.com/mansenfranzen/autodoc_pydantic/issues/176>`__ -
  Remove ``sphinxcontrib/__init__.py`` causing ``ModuleNotFoundError`` 
  exception in some environments.  This should be a namespace package per
  `PEP 420 <https://peps.python.org/pep-0420/>`__ without ``__init_.py`` to 
  match with other extensions.

v2.0.1 - 2023-08-01
-------------------

This is a bugfix release handling an exception while documenting pydantic
models using enums.

Internal
~~~~~~~~

- Simplify model field's constraint extraction removing dependency on private
  methods.

Bugfix
~~~~~~

- Properly handle constraint extraction avoiding exceptions due to prior
  reliance on unpredictable behavior of private attributes.
- Fix incorrect type annotation string results for non-builtin types in
  ``intercept_type_annotations_py_gt_39``.

Testing
~~~~~~~

- Add pydantic 2.1 to test matrix.
- Add tests for various kinds of constrained types.
- Add "no exception" tests for specific pydantic models, such as containing
  enums.

Contributors
~~~~~~~~~~~~

- Thanks to `nagledb <https://github.com/nagledb>`__ for reporting a bug
  related to enums
  `#169 <https://github.com/mansenfranzen/autodoc_pydantic/issues/169>`__.
- Thanks to `jerryjiahaha <https://github.com/jerryjiahaha>`__ for providing
  a pull request fixing the enums bug
  `#170 <https://github.com/mansenfranzen/autodoc_pydantic/pull/170>`__.


v2.0.0 - 2023-07-24
-------------------

This is a major release supporting pydantic v2. In June 2023, pydantic v2 was
released while introducing backwards incompatible API and behavioral changes in
comparison to pydantic v1. Supporting pydantic v2 required substantial
adjustments to the codebase leading to a new major release of autodoc_pydantic
(v1.9.0 -> v2.0.0), too.

In order to keep the codebase clean and concise, separate versions for v1 and
v2 were created. The v2 branch will eventually become the new main branch
while the code for v1 remains in the main-1.x branch.

Changed Behavior
~~~~~~~~~~~~~~~~

- Documenting pydantic model configurations in isolation or as a separate
  member of the pydantic model is no longer available. The following options
  have been removed:

  - ``autodoc_pydantic_model_show_config_member``
  - ``autodoc_pydantic_settings_show_config_member``
  - ``autodoc_pydantic_config_members``
  - ``autodoc_pydantic_config_signature_prefix``

- All semantic changes from pydantic v1 to v2 take full effect.
  **autodoc_pydantic** does not modify the underlying behavior of pydantic in
  any way. Instead, it only documents whatever pydantic exposes. Hence, all
  behavioral changes such as the new default strict mode are preserved in v2.

- Sphinx ``< 4.0.0`` is no longer supported.

Features
~~~~~~~~

- Support for pydantic v2 💫.
- Support annotated type hints.

Internal
~~~~~~~~

- Adjust imports to refer to ``pydantic-settings`` (v2) instead of ``pydantic`` (v1).
- Adjust imports to refer to ``field_validator`` (v2) insteaf of ``validator`` (v1).
- Adjust imports to refer to ``model_validator`` (v2) insteaf of ``root_validator`` (v1).
- Replace ``pydantic.generics.GenericModel`` (v1) with ``typing.Generic`` (v2).
- Simplify ``ValidatorAdapter`` and ``ValidatorInspector``.
- Simplify reused validators retrieval.
- Completely rewrite the model's field constraint retrieval functionality in ``inspection.FieldInspector``.
- Adjust model's field serializability checks in ``inspection.FieldInspector``.
- Replace ``BaseModel`` with ``NamedTuple`` for ``ValidatorAdapter``.
- Remove obsolete pre/post validator attributes.
- Introduce ``importlib-metadata`` to fetch version number including support for python 3.7.

Testing
~~~~~~~

- Remove all obsolete pydantic versions from test matrix.
- Remove all tests for documenting config members.
- Remove compatibility helpers for older pydantic versions.
- Remove obsolete pydantic model example which was not used anywhere.
- Adjust serializability tests to account for changed behavior in v2.
- Adjust optional/required field marker tests to account for changed behavior in v2.
- Adjust field constraint tests to account for changed behavior in v2.
- Adjust erdantic tests to exclude the erdantic version number which caused tests to fail upon erdantic update.

Documentation
~~~~~~~~~~~~~

- Add FAQ section regarding migration guide from v1 to v2.
- Remove ``complete`` showcase from user's example.
- Update READMEs with newest features and version specifiers.
- Update developer's setup section to address v1 to v2 changes.
- Updates user's installation section to address v1 to v2 changes.
- Remove all obsolete documentation on removed config documenters.
- Rename all occurences to v2 ``field_validator`` and ``model_validator``.

Contributors
~~~~~~~~~~~~

- Special thanks to `awoimbee <https://github.com/awoimbee>`__ for providing
  a draft for the v1 to v2 migration which really initiated the work on
  supporting pydantic v2
  `#160 <https://github.com/mansenfranzen/autodoc_pydantic/pull/160>`__.
- Many thanks to `PriOliveira <https://github.com/PriOliveira>`__ for reviewing
  changes required for the v1 to v2 release
  `#160 <https://github.com/mansenfranzen/autodoc_pydantic/pull/160>`__.


v1.9.0 - 2023-06-08
-------------------

This is a feature release adding support for entity relationship diagrams
while dropping python 3.6. Additionally, pydantic v2 is currently excluded
until support will be added. Moreover, newest sphinx versions are
added to test matrix.

Feature
~~~~~~~

- Introduce ``erdantic-figure`` and ``erdantic-figure-collapsed`` configuration
  option for pydantic models to add entity relationship diagrams to models'
  documentation either in collapsed form or as an image included to the HTML.
  `#148 <https://github.com/mansenfranzen/autodoc_pydantic/pull/148>`__.

Bugfix
~~~~~~

- Run github actions on newest ``ubuntu-22.04``.
- Fix pytest errors with ``sphinx>=6.1`` where the type returned by
  ``autodoc_typehints_format`` changed.
- Provide upper version boundary for pydantic to exclude v2 which
  is not supported, yet.

Internal
~~~~~~~~

- Add ``to_collapsable`` to ``directives.templates`` that provides a
  standardized interface to create a collapsable field.
- Add ``erdantic`` to extras dependencies.

Documentation
~~~~~~~~~~~~~

- Add descriptions for ``erdantic-figure`` and ``erdantic-figure-collapsed``
  options in the configuration section.
- Add an example of ERD in the example section.

Testing
~~~~~~~

- Exclude ``python 3.6`` in test matrix.
- Include ``sphinx`` 6.0, 6.1, 6.2 and 7.0 in test matrix.
- Add tests for ``erdantic-figure`` and ``erdantic-figure-collapsed``.
- Fix github actions CI pipeline due to unsupported ubuntu while upgrading to
  newest ``ubuntu-22.04``.

Contributors
~~~~~~~~~~~~

- Many thanks to `yves-renier <https://github.com/yves-renier>`__ for adding
  entity relationship diagrams and fixing the CI pipeline
  `#148 <https://github.com/mansenfranzen/autodoc_pydantic/pull/148>`__.

v1.8.0 - 2022-10-13
-------------------

This is a feature and bugfix release with major internal refactorings and
added support for pydantic ``1.10`` and sphinx ``5.1`` and ``5.2``.

Feature
~~~~~~~

- Introduce ``hide-reused-validator`` configuration option for pydantic models
  and settings to hide class methods that are created while declaring functions
  as reusable validators
  `#122 <https://github.com/mansenfranzen/autodoc_pydantic/issues/122>`__.

Bugfix
~~~~~~

- Fix incorrect reference of reused validators
  `#122 <https://github.com/mansenfranzen/autodoc_pydantic/issues/122>`__.
- Provide deterministic sort order for model's validator summary and field's
  validator list.
- Hide pydantic user warnings in sphinx output when testing for pydantic field
  serializability.

Internal
~~~~~~~~

- Add ``ValidatorAdapter`` that provides a standardized interface to pydantic's
  validator objects with additional metadata (e.g. root validator) for internal
  usage in autodoc_pydantic.
- Introduce ``field_validator_mappings`` to ``inspection.ModelInspector`` which
  holds all mappings between fields and validators. It makes many helper
  functions of ``ValidatorInspector`` and ``FieldInspector`` obsolete. Overall,
  this greatly simplifies the inspection codebase.
- Add ``PydanticAutoDoc.resolve_inherited_validator_reference`` to allow
  proper reference resolution for inherited validators.

Documentation
~~~~~~~~~~~~~

- Add description for ``autodoc_pydantic_model_hide_reused_validator`` and
  ``autodoc_pydantic_settings_hide_reused_validator``.
- Add example section for reused validators with detailed explanation.
- Refactor sphinx extension helper for building ``autodoc_pydantic`` docs
  for better readability and maintainability.
- Add ``example_path`` to sphinx extension helper ``config_description``.
- Add FAQ question regarding interoperability with ``autoapi``.

Testing
~~~~~~~

- Include pydantic ``1.10`` and sphinx ``5.1`` / ``5.2`` in test matrix.
- Provide compatibility for new pydantic and sphinx versions.
- Fix incorrect pydantic version comparison.

Contributors
~~~~~~~~~~~~

- Thanks to `GlenNicholls <https://github.com/GlenNicholls>`__ for
  reporting a bug regarding incorrect references of reused validators
  `#122 <https://github.com/mansenfranzen/autodoc_pydantic/issues/122>`__ .
- Thanks to `csm10495 <https://github.com/csm10495>`__ for asking a question
  regarding ``autoapi`` interoperability
  `#138 <https://github.com/mansenfranzen/autodoc_pydantic/issues/138>`__ .


v1.7.2 - 2022-06-12
-------------------

This is a bugfix release.

Bugfix
~~~~~~

- Adjust ``PydanticFieldDocumenter.can_document_member`` to ignore non
  pydantic fields
  `#123 <https://github.com/mansenfranzen/autodoc_pydantic/issues/123>`__,
  `#128 <https://github.com/mansenfranzen/autodoc_pydantic/issues/128>`__.
- Allow pydantic models to be documented as class attributes while adjusting
  ``ModelInspector.from_child_signode`` to support nested object paths
  `#124 <https://github.com/mansenfranzen/autodoc_pydantic/issues/123>`__,
  `#129 <https://github.com/mansenfranzen/autodoc_pydantic/issues/128>`__.

Contributors
~~~~~~~~~~~~

- Thanks to `sneakers-the-rat  <https://github.com/sneakers-the-rat>`__ and
  `PipeKnight <https://github.com/PipeKnight>`__ for
  reporting a bug when encountering attributes that are not pydantic fields
  `#123 <https://github.com/mansenfranzen/autodoc_pydantic/issues/123>`__,
  `#128 <https://github.com/mansenfranzen/autodoc_pydantic/issues/128>`__.
- Thanks to `iwishiwasaneagle  <https://github.com/iwishiwasaneagle>`__ and
  `nickeldan <https://github.com/nickeldan>`__ for
  reporting a bug pydantic models were documented as class attributes or
  ``ModelInspector.from_child_signode`` returned the incorrect model reference
  `#124 <https://github.com/mansenfranzen/autodoc_pydantic/issues/123>`__,
  `#129 <https://github.com/mansenfranzen/autodoc_pydantic/issues/128>`__.

Internal
~~~~~~~~

- Renamed ``from_signode`` to ``from_child_signode`` for better clarity.
- Added explicit check to raise an exception if loaded object in
  ``ModelInspector.from_child_signode`` is not a pydantic model.


v1.7.1 - 2022-05-30
-------------------

This is a bugfix release supporting sphinx 5.0.

Bugfix
~~~~~~

- Adjust modified function signature of
  ``sphinx.ext.autodoc.ClassDocumenter.add_content`` in sphinx 5.0 which causes
  a type error otherwise
  `#125 <https://github.com/mansenfranzen/autodoc_pydantic/issues/125>`__ .

Packaging
~~~~~~~~~

- Convert ``sphinx-tabs`` and ``sphinxcontrib-mermaid`` to optional deps and
  relax their version specification.

Testing
~~~~~~~

- Add sphinx 5.0 to test matrix.
- Adjust several tests for changed default behaviour of
  ``autodoc_typehints_format``.

Contributors
~~~~~~~~~~~~

- Thanks to `lukehsiao <https://github.com/lukehsiao>`__ for
  reporting breaking changes in sphinx 5.0
  `#125 <https://github.com/mansenfranzen/autodoc_pydantic/issues/125>`__ .

v1.7.0 - 2022-05-18
-------------------

This is a feature release.

Changing behavior
~~~~~~~~~~~~~~~~~

- Default values of pydantic fields such as ``UndefinedPydantic`` and
  ``Ellipsis`` will now be shown as ``None``.

Bugfix
~~~~~~

- Fix missing validator-field references in ``model-show-validator-summary`` in
  case a single validator method process multiple fields.

Feature
~~~~~~~

- Add ``autodoc_pydantic_field_show_optional`` configuration which provides
  ``[Optional]`` marker for pydantic fields with ``default_factory``. This
  configuration is activated by default. If deactivated, default values might
  be displayed incorrectly. For more, see
  `#114 <https://github.com/mansenfranzen/autodoc_pydantic/issues/114>`__
- Add ``autodoc_pydantic_field_swap_name_and_alias`` configuration which allows
  to use a field's alias as a name instead of the original field name
  `#99 <https://github.com/mansenfranzen/autodoc_pydantic/issues/99>`__ .
- Respect interaction between ``autodoc_pydantic_field_swap_name_and_alias``
  with ``model-show-validator-summary``, ``model-show-field-summary``,
  ``validator-replace-signature`` and ``validator-list-fields`` by replacing
  the field name with field alias in rendered documentation.

Internals
~~~~~~~~~

- Determining default values of pydantic fields no longer use
  ``Field.field_info.default`` but ``Field.default``. As a consequence,
  default values such as ``UndefinedPydantic`` and ``Ellipsis`` will now be
  shown as ``None``.
- Autodocumenter ``PydanticFieldDocumenter`` now passes ``field-show-alias``
  and ``alias`` to ``PydanticField`` directive. Before, only ``alias`` was
  passed with value to denote ``field-show-alias``. However, since
  ``field-swap-name-and-alias`` was added, the value of the alias might be
  required even without ``field-show-alias`` being activated.
- Refactor and split ``PydanticModelDocumenter.add_validators_summary`` in
  multiple methods for better readability and maintainability.
- Add ``get_field_name_or_alias`` to ``PydanticAutoDoc`` to centrally manage
  the determination of field name/alias for all auto-documenters.
- Rename ``sanitize_configuration_option_name`` into ``determine_app_cfg_name``
  in ``directives/options/composites.py`` for better clarity.
- Add ``configuration_names`` to ``AutoDocOptions`` to distinguish foreign
  directive options in ``determine_app_cfg_name`` which is required because
  ``field-swap-name-and-alias`` is also used by model/validator
  auto-documenters.

Documentation
~~~~~~~~~~~~~

- Add example section for ``field-swap-name-and-alias``.
- Add configuration description for ``field-swap-name-and-alias``.

Contributors
~~~~~~~~~~~~

- Thanks to `spacemanspiff2007 <https://github.com/spacemanspiff2007>`__ for
  providing and supporting a feature request to show ``[Optional]`` marker
  `#114 <https://github.com/mansenfranzen/autodoc_pydantic/issues/114>`__ and
  a feature request to swap name and alias
  `#99 <https://github.com/mansenfranzen/autodoc_pydantic/issues/99>`__ .

v1.6.2 - 2022-04-15
-------------------

This is a documentation and bugfix release supporting sphinx 4.5.

Bugfix
~~~~~~

- Fix incorrect source-to-doc hyperlink in users example section
  `#96 <https://github.com/mansenfranzen/autodoc_pydantic/issues/96>`__.
- Fix incorrect ``[Required]`` mark for optional fields like ``Optional[int]``
  `#97 <https://github.com/mansenfranzen/autodoc_pydantic/issues/97>`__.
- Fix incorrect warning of JSON non-serializable field in case of composite
  types like ``Union``.
  `#98 <https://github.com/mansenfranzen/autodoc_pydantic/issues/98>`__.
- Fix incorrect showing of additional keyword arguments passed to pydantic
  `Field` in the field's constraint documentation section
  `#110 <https://github.com/mansenfranzen/autodoc_pydantic/issues/110>`__.

Documentation
~~~~~~~~~~~~~

- Separate example page into configuration and specifics.
- Add examples for required and optional values.
- Add examples for generic models.
- Use separate python modules for user's usage and example sections to prevent
  ambiguous source-to-doc hyperlinks.

Testing
~~~~~~~

- Add sphinx 4.5 to CI.
- Add test to ensure that optional fields do not have the ``[Required]`` mark.
- Add test to ensure that pydantic field with composite type like ``Union`` is
  correctly identified as JSON serializable.
- Add test to ensure that additional keyword arguments passed to pydantic
  `Field` are not shown in the field's constraint documentation section.
- Pin ``jinja2<3.1.0`` for ``sphinx<4`` to fix broken CI.

Contributors
~~~~~~~~~~~~

- Thanks to `jgunstone <https://github.com/jgunstone>`__ for reporting a bug
  regarding incorrect source-to-doc hyperlink in users example section.
- Thanks to `Czaki <https://github.com/Czaki>`__ for reporting a bug regarding
  incorrect warning of JSON non-serializable field in case of composite types
  like ``Union``.
- Thanks to `StigKorsnes <https://github.com/StigKorsnes>`__ for reporting a
  bug regarding incorrect ``[Required]`` mark for optional fields like
  ``Optional[int]``
- Thanks to `spacemanspiff2007 <https://github.com/spacemanspiff2007>`__ for
  reporting a bug regarding incorrect showing of additional keyword arguments
  passed to pydantic `Field` in the field's constraint documentation section.

v1.6.1 - 2022-01-28
-------------------

This is a minor bugfix release including support for sphinx 4.4.

Bugfix
~~~~~~

- Fix incorrect rendering of pydantic field's ``description`` attribute which
  was not in line with default reST rendering of docstrings of classes or
  functions.
  `#91 <https://github.com/mansenfranzen/autodoc_pydantic/issues/91>`__.

Testing
~~~~~~~

- Add test to ensure that pydantic field's ``description`` attribute is
  correctly rendered.
- Add sphinx 4.4 to CI.
- Simplify ``test_autodoc_pydantic_settings_hide_paramlist_false`` replacing
  version specifics with generic assert function.

Contributors
~~~~~~~~~~~~

- Thanks to `iliakur <https://github.com/iliakur>`__ for reporting the
  incorrect reST rendering of pydantic field's ``description`` attribute.

v1.6.0 - 2022-01-03
-------------------

This is a feature and bug fix release including support for pydantic 1.9.

Changing behavior
~~~~~~~~~~~~~~~~~

- Documented pydantic models/settings as class attributes will no longer show
  additional content
  `#78 <https://github.com/mansenfranzen/autodoc_pydantic/issues/78>`__.
- Generated docutils will now have additional fallback css classes
  `#77 <https://github.com/mansenfranzen/autodoc_pydantic/issues/77>`__.

Bugfix
~~~~~~

- Fix a bug which occurred while documenting a pydantic model as an attribute
  and using `bysource` for model summary list order
  `#78 <https://github.com/mansenfranzen/autodoc_pydantic/issues/78>`__.

Feature
~~~~~~~

- Remove any additional content generated by **autodoc_pydantic** for
  pydantic models/settings when documented as an attribute
  `#78 <https://github.com/mansenfranzen/autodoc_pydantic/issues/78>`__.
- By default add fallback css classes for all docutils generated by
  **autodoc_pydantic**. This can be deactivated via newly added config
  ``autodoc_pydantic_add_fallback_css_class``
  `#77 <https://github.com/mansenfranzen/autodoc_pydantic/issues/77>`__.

Testing
~~~~~~~

- Add tests to ensure that no additional content is provided if model/settings
  are documented as an attribute, see `test_edgecases`.
- Add tests to ensure that fallback css classes are added if required,
  see `test_events`.
- Streamline naming convention for tests regarding edge cases.
- Adjust tests to comply with pydantic 1.9.
- Add pydantic 1.9 to CI.
- Add ``prod_app`` fixture to run production sphinx app based on cmd line entry
  point while returning captured sphinx app and doctrees.
- Provide important doc strings to existing ``autodocument``, ``parst_rst`` and
  ``test_app`` fixtures for better understandability.

Documentation
~~~~~~~~~~~~~

- Add FAQ section describing changed behaviour of models/settings when used
  as class attributes.
- Add FAQ section describing fallback css classes.
- Rename ``BaseModel`` to ``Model`` and ``BaseSettings`` to ``Settings`` in
  configuration section.
- Add ``autodoc_pydantic_add_fallback_css_class`` setting to users
  configuration page.
- Add ``ShowVersions`` directive to show relevant package versions of current
  documentation build environment in setup page of developer documentation.

Contributors
~~~~~~~~~~~~

- Thanks to `StigKorsnes <https://github.com/StigKorsnes>`__ for reporting an
  unexpected behavior when using **autodoc_pydantic** with themes like
  Jupyter-Book that rely on setting css styles for default sphinx autdoc
  objtypes ``class``, ``attribute`` and ``method``
  `#77 <https://github.com/mansenfranzen/autodoc_pydantic/issues/77>`__.
- Thanks to `nchaly <https://github.com/nchaly>`__ for reporting a bug and
  raising the topic of how to document models/settings as an attribute
  `#78 <https://github.com/mansenfranzen/autodoc_pydantic/issues/78>`__.

v1.5.1 - 2021-11-12
-------------------

This is a minor bug fix release with testing and documentation improvements.
Additionally, it adds support for sphinx 4.3.

Bugfix
~~~~~~

- Fix a corner-case where a module that imported
  ``numpy.typing.NDArray`` caused autodoc_pydantic to experience
  an uncaught exception
  `#57 <https://github.com/mansenfranzen/autodoc_pydantic/issues/57>`__.

Internal
~~~~~~~~

- Account for modified method signature in ``get_signature_prefix`` in sphinx
  4.3 `#62 <https://github.com/mansenfranzen/autodoc_pydantic/issues/62>`__.

Testing
~~~~~~~

- Fix broken CI for sphinx 3.4 due to unpinned versions of ``docutils``. This
  generates new sphinx loggings which have not been present before that in turn
  cause tests to fail which are dependent on inspecting sphinx loggings
  `#68 <https://github.com/mansenfranzen/autodoc_pydantic/issues/68>`__.
- Add sphinx 4.3 to CI matrix.
- Add compatibility module to abstract away minor implementation differences
  between sphinx versions 4.3 and prior.
- Add tests for development versions while continuing on error.
- Replace codacy with codecov for code coverage reports.
- Add code coverage for all stable and latest version.
- Allow CI to be executed on pull requests from forks of new contributors.

Documentation
~~~~~~~~~~~~~

- Add ``Exclude __init__ docstring`` section to FAQ of the user guide
  `#58 <https://github.com/mansenfranzen/autodoc_pydantic/issues/58>`__.
- Add github issue links to topics of FAQ of the user guide.

Contributors
~~~~~~~~~~~~

- Thanks to `j-carson <https://github.com/j-carson>`__ for reporting a bug
  and providing a PR related to autodoc_pydantic's inspection module
  `#57 <https://github.com/mansenfranzen/autodoc_pydantic/issues/57>`__.
- Thanks to `Yoshanuikabundi <https://github.com/Yoshanuikabundi>`__  and
  `jakobandersen <https://github.com/jakobandersen>`__ for reporting and
  mitigating a compatibility issue with sphinx 4.3
  `#62 <https://github.com/mansenfranzen/autodoc_pydantic/issues/62>`__.
- Thanks to `lilyminium <https://github.com/lilyminium>`__ for adding the
  ``Exclude __init__ docstring`` section to FAQ of the user guide
  `#58 <https://github.com/mansenfranzen/autodoc_pydantic/issues/58>`__.

v1.5.0 - 2021-10-10
-------------------

This release includes major internal refactorings, new documentation sections,
a new feature, a bug fix and tests for new sphinx and python versions.

Added
~~~~~

- Provide ``summary-list-order`` configuration property which allows to sort
  summary list items in alphabetical order or by source.

Bugfix
~~~~~~

- Using ``@root_validator(pre=True)`` caused the sphinx build process to fail
  due to an incorrect implementation. This has been fixed.
  `#55 <https://github.com/mansenfranzen/autodoc_pydantic/issues/55>`__.

Testing
~~~~~~~

- Refactor all configuration test modules removing repeated function arguments
  to increase readability and maintainability.
- Add specific test to ensure that using ``@root_validator(pre=True)`` does not
  break the sphinx build process.
- Add sphinx versions ``4.1.0`` and ``4.2.0`` to CI matrix.
- Add python version ``3.10`` to CI matrix.

Documentation
~~~~~~~~~~~~~

- Add section in configuration page describing ``summary-list-order``.
- Add developer design section providing gentle introduction to code base.
- Add developer guides focusing on concrete implementation details.
- Add class diagrams via mermaid.js.
- Streamline naming convention for ``TabDocDirective`` for better clarity.
- Add ``version`` parameter to ``TabDocDirective`` to show the version in which
  a configuration property was added.
- Add API documentation for selected modules including directory tree with
  references.
- Activate ``sphinxcontrib.mermaid`` and ``sphinx.ext.viewcode`` extensions.

Internal
~~~~~~~~

- Completely remove the ``ModelWrapper`` with the ``ModelInspector`` with all
  its composite classes.
- Moving inspection logic from auto-documenters to ``ModelInspector``.
- Streamline naming conventions for composite classes.
- Create separate sub directory for directive options including individual
  modules for composites, definitions, enums and validators.
- Move reST templates to separate module.

Packaging
~~~~~~~~~

- Update to newest versions of ``sphinx-rtd-theme`` and ``sphinx-tabs``.
- Add ``sphinxcontrib-mermaid`` under dev and doc dependencies.

Contributors
~~~~~~~~~~~~

- Thanks to `goroderickgo <https://github.com/goroderickgo>`__ for reporting a bug
  related to pre root validators breaking the sphinx build process
  `#55 <https://github.com/mansenfranzen/autodoc_pydantic/issues/55>`__.

v1.4.0 - 2021-08-20
-------------------

This is a feature and bug release.

Added
~~~~~

- Provide ``field-show-required`` configuration property. If activated, it adds
  a ``[Required]`` marker for pydantic fields which do not have a default value.
  Otherwise, misleading default values like *Ellipsis* or *PydanticUndefined*
  are shown.
  `#34 <https://github.com/mansenfranzen/autodoc_pydantic/issues/34>`__.
- Include ``show-json-error-strategy`` for pydantic models and settings to define
  error handling in case a pydantic field breaks the JSON schema generation
  `#8 <https://github.com/mansenfranzen/autodoc_pydantic/issues/8>`__.

Bugfix
~~~~~~

- Respect ``inherited-members`` for field and validator summaries to prevent
  different members being displayed between header and body `#32 <https://github.com/mansenfranzen/autodoc_pydantic/issues/32>`__.
- Improve handling of non serializable pydantic fields for JSON model generation.
  Using ``pd.DataFrame`` as a type annotation raised an exception instead of being
  handled appropriately `#28 <https://github.com/mansenfranzen/autodoc_pydantic/issues/28>`__.
- Allow typed fields within doc strings to successfully reference pydantic models
  and settings `#27 <https://github.com/mansenfranzen/autodoc_pydantic/issues/27>`__.
- Remove ``env`` key from field constraints.

Testing
~~~~~~~

- Add explicit tests for references originating from typed fields.
- Add more diverse tests for handling non serializable fields breaking JSON model
  generation.
- Add tests for different error handling strategies regarding ``show-json-error-strategy``.
- Add tests for ``field-show-required``.
- Add tests for field and validator summaries respecting ``inherited-members``.

Documentation
~~~~~~~~~~~~~

- Add section in configuration page describing ``show-json-error-strategy``.
- Add section in configuration page describing ``field-show-required``.
- Add FAQ page with section about using ``inherited-members``.
- Generally overhaul the documentation to improve readability and conciseness.

Contributors
~~~~~~~~~~~~

- Thanks to `davidchall <https://github.com/davidchall>`__ for suggesting to add a
  ``[Required]`` marker for mandatory pydantic fields `#34 <https://github.com/mansenfranzen/autodoc_pydantic/issues/34>`__.
- Thanks to `matutter <https://github.com/matutter>`__ for reporting a bug
  related to incorrect field and validator summaries not respecting ``inherited-members``
  `#32 <https://github.com/mansenfranzen/autodoc_pydantic/issues/32>`__.
- Thanks to `thomas-pedot <https://github.com/thomas-pedot>`__ for reporting a bug related to
  error handling of pydantic fields breaking JSON schema generation `#28 <https://github.com/mansenfranzen/autodoc_pydantic/issues/28>`__.
- Thanks to `tahoward <https://github.com/tahoward>`__ for reporting a bug related to
  missing references in typed fields `#27 <https://github.com/mansenfranzen/autodoc_pydantic/issues/27>`__.

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
   ``PydanticField``, ``PydanticValidator``

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

