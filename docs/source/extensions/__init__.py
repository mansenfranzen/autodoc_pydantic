from sphinx.application import Sphinx

from .helper import AutoCodeBlock
from .helper import TabDocDirective


def setup(app: Sphinx) -> None:
    app.add_directive("autocodeblock", AutoCodeBlock)
    app.add_directive("tabdocconfig", TabDocDirective)