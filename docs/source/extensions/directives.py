import inspect
import pydoc
from typing import List, Tuple

import pydantic
import sphinx
import sphinx_copybutton
import sphinx_rtd_theme
import sphinx_tabs
from docutils.nodes import Node
from docutils.statemachine import StringList
from docutils.parsers.rst import directives

from sphinx.directives.code import CodeBlock
from sphinx.ext.autodoc.directive import DummyOptionSpec
from sphinx.util.docutils import SphinxDirective

from docs.source.extensions.helper import generate_nodes, parse_options
from docs.source.extensions.templates import CONFIG_DESC_TAB_TPL, \
    CONFIG_DESC_TPL, VERSION_TEMPLATE


class DocumenterConfigToc(SphinxDirective):
    """Generates a table of contents with configuration options for given
    autodoc_pydantic auto-documenter. Each configuration option provides a
    reference to its user's configuration section describing the configuration
    in very detail.

    """

    option_spec = DummyOptionSpec()
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True

    def run(self) -> List[Node]:
        name = self.arguments[0]
        startswith = f'autodoc_pydantic_{name}_'
        configs = [x for x in self.env.config.values.keys()
                   if x.startswith(startswith)]

        content = [":Options:"] + [self.create_link(x) for x in configs]
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


class ConfigDescription(SphinxDirective):
    """Generates detailed documentation section for individual configuration
    settings including description, possible values, examples and more.

    Parameters
    ----------

    directive header:
        Represents the argument of the directive. Define the auto-documenter
        to be used and documented.
    title:
        Set the title of resulting section.
    path:
        Provide path to a pydantic object which is used to render exemplary
        output for provided configuration values.
    example_path: optional
        Optionally provide explicit path to example code if ``path`` is not
        sufficient for example code.
    confpy:
        Represents the name of the global configuration setting that can be
        modified in ``conf.py``.
    directive_option:
        Represents the name of the local configuration setting that is can be
        used as a directive option.
    enable:
        You may need to enable additional configuration settings for the
        output to render properly. In this case, showing the summary list
        order requires to show summary lists in the first place. Hence, this
        is enabled via ``model-show-validator-summary`` and
        ``model-show-field-summary``.
    values:
        Contains a list of available configuration values for this feature
        which  each will be used to render the output.
    version: optional
        Set the version when this configuration was added.
    directive body:
        Represents the content of the directive. Provide reST describing the
        feature.

    Examples:

    .. code-block::

      .. config_description:: autopydantic_model
         :title: Summary List Order
         :path: target.configuration.ModelSummaryListOrder
         :confpy: autodoc_pydantic_model_summary_list_order
         :directive_option: model-summary-list-order
         :enable: model-show-validator-summary, model-show-field-summary
         :values: alphabetical, bysource
         :version: 1.5.0

         Define the sort order within validator and field summaries (which can be
         activated via :ref:`model-show-validator-summary <autodoc_pydantic_model_show_validator_summary>`
         and :ref:`model-show-field-summary <autodoc_pydantic_model_show_field_summary>`,
         respectively).

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

    def process_enable(self) -> str:
        """Parse the list of additional options which need to be enabled to
        properly render output.

        """

        enable = self.options.get("enable", "")
        if enable:
            enable = parse_options(enable)

        return enable

    def process_tabs(self):
        """Create the tab content.

        """

        enable = self.process_enable()

        tabs = []
        for value, label in self.process_values():
            tab_rst = CONFIG_DESC_TAB_TPL.format(
                value=value,
                value_label=label,
                path=self.options["path"],
                directive_option=self.options["directive_option"],
                enable=enable,
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
        version = self.options.get("version") or "0.1.0"
        path = self.options.get("example_path") or self.options["path"]

        content = CONFIG_DESC_TPL.format(
            title=title,
            description="\n".join(self.content),
            tabs=tabs,
            example_path=path,
            confpy=self.options["confpy"],
            directive_option=self.options["directive_option"],
            version=version
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


class ShowVersions(SphinxDirective):
    """Generates documentation section describing configuration parameters.

    """

    has_content = False
    required_arguments = 0
    optional_arguments = 0

    def run(self) -> List[Node]:
        """Generate reST.

        """

        mermaid = self.env.app.extensions["sphinxcontrib.mermaid"].version

        content = VERSION_TEMPLATE.format(
            sphinx=sphinx.__version__,
            pydantic=pydantic.version.VERSION,
            sphinx_rtd_theme=sphinx_rtd_theme.__version__,
            sphinx_tabs=sphinx_tabs.__version__,
            sphinx_copybutton=sphinx_copybutton.__version__,
            sphinxcontrib_mermaid=mermaid
        )

        content = StringList(content.split("\n"))
        return generate_nodes(self.state, content)
