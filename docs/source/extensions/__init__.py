from sphinx.application import Sphinx

from .directives import (
    DocumenterConfigToc,
    ConfigDescription,
    AutoCodeBlock,
    ShowVersions,
)


def setup(app: Sphinx) -> None:
    app.add_directive('autocodeblock', AutoCodeBlock)
    app.add_directive('config_description', ConfigDescription)
    app.add_directive('documenter_config_toc', DocumenterConfigToc)
    app.add_directive('show_versions', ShowVersions)
