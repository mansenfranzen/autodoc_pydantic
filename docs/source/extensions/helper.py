"""This module contains modified `:codeblock:` directive which allows to load
the source code via a object path and render it via the standard sphinx code
block.

Additionally, it contains the `TabDocDirective` which creates a complete
documentation section for config parameters.

"""

import inspect
from typing import List

from docutils import nodes
from docutils.nodes import Node
from docutils.parsers.rst import directives
from docutils.statemachine import StringList
from sphinx.directives import CodeBlock
import pydoc

from sphinx.ext.autodoc.directive import DummyOptionSpec
from sphinx.util import nested_parse_with_titles
from sphinx.util.docutils import switch_source_input, SphinxDirective


tab_sub_tpl = """
   .. tab:: {value_label}

      .. {directive}:: {path}
         :__doc_disable_except__: {option}
         :{option}: {value}{option_additional}
         :noindex:
"""

tab_tpl = """
{title}

{description}

:conf.py: *{config}*

:option: *{option}*

**Available values with rendered examples:**

.. tabs::

{tabs}
           
   .. tab:: *example code*

      .. autocodeblock:: {path}

"""


def parse_option(option: str) -> str:
    """Helper function to parse a provided option value.

    """

    if "=" in option:
        key, value = option.split("=")
        return f"         :{key.strip()}: {value.strip()}"
    else:
        return f"         :{option.strip()}:"


def parse_options(options: str) -> str:
    """Helper function to parse multiple option values.

    """

    options = options.split(",")
    lines = [parse_option(option) for option in options]
    return "\n" + "\n".join(lines)


class TabDocDirective(SphinxDirective):
    """Generates documentation section describing configuration parameters.

    """

    option_spec = DummyOptionSpec()
    has_content = True
    required_arguments = 1
    optional_arguments = 2
    final_argument_whitespace = True

    def run(self) -> List[Node]:

        option_addition = self.options.get("option_additional", "")
        if option_addition:
            option_addition = parse_options(option_addition)

        defaults = self.options["values"].split(",")
        defaults = [x.strip() for x in defaults]
        defaults_remaining = ", ".join(defaults[1:])

        tabs = []
        for default in defaults:
            value_label = default if len(tabs) else default + " (default)"
            tab_rst = tab_sub_tpl.format(
                value=default,
                value_label=value_label,
                path=self.options["path"],
                config=self.options["config"],
                option=self.options["option"],
                option_additional=option_addition,
                directive=self.arguments[0]
            )
            tabs.append(tab_rst)

        title = self.options["title"]
        title = title + "\n" + ("-" * len(title))

        content = tab_tpl.format(
            title=title,
            description=" ".join(self.content),
            tabs="\n".join(tabs),
            directive=self.arguments[0],
            path=self.options["path"],
            config=self.options["config"],
            option=self.options["option"],
            option_additional=option_addition,
            default=defaults[0],
            default_remaining=defaults_remaining,
        )

        content = StringList(content.split("\n"))
        with switch_source_input(self.state, content):
            node = nodes.section()  # type: Element
            # necessary so that the child nodes get the right source/line set
            node.document = self.state.document
            nested_parse_with_titles(self.state, content, node)

            return node.children


class AutoCodeBlock(CodeBlock):
    """Modified :codeblock: directive to display the source code of a referenced
    object.

    """

    has_content = False
    required_arguments = 1

    option_spec = CodeBlock.option_spec.copy()
    option_spec.update({"language": directives.unchanged})

    def run(self) -> List[Node]:
        """Modify content and argument to make it work with parent class without
        any more changes.

        """

        self.content = self.get_source_code(self.arguments[0])
        self.arguments[0] = self.options.get("language") or "python"

        return super().run()

    def get_source_code(self, objpath: str) -> List[str]:
        """Return the source code from a given object path.

        Thanks to pydoc and inspect modules this is plain simple.  Please note,
        using `inspect.getsource` does not work for pydantic fields.

        """

        obj = pydoc.locate(objpath)
        lines = inspect.getsourcelines(obj)[0]
        sanitized = [line.replace("\n", "") for line in lines]

        return sanitized
