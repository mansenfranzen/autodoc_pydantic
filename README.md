# autodoc_pydantic

**Seamlessly integrate your pydantic models within your Sphinx documentation.** You love pydantic and you want to document your models and configuration settings with sphinx? Perfect, let's go. But wait, sphinx' autodoc does not integrate too well with pydantic models. Don't worry - just `pip install autodoc_pydantic`.

## Features

- provides default values, alias and constraints for model fields
- adds references between validators and processed fields
- includes collapsable model json schema
- defines explicit pydantic prefixes for models, settings, fields, validators and model config
- shows summary section for model configuration and validators
- hides overloaded and redundant model class signature
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
