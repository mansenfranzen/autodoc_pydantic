"""This module contains modified `:codeblock:` directive which allows to load
the source code via a object path and render it via the standard sphinx code
block.

Additionally, it contains the `TabDocDirective` which creates a complete
documentation section for config parameters.

"""

import inspect
from typing import List, Tuple

from docutils import nodes
from docutils.nodes import Node
from docutils.parsers.rst import directives
from docutils.statemachine import StringList
from sphinx.directives.code import CodeBlock
import pydoc

from sphinx.ext.autodoc.directive import DummyOptionSpec
from sphinx.util import nested_parse_with_titles
from sphinx.util.docutils import switch_source_input, SphinxDirective

TAB_TEMPLATE = """
.. _{config}:

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

TAB_TEMPLATE_SUB = """
   .. tab:: {value_label}

      .. {directive}:: {path}
         :__doc_disable_except__: {option}
         :{option}: {value}{option_additional}
         :noindex:
"""


def parse_option(option: str) -> str:
    """Helper function to parse a provided option value.

    """

    if "=" not in option:
        return f"         :{option.strip()}:"

    key, value = option.split("=")
    return f"         :{key.strip()}: {value.strip()}"


def parse_options(options: str) -> str:
    """Helper function to parse multiple option values.

    """

    options = options.split(",")
    lines = [parse_option(option) for option in options]
    return "\n" + "\n".join(lines)


def generate_nodes(state, content: StringList):
    """Helper function that takes reST and generates nodes.

    """

    with switch_source_input(state, content):
        node = nodes.section()  # type: Element
        node.document = state.document
        nested_parse_with_titles(state, content, node)

        return node.children


class ConfigurationToc(SphinxDirective):
    """Generates documentation section describing configuration parameters.

    """

    option_spec = DummyOptionSpec()
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True

    def run(self) -> List[Node]:
        name = self.arguments[0]
        prefix = "autodoc_pydantic_"
        startswith = f"{prefix}{name}_"
        configs = [x for x in self.env.config.values.keys()
                   if x.startswith(startswith)]

        content = [":Options:", *[self.create_link(x) for x in configs]]
        content = StringList(content)

        return generate_nodes(self.state, content)

    def sanitize(self, option: str) -> str:
        """Helper function to sanitize option name.

        """

        name = self.arguments[0]
        prefix = "autodoc_pydantic_"
        special = {f"{name}-undoc-members",
                   f"{name}-members",
                   f"{name}-member-order"}

        replaced = option.replace(prefix, "").replace("_", "-")
        if replaced in special:
            replaced = replaced.replace(f"{name}-", "")

        return f":{replaced}:"

    def create_link(self, option: str) -> str:
        """Creates reST reference for given option to configuration section.

        """

        label = self.sanitize(option)
        return f"   - :ref:`{label} <{option}>`"


class TabDocDirective(SphinxDirective):
    """Generates documentation section describing configuration parameters.

    """

    option_spec = DummyOptionSpec()
    has_content = True
    required_arguments = 1
    optional_arguments = 2
    final_argument_whitespace = True

    def process_values(self) -> List[Tuple[str, str]]:
        """Parse the list of provided values and return list of tuples
        representing the actual value and its label.

        Please note, that an asterisk marks the default value. If not asterisk
        is provided, the first value is marked as the default value.

        """

        values = self.options["values"].split(",")
        stripped = [x.strip() for x in values]

        if "*" not in self.options["values"]:
            stripped[0] = stripped[0] + "*"

        return [(x.replace("*", ""), x.replace("*", " (default)"))
                for x in stripped]

    def process_options_additional(self) -> str:
        """Parse the list of additional options.

        """

        option_addition = self.options.get("option_additional", "")
        if option_addition:
            option_addition = parse_options(option_addition)

        return option_addition

    def process_tabs(self):
        """Create the tab content.

        """

        option_additional = self.process_options_additional()

        tabs = []
        for value, label in self.process_values():
            tab_rst = TAB_TEMPLATE_SUB.format(
                value=value,
                value_label=label,
                path=self.options["path"],
                config=self.options["config"],
                option=self.options["option"],
                option_additional=option_additional,
                directive=self.arguments[0]
            )
            tabs.append(tab_rst)

        return "\n".join(tabs)

    def process_title(self) -> str:
        """Generate title.

        """

        title = self.options["title"]
        return title + "\n" + ("-" * len(title))

    def run(self) -> List[Node]:
        """Generate reST.

        """

        tabs = self.process_tabs()
        title = self.process_title()

        content = TAB_TEMPLATE.format(
            title=title,
            description="\n".join(self.content),
            tabs=tabs,
            directive=self.arguments[0],
            path=self.options["path"],
            config=self.options["config"],
            option=self.options["option"]
        )

        content = StringList(content.split("\n"))
        return generate_nodes(self.state, content)


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
        return [line.replace("\n", "") for line in lines]
