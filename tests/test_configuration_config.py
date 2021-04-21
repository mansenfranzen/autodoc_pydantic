"""This module contains tests for pydantic config class configurations.

"""

from docutils.nodes import paragraph
from sphinx.addnodes import (
    index,
    desc,
    desc_signature,
    desc_annotation,
    desc_addname,
    desc_name,
    desc_content
)
from sphinx.testing.util import assert_node
import sphinx
import pytest


@pytest.mark.skipif(sphinx.version_info[:2] <= (3, 4),
                    reason="Older sphinx version to not document attribute "
                           "doc string correctly.")
def test_autodoc_pydantic_config_members_true_gt34(autodocument):
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

    # explict global
    actual = autodocument(
        documenter='pydantic_config',
        object_path='target.configuration.ConfigMembers.Config',
        options_app={"autodoc_pydantic_config_members": True},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_config',
        object_path='target.configuration.ConfigMembers.Config',
        options_doc={"members": None},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_config',
        object_path='target.configuration.ConfigMembers.Config',
        options_app={"autodoc_pydantic_config_members": False},
        options_doc={"members": None},
        deactivate_all=True)
    assert result == actual


@pytest.mark.skipif(sphinx.version_info[:2] > (3, 4),
                    reason="Newer sphinx version correctly document attribute "
                           "doc strings.")
def test_autodoc_pydantic_config_members_true_le34(autodocument):
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
        '',
        '   .. py:attribute:: Config.title',
        '      :module: target.configuration.ConfigMembers',
        "      :value: 'foobar'",
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_config',
        object_path='target.configuration.ConfigMembers.Config',
        options_app={"autodoc_pydantic_config_members": True},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_config',
        object_path='target.configuration.ConfigMembers.Config',
        options_doc={"members": None},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_config',
        object_path='target.configuration.ConfigMembers.Config',
        options_app={"autodoc_pydantic_config_members": False},
        options_doc={"members": None},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_config_members_false(autodocument):
    result = [
        '',
        ".. py:pydantic_config:: Config()",
        '   :module: target.configuration.ConfigMembers',
        '',
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_config',
        object_path='target.configuration.ConfigMembers.Config',
        options_app={"autodoc_pydantic_config_members": False},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_config',
        object_path='target.configuration.ConfigMembers.Config',
        options_doc={"members": "False"},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_config',
        object_path='target.configuration.ConfigMembers.Config',
        options_app={"autodoc_pydantic_config_members": True},
        options_doc={"members": "False"},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_config_signature_prefix(autodocument):

    # default
    result = [
        '',
        ".. py:pydantic_config:: Config()",
        '   :module: target.configuration.ConfigSignaturePrefix',
        '',
        '   Config.',
        ''
    ]

    actual = autodocument(
        documenter='pydantic_config',
        object_path='target.configuration.ConfigSignaturePrefix.Config',
        deactivate_all=True)
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

    actual = autodocument(
        documenter='pydantic_config',
        object_path='target.configuration.ConfigSignaturePrefix.Config',
        options_doc={"config-signature-prefix": "foobar"},
        deactivate_all=True)
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

    actual = autodocument(
        documenter='pydantic_config',
        object_path='target.configuration.ConfigSignaturePrefix.Config',
        options_doc={"config-signature-prefix": ""},
        deactivate_all=True)
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
