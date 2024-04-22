from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sphinxcontrib.autodoc_pydantic import application

try:
    from importlib.metadata import version
except ModuleNotFoundError:
    from importlib_metadata import version  # type: ignore[no-redef,import-not-found]

__version__ = version('autodoc_pydantic')

if TYPE_CHECKING:
    from sphinx.application import Sphinx


def setup(app: Sphinx) -> dict[str, Any]:
    application.add_configuration_values(app)
    application.add_directives_and_autodocumenters(app)
    application.add_domain_object_types(app)
    app.add_css_file('autodoc_pydantic.css')
    app.connect('build-finished', application.add_css_file)

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
