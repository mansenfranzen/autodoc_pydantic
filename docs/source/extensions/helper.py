from docutils import nodes
from docutils.statemachine import StringList

from sphinx.util import nested_parse_with_titles
from sphinx.util.docutils import switch_source_input


def parse_option(option: str) -> str:
    """Helper function to parse a provided option value."""

    if '=' not in option:
        return f'         :{option.strip()}:'

    key, value = option.split('=')
    return f'         :{key.strip()}: {value.strip()}'


def parse_options(options: str) -> str:
    """Helper function to parse multiple option values."""

    options = options.split(',')
    lines = [parse_option(option) for option in options]
    return '\n' + '\n'.join(lines)


def generate_nodes(state, content: StringList):
    """Helper function that takes reST and generates nodes."""

    with switch_source_input(state, content):
        node = nodes.section()  # type: Element
        node.document = state.document
        nested_parse_with_titles(state, content, node)

        return node.children
