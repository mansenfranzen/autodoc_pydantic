"""Contains the extension setup.

"""

from pathlib import Path
from typing import Dict, Any

from sphinx.domains import ObjType
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

__version__ = "1.3.1"


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


def add_domain_object_types(app: Sphinx):
    """Hack to add object types to already instantiated python domain since
    `add_object_type` currently only works for std domain.

    """

    object_types = app.registry.domain_object_types.setdefault("py", {})

    obj_types = ["pydantic_model",
                 "pydantic_settings",
                 "pydantic_field",
                 "pydantic_validator",
                 "pydantic_config"]

    for obj_type in obj_types:
        object_types[obj_type] = ObjType(obj_type, "obj", "any")


def add_configuration_values(app: Sphinx):
    """Adds all configuration values to sphinx application.

    """

    stem = "autodoc_pydantic_"
    add = app.add_config_value

    add(f'{stem}config_signature_prefix', "model", True, str)
    add(f'{stem}config_members', True, True, bool)

    add(f'{stem}settings_show_json', True, True, bool)
    add(f'{stem}settings_show_config_member', False, True, bool)
    add(f'{stem}settings_show_config_summary', True, True, bool)
    add(f'{stem}settings_show_validator_members', True, True, bool)
    add(f'{stem}settings_show_validator_summary', True, True, bool)
    add(f'{stem}settings_show_field_summary', True, True, bool)
    add(f'{stem}settings_hide_paramlist', True, True, bool)
    add(f'{stem}settings_undoc_members', True, True, bool)
    add(f'{stem}settings_members', True, True, bool)
    add(f'{stem}settings_member_order', 'groupwise', True, str)
    add(f'{stem}settings_signature_prefix', "pydantic settings", True, str)

    add(f'{stem}model_show_json', True, True, bool)
    add(f'{stem}model_show_config_member', False, True, bool)
    add(f'{stem}model_show_config_summary', True, True, bool)
    add(f'{stem}model_show_validator_members', True, True, bool)
    add(f'{stem}model_show_validator_summary', True, True, bool)
    add(f'{stem}model_show_field_summary', True, True, bool)
    add(f'{stem}model_hide_paramlist', True, True, bool)
    add(f'{stem}model_undoc_members', True, True, bool)
    add(f'{stem}model_members', True, True, bool)
    add(f'{stem}model_member_order', 'groupwise', True, str)
    add(f'{stem}model_signature_prefix', "pydantic model", True, str)

    add(f'{stem}validator_signature_prefix', "validator", True, str)
    add(f'{stem}validator_replace_signature', True, True, bool)
    add(f'{stem}validator_list_fields', False, True, bool)

    add(f'{stem}field_list_validators', True, True, bool)
    add(f'{stem}field_doc_policy', 'both', True, str)
    add(f'{stem}field_show_constraints', True, True, bool)
    add(f'{stem}field_show_alias', True, True, bool)
    add(f'{stem}field_show_default', True, True, bool)
    add(f'{stem}field_signature_prefix', "field", True, str)


def add_directives_and_autodocumenters(app: Sphinx):
    """Adds custom pydantic directives and autodocumenters to sphinx
    application.

    """

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


def setup(app: Sphinx) -> Dict[str, Any]:
    add_configuration_values(app)
    add_directives_and_autodocumenters(app)
    add_domain_object_types(app)
    app.add_css_file("autodoc_pydantic.css")
    app.connect("build-finished", add_css_file)

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
