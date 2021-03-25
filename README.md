# autodoc_pydantic
> Seamlessly integrate your pydantic models within your Sphinx documentation.

You love pydantic and you want to document your models and configuration settings with sphinx? Perfect, let's go. But wait, sphinx' autodoc does not integrate too well with pydantic models. Don't worry - just `pip install autodoc_pydantic`.

## Features

- provides default values, alias and constraints for model fields
- adds references from validators to processed fields and vice versa
- includes collapsable model json schema
- defines explicit prefixes for models, settings, fields, validators and model config
- shows summary section for model configuration and validators
- hides overloaded class signature
- sorts fields, validators and model config within models by type

All of these modifications and addons are completely configurable.

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
 
## Configuration

### General 

- `autodoc_pydantic_show_config` = *True*: By default document `Config` class as class members. If *False*, hides it completely.
- `autodoc_pydantic_show_validators` = *True*: By default document pydantic validators as class members. If *False*, hides it completely.

### Model / Settings

- `autodoc_pydantic_model_show_schema` = *True*: By default, adds collapsable section including formatted model json schema.
- `autodoc_pydantic_model_show_config` = *True*: By defautl, adds model configuration settings to model doc string.
