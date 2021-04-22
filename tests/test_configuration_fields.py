"""This module contains tests for pydantic validator configurations.

"""

from docutils.nodes import (
    paragraph,
    emphasis,
)
from sphinx.addnodes import (
    desc,
    desc_signature,
    desc_name,
    desc_content,
    desc_annotation,
    desc_addname,
    pending_xref,
    index
)
from sphinx.testing.util import assert_node


def test_autodoc_pydantic_field_list_validators_true(autodocument):
    result = [
        '',
        '.. py:pydantic_field:: FieldListValidators.field',
        '   :module: target.configuration',
        '   :type: int',
        '   :value: 1',
        '',
        '   Field.',
        '',
        '   :Validated by:',
        '      - :py:obj:`check <target.configuration.FieldListValidators.check>`',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldListValidators.field',
        options_app={"autodoc_pydantic_field_list_validators": True},
        deactivate_all=True)
    assert result == actual

    # explicit local
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldListValidators.field',
        options_doc={"field-list-validators": True},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldListValidators.field',
        options_app={"autodoc_pydantic_field_list_validators": False},
        options_doc={"field-list-validators": True},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_field_list_validators_false(autodocument):
    result = [
        '',
        '.. py:pydantic_field:: FieldListValidators.field',
        '   :module: target.configuration',
        '   :type: int',
        '   :value: 1',
        '',
        '   Field.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldListValidators.field',
        options_app={"autodoc_pydantic_field_list_validators": False},
        deactivate_all=True)
    assert result == actual

    # explicit local
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldListValidators.field',
        options_doc={"field-list-validators": False},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldListValidators.field',
        options_app={"autodoc_pydantic_field_list_validators": True},
        options_doc={"field-list-validators": False},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_field_doc_policy_docstring(autodocument):
    result = [
        '',
        '.. py:pydantic_field:: FieldDocPolicy.field',
        '   :module: target.configuration',
        '   :type: int',
        '   :value: 1',
        '',
        '   Field.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldDocPolicy.field',
        options_app={"autodoc_pydantic_field_doc_policy": "docstring"},
        deactivate_all=True)
    assert result == actual

    # explicit local
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldDocPolicy.field',
        options_doc={"field-doc-policy": "docstring"},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldDocPolicy.field',
        options_app={"autodoc_pydantic_field_doc_policy": "both"},
        options_doc={"field-doc-policy": "docstring"},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_field_doc_policy_description(autodocument):
    result = [
        '',
        '.. py:pydantic_field:: FieldDocPolicy.field',
        '   :module: target.configuration',
        '   :type: int',
        '   :value: 1',
        '',
        '   Custom Desc.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldDocPolicy.field',
        options_app={"autodoc_pydantic_field_doc_policy": "description"},
        deactivate_all=True)
    assert result == actual

    # explicit local
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldDocPolicy.field',
        options_doc={"field-doc-policy": "description"},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldDocPolicy.field',
        options_app={"autodoc_pydantic_field_doc_policy": "both"},
        options_doc={"field-doc-policy": "description"},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_field_doc_policy_both(autodocument):
    result = [
        '',
        '.. py:pydantic_field:: FieldDocPolicy.field',
        '   :module: target.configuration',
        '   :type: int',
        '   :value: 1',
        '',
        '   Field.',
        '',
        '   Custom Desc.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldDocPolicy.field',
        options_app={"autodoc_pydantic_field_doc_policy": "both"},
        deactivate_all=True)
    assert result == actual

    # explicit local
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldDocPolicy.field',
        options_doc={"field-doc-policy": "both"},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldDocPolicy.field',
        options_app={"autodoc_pydantic_field_doc_policy": "docstring"},
        options_doc={"field-doc-policy": "both"},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_field_list_validators_false(autodocument):
    result = [
        '',
        '.. py:pydantic_field:: FieldListValidators.field',
        '   :module: target.configuration',
        '   :type: int',
        '   :value: 1',
        '',
        '   Field.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldListValidators.field',
        options_app={"autodoc_pydantic_field_list_validators": False},
        deactivate_all=True)
    assert result == actual

    # explicit local
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldListValidators.field',
        options_doc={"field-list-validators": False},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldListValidators.field',
        options_app={"autodoc_pydantic_field_list_validators": True},
        options_doc={"field-list-validators": False},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_field_show_constraints_true(autodocument):
    result = [
        '',
        '.. py:pydantic_field:: FieldShowConstraints.field',
        '   :module: target.configuration',
        '   :type: int',
        '   :value: 1',
        '',
        '   Field.',
        '',
        '   :Constraints:',
        '      - **minimum** = 0',
        '      - **maximum** = 100',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldShowConstraints.field',
        options_app={"autodoc_pydantic_field_show_constraints": True},
        deactivate_all=True)
    assert result == actual

    # explicit local
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldShowConstraints.field',
        options_doc={"field-show-constraints": True},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldShowConstraints.field',
        options_app={"autodoc_pydantic_field_show_constraints": False},
        options_doc={"field-show-constraints": True},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_field_show_constraints_false(autodocument):
    result = [
        '',
        '.. py:pydantic_field:: FieldShowConstraints.field',
        '   :module: target.configuration',
        '   :type: int',
        '   :value: 1',
        '',
        '   Field.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldShowConstraints.field',
        options_app={"autodoc_pydantic_field_show_constraints": False},
        deactivate_all=True)
    assert result == actual

    # explicit local
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldShowConstraints.field',
        options_doc={"field-show-constraints": False},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldShowConstraints.field',
        options_app={"autodoc_pydantic_field_show_constraints": True},
        options_doc={"field-show-constraints": False},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_field_show_alias_true(autodocument):
    result = [
        '',
        '.. py:pydantic_field:: FieldShowAlias.field',
        '   :module: target.configuration',
        '   :type: int',
        '   :value: 1',
        '   :field-show-alias: True',
        '',
        '   Field.',
        '',
    ]

    # explicit local
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldShowAlias.field',
        options_doc={"field-show-alias": True},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldShowAlias.field',
        options_app={"autodoc_pydantic_field_show_alias": False},
        options_doc={"field-show-alias": True},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_field_show_alias_false(autodocument):
    result = [
        '',
        '.. py:pydantic_field:: FieldShowAlias.field',
        '   :module: target.configuration',
        '   :type: int',
        '   :value: 1',
        '   :field-show-alias: False',
        '',
        '   Field.',
        '',
    ]

    # explicit local
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldShowAlias.field',
        options_doc={"field-show-alias": False},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldShowAlias.field',
        options_app={"autodoc_pydantic_field_show_alias": True},
        options_doc={"field-show-alias": False},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_field_show_alias_true_directive(parse_rst):
    """Tests pydantic_validator directive.

    """

    output_nodes = (
        index,
        [desc, ([desc_signature, ([desc_annotation, "field "],
                                  [desc_addname, "FieldShowAlias."],
                                  [desc_name, "field"],
                                  [desc_annotation, " = 1"],
                                  [desc_annotation, " (alias 'field2')"])],
                [desc_content, ()])
         ]
    )


    # explicit local
    input_rst = [
        '',
        '.. py:pydantic_field:: FieldShowAlias.field',
        '   :module: target.configuration',
        '   :value: 1',
        '   :field-show-alias: True',
        ''
    ]

    doctree = parse_rst(input_rst)
    assert_node(doctree, output_nodes)


    # explicit local overwrite explict global
    doctree = parse_rst(input_rst,
                        conf={"autodoc_pydantic_field_show_alias": False})
    assert_node(doctree, output_nodes)

    # explicit global
    input_rst = [
        '',
        '.. py:pydantic_field:: FieldShowAlias.field',
        '   :module: target.configuration',
        '   :value: 1',
        ''
    ]
    doctree = parse_rst(input_rst,
                        conf={"autodoc_pydantic_field_show_alias": True})
    assert_node(doctree, output_nodes)


