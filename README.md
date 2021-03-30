# autodoc_pydantic

[![PyPI version](https://badge.fury.io/py/autodoc-pydantic.svg)](https://badge.fury.io/py/autodoc-pydantic)
![Master](https://github.com/mansenfranzen/autodoc_pydantic/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/30a083d784f245a98a0d5e6857708cc8)](https://www.codacy.com/gh/mansenfranzen/autodoc_pydantic/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mansenfranzen/autodoc_pydantic&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/30a083d784f245a98a0d5e6857708cc8)](https://www.codacy.com/gh/mansenfranzen/autodoc_pydantic/dashboard?utm_source=github.com&utm_medium=referral&utm_content=mansenfranzen/autodoc_pydantic&utm_campaign=Badge_Coverage)
![PyPI](https://img.shields.io/pypi/dw/autodoc_pydantic)
[![Open Source Love](https://badges.frapsoft.com/os/v3/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

You love [pydantic](https://pydantic-docs.helpmanual.io/) :heart: and you want to document your models and configuration settings with [sphinx](https://www.sphinx-doc.org/en/master/)? 

Perfect, let's go. But wait, sphinx' [autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) does not integrate too well with pydantic models :confused:. 

Don't worry - just `pip install autodoc_pydantic` :relaxed:.

## Features

- :speech_balloon: provides default values, alias and constraints for model fields
- :link: adds references between validators and corresponding fields
- :page_with_curl: includes collapsable model json schema
- :surfer: natively integrates with autodoc extension
- :paperclip: defines explicit pydantic prefixes for models, settings, fields, validators and model config
- :clipboard: shows summary section for model configuration and validators
- :eyes: hides overloaded and redundant model class signature
- :books: sorts fields, validators and model config within models by type
- 🍀 Supports `pydantic >= 1.0.0` and `sphinx >= 3.4.0`

All of these addons are completely configurable.

## Installation

1. Install via `pip install autodoc_pydantic`
2. Add `'sphinxcontrib.autodoc_pydantic'` to the `extensions` list in `conf.py`:

   ```python
   extensions = ['sphinxcontrib.autodoc_pydantic']
   ```

3. Configure `autodoc_pydantic` in `conf.py`:

   ```python
   autodoc_pydantic_field_show_constraints = True
   autodoc_pydantic_model_show_schema = True
   ```
 
## Usage

The standard `automodule` directive already understands pydantic models that it encounters by default. No more tweaks are required.

```rest
.. automodule:: package.module
   :members:
```

Additionally, autodoc_pydantic provides specific directives for models, settings, fields, validators and class config:

```rest
.. autopydantic_model:: package.module.MyModel
   :members:
   
.. autopydantic_settings:: package.module.MySettings
   :members:
   
.. autopydantic_field:: package.module.MyModel.foobar

.. autopydantic_validator:: package.module.MyModel.validator

.. autopydantic_class_config:: package.module.MyModel.Config
   :members:
```
 
## Configuration

### General 

- `autodoc_pydantic_show_config` = *True*: By default document `Config` class as class members. If *False*, hides it completely.
- `autodoc_pydantic_show_validators` = *True*: By default document pydantic validators as class members. If *False*, hides it completely.

### Models / Settings

- `autodoc_pydantic_model_show_schema` = *True*: By default, adds collapsable section including formatted model json schema.
- `autodoc_pydantic_model_show_config` = *True*: By default, adds model configuration settings to model doc string.
- `autodoc_pydantic_model_show_validators` = *True*: By default, adds validator -> field mappings to model doc string.
- `autodoc_pydantic_model_show_paramlist` = *False*: By default, hides overloaded and redundant parameter list from model signature.
- `autodoc_pydantic_model_member_order` = *'groupwise'*: By default, sorts model members by type to group fields, validators and class config members.

### Fields

- `autodoc_pydantic_field_list_validators` = *True*: By default, lists all validators processing corresponding field.
- `autodoc_pydantic_field_doc_policy` = *'both'*: By default, show doc string and and field description. If *'description'*, show field description only. If *'docstring'*, show doc string only.  
- `autodoc_pydantic_field_show_constraints` = *True*: By default, show field constraints (e.g. minimum, maximum etc.).
- `autodoc_pydantic_field_show_alias` = *True*: By default, show field alias in signature.

### Validators

- `autodoc_pydantic_validator_show_paramlist` = *False*: By default, hides meaningless parameter list from validators.
- `autodoc_pydantic_validator_replace_retann` = *True*: By default, replaces validators' return annotation with references to processed fields.
- `autodoc_pydantic_validator_list_fields` = *True*: By default, adds list of references to validators' doc string.
