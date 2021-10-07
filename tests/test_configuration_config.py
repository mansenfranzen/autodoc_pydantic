"""This module contains tests for pydantic config class configurations.

"""

from sphinx.addnodes import desc_annotation
from sphinx.testing.util import assert_node
import sphinx

from sphinxcontrib.autodoc_pydantic import PydanticConfigClassDocumenter

KWARGS = dict(documenter=PydanticConfigClassDocumenter.directivetype,
              deactivate_all=True)


def test_autodoc_pydantic_config_members_true(autodocument):
    kwargs = dict(object_path='target.configuration.ConfigMembers.Config',
                  **KWARGS)

    result = [
        '',
        ".. py:pydantic_config:: Config()",
        '   :module: target.configuration.ConfigMembers',
        '',
        '',
        '   .. py:attribute:: Config.allow_mutation',
        '      :module: target.configuration.ConfigMembers',
        '      :value: True',
        '',
        '      Allow Mutation.',
        '',
        '',
        '   .. py:attribute:: Config.title',
        '      :module: target.configuration.ConfigMembers',
        "      :value: 'foobar'",
        ''
    ]

    if sphinx.version_info[:2] <= (3, 4):
        result.pop(9)
        result.pop(10)

    # explict global
    actual = autodocument(
        options_app={"autodoc_pydantic_config_members": True}, **kwargs)
    assert result == actual

    # explict local
    actual = autodocument(options_doc={"members": None}, **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_config_members": False},
        options_doc={"members": None},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_config_members_false(autodocument):
    kwargs = dict(object_path='target.configuration.ConfigMembers.Config',
                  **KWARGS)

    result = [
        '',
        ".. py:pydantic_config:: Config()",
        '   :module: target.configuration.ConfigMembers',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={"autodoc_pydantic_config_members": False},
        **kwargs)
    assert result == actual

    # explict local
    actual = autodocument(options_doc={"members": "False"}, **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_config_members": True},
        options_doc={"members": "False"},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_config_signature_prefix(autodocument):
    kwargs = dict(
        object_path='target.configuration.ConfigSignaturePrefix.Config',
        **KWARGS)

    # default
    result = [
        '',
        ".. py:pydantic_config:: Config()",
        '   :module: target.configuration.ConfigSignaturePrefix',
        '',
        '   Config.',
        ''
    ]

    actual = autodocument(**kwargs)
    assert result == actual

    # explicit value
    result = [
        '',
        ".. py:pydantic_config:: Config()",
        '   :module: target.configuration.ConfigSignaturePrefix',
        '   :config-signature-prefix: foobar',
        '',
        '   Config.',
        ''
    ]

    actual = autodocument(options_doc={"config-signature-prefix": "foobar"},
                          **kwargs)
    assert result == actual

    # explict empty
    result = [
        '',
        ".. py:pydantic_config:: Config()",
        '   :module: target.configuration.ConfigSignaturePrefix',
        '   :config-signature-prefix: ',
        '',
        '   Config.',
        ''
    ]

    actual = autodocument(options_doc={"config-signature-prefix": ""},
                          **kwargs)
    assert result == actual


def test_autodoc_pydantic_config_signature_prefix_directive(parse_rst):
    # default
    input_rst = [
        '',
        ".. py:pydantic_config:: Config()",
        '   :module: target.configuration.ConfigSignaturePrefix',
        '',
        '   Config.',
        ''
    ]

    doctree = parse_rst(input_rst)
    assert_node(doctree[1][0][0], [desc_annotation, "model "])

    # empty
    doctree = parse_rst(input_rst,
                        conf={"autodoc_pydantic_config_signature_prefix": ""})
    assert_node(doctree[1][0][0], [desc_annotation, "class "])

    # custom
    input_rst = [
        '',
        ".. py:pydantic_config:: Config()",
        '   :module: target.configuration.ConfigSignaturePrefix',
        '   :config-signature-prefix: foobar',
        '',
        '   Config.',
        ''
    ]

    doctree = parse_rst(input_rst)
    assert_node(doctree[1][0][0], [desc_annotation, "foobar "])