def test_autodoc_pydantic_field_show_alias_false_directive(parse_rst):
    """Tests pydantic_validator directive.

    """

    output_nodes = (
        index,
        [desc, ([desc_signature, ([desc_annotation, "field "],
                                  [desc_addname, "FieldShowAlias."],
                                  [desc_name, "field"],
                                  [desc_annotation, " = 1"])],
                [desc_content, ()])
         ]
    )


    # explicit local
    input_rst = [
        '',
        '.. py:pydantic_field:: FieldShowAlias.field',
        '   :module: target.configuration',
        '   :value: 1',
        '   :field-show-alias: False',
        ''
    ]

    doctree = parse_rst(input_rst)
    assert_node(doctree, output_nodes)


    # explicit local overwrite explict global
    doctree = parse_rst(input_rst,
                        conf={"autodoc_pydantic_field_show_alias": True})
    assert_node(doctree, output_nodes)

    # explicit global
    input_rst = [
        '',
        '.. py:pydantic_field:: FieldShowAlias.field',
        '   :module: target.configuration',
        '   :value: 1',
        ''
    ]
    doctree = parse_rst(input_rst,
                        conf={"autodoc_pydantic_field_show_alias": False})
    assert_node(doctree, output_nodes)


def test_autodoc_pydantic_field_show_default_true(autodocument):
    result = [
        '',
        '.. py:pydantic_field:: FieldShowDefault.field',
        '   :module: target.configuration',
        '   :type: int',
        '   :value: 1',
        '',
        '   Field.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldShowDefault.field',
        options_app={"autodoc_pydantic_field_show_default": True},
        deactivate_all=True)
    assert result == actual

    # explicit local
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldShowDefault.field',
        options_doc={"field-show-default": True},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldShowDefault.field',
        options_app={"autodoc_pydantic_field_show_default": False},
        options_doc={"field-show-default": True},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_field_show_default_false(autodocument):
    result = [
        '',
        '.. py:pydantic_field:: FieldShowDefault.field',
        '   :module: target.configuration',
        '   :type: int',
        '',
        '   Field.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldShowDefault.field',
        options_app={"autodoc_pydantic_field_show_default": False},
        deactivate_all=True)
    assert result == actual

    # explicit local
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldShowDefault.field',
        options_doc={"field-show-default": False},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldShowDefault.field',
        options_app={"autodoc_pydantic_field_show_default": True},
        options_doc={"field-show-default": False},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_field_signature_prefix(autodocument):

    # default
    result = [
        '',
        ".. py:pydantic_field:: FieldSignaturePrefix.field",
        '   :module: target.configuration',
        '   :type: int',
        '   :value: 1',
        '',
        '   Field.',
        ''
    ]

    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldSignaturePrefix.field',
        deactivate_all=True)
    assert result == actual

    # explicit value
    result = [
        '',
        ".. py:pydantic_field:: FieldSignaturePrefix.field",
        '   :module: target.configuration',
        '   :type: int',
        '   :value: 1',
        '   :field-signature-prefix: foobar',
        '',
        '   Field.',
        ''
    ]

    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldSignaturePrefix.field',
        options_doc={"field-signature-prefix": "foobar"},
        deactivate_all=True)
    assert result == actual

    # explict empty
    result = [
        '',
        ".. py:pydantic_field:: FieldSignaturePrefix.field",
        '   :module: target.configuration',
        '   :type: int',
        '   :value: 1',
        '   :field-signature-prefix: ',
        '',
        '   Field.',
        ''
    ]

    actual = autodocument(
        documenter='pydantic_field',
        object_path='target.configuration.FieldSignaturePrefix.field',
        options_doc={"field-signature-prefix": ""},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_field_signature_prefix_directive(parse_rst):

    # default
    input_rst = [
        '',
        ".. py:pydantic_field:: FieldSignaturePrefix.field",
        '   :module: target.configuration',
        '',
        '   Field.',
        ''
    ]

    doctree = parse_rst(input_rst)
    assert_node(doctree[1][0][0], [desc_annotation, "field "])

    # empty
    doctree = parse_rst(input_rst,
                        conf={"autodoc_pydantic_field_signature_prefix": ""})
    assert_node(doctree[1][0][0], [desc_annotation, "attribute "])

    # custom
    input_rst = [
        '',
        ".. py:pydantic_field:: FieldSignaturePrefix.field",
        '   :module: target.configuration',
        '   :field-signature-prefix: foobar',
        '',
        '   Field.',
        ''
    ]

    doctree = parse_rst(input_rst)
    assert_node(doctree[1][0][0], [desc_annotation, "foobar "])
