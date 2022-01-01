from sphinx.application import Sphinx

from .helper import (
    AutoCodeBlock,
    TabDocDirective,
    ConfigurationToc,
    ShowVersions
)

def setup(app: Sphinx) -> None:
    app.add_directive("autocodeblock", AutoCodeBlock)
    app.add_directive("tabdocconfig", TabDocDirective)
    app.add_directive("configtoc", ConfigurationToc)
    app.add_directive("show_versions", ShowVersions)
