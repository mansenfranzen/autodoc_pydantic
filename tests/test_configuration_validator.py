"""This module contains tests for pydantic specific directives.

"""

from docutils.nodes import (
    paragraph,
    field_list,
    field,
    field_name,
    field_body,
    bullet_list,
    list_item,
    literal,
    emphasis,
    strong
)
from sphinx.addnodes import (
    desc,
    desc_signature,
    desc_name,
    desc_parameterlist,
    desc_content,
    desc_annotation,
    desc_addname,
    pending_xref,
    index
)
from sphinx.testing.util import assert_node

def test_autodoc_pydantic_validator_replace_signature_true(autodocument):
    result = [
        '',
        '.. py:pydantic_validator:: ValidatorReplaceSignature.check',
        '   :module: target.configuration',
        '   :classmethod:',
        '',
        '   Check.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_validator',
        object_path='target.configuration.ValidatorReplaceSignature.check',
        options_app={"autodoc_pydantic_validator_replace_signature": True},
        deactivate_all=True)
    assert result == actual

    # explict local
    result = [
        '',
        '.. py:pydantic_validator:: ValidatorReplaceSignature.check',
        '   :module: target.configuration',
        '   :classmethod:',
        '   :validator-replace-signature: True',
        '',
        '   Check.',
        ''
    ]

    actual = autodocument(
        documenter='pydantic_validator',
        object_path='target.configuration.ValidatorReplaceSignature.check',
        options_doc={"validator-replace-signature": True},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    result = [
        '',
        '.. py:pydantic_validator:: ValidatorReplaceSignature.check',
        '   :module: target.configuration',
        '   :classmethod:',
        '   :validator-replace-signature: True',
        '',
        '   Check.',
        ''
    ]

    actual = autodocument(
        documenter='pydantic_validator',
        object_path='target.configuration.ValidatorReplaceSignature.check',
        options_app={"autodoc_pydantic_validator_replace_signature": False},
        options_doc={"validator-replace-signature": True},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_validator_replace_signature_false(autodocument):
    # explict global
    result = [
        '',
        '.. py:pydantic_validator:: ValidatorReplaceSignature.check(v) -> str',
        '   :module: target.configuration',
        '   :classmethod:',
        '',
        '   Check.',
        ''
    ]

    actual = autodocument(
        documenter='pydantic_validator',
        object_path='target.configuration.ValidatorReplaceSignature.check',
        options_app={"autodoc_pydantic_validator_replace_signature": False},
        deactivate_all=True)
    assert result == actual

    # explict local
    result = [
        '',
        '.. py:pydantic_validator:: ValidatorReplaceSignature.check(v) -> str',
        '   :module: target.configuration',
        '   :classmethod:',
        '   :validator-replace-signature: False',
        '',
        '   Check.',
        ''
    ]

    actual = autodocument(
        documenter='pydantic_validator',
        object_path='target.configuration.ValidatorReplaceSignature.check',
        options_doc={"validator-replace-signature": False},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_validator',
        object_path='target.configuration.ValidatorReplaceSignature.check',
        options_app={"autodoc_pydantic_validator_replace_signature": True},
        options_doc={"validator-replace-signature": False},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_validator_replace_signature_true_directive(parse_rst):
    """Tests pydantic_validator directive.

    """

    output_nodes = (
        index,
        [desc, ([desc_signature, ([desc_annotation, "validator "],
                                  [desc_addname, "ValidatorReplaceSignature."],
                                  [desc_name, "check"],
                                  [desc_annotation, "  »  "],
                                  [pending_xref, ([emphasis, "field"])])],
                [desc_content, ([paragraph, "Check."])])
         ]
    )


    # explicit local
    input_rst = [
        '',
        '.. py:pydantic_validator:: ValidatorReplaceSignature.check',
        '   :module: target.configuration',
        '   :classmethod:',
        '   :validator-replace-signature: True',
        '',
        '   Check.',
        ''
    ]
    doctree = parse_rst(input_rst)
    assert_node(doctree, output_nodes)

    # explicit global
    input_rst = [
        '',
        '.. py:pydantic_validator:: ValidatorReplaceSignature.check',
        '   :module: target.configuration',
        '   :classmethod:',
        '',
        '   Check.',
        ''
    ]
    doctree = parse_rst(input_rst,
                        conf={"autodoc_pydantic_validator_replace_signature": True})
    assert_node(doctree, output_nodes)
