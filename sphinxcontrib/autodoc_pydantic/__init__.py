from pathlib import Path

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

def add_css_file(app: Sphinx, exception: Exception):
    """Adds custom css to HTML output.

    """

    filename = "autodoc_pydantic.css"
    static_path = (Path(app.outdir) / "_static").absolute()
    static_path.mkdir(exist_ok=True, parents=True)
    path_css = Path(__file__).parent.joinpath("css", filename)

    if not (static_path / filename).exists():
        content = path_css.read_text()
        (static_path / filename).write_text(content)


def setup(app: Sphinx) -> None:
    stem = "autodoc_pydantic_"

    app.add_config_value(f'{stem}config_signature_prefix', "model", True, str)
    app.add_config_value(f'{stem}config_members', True, True, bool)

    app.add_config_value(f'{stem}settings_show_json', True, True, bool)
    app.add_config_value(f'{stem}settings_show_config_member', False, True, bool)
    app.add_config_value(f'{stem}settings_show_config_summary', True, True, bool)
    app.add_config_value(f'{stem}settings_show_validator_members', True, True, bool)
    app.add_config_value(f'{stem}settings_show_validator_summary', True, True, bool)
    app.add_config_value(f'{stem}settings_hide_paramlist', True, True, bool)
    app.add_config_value(f'{stem}settings_undoc_members', True, True, bool)
    app.add_config_value(f'{stem}settings_members', True, True, bool)
    app.add_config_value(f'{stem}settings_member_order', 'groupwise', True, str)
    app.add_config_value(f'{stem}settings_signature_prefix', "pydantic settings", True, str)

    app.add_config_value(f'{stem}model_show_json', True, True, bool)
    app.add_config_value(f'{stem}model_show_config_member', False, True, bool)
    app.add_config_value(f'{stem}model_show_config_summary', True, True, bool)
    app.add_config_value(f'{stem}model_show_validator_members', True, True, bool)
    app.add_config_value(f'{stem}model_show_validator_summary', True, True, bool)
    app.add_config_value(f'{stem}model_hide_paramlist', True, True, bool)
    app.add_config_value(f'{stem}model_undoc_members', True, True, bool)
    app.add_config_value(f'{stem}model_members', True, True, bool)
    app.add_config_value(f'{stem}model_member_order', 'groupwise', True, str)
    app.add_config_value(f'{stem}model_signature_prefix', "pydantic model", True, str)

    app.add_config_value(f'{stem}validator_signature_prefix', "validator", True, str)
    app.add_config_value(f'{stem}validator_replace_signature', True, True, bool)
    app.add_config_value(f'{stem}validator_list_fields', False, True, bool)

    app.add_config_value(f'{stem}field_list_validators', True, True, bool)
    app.add_config_value(f'{stem}field_doc_policy', 'both', True, str)
    app.add_config_value(f'{stem}field_show_constraints', True, True, bool)
    app.add_config_value(f'{stem}field_show_alias', True, True, bool)
    app.add_config_value(f'{stem}field_show_default', True, True, bool)
    app.add_config_value(f'{stem}field_signature_prefix', "field", True, str)

    app.add_directive_to_domain("py", "pydantic_field", PydanticField)
    app.add_directive_to_domain("py", "pydantic_model", PydanticModel)
    app.add_directive_to_domain("py", "pydantic_settings", PydanticSettings)
    app.add_directive_to_domain("py", "pydantic_config", PydanticConfigClass)
    app.add_directive_to_domain("py", "pydantic_validator", PydanticValidator)

    app.setup_extension('sphinx.ext.autodoc')  # Require autodoc extension
    app.add_autodocumenter(PydanticFieldDocumenter)
    app.add_autodocumenter(PydanticModelDocumenter)
    app.add_autodocumenter(PydanticSettingsDocumenter)
    app.add_autodocumenter(PydanticValidatorDocumenter)
    app.add_autodocumenter(PydanticConfigClassDocumenter)

    app.add_css_file("autodoc_pydantic.css")
    app.connect("build-finished", add_css_file)

