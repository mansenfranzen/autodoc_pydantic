"""Contains the extension setup."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal

try:
    from importlib.metadata import version
except ModuleNotFoundError:
    from importlib_metadata import version  # type: ignore[no-redef,import-not-found]

from pydantic import BaseModel
from sphinx.domains import ObjType

from sphinxcontrib.autodoc_pydantic.directives.autodocumenters import (
    PydanticFieldDocumenter,
    PydanticModelDocumenter,
    PydanticSettingsDocumenter,
    PydanticValidatorDocumenter,
)
from sphinxcontrib.autodoc_pydantic.directives.directives import (
    PydanticField,
    PydanticModel,
    PydanticSettings,
    PydanticValidator,
)
from sphinxcontrib.autodoc_pydantic.directives.options.enums import (
    OptionsFieldDocPolicy,
    OptionsJsonErrorStrategy,
    OptionsSummaryListOrder,
)
from sphinxcontrib.autodoc_pydantic.events import add_fallback_css_class

__version__ = version('autodoc_pydantic')

if TYPE_CHECKING:
    from sphinx.application import Sphinx


PRE = 'autodoc_pydantic_'


class AppConfig(BaseModel):
    name: str
    default: Any
    types: type
    rebuild: Literal['env'] = 'env'


APP_CONFIGURATIONS = [
    # settings
    AppConfig(name=f'{PRE}settings_show_json', default=True, types=bool),
    AppConfig(
        name=f'{PRE}settings_show_json_error_strategy',
        default=OptionsJsonErrorStrategy.WARN,
        types=str,
    ),
    AppConfig(name=f'{PRE}settings_show_config_summary', default=True, types=bool),
    AppConfig(name=f'{PRE}settings_show_validator_members', default=True, types=bool),
    AppConfig(name=f'{PRE}settings_show_validator_summary', default=True, types=bool),
    AppConfig(name=f'{PRE}settings_show_field_summary', default=True, types=bool),
    AppConfig(
        name=f'{PRE}settings_summary_list_order',
        default=OptionsSummaryListOrder.ALPHABETICAL,
        types=str,
    ),
    AppConfig(name=f'{PRE}settings_hide_paramlist', default=True, types=bool),
    AppConfig(name=f'{PRE}settings_hide_reused_validator', default=True, types=bool),
    AppConfig(name=f'{PRE}settings_undoc_members', default=True, types=bool),
    AppConfig(name=f'{PRE}settings_members', default=True, types=bool),
    AppConfig(name=f'{PRE}settings_member_order', default='groupwise', types=str),
    AppConfig(
        name=f'{PRE}settings_signature_prefix',
        default='pydantic settings',
        types=str,
    ),
    # model
    AppConfig(name=f'{PRE}model_show_json', default=True, types=bool),
    AppConfig(
        name=f'{PRE}model_show_json_error_strategy',
        default=OptionsJsonErrorStrategy.WARN,
        types=str,
    ),
    AppConfig(name=f'{PRE}model_show_config_summary', default=True, types=bool),
    AppConfig(name=f'{PRE}model_show_validator_members', default=True, types=bool),
    AppConfig(name=f'{PRE}model_show_validator_summary', default=True, types=bool),
    AppConfig(name=f'{PRE}model_show_field_summary', default=True, types=bool),
    AppConfig(
        name=f'{PRE}model_summary_list_order',
        default=OptionsSummaryListOrder.ALPHABETICAL,
        types=str,
    ),
    AppConfig(name=f'{PRE}model_hide_paramlist', default=True, types=bool),
    AppConfig(name=f'{PRE}model_hide_reused_validator', default=True, types=bool),
    AppConfig(name=f'{PRE}model_undoc_members', default=True, types=bool),
    AppConfig(name=f'{PRE}model_members', default=True, types=bool),
    AppConfig(name=f'{PRE}model_member_order', default='groupwise', types=str),
    AppConfig(name=f'{PRE}model_signature_prefix', default='pydantic model', types=str),
    AppConfig(name=f'{PRE}model_erdantic_figure', default=False, types=bool),
    AppConfig(name=f'{PRE}model_erdantic_figure_collapsed', default=True, types=bool),
    # validator
    AppConfig(name=f'{PRE}validator_signature_prefix', default='validator', types=str),
    AppConfig(name=f'{PRE}validator_replace_signature', default=True, types=bool),
    AppConfig(name=f'{PRE}validator_list_fields', default=False, types=bool),
    # field
    AppConfig(name=f'{PRE}field_list_validators', default=True, types=bool),
    AppConfig(
        name=f'{PRE}field_doc_policy', default=OptionsFieldDocPolicy.BOTH, types=str
    ),
    AppConfig(name=f'{PRE}field_show_constraints', default=True, types=bool),
    AppConfig(name=f'{PRE}field_show_alias', default=True, types=bool),
    AppConfig(name=f'{PRE}field_show_default', default=True, types=bool),
    AppConfig(name=f'{PRE}field_show_required', default=True, types=bool),
    AppConfig(name=f'{PRE}field_show_optional', default=True, types=bool),
    AppConfig(name=f'{PRE}field_swap_name_and_alias', default=False, types=bool),
    AppConfig(name=f'{PRE}field_signature_prefix', default='field', types=str),
    # general
    AppConfig(name=f'{PRE}add_fallback_css_class', default=True, types=bool),
]


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

    obj_types_mapping = {
        ('field', 'validator', 'config'): ('obj', 'any'),
        ('model', 'settings'): ('obj', 'any', 'class'),
    }

    for obj_types, roles in obj_types_mapping.items():
        for obj_type in obj_types:
            object_types[f'pydantic_{obj_type}'] = ObjType(obj_type, *roles)


def add_configuration_values(app: Sphinx) -> None:
    """Adds all configuration values to sphinx application."""

    for config in APP_CONFIGURATIONS:
        app.add_config_value(
            name=config.name,
            default=config.default,
            types=config.types,
            rebuild=config.rebuild,
        )


def add_directives_and_autodocumenters(app: Sphinx) -> None:
    """Adds custom pydantic directives and autodocumenters to sphinx
    application.

    """

    app.add_directive_to_domain('py', 'pydantic_field', PydanticField)
    app.add_directive_to_domain('py', 'pydantic_model', PydanticModel)
    app.add_directive_to_domain('py', 'pydantic_settings', PydanticSettings)
    app.add_directive_to_domain('py', 'pydantic_validator', PydanticValidator)

    app.setup_extension('sphinx.ext.autodoc')
    app.add_autodocumenter(PydanticFieldDocumenter)
    app.add_autodocumenter(PydanticModelDocumenter)
    app.add_autodocumenter(PydanticSettingsDocumenter)
    app.add_autodocumenter(PydanticValidatorDocumenter)

    app.connect('object-description-transform', add_fallback_css_class)


def setup(app: Sphinx) -> dict[str, Any]:
    add_configuration_values(app)
    add_directives_and_autodocumenters(app)
    add_domain_object_types(app)
    app.add_css_file('autodoc_pydantic.css')
    app.connect('build-finished', add_css_file)

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
