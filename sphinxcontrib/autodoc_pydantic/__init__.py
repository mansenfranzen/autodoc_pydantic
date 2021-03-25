from sphinx.application import Sphinx

from sphinxcontrib.autodoc_pydantic.autodoc import (
    PydanticValidatorDocumenter,
    PydanticModelDocumenter,
    PydanticConfigClassDocumenter,
    PydanticFieldDocumenter,
    PydanticSettingsDocumenter
)

from sphinxcontrib.autodoc_pydantic.directives import (
    PydanticField,
    PydanticConfigClass,
    PydanticValidator,
    PydanticModel,
    PydanticSettings
)



def setup(app: Sphinx) -> None:
    stem = "autodoc_pydantic_"

    app.add_config_value(f'{stem}show_config', True, True, bool)
    app.add_config_value(f'{stem}show_validators', True, True, bool)

    app.add_config_value(f'{stem}model_member_order', 'groupwise', True, str)
    app.add_config_value(f'{stem}model_show_schema', True, True, bool)
    app.add_config_value(f'{stem}model_show_config', True, True, bool)
    app.add_config_value(f'{stem}model_show_validators', True, True, bool)
    app.add_config_value(f'{stem}model_show_paramlist', False, True, bool)

    app.add_config_value(f'{stem}validator_show_paramlist', False, True, bool)
    app.add_config_value(f'{stem}validator_replace_retann', True, True, bool)
    app.add_config_value(f'{stem}validator_list_fields', True, True, bool)

    app.add_config_value(f'{stem}field_list_validators', True, True, bool)
    app.add_config_value(f'{stem}field_doc_policy', 'description', True, str)
    app.add_config_value(f'{stem}field_show_constraints', True, True, bool)
    app.add_config_value(f'{stem}field_show_alias', True, True, bool)

    app.add_directive_to_domain("py", "pydantic_field", PydanticField)
    app.add_directive_to_domain("py", "pydantic_model", PydanticModel)
    app.add_directive_to_domain("py", "pydantic_settings", PydanticSettings)
    app.add_directive_to_domain("py", "pydantic_config_class", PydanticConfigClass)
    app.add_directive_to_domain("py", "pydantic_validator", PydanticValidator)

    app.setup_extension('sphinx.ext.autodoc')  # Require autodoc extension
    app.add_autodocumenter(PydanticFieldDocumenter)
    app.add_autodocumenter(PydanticModelDocumenter)
    app.add_autodocumenter(PydanticSettingsDocumenter)
    app.add_autodocumenter(PydanticValidatorDocumenter)
    app.add_autodocumenter(PydanticConfigClassDocumenter)
