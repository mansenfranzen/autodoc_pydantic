"""Contains the extension setup."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel
from sphinx.domains import ObjType

from sphinxcontrib.autodoc_pydantic.directives import autodocumenters, directives
from sphinxcontrib.autodoc_pydantic.directives.options import enums
from sphinxcontrib.autodoc_pydantic.events import (
    add_fallback_css_class,
)

if TYPE_CHECKING:
    from sphinx.application import Sphinx

EXTENSION_PREFIX = 'autodoc_pydantic_'

AUTODOCUMENTERS = [
    autodocumenters.PydanticFieldDocumenter,
    autodocumenters.PydanticModelDocumenter,
    autodocumenters.PydanticSettingsDocumenter,
    autodocumenters.PydanticValidatorDocumenter,
]

DOMAIN_DIRECTIVES = {
    'pydantic_field': directives.PydanticField,
    'pydantic_model': directives.PydanticModel,
    'pydantic_settings': directives.PydanticSettings,
    'pydantic_validator': directives.PydanticValidator,
}


class Config(BaseModel):
    name: str
    default: Any
    types: type
    rebuild: Literal['env'] = 'env'

    @property
    def full_name(self) -> str:
        return f'{EXTENSION_PREFIX}{self.name}'


# fmt: off
APP_CONFIGURATIONS = [
    # settings
    Config(
        name='settings_show_json',
        default=True,
        types=bool,
    ),
    Config(
        name='settings_show_json_error_strategy',
        default=enums.OptionsJsonErrorStrategy.WARN,
        types=str,
    ),
    Config(
        name='settings_show_config_summary',
        default=True,
        types=bool,
    ),
    Config(
        name='settings_show_validator_members',
        default=True,
        types=bool,
    ),
    Config(
        name='settings_show_validator_summary',
        default=True,
        types=bool,
    ),
    Config(
        name='settings_show_field_summary',
        default=True,
        types=bool,
    ),
    Config(
        name='settings_summary_list_order',
        default=enums.OptionsSummaryListOrder.ALPHABETICAL,
        types=str,
    ),
    Config(
        name='settings_hide_paramlist',
        default=True,
        types=bool,
    ),
    Config(
        name='settings_hide_reused_validator',
        default=True,
        types=bool,
    ),
    Config(
        name='settings_undoc_members',
        default=True,
        types=bool,
    ),
    Config(
        name='settings_members',
        default=True,
        types=bool,
    ),
    Config(
        name='settings_member_order',
        default='groupwise',
        types=str,
    ),
    Config(
        name='settings_signature_prefix',
        default='pydantic settings',
        types=str,
    ),

    # model
    Config(
        name='model_show_json',
        default=True,
        types=bool,
    ),
    Config(
        name='model_show_json_error_strategy',
        default=enums.OptionsJsonErrorStrategy.WARN,
        types=str,
    ),
    Config(
        name='model_show_config_summary',
        default=True,
        types=bool,
    ),
    Config(
        name='model_show_validator_members',
        default=True,
        types=bool,
    ),
    Config(
        name='model_show_validator_summary',
        default=True,
        types=bool,
    ),
    Config(
        name='model_show_field_summary',
        default=True,
        types=bool,
    ),
    Config(
        name='model_summary_list_order',
        default=enums.OptionsSummaryListOrder.ALPHABETICAL,
        types=str,
    ),
    Config(
        name='model_hide_paramlist',
        default=True,
        types=bool,
    ),
    Config(
        name='model_hide_reused_validator',
        default=True,
        types=bool,
    ),
    Config(
        name='model_undoc_members',
        default=True,
        types=bool,
    ),
    Config(
        name='model_members',
        default=True,
        types=bool,
    ),
    Config(
        name='model_member_order',
        default='groupwise',
        types=str,
    ),
    Config(
        name='model_signature_prefix',
        default='pydantic model',
        types=str,
    ),
    Config(
        name='model_erdantic_figure',
        default=False,
        types=bool,
    ),
    Config(
        name='model_erdantic_figure_collapsed',
        default=True,
        types=bool,
    ),

    # validator
    Config(
        name='validator_signature_prefix',
        default='validator',
        types=str,
    ),
    Config(
        name='validator_replace_signature',
        default=True,
        types=bool,
    ),
    Config(
        name='validator_list_fields',
        default=False,
        types=bool,
    ),

    # field
    Config(
        name='field_list_validators',
        default=True,
        types=bool,
    ),
    Config(
        name='field_doc_policy',
        default=enums.OptionsFieldDocPolicy.BOTH,
        types=str,
    ),
    Config(
        name='field_show_constraints',
        default=True,
        types=bool,
    ),
    Config(
        name='field_show_alias',
        default=True,
        types=bool,
    ),
    Config(
        name='field_show_default',
        default=True,
        types=bool,
    ),
    Config(
        name='field_show_required',
        default=True,
        types=bool,
    ),
    Config(
        name='field_show_optional',
        default=True,
        types=bool,
    ),
    Config(
        name='field_swap_name_and_alias',
        default=False,
        types=bool,
    ),
    Config(
        name='field_signature_prefix',
        default='field',
        types=str,
    ),
    Config(
        name='field_show_examples',
        default=True,
        types=bool,
    ),

    # general
    Config(
        name='add_fallback_css_class',
        default=True,
        types=bool,
    ),
]
# fmt: on


OBJ_TYPES_MAPPING = {
    ('field', 'validator', 'config'): (
        'obj',
        'any',
    ),
    ('model', 'settings'): (
        'obj',
        'any',
        'class',
    ),
}


def add_css_file(app: Sphinx, *_) -> None:  # noqa: ANN002
    """Adds custom css to HTML output."""

    filename = 'autodoc_pydantic.css'
    static_path = (Path(app.outdir) / '_static').absolute()
    static_path.mkdir(exist_ok=True, parents=True)
    path_css = Path(__file__).parent.joinpath('css', filename)

    if not (static_path / filename).exists():
        content = path_css.read_text()
        (static_path / filename).write_text(content)


def add_domain_object_types(app: Sphinx) -> None:
    """Hack to add object types to already instantiated python domain since
    `add_object_type` currently only works for std domain.

    """

    object_types = app.registry.domain_object_types.setdefault('py', {})
    for obj_types, roles in OBJ_TYPES_MAPPING.items():
        for obj_type in obj_types:
            object_types[f'pydantic_{obj_type}'] = ObjType(obj_type, *roles)


def add_configuration_values(app: Sphinx) -> None:
    """Adds all configuration values to sphinx application."""

    for config in APP_CONFIGURATIONS:
        app.add_config_value(
            name=config.full_name,
            default=config.default,
            types=config.types,
            rebuild=config.rebuild,
        )


def add_directives_and_autodocumenters(
    app: Sphinx,
) -> None:
    """Adds custom pydantic directives and autodocumenters to sphinx
    application.

    """

    for name, directive in DOMAIN_DIRECTIVES.items():
        app.add_directive_to_domain('py', name, directive)

    app.setup_extension('sphinx.ext.autodoc')
    for autodocumenter in AUTODOCUMENTERS:
        app.add_autodocumenter(autodocumenter)

    app.connect(
        'object-description-transform',
        add_fallback_css_class,
    )
