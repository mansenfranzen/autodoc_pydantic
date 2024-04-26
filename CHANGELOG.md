# Changelog

## [2.2.0](https://github.com/mansenfranzen/autodoc_pydantic/compare/v2.1.0...v2.2.0) (2024-04-26)


### ✨ Features

* Allow empty strings for directive prefixes ([#285](https://github.com/mansenfranzen/autodoc_pydantic/issues/285)) ([be21d37](https://github.com/mansenfranzen/autodoc_pydantic/commit/be21d377d085bde35ac608e68d79b1fe3d70ddf0))
* Remove duplicated docs strings when `use_attribute_docstrings` is used in `pydantic &gt;= 2.7` ([#276](https://github.com/mansenfranzen/autodoc_pydantic/issues/276)) ([0ddb12f](https://github.com/mansenfranzen/autodoc_pydantic/commit/0ddb12ff0ad98ae79116dc1701e2700685a1a568))


### 🐛 Bug Fixes

* **deps:** update dependency erdantic to &lt;v2 ([#246](https://github.com/mansenfranzen/autodoc_pydantic/issues/246)) ([3c8daa8](https://github.com/mansenfranzen/autodoc_pydantic/commit/3c8daa8cdb5c4c643dbcea62ee7aa02982006a65))
* **deps:** update dependency erdantic to ^0.7.0 ([#226](https://github.com/mansenfranzen/autodoc_pydantic/issues/226)) ([0909963](https://github.com/mansenfranzen/autodoc_pydantic/commit/09099635fdbd0675cf4f3a3e4da7db1b3a3fe2eb))
* **deps:** update dependency flake8 to v7 ([#233](https://github.com/mansenfranzen/autodoc_pydantic/issues/233)) ([c270e8a](https://github.com/mansenfranzen/autodoc_pydantic/commit/c270e8ae447f9c65659f1d718c458f768c91be6b))
* **deps:** update dependency pytest to v8 ([#234](https://github.com/mansenfranzen/autodoc_pydantic/issues/234)) ([8b330af](https://github.com/mansenfranzen/autodoc_pydantic/commit/8b330af0905ea91439a0ed0ff23d8512eb1445b6))
* **deps:** update dependency sphinx-copybutton to ^0.5.0 ([#227](https://github.com/mansenfranzen/autodoc_pydantic/issues/227)) ([7ada937](https://github.com/mansenfranzen/autodoc_pydantic/commit/7ada937a62da35f7715edf3b5e2a441075cc6457))
* **deps:** update dependency sphinx-rtd-theme to v2 ([#235](https://github.com/mansenfranzen/autodoc_pydantic/issues/235)) ([f43cfa9](https://github.com/mansenfranzen/autodoc_pydantic/commit/f43cfa914a9eb7d74ea66c588f124c3aed3a315f))
* **deps:** update dependency sphinxcontrib-mermaid to ^0.9.0 ([#229](https://github.com/mansenfranzen/autodoc_pydantic/issues/229)) ([984ce05](https://github.com/mansenfranzen/autodoc_pydantic/commit/984ce051e3dba7f2ecf267662ecb8cfdd4411ae3))
* Improve error message for `_sort_summary_list` failures ([#243](https://github.com/mansenfranzen/autodoc_pydantic/issues/243)) ([87923a1](https://github.com/mansenfranzen/autodoc_pydantic/commit/87923a128d32343a6291d29c996a413994ede89c))
* Test please-release ([d4595bf](https://github.com/mansenfranzen/autodoc_pydantic/commit/d4595bf403ce0f85a23572397c0f12bffb68f3ef))
* Use more precise `name` instead of `object_name` for `_sort_summary_list` error msg ([#244](https://github.com/mansenfranzen/autodoc_pydantic/issues/244)) ([42bdd4b](https://github.com/mansenfranzen/autodoc_pydantic/commit/42bdd4bd2788b0a2eb2f932847355a153ce7ebd8))


### ⛏ Other Changes

* Add `changelog-sections` to please-release ([#218](https://github.com/mansenfranzen/autodoc_pydantic/issues/218)) ([5355f98](https://github.com/mansenfranzen/autodoc_pydantic/commit/5355f98d77c5b0fe94358f4109d22d89a1eaedf2))
* Add `refactor` and more categories to release-please configuration. ([#258](https://github.com/mansenfranzen/autodoc_pydantic/issues/258)) ([71e1c60](https://github.com/mansenfranzen/autodoc_pydantic/commit/71e1c605be3d05aabb739d7c36d6a201ba57e465))
* Add Coduim PR Agent Workflow ([#236](https://github.com/mansenfranzen/autodoc_pydantic/issues/236)) ([38f9e16](https://github.com/mansenfranzen/autodoc_pydantic/commit/38f9e16525904223be867d6799a880e9aae16d95))
* Configure Renovate ([#225](https://github.com/mansenfranzen/autodoc_pydantic/issues/225)) ([efc2f9a](https://github.com/mansenfranzen/autodoc_pydantic/commit/efc2f9aefec73d6f6cfa8fe521e8eca4406fc148))
* Deactivate dependency dashboard ([#238](https://github.com/mansenfranzen/autodoc_pydantic/issues/238)) ([11afaf3](https://github.com/mansenfranzen/autodoc_pydantic/commit/11afaf39160d1ad628b08dc3fc1024af6c396235))
* **deps:** update abatilo/actions-poetry action to v3 ([#230](https://github.com/mansenfranzen/autodoc_pydantic/issues/230)) ([be248a4](https://github.com/mansenfranzen/autodoc_pydantic/commit/be248a466885393c9e1420ecff60b64ce9132d0c))
* **deps:** update actions/checkout action to v4 ([#231](https://github.com/mansenfranzen/autodoc_pydantic/issues/231)) ([5774bdf](https://github.com/mansenfranzen/autodoc_pydantic/commit/5774bdf6340500a362709afdf8814efcfaea4d6a))
* **deps:** update actions/setup-python action to v5 ([#232](https://github.com/mansenfranzen/autodoc_pydantic/issues/232)) ([2bc973b](https://github.com/mansenfranzen/autodoc_pydantic/commit/2bc973b9704b2dab6c9122eee15930a4f7deecce))
* fix link in all-contributors bot ([#281](https://github.com/mansenfranzen/autodoc_pydantic/issues/281)) ([8261254](https://github.com/mansenfranzen/autodoc_pydantic/commit/8261254f868ae68149aa86433b4d0f69a01ad80c))
* improve changelog ([b22840f](https://github.com/mansenfranzen/autodoc_pydantic/commit/b22840f1095cf82256a56d9fb2f27bd1710dae6c))
* Remove `dev` extras and `tox` from pyproject.toml ([204f246](https://github.com/mansenfranzen/autodoc_pydantic/commit/204f24669d643505edb7be4acf07a856948e5027))
* Remove dependabot in favor for Mend's renovate ([#267](https://github.com/mansenfranzen/autodoc_pydantic/issues/267)) ([9726cc5](https://github.com/mansenfranzen/autodoc_pydantic/commit/9726cc56e37f0659d33840aec1337fe00e1d39a8))
* Revert all-contributors commit type ([#282](https://github.com/mansenfranzen/autodoc_pydantic/issues/282)) [skip ci] ([c4c8fe7](https://github.com/mansenfranzen/autodoc_pydantic/commit/c4c8fe7c05fcc5044eac841efdb9720488b195f9))
* Use ruff for linting and formatting ([#242](https://github.com/mansenfranzen/autodoc_pydantic/issues/242)) ([461be30](https://github.com/mansenfranzen/autodoc_pydantic/commit/461be30c98424f561a7c7d5d8a5ff275a18fad7a))


### 📖 Documentation

* add exs-dwoodward as a contributor for code ([#250](https://github.com/mansenfranzen/autodoc_pydantic/issues/250)) ([532b54f](https://github.com/mansenfranzen/autodoc_pydantic/commit/532b54fbcdb409b8cb0b46b6db361db779610602))
* Add hint mentioning that pydantic directive prefixes allow empty strings ([be21d37](https://github.com/mansenfranzen/autodoc_pydantic/commit/be21d377d085bde35ac608e68d79b1fe3d70ddf0))
* Add missing erdantic version number ([#224](https://github.com/mansenfranzen/autodoc_pydantic/issues/224)) ([4c9c6b2](https://github.com/mansenfranzen/autodoc_pydantic/commit/4c9c6b2031734ace78b8fe61db26b940ebd89160))
* Fix broken link in example section ([40b5b22](https://github.com/mansenfranzen/autodoc_pydantic/commit/40b5b22119b0e83ef9d2d861ddc37cde9e835740))
* Improve `README.md` with update badges and remove animated gif comparison examples ([40b5b22](https://github.com/mansenfranzen/autodoc_pydantic/commit/40b5b22119b0e83ef9d2d861ddc37cde9e835740))
* improve erdantic example ([3c8daa8](https://github.com/mansenfranzen/autodoc_pydantic/commit/3c8daa8cdb5c4c643dbcea62ee7aa02982006a65))
* Recommend globally installed tox instead of poetry installed tox ([#223](https://github.com/mansenfranzen/autodoc_pydantic/issues/223)) ([204f246](https://github.com/mansenfranzen/autodoc_pydantic/commit/204f24669d643505edb7be4acf07a856948e5027))
* Remove pydantic v1/v2 branch note from developer setup guide ([204f246](https://github.com/mansenfranzen/autodoc_pydantic/commit/204f24669d643505edb7be4acf07a856948e5027))
* Replace Sphinx `index.rst` with repo's `README.md` ([#270](https://github.com/mansenfranzen/autodoc_pydantic/issues/270)) ([40b5b22](https://github.com/mansenfranzen/autodoc_pydantic/commit/40b5b22119b0e83ef9d2d861ddc37cde9e835740))
* Use `myst_parser` to include `CHANGELOG.md` instead of rst ([#245](https://github.com/mansenfranzen/autodoc_pydantic/issues/245)) ([e6fe9e1](https://github.com/mansenfranzen/autodoc_pydantic/commit/e6fe9e1f59ff9d6758cebdb1a4f0aa17be15fb49))


### 🚀 CI/CD Pipeline

* Add `pip-audit` security scanner ([#268](https://github.com/mansenfranzen/autodoc_pydantic/issues/268)) ([0be2710](https://github.com/mansenfranzen/autodoc_pydantic/commit/0be2710fccf05907489d2f5d9961e09081469733))
* Add daily scheduled GH workflow with test for pre-release versions ([#265](https://github.com/mansenfranzen/autodoc_pydantic/issues/265)) ([a4c5140](https://github.com/mansenfranzen/autodoc_pydantic/commit/a4c514027be956ad2a29e35ef8ae88c3a82ed758))
* Add dependabot configuration ([#248](https://github.com/mansenfranzen/autodoc_pydantic/issues/248)) ([dc0a81d](https://github.com/mansenfranzen/autodoc_pydantic/commit/dc0a81d9cecd74a13befed4b1f7ed5808bec992c))
* Add explicit `pydantic_settings` versions to prevent unwanted pydantic version upgrades in CI matrix ([#263](https://github.com/mansenfranzen/autodoc_pydantic/issues/263)) ([2c5c4d5](https://github.com/mansenfranzen/autodoc_pydantic/commit/2c5c4d53d07472f8c15050aa3ff348e09dfcda10))
* Add pydantic 2.7 to test matrix ([#253](https://github.com/mansenfranzen/autodoc_pydantic/issues/253)) ([afdec96](https://github.com/mansenfranzen/autodoc_pydantic/commit/afdec966659d994c585d8a7f0df27b7eb4212813))
* fix broken tox environment naming convention preventing correct version selection ([134c3cb](https://github.com/mansenfranzen/autodoc_pydantic/commit/134c3cb00ec961e3294fb2b81c690e84a7a8202f))
* Fix incorrect tox env name for security scans ([#271](https://github.com/mansenfranzen/autodoc_pydantic/issues/271)) ([bcb9ee0](https://github.com/mansenfranzen/autodoc_pydantic/commit/bcb9ee09784a61e44d7f50b8009e19306e2db37d))
* Ignore release-please branches for CI tests ([#221](https://github.com/mansenfranzen/autodoc_pydantic/issues/221)) ([5f4c0dc](https://github.com/mansenfranzen/autodoc_pydantic/commit/5f4c0dc46f55c9935e2de6645a93738f14b094a1))
* Integrate `mypy` type checking ([#259](https://github.com/mansenfranzen/autodoc_pydantic/issues/259)) ([134c3cb](https://github.com/mansenfranzen/autodoc_pydantic/commit/134c3cb00ec961e3294fb2b81c690e84a7a8202f))
* Move publish step into release-please workflow ([#237](https://github.com/mansenfranzen/autodoc_pydantic/issues/237)) ([0864395](https://github.com/mansenfranzen/autodoc_pydantic/commit/0864395bf15750e5a514a7feac7b1c65f8875a5c))
* Protect workflows via CODEOWNERS and explicit user matching ([#240](https://github.com/mansenfranzen/autodoc_pydantic/issues/240)) ([c07d1f2](https://github.com/mansenfranzen/autodoc_pydantic/commit/c07d1f2223897d2fa5983423bbe73ac73a624fee))
* Refactor CI with resusable, custom GitHub Action ([#252](https://github.com/mansenfranzen/autodoc_pydantic/issues/252)) ([0d582c7](https://github.com/mansenfranzen/autodoc_pydantic/commit/0d582c7bdd08425c6a267fc06c0cdac58b8fab2d))
* Replace flake8 with ruff for linting/formatting ([461be30](https://github.com/mansenfranzen/autodoc_pydantic/commit/461be30c98424f561a7c7d5d8a5ff275a18fad7a))
* Streamline GH workflow names ([0be2710](https://github.com/mansenfranzen/autodoc_pydantic/commit/0be2710fccf05907489d2f5d9961e09081469733))
* Support pydantic 2.7 and sphinx 7.3 ([#261](https://github.com/mansenfranzen/autodoc_pydantic/issues/261)) ([a797a77](https://github.com/mansenfranzen/autodoc_pydantic/commit/a797a771bdc1bc5c8b7e9a345ea34b6156a610ef))
* Update codcov GH action to newest version ([#219](https://github.com/mansenfranzen/autodoc_pydantic/issues/219)) ([b129602](https://github.com/mansenfranzen/autodoc_pydantic/commit/b1296028cc98f9b630c163e1483eed01d6011077))
* Update GH Actions to newest Versions ([#222](https://github.com/mansenfranzen/autodoc_pydantic/issues/222)) ([5a21c2a](https://github.com/mansenfranzen/autodoc_pydantic/commit/5a21c2a2211153d0b914b47d3fa4213741d1e9d5))


### 🔧 Testing

* Fix warnings due to deprecated test examples ([#273](https://github.com/mansenfranzen/autodoc_pydantic/issues/273)) ([65ed9cc](https://github.com/mansenfranzen/autodoc_pydantic/commit/65ed9cc4479992fc01681dc6a18727cc93154bb3))
* remove `package_is_missing` ([3c8daa8](https://github.com/mansenfranzen/autodoc_pydantic/commit/3c8daa8cdb5c4c643dbcea62ee7aa02982006a65))
* Remove obsolete test classes ([65ed9cc](https://github.com/mansenfranzen/autodoc_pydantic/commit/65ed9cc4479992fc01681dc6a18727cc93154bb3))
* simplify erdantic tests ([3c8daa8](https://github.com/mansenfranzen/autodoc_pydantic/commit/3c8daa8cdb5c4c643dbcea62ee7aa02982006a65))


### 🔨 Refactoring

* Move extension setup logic into seperate `application` module ([#264](https://github.com/mansenfranzen/autodoc_pydantic/issues/264)) ([e8f7f06](https://github.com/mansenfranzen/autodoc_pydantic/commit/e8f7f062bd8a1a5499dd9ec487700ea17c9d97b6))
* rename `PydanticDirectiveBase` to `PydanticDirectiveMixin` for better clarity ([134c3cb](https://github.com/mansenfranzen/autodoc_pydantic/commit/134c3cb00ec961e3294fb2b81c690e84a7a8202f))
* restructure sphinx app cfg values in `__init__` ([134c3cb](https://github.com/mansenfranzen/autodoc_pydantic/commit/134c3cb00ec961e3294fb2b81c690e84a7a8202f))


### ⬆️ Dependency Updates

* update dependency myst-parser to v3 ([#269](https://github.com/mansenfranzen/autodoc_pydantic/issues/269)) ([4c3e61f](https://github.com/mansenfranzen/autodoc_pydantic/commit/4c3e61f8ac9de9bb1337bd2c14301f5c8ae103e7))
* update dependency ruff to ^0.4.0 ([#256](https://github.com/mansenfranzen/autodoc_pydantic/issues/256)) ([4eb1629](https://github.com/mansenfranzen/autodoc_pydantic/commit/4eb162960bf25285fbe858dfbb45f05638bf99b3))


### 👥 Contributors

* add annerademacher as a contributor for financial ([#284](https://github.com/mansenfranzen/autodoc_pydantic/issues/284)) ([80cf3e9](https://github.com/mansenfranzen/autodoc_pydantic/commit/80cf3e9d6f9c363c4eadf53104c4480e932ba7fa))
* add azmeuk as a contributor for bug ([#286](https://github.com/mansenfranzen/autodoc_pydantic/issues/286)) ([36056f7](https://github.com/mansenfranzen/autodoc_pydantic/commit/36056f793d5729974872034c3bda5b7e346e0b14))
* add bruno-f-cruz as a contributor for bug ([#280](https://github.com/mansenfranzen/autodoc_pydantic/issues/280)) ([47e98df](https://github.com/mansenfranzen/autodoc_pydantic/commit/47e98dffce7373ac2e7ad48c6f1ae38f6455c6de))
* add Carson-Shaar as a contributor for bug ([#278](https://github.com/mansenfranzen/autodoc_pydantic/issues/278)) [skip ci] ([bc4cdb6](https://github.com/mansenfranzen/autodoc_pydantic/commit/bc4cdb6a96587100ee9dd35b15732b1025f693e3))
* add Galarzaa90 as a contributor for bug ([#277](https://github.com/mansenfranzen/autodoc_pydantic/issues/277)) ([15cead4](https://github.com/mansenfranzen/autodoc_pydantic/commit/15cead49f007b6200bf671ce0f6b5b2a5427924c))
* add ITProKyle as a contributor for bug ([#279](https://github.com/mansenfranzen/autodoc_pydantic/issues/279)) [skip ci] ([2a899f1](https://github.com/mansenfranzen/autodoc_pydantic/commit/2a899f132a4204cb2c22b2be74f937a5e07f6fd3))
* add lwasser as a contributor for bug ([#262](https://github.com/mansenfranzen/autodoc_pydantic/issues/262)) ([83d2b94](https://github.com/mansenfranzen/autodoc_pydantic/commit/83d2b948e4c2b8437720ff64666e06763ac854a7))

## v2.1.0 - 2024-03-18

This is a maintenance and bugfix release extending support to pydantic
v2.6, sphinx v7.2 and python 3.12 while dropping support for python 3.7
which has reached EOL.

### Features

-   Hide `model_computed_fields` for pydantic models.
-   Hide `settings_customise_sources` for pydantic settings.

### Testing

-   Add pydantic 2.2/2.3/2.4/2.5/2.6 and sphinx 7.1/7.2 and python 3.12
    to test matrix.
-   Remove python 3.7 from test matrix.
-   Remove obsolete `skip ci` condition from github actions.
-   Update `conftest` to use `pathlib` instead of older Sphinx
    `sphinx.testing.path` module that is being deprecated for
    forward-compatibility with newer Sphinx versions.
-   Fix duplicated teset name `test_non_field_attributes`.
-   Add tests to cover inheritance behavior given `inherited-members`
    for field and validator members and summaries.

### Bugfix

-   Fix incompatibity with sphinx 7.2 due to changed usage of path
    objects. For more, see
    [#11606](https://github.com/sphinx-doc/sphinx/issues/11605).
-   [#176](https://github.com/mansenfranzen/autodoc_pydantic/issues/176)
    Remove `sphinxcontrib/__init__.py` causing `ModuleNotFoundError`
    exception in some environments. This should be a namespace package
    per [PEP 420](https://peps.python.org/pep-0420/) without
    `__init_.py` to match with other extensions.
-   Removing deprecation warning `sphinx.util.typing.stringify`.
-   Fix bug a bug while sorting members
    [#137](https://github.com/mansenfranzen/autodoc_pydantic/issues/137).

### Internal

-   Fix deprecation warning for tuple interface of `ObjectMember` in
    `directives/autodocumenters.py`.
-   Remove obsolete configuration options which have been removed in v2.
-   Introduce `pydantic.options.exists` to check for existence of sphinx
    options.

### Documentation

-   Add pydantic to PyPI classifiers to improve discoverability.
-   Correct erdantic installation command in users coniguration section.
-   Improve users FAQ regarding documentation of inherited members.

### Contributors

-   Thanks to [devmonkey22](https://github.com/devmonkey22) for
    providing a PR to solve a nasty namespace package issue
    [#176](https://github.com/mansenfranzen/autodoc_pydantic/issues/176)
    and [daquinteroflex](https://github.com/daquinteroflex) for testing
    and providing feedback.
-   Thanks to [rafa-guedes](https://github.com/rafa-guedes) for
    providing a PR to fix a deprecation warning for tuple interface of
    `ObjectMember` in `directives/autodocumenters.py`
    [#174](https://github.com/mansenfranzen/autodoc_pydantic/issues/174)
    and [j-carson](https://github.com/j-carson) for reporting it.
-   Thanks to [caerulescens](https://github.com/caerulescens) for
    providing a PR to add pydantic to PyPI classifiers
    [#179](https://github.com/mansenfranzen/autodoc_pydantic/pull/179).
-   Thanks to [spacemanspiff2007](https://github.com/spacemanspiff2007)
    for hiding `model_computed_fields` and `settings_customise_sources`
    [#202](https://github.com/mansenfranzen/autodoc_pydantic/pull/202).
-   Thanks to [tony](https://github.com/tony) for fixing a typo in the
    erdantic docs
    [#200](https://github.com/mansenfranzen/autodoc_pydantic/pull/200).
-   Thanks to [j-carson](https://github.com/j-carson) for providing a PR
    that:
    -   fixes a bug while sorting members
        [#137](https://github.com/mansenfranzen/autodoc_pydantic/issues/137).
    -   fixes broken CI pipeline with Sphinx 4.\*
    -   removing deprecation warning
        [#178](https://github.com/mansenfranzen/autodoc_pydantic/issues/178).

## v2.0.1 - 2023-08-01

This is a bugfix release handling an exception while documenting
pydantic models using enums.

### Internal

-   Simplify model field\'s constraint extraction removing dependency on
    private methods.

### Bugfix

-   Properly handle constraint extraction avoiding exceptions due to
    prior reliance on unpredictable behavior of private attributes.
-   Fix incorrect type annotation string results for non-builtin types
    in `intercept_type_annotations_py_gt_39`.

### Testing

-   Add pydantic 2.1 to test matrix.
-   Add tests for various kinds of constrained types.
-   Add \"no exception\" tests for specific pydantic models, such as
    containing enums.

### Contributors

-   Thanks to [nagledb](https://github.com/nagledb) for reporting a bug
    related to enums
    [#169](https://github.com/mansenfranzen/autodoc_pydantic/issues/169).
-   Thanks to [jerryjiahaha](https://github.com/jerryjiahaha) for
    providing a pull request fixing the enums bug
    [#170](https://github.com/mansenfranzen/autodoc_pydantic/pull/170).

## v2.0.0 - 2023-07-24

This is a major release supporting pydantic v2. In June 2023, pydantic
v2 was released while introducing backwards incompatible API and
behavioral changes in comparison to pydantic v1. Supporting pydantic v2
required substantial adjustments to the codebase leading to a new major
release of autodoc_pydantic (v1.9.0 -\> v2.0.0), too.

In order to keep the codebase clean and concise, separate versions for
v1 and v2 were created. The v2 branch will eventually become the new
main branch while the code for v1 remains in the main-1.x branch.

### Changed Behavior

-   Documenting pydantic model configurations in isolation or as a
    separate member of the pydantic model is no longer available. The
    following options have been removed:
    -   `autodoc_pydantic_model_show_config_member`
    -   `autodoc_pydantic_settings_show_config_member`
    -   `autodoc_pydantic_config_members`
    -   `autodoc_pydantic_config_signature_prefix`
-   All semantic changes from pydantic v1 to v2 take full effect.
    **autodoc_pydantic** does not modify the underlying behavior of
    pydantic in any way. Instead, it only documents whatever pydantic
    exposes. Hence, all behavioral changes such as the new default
    strict mode are preserved in v2.
-   Sphinx `< 4.0.0` is no longer supported.

### Features

-   Support for pydantic v2 💫.
-   Support annotated type hints.

### Internal

-   Adjust imports to refer to `pydantic-settings` (v2) instead of
    `pydantic` (v1).
-   Adjust imports to refer to `field_validator` (v2) insteaf of
    `validator` (v1).
-   Adjust imports to refer to `model_validator` (v2) insteaf of
    `root_validator` (v1).
-   Replace `pydantic.generics.GenericModel` (v1) with `typing.Generic`
    (v2).
-   Simplify `ValidatorAdapter` and `ValidatorInspector`.
-   Simplify reused validators retrieval.
-   Completely rewrite the model\'s field constraint retrieval
    functionality in `inspection.FieldInspector`.
-   Adjust model\'s field serializability checks in
    `inspection.FieldInspector`.
-   Replace `BaseModel` with `NamedTuple` for `ValidatorAdapter`.
-   Remove obsolete pre/post validator attributes.
-   Introduce `importlib-metadata` to fetch version number including
    support for python 3.7.

### Testing

-   Remove all obsolete pydantic versions from test matrix.
-   Remove all tests for documenting config members.
-   Remove compatibility helpers for older pydantic versions.
-   Remove obsolete pydantic model example which was not used anywhere.
-   Adjust serializability tests to account for changed behavior in v2.
-   Adjust optional/required field marker tests to account for changed
    behavior in v2.
-   Adjust field constraint tests to account for changed behavior in v2.
-   Adjust erdantic tests to exclude the erdantic version number which
    caused tests to fail upon erdantic update.

### Documentation

-   Add FAQ section regarding migration guide from v1 to v2.
-   Remove `complete` showcase from user\'s example.
-   Update READMEs with newest features and version specifiers.
-   Update developer\'s setup section to address v1 to v2 changes.
-   Updates user\'s installation section to address v1 to v2 changes.
-   Remove all obsolete documentation on removed config documenters.
-   Rename all occurences to v2 `field_validator` and `model_validator`.

### Contributors

-   Special thanks to [awoimbee](https://github.com/awoimbee) for
    providing a draft for the v1 to v2 migration which really initiated
    the work on supporting pydantic v2
    [#160](https://github.com/mansenfranzen/autodoc_pydantic/pull/160).
-   Many thanks to [PriOliveira](https://github.com/PriOliveira) for
    reviewing changes required for the v1 to v2 release
    [#160](https://github.com/mansenfranzen/autodoc_pydantic/pull/160).

## v1.9.0 - 2023-06-08

This is a feature release adding support for entity relationship
diagrams while dropping python 3.6. Additionally, pydantic v2 is
currently excluded until support will be added. Moreover, newest sphinx
versions are added to test matrix.

### Feature

-   Introduce `erdantic-figure` and `erdantic-figure-collapsed`
    configuration option for pydantic models to add entity relationship
    diagrams to models\' documentation either in collapsed form or as an
    image included to the HTML.
    [#148](https://github.com/mansenfranzen/autodoc_pydantic/pull/148).

### Bugfix

-   Run github actions on newest `ubuntu-22.04`.
-   Fix pytest errors with `sphinx>=6.1` where the type returned by
    `autodoc_typehints_format` changed.
-   Provide upper version boundary for pydantic to exclude v2 which is
    not supported, yet.

### Internal

-   Add `to_collapsable` to `directives.templates` that provides a
    standardized interface to create a collapsable field.
-   Add `erdantic` to extras dependencies.

### Documentation

-   Add descriptions for `erdantic-figure` and
    `erdantic-figure-collapsed` options in the configuration section.
-   Add an example of ERD in the example section.

### Testing

-   Exclude `python 3.6` in test matrix.
-   Include `sphinx` 6.0, 6.1, 6.2 and 7.0 in test matrix.
-   Add tests for `erdantic-figure` and `erdantic-figure-collapsed`.
-   Fix github actions CI pipeline due to unsupported ubuntu while
    upgrading to newest `ubuntu-22.04`.

### Contributors

-   Many thanks to [yves-renier](https://github.com/yves-renier) for
    adding entity relationship diagrams and fixing the CI pipeline
    [#148](https://github.com/mansenfranzen/autodoc_pydantic/pull/148).

## v1.8.0 - 2022-10-13

This is a feature and bugfix release with major internal refactorings
and added support for pydantic `1.10` and sphinx `5.1` and `5.2`.

### Feature

-   Introduce `hide-reused-validator` configuration option for pydantic
    models and settings to hide class methods that are created while
    declaring functions as reusable validators
    [#122](https://github.com/mansenfranzen/autodoc_pydantic/issues/122).

### Bugfix

-   Fix incorrect reference of reused validators
    [#122](https://github.com/mansenfranzen/autodoc_pydantic/issues/122).
-   Provide deterministic sort order for model\'s validator summary and
    field\'s validator list.
-   Hide pydantic user warnings in sphinx output when testing for
    pydantic field serializability.

### Internal

-   Add `ValidatorAdapter` that provides a standardized interface to
    pydantic\'s validator objects with additional metadata (e.g. root
    validator) for internal usage in autodoc_pydantic.
-   Introduce `field_validator_mappings` to `inspection.ModelInspector`
    which holds all mappings between fields and validators. It makes
    many helper functions of `ValidatorInspector` and `FieldInspector`
    obsolete. Overall, this greatly simplifies the inspection codebase.
-   Add `PydanticAutoDoc.resolve_inherited_validator_reference` to allow
    proper reference resolution for inherited validators.

### Documentation

-   Add description for `autodoc_pydantic_model_hide_reused_validator`
    and `autodoc_pydantic_settings_hide_reused_validator`.
-   Add example section for reused validators with detailed explanation.
-   Refactor sphinx extension helper for building `autodoc_pydantic`
    docs for better readability and maintainability.
-   Add `example_path` to sphinx extension helper `config_description`.
-   Add FAQ question regarding interoperability with `autoapi`.

### Testing

-   Include pydantic `1.10` and sphinx `5.1` / `5.2` in test matrix.
-   Provide compatibility for new pydantic and sphinx versions.
-   Fix incorrect pydantic version comparison.

### Contributors

-   Thanks to [GlenNicholls](https://github.com/GlenNicholls) for
    reporting a bug regarding incorrect references of reused validators
    [#122](https://github.com/mansenfranzen/autodoc_pydantic/issues/122)
    .
-   Thanks to [csm10495](https://github.com/csm10495) for asking a
    question regarding `autoapi` interoperability
    [#138](https://github.com/mansenfranzen/autodoc_pydantic/issues/138)
    .

## v1.7.2 - 2022-06-12

This is a bugfix release.

### Bugfix

-   Adjust `PydanticFieldDocumenter.can_document_member` to ignore non
    pydantic fields
    [#123](https://github.com/mansenfranzen/autodoc_pydantic/issues/123),
    [#128](https://github.com/mansenfranzen/autodoc_pydantic/issues/128).
-   Allow pydantic models to be documented as class attributes while
    adjusting `ModelInspector.from_child_signode` to support nested
    object paths
    [#124](https://github.com/mansenfranzen/autodoc_pydantic/issues/123),
    [#129](https://github.com/mansenfranzen/autodoc_pydantic/issues/128).

### Contributors

-   Thanks to [sneakers-the-rat](https://github.com/sneakers-the-rat)
    and [PipeKnight](https://github.com/PipeKnight) for reporting a bug
    when encountering attributes that are not pydantic fields
    [#123](https://github.com/mansenfranzen/autodoc_pydantic/issues/123),
    [#128](https://github.com/mansenfranzen/autodoc_pydantic/issues/128).
-   Thanks to [iwishiwasaneagle](https://github.com/iwishiwasaneagle)
    and [nickeldan](https://github.com/nickeldan) for reporting a bug
    pydantic models were documented as class attributes or
    `ModelInspector.from_child_signode` returned the incorrect model
    reference
    [#124](https://github.com/mansenfranzen/autodoc_pydantic/issues/123),
    [#129](https://github.com/mansenfranzen/autodoc_pydantic/issues/128).

### Internal

-   Renamed `from_signode` to `from_child_signode` for better clarity.
-   Added explicit check to raise an exception if loaded object in
    `ModelInspector.from_child_signode` is not a pydantic model.

## v1.7.1 - 2022-05-30

This is a bugfix release supporting sphinx 5.0.

### Bugfix

-   Adjust modified function signature of
    `sphinx.ext.autodoc.ClassDocumenter.add_content` in sphinx 5.0 which
    causes a type error otherwise
    [#125](https://github.com/mansenfranzen/autodoc_pydantic/issues/125)
    .

### Packaging

-   Convert `sphinx-tabs` and `sphinxcontrib-mermaid` to optional deps
    and relax their version specification.

### Testing

-   Add sphinx 5.0 to test matrix.
-   Adjust several tests for changed default behaviour of
    `autodoc_typehints_format`.

### Contributors

-   Thanks to [lukehsiao](https://github.com/lukehsiao) for reporting
    breaking changes in sphinx 5.0
    [#125](https://github.com/mansenfranzen/autodoc_pydantic/issues/125)
    .

## v1.7.0 - 2022-05-18

This is a feature release.

### Changing behavior

-   Default values of pydantic fields such as `UndefinedPydantic` and
    `Ellipsis` will now be shown as `None`.

### Bugfix

-   Fix missing validator-field references in
    `model-show-validator-summary` in case a single validator method
    process multiple fields.

### Feature

-   Add `autodoc_pydantic_field_show_optional` configuration which
    provides `[Optional]` marker for pydantic fields with
    `default_factory`. This configuration is activated by default. If
    deactivated, default values might be displayed incorrectly. For
    more, see
    [#114](https://github.com/mansenfranzen/autodoc_pydantic/issues/114)
-   Add `autodoc_pydantic_field_swap_name_and_alias` configuration which
    allows to use a field\'s alias as a name instead of the original
    field name
    [#99](https://github.com/mansenfranzen/autodoc_pydantic/issues/99) .
-   Respect interaction between
    `autodoc_pydantic_field_swap_name_and_alias` with
    `model-show-validator-summary`, `model-show-field-summary`,
    `validator-replace-signature` and `validator-list-fields` by
    replacing the field name with field alias in rendered documentation.

### Internals

-   Determining default values of pydantic fields no longer use
    `Field.field_info.default` but `Field.default`. As a consequence,
    default values such as `UndefinedPydantic` and `Ellipsis` will now
    be shown as `None`.
-   Autodocumenter `PydanticFieldDocumenter` now passes
    `field-show-alias` and `alias` to `PydanticField` directive. Before,
    only `alias` was passed with value to denote `field-show-alias`.
    However, since `field-swap-name-and-alias` was added, the value of
    the alias might be required even without `field-show-alias` being
    activated.
-   Refactor and split `PydanticModelDocumenter.add_validators_summary`
    in multiple methods for better readability and maintainability.
-   Add `get_field_name_or_alias` to `PydanticAutoDoc` to centrally
    manage the determination of field name/alias for all
    auto-documenters.
-   Rename `sanitize_configuration_option_name` into
    `determine_app_cfg_name` in `directives/options/composites.py` for
    better clarity.
-   Add `configuration_names` to `AutoDocOptions` to distinguish foreign
    directive options in `determine_app_cfg_name` which is required
    because `field-swap-name-and-alias` is also used by model/validator
    auto-documenters.

### Documentation

-   Add example section for `field-swap-name-and-alias`.
-   Add configuration description for `field-swap-name-and-alias`.

### Contributors

-   Thanks to [spacemanspiff2007](https://github.com/spacemanspiff2007)
    for providing and supporting a feature request to show `[Optional]`
    marker
    [#114](https://github.com/mansenfranzen/autodoc_pydantic/issues/114)
    and a feature request to swap name and alias
    [#99](https://github.com/mansenfranzen/autodoc_pydantic/issues/99) .

## v1.6.2 - 2022-04-15

This is a documentation and bugfix release supporting sphinx 4.5.

### Bugfix

-   Fix incorrect source-to-doc hyperlink in users example section
    [#96](https://github.com/mansenfranzen/autodoc_pydantic/issues/96).
-   Fix incorrect `[Required]` mark for optional fields like
    `Optional[int]`
    [#97](https://github.com/mansenfranzen/autodoc_pydantic/issues/97).
-   Fix incorrect warning of JSON non-serializable field in case of
    composite types like `Union`.
    [#98](https://github.com/mansenfranzen/autodoc_pydantic/issues/98).
-   Fix incorrect showing of additional keyword arguments passed to
    pydantic [Field]{.title-ref} in the field\'s constraint
    documentation section
    [#110](https://github.com/mansenfranzen/autodoc_pydantic/issues/110).

### Documentation

-   Separate example page into configuration and specifics.
-   Add examples for required and optional values.
-   Add examples for generic models.
-   Use separate python modules for user\'s usage and example sections
    to prevent ambiguous source-to-doc hyperlinks.

### Testing

-   Add sphinx 4.5 to CI.
-   Add test to ensure that optional fields do not have the `[Required]`
    mark.
-   Add test to ensure that pydantic field with composite type like
    `Union` is correctly identified as JSON serializable.
-   Add test to ensure that additional keyword arguments passed to
    pydantic [Field]{.title-ref} are not shown in the field\'s
    constraint documentation section.
-   Pin `jinja2<3.1.0` for `sphinx<4` to fix broken CI.

### Contributors

-   Thanks to [jgunstone](https://github.com/jgunstone) for reporting a
    bug regarding incorrect source-to-doc hyperlink in users example
    section.
-   Thanks to [Czaki](https://github.com/Czaki) for reporting a bug
    regarding incorrect warning of JSON non-serializable field in case
    of composite types like `Union`.
-   Thanks to [StigKorsnes](https://github.com/StigKorsnes) for
    reporting a bug regarding incorrect `[Required]` mark for optional
    fields like `Optional[int]`
-   Thanks to [spacemanspiff2007](https://github.com/spacemanspiff2007)
    for reporting a bug regarding incorrect showing of additional
    keyword arguments passed to pydantic [Field]{.title-ref} in the
    field\'s constraint documentation section.

## v1.6.1 - 2022-01-28

This is a minor bugfix release including support for sphinx 4.4.

### Bugfix

-   Fix incorrect rendering of pydantic field\'s `description` attribute
    which was not in line with default reST rendering of docstrings of
    classes or functions.
    [#91](https://github.com/mansenfranzen/autodoc_pydantic/issues/91).

### Testing

-   Add test to ensure that pydantic field\'s `description` attribute is
    correctly rendered.
-   Add sphinx 4.4 to CI.
-   Simplify `test_autodoc_pydantic_settings_hide_paramlist_false`
    replacing version specifics with generic assert function.

### Contributors

-   Thanks to [iliakur](https://github.com/iliakur) for reporting the
    incorrect reST rendering of pydantic field\'s `description`
    attribute.

## v1.6.0 - 2022-01-03

This is a feature and bug fix release including support for pydantic
1.9.

### Changing behavior

-   Documented pydantic models/settings as class attributes will no
    longer show additional content
    [#78](https://github.com/mansenfranzen/autodoc_pydantic/issues/78).
-   Generated docutils will now have additional fallback css classes
    [#77](https://github.com/mansenfranzen/autodoc_pydantic/issues/77).

### Bugfix

-   Fix a bug which occurred while documenting a pydantic model as an
    attribute and using [bysource]{.title-ref} for model summary list
    order
    [#78](https://github.com/mansenfranzen/autodoc_pydantic/issues/78).

### Feature

-   Remove any additional content generated by **autodoc_pydantic** for
    pydantic models/settings when documented as an attribute
    [#78](https://github.com/mansenfranzen/autodoc_pydantic/issues/78).
-   By default add fallback css classes for all docutils generated by
    **autodoc_pydantic**. This can be deactivated via newly added config
    `autodoc_pydantic_add_fallback_css_class`
    [#77](https://github.com/mansenfranzen/autodoc_pydantic/issues/77).

### Testing

-   Add tests to ensure that no additional content is provided if
    model/settings are documented as an attribute, see
    [test_edgecases]{.title-ref}.
-   Add tests to ensure that fallback css classes are added if required,
    see [test_events]{.title-ref}.
-   Streamline naming convention for tests regarding edge cases.
-   Adjust tests to comply with pydantic 1.9.
-   Add pydantic 1.9 to CI.
-   Add `prod_app` fixture to run production sphinx app based on cmd
    line entry point while returning captured sphinx app and doctrees.
-   Provide important doc strings to existing `autodocument`,
    `parst_rst` and `test_app` fixtures for better understandability.

### Documentation

-   Add FAQ section describing changed behaviour of models/settings when
    used as class attributes.
-   Add FAQ section describing fallback css classes.
-   Rename `BaseModel` to `Model` and `BaseSettings` to `Settings` in
    configuration section.
-   Add `autodoc_pydantic_add_fallback_css_class` setting to users
    configuration page.
-   Add `ShowVersions` directive to show relevant package versions of
    current documentation build environment in setup page of developer
    documentation.

### Contributors

-   Thanks to [StigKorsnes](https://github.com/StigKorsnes) for
    reporting an unexpected behavior when using **autodoc_pydantic**
    with themes like Jupyter-Book that rely on setting css styles for
    default sphinx autdoc objtypes `class`, `attribute` and `method`
    [#77](https://github.com/mansenfranzen/autodoc_pydantic/issues/77).
-   Thanks to [nchaly](https://github.com/nchaly) for reporting a bug
    and raising the topic of how to document models/settings as an
    attribute
    [#78](https://github.com/mansenfranzen/autodoc_pydantic/issues/78).

## v1.5.1 - 2021-11-12

This is a minor bug fix release with testing and documentation
improvements. Additionally, it adds support for sphinx 4.3.

### Bugfix

-   Fix a corner-case where a module that imported
    `numpy.typing.NDArray` caused autodoc_pydantic to experience an
    uncaught exception
    [#57](https://github.com/mansenfranzen/autodoc_pydantic/issues/57).

### Internal

-   Account for modified method signature in `get_signature_prefix` in
    sphinx 4.3
    [#62](https://github.com/mansenfranzen/autodoc_pydantic/issues/62).

### Testing

-   Fix broken CI for sphinx 3.4 due to unpinned versions of `docutils`.
    This generates new sphinx loggings which have not been present
    before that in turn cause tests to fail which are dependent on
    inspecting sphinx loggings
    [#68](https://github.com/mansenfranzen/autodoc_pydantic/issues/68).
-   Add sphinx 4.3 to CI matrix.
-   Add compatibility module to abstract away minor implementation
    differences between sphinx versions 4.3 and prior.
-   Add tests for development versions while continuing on error.
-   Replace codacy with codecov for code coverage reports.
-   Add code coverage for all stable and latest version.
-   Allow CI to be executed on pull requests from forks of new
    contributors.

### Documentation

-   Add `Exclude __init__ docstring` section to FAQ of the user guide
    [#58](https://github.com/mansenfranzen/autodoc_pydantic/issues/58).
-   Add github issue links to topics of FAQ of the user guide.

### Contributors

-   Thanks to [j-carson](https://github.com/j-carson) for reporting a
    bug and providing a PR related to autodoc_pydantic\'s inspection
    module
    [#57](https://github.com/mansenfranzen/autodoc_pydantic/issues/57).
-   Thanks to [Yoshanuikabundi](https://github.com/Yoshanuikabundi) and
    [jakobandersen](https://github.com/jakobandersen) for reporting and
    mitigating a compatibility issue with sphinx 4.3
    [#62](https://github.com/mansenfranzen/autodoc_pydantic/issues/62).
-   Thanks to [lilyminium](https://github.com/lilyminium) for adding the
    `Exclude __init__ docstring` section to FAQ of the user guide
    [#58](https://github.com/mansenfranzen/autodoc_pydantic/issues/58).

## v1.5.0 - 2021-10-10

This release includes major internal refactorings, new documentation
sections, a new feature, a bug fix and tests for new sphinx and python
versions.

### Added

-   Provide `summary-list-order` configuration property which allows to
    sort summary list items in alphabetical order or by source.

### Bugfix

-   Using `@root_validator(pre=True)` caused the sphinx build process to
    fail due to an incorrect implementation. This has been fixed.
    [#55](https://github.com/mansenfranzen/autodoc_pydantic/issues/55).

### Testing

-   Refactor all configuration test modules removing repeated function
    arguments to increase readability and maintainability.
-   Add specific test to ensure that using `@root_validator(pre=True)`
    does not break the sphinx build process.
-   Add sphinx versions `4.1.0` and `4.2.0` to CI matrix.
-   Add python version `3.10` to CI matrix.

### Documentation

-   Add section in configuration page describing `summary-list-order`.
-   Add developer design section providing gentle introduction to code
    base.
-   Add developer guides focusing on concrete implementation details.
-   Add class diagrams via mermaid.js.
-   Streamline naming convention for `TabDocDirective` for better
    clarity.
-   Add `version` parameter to `TabDocDirective` to show the version in
    which a configuration property was added.
-   Add API documentation for selected modules including directory tree
    with references.
-   Activate `sphinxcontrib.mermaid` and `sphinx.ext.viewcode`
    extensions.

### Internal

-   Completely remove the `ModelWrapper` with the `ModelInspector` with
    all its composite classes.
-   Moving inspection logic from auto-documenters to `ModelInspector`.
-   Streamline naming conventions for composite classes.
-   Create separate sub directory for directive options including
    individual modules for composites, definitions, enums and
    validators.
-   Move reST templates to separate module.

### Packaging

-   Update to newest versions of `sphinx-rtd-theme` and `sphinx-tabs`.
-   Add `sphinxcontrib-mermaid` under dev and doc dependencies.

### Contributors

-   Thanks to [goroderickgo](https://github.com/goroderickgo) for
    reporting a bug related to pre root validators breaking the sphinx
    build process
    [#55](https://github.com/mansenfranzen/autodoc_pydantic/issues/55).

## v1.4.0 - 2021-08-20

This is a feature and bug release.

### Added

-   Provide `field-show-required` configuration property. If activated,
    it adds a `[Required]` marker for pydantic fields which do not have
    a default value. Otherwise, misleading default values like
    *Ellipsis* or *PydanticUndefined* are shown.
    [#34](https://github.com/mansenfranzen/autodoc_pydantic/issues/34).
-   Include `show-json-error-strategy` for pydantic models and settings
    to define error handling in case a pydantic field breaks the JSON
    schema generation
    [#8](https://github.com/mansenfranzen/autodoc_pydantic/issues/8).

### Bugfix

-   Respect `inherited-members` for field and validator summaries to
    prevent different members being displayed between header and body
    [#32](https://github.com/mansenfranzen/autodoc_pydantic/issues/32).
-   Improve handling of non serializable pydantic fields for JSON model
    generation. Using `pd.DataFrame` as a type annotation raised an
    exception instead of being handled appropriately
    [#28](https://github.com/mansenfranzen/autodoc_pydantic/issues/28).
-   Allow typed fields within doc strings to successfully reference
    pydantic models and settings
    [#27](https://github.com/mansenfranzen/autodoc_pydantic/issues/27).
-   Remove `env` key from field constraints.

### Testing

-   Add explicit tests for references originating from typed fields.
-   Add more diverse tests for handling non serializable fields breaking
    JSON model generation.
-   Add tests for different error handling strategies regarding
    `show-json-error-strategy`.
-   Add tests for `field-show-required`.
-   Add tests for field and validator summaries respecting
    `inherited-members`.

### Documentation

-   Add section in configuration page describing
    `show-json-error-strategy`.
-   Add section in configuration page describing `field-show-required`.
-   Add FAQ page with section about using `inherited-members`.
-   Generally overhaul the documentation to improve readability and
    conciseness.

### Contributors

-   Thanks to [davidchall](https://github.com/davidchall) for suggesting
    to add a `[Required]` marker for mandatory pydantic fields
    [#34](https://github.com/mansenfranzen/autodoc_pydantic/issues/34).
-   Thanks to [matutter](https://github.com/matutter) for reporting a
    bug related to incorrect field and validator summaries not
    respecting `inherited-members`
    [#32](https://github.com/mansenfranzen/autodoc_pydantic/issues/32).
-   Thanks to [thomas-pedot](https://github.com/thomas-pedot) for
    reporting a bug related to error handling of pydantic fields
    breaking JSON schema generation
    [#28](https://github.com/mansenfranzen/autodoc_pydantic/issues/28).
-   Thanks to [tahoward](https://github.com/tahoward) for reporting a
    bug related to missing references in typed fields
    [#27](https://github.com/mansenfranzen/autodoc_pydantic/issues/27).

## v1.3.1 - 2021-07-21

This is a minor release including the following:

-   Providing support for `root_validator`
    [#20](https://github.com/mansenfranzen/autodoc_pydantic/issues/20) .
-   Fixing a bug concerning overwriting `member-order`
    [#21](https://github.com/mansenfranzen/autodoc_pydantic/issues/21) .
-   Integrating flake8 for static code analysis.

### Bugfix

-   Fix `member-order` being overwritten by autodoc pydantic\'s
    autodocumenters
    [#21](https://github.com/mansenfranzen/autodoc_pydantic/issues/21).

### Documentation

-   Add example showing representation of asterisk and root validators.
-   Add [sphinx-copybutton]{.title-ref} extension.

### Testing

-   Add explicit tests for asterisk and root validators.
-   Add test case ensuring that `member-order` is not affected by other
    auto-documenters.
-   Fix several tests which in fact tested wrong behaviour.

### Internal

-   Refactor and simplify field validator mapping generation of
    `inspection.ModelWrapper`.
-   Replace `set_default_option_with_value` with specific
    `set_members_all`.
-   Create separate copy for every auto-documenters `option` object to
    prevent shared options.

### Contributors

-   Thanks to [roguh](https://github.com/roguh) for submitting a feature
    request for `root_validators`
    [#20](https://github.com/mansenfranzen/autodoc_pydantic/issues/20).
-   Thanks to [ybnd](https://github.com/ybnd) for submitting a bug
    report concerning incorrect behaviour for `member-order`
    [#21](https://github.com/mansenfranzen/autodoc_pydantic/issues/21)

## v1.3.0 - 2021-05-10

This is a release focusing on testing and packaging. It includes tests
for sphinx 4.0 support. Additionally, it moves all test invocation
specifications to `tox.ini`.

### Documentation

-   Add acknowledgements to index.
-   Add detailed description for running tests with pytest and tox.
-   Convert changelog page from markdown to reST.

### Testing

-   Use tox for defining different test environments (specific stable,
    latest stable and development). Remove test environment
    specifications from github ci and move it to `tox.ini` addressing
    \#[7](https://github.com/mansenfranzen/autodoc_pydantic/issues/7).
-   Add sphinx 4.0 to test environments addressing
    \#[16](https://github.com/mansenfranzen/autodoc_pydantic/issues/16).
-   Define specific test environments instead of testing all matrix
    combinations.
-   Provide version information about *autdoc_pydantic* and relevant
    dependencies.

### Packaging

-   Replace `pytest-cov` with `coverage`.
-   Remove `myst-parser` dependency addressing
    \#[16](https://github.com/mansenfranzen/autodoc_pydantic/issues/16).
-   Add `tox` for executing tests in CI.
-   Remove poetry development dependencies and replace it with explicit
    `extras` for *docs*, *test* and *dev*.

### Internal

-   Rename `util` module to `composites` to improve naming convention.

### Added

-   `show_versions` function to show important dependency information
    which are relevant for tracking down bugs as part of the new
    `utility` module.

## v1.2.0 - 2021-05-09

This is a feature release adding the field summary for pydantic
models/settings.

### Documentation

-   Refactor and simplify sphinx extension `helper` module for better
    maintainability and readability.
-   Improve many of the available descriptions in the `configuration`
    section.
-   Provide correct markers for the actual default values in the
    `configuration` section.

### Added

-   Introduce `model-show-field-summary` and
    `settings-show-field-summary` which partially addresses
    \#[14](https://github.com/mansenfranzen/autodoc_pydantic/issues/14).

### Internal

-   Add `get_fields` to `inspection` module.

## v1.1.3 - 2021-05-08

This is a patch release addressing missing cross reference ability and
minor refactorings.

### Internal

-   Add `add_domain_object_types` to extension `setup`.
-   Add version and extension meta data to `setup`.
-   Refactor rather complex `setup` into separate functions.

### Testing

-   Rename test directory `test-ext-autodoc-pydantic` to `test-base` to
    streamline naming convention.
-   Add test directory `test-edgecase-any-reference` to mock issue with
    failing `:any:` reference to pydantic objects including
    `test_any_reference` test.
-   Add `test_sphinx_build` test module to check that the sphinx docs
    build without error and warning which can be seen as an end to end
    test because *autodoc_pydantic*\'s documentation is built with
    sphinx and contains an entire collection of usage examples for
    *autodoc_pydantic* itself.

### Bugfix

-   Enable cross referencing of pydantic objects which are documented
    with *autodoc_pydantic* directives and linked via `:any:` role
    \#[3](https://github.com/mansenfranzen/autodoc_pydantic/issues/3).

### Documentation

-   Add *complete configuration* and *fields only* example to
    documentation.

## v1.1.2 - 2021-05-06

This is a bugfix release on compatibility issues with sphinx
autosummary.

### Internal

-   Remove custom object import and use autodoc\'s provided
    functionality.
-   Add `option_is_true` and `option_is_false` for
    `PydanticAutoDirective` respecting missing values via custom `NONE`
    object.
-   Move member option processing from `__init__` to `document_members`
    for `PydanticModelDocumenter`.
-   Introduce `PydanticDirectiveBase` base class for all pydantic
    directives to remove code redundancies.

### Bugfix

-   Respect `.. currentmodule::` directive for object imports
    [#12](https://github.com/mansenfranzen/autodoc_pydantic/issues/12).
-   Make `autosummary`\'s `FakeDirective` work with pydantic
    autodocumenters
    [#11](https://github.com/mansenfranzen/autodoc_pydantic/issues/11).
-   Allow `AutoSummary.get_items` to successfully list pydantic
    autodocumenters which wrap objects imported to external modules
    [#11](https://github.com/mansenfranzen/autodoc_pydantic/issues/11).

### Documentation

-   Add `autosummary` explanation to usage section.

### Testing

-   Add test module for ensuring `autosummary` interoperability.

### Contributors

-   Thanks to [antvig](https://github.com/antvig) for reporting and
    testing an issue related to autosummary
    [#11](https://github.com/mansenfranzen/autodoc_pydantic/issues/11).

## v1.1.1 - 2021-04-26

This is a minor release with focus on refactoring and doc strings.

### Internal

-   Several minor readability refactorings.

### Documentation

-   Add changelog and `myst_parser` for parsing markdown files.

### Project

-   Add animated example to showcase difference between standard sphinx
    autodoc and pydantic autodoc.
-   Add project logo.
-   Add changelog.

## v1.1.0 - 2021-04-24

This is small feature release enabling `autodoc_pydantic` to handle non
JSON serializable fields properly.

### Internal

-   Replace inspection methods that use models JSON schema with methods
    that directly access relevant pydantic object attributes.
-   Intercept non JSON serializable fields and overwrite types and
    default values indicating serialization error.

### Documentation

-   Add explicit note about how non JSON serializable fields are handled
    for `model-show-json` and `settings-show-json`.

## v1.0.0 - 2021-04-23

This is a major release providing API stability with main focus on
extensive tests and documentation.

### Added

-   Add custom css for `autodoc_pydantic` extension.

### Internal

-   Add `PydanticAutoDirective` as composite class to mainly manage
    option/configuration management for directives.
-   Add `PydanticAutoDoc` as composite class to mainly manage
    option/configuration management for autodocumenters.
-   Unify directive options and global configuration settings via
    composite classes.
-   Add option validators `option_members`, `option_one_of_factory`,
    `option_default_true`, `option_list_like`.

### Documentation

-   Add extensions to automate documentation generation:
-   `ConfigurationToc` to generate options/conf toc mappings from usage
    to configuration section
-   `TabDocDirective` to generate rendered examples in configuration
    section
-   `AutoCodeBlock` to generate code block from object path
-   Add user guide:
-   Installation
-   Usage
-   Configuration
-   Examples
-   Add developer guide:
-   Setting up development environment
-   Running tests
-   Building docs
-   Add `.readthedocs.yaml`.

### Testing

-   Add test python package with code examples for test execution (same
    structure as sphinx tests).
-   Add fixture `test_app` to instantiate test app with settable
    configuration settings.
-   Add fixture `autodocument` to handle restructured text generation
    tests (autodocumenter tests).
-   Add fixture `parse_rst` to handle node generation tests from
    restructured text (directive tests).
-   Add autodoc/directive tests for all available configuration settings
-   Include sourcery in CI pipeline.

### Packaging

-   Modify package dependencies to `sphinx >=3.4` and `pydantic >= 1.5`.

## v0.1.1 - 2021-04-04

This release adds the sphinx documentation skeleton.

### Documentation

-   Add initial sphinx documentation.

## v0.1.0 - 2021-03-30

This is the initial of autodoc_pydantic.

### Added

-   Autodocumenter `PydanticModelDocumenter` with configurations:
    -   `model_show_json`
    -   `model_show_config_member`
    -   `model_show_config_summary`
    -   `model_show_validator_members`
    -   `model_show_validator_summary`
    -   `model_hide_paramlist`
    -   `model_undoc_members`
    -   `model_members`
    -   `model_member_order`
    -   `model_signature_prefix`
-   Autodocumenter `PydanticSettingsDocumenter` with configurations:
    -   `settings_show_json`
    -   `settings_show_config_member`
    -   `settings_show_config_summary`
    -   `settings_show_validator_members`
    -   `settings_show_validator_summary`
    -   `settings_hide_paramlist`
    -   `settings_undoc_members`
    -   `settings_members`
    -   `settings_member_order`
    -   `settings_signature_prefix`
-   Autodocumenter `PydanticFieldDocumenter` with configurations:
    -   `field_list_validators`
    -   `field_doc_policy`
    -   `field_show_constraints`
    -   `field_show_alias`
    -   `field_show_default`
    -   `field_signature_prefix`
-   Autodocumenter `PydanticValidatorDocumenter` with configurations:
    -   `validator_signature_prefix`
    -   `validator_replace_signature`
    -   `validator_list_fields`
-   Autodocumenter `PydanticConfigClassDocumenter` with configurations:
    -   `config_signature_prefix`
    -   `config_members`
-   Directives `PydanticModel`, `PydanticSettings`, `PydanticField`,
    `PydanticValidator`

### Internal

-   Add `inspection` along with `ModelWrapper` module providing
    functionality to inspect pydantic objects to retrieve relevant
    informations for documentation.

### Testing

-   Add end to end tests for autodocumenters and directives.
-   Setup github actions for CI.
-   Add codacy integration.
-   Add code coverage.

### Packaging

-   Use poetry for package management.
-   Add `pyproject.toml`.
-   Add github action to upload to PyPI upon version tags on main
    branch.
