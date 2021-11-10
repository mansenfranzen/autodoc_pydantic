"""This module contains tests for pydantic validator configurations.

"""

import pydantic
import pytest

from sphinx.addnodes import (
    desc,
    desc_signature,
    desc_name,
    desc_content,
    desc_annotation,
    desc_addname,
    index
)
from sphinx.testing.util import assert_node
from sphinxcontrib.autodoc_pydantic import PydanticFieldDocumenter
from .compatability import desc_annotation_default_value, \
    desc_annotation_directive_prefix

KWARGS = dict(documenter=PydanticFieldDocumenter.directivetype,
              deactivate_all=True)


def test_autodoc_pydantic_field_list_validators_true(autodocument):
    kwargs = dict(object_path='target.configuration.FieldListValidators.field',
                  **KWARGS)

    result = [
        '',
        '.. py:pydantic_field:: FieldListValidators.field',
        '   :module: target.configuration',
        '   :type: int',
        '',
        '   Field.',
        '',
        '   :Validated by:',
        '      - :py:obj:`check <target.configuration.FieldListValidators.check>`',
        ''
    ]

    # explict global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_list_validators": True},
        **kwargs)
    assert result == actual

    # explicit local
    actual = autodocument(
        options_doc={"field-list-validators": True},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_list_validators": False},
        options_doc={"field-list-validators": True},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_field_list_validators_false(autodocument):
    kwargs = dict(object_path='target.configuration.FieldListValidators.field',
                  **KWARGS)

    result = [
        '',
        '.. py:pydantic_field:: FieldListValidators.field',
        '   :module: target.configuration',
        '   :type: int',
        '',
        '   Field.',
        ''
    ]

    # explict global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_list_validators": False},
        **kwargs)
    assert result == actual

    # explicit local
    actual = autodocument(
        options_doc={"field-list-validators": False},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_list_validators": True},
        options_doc={"field-list-validators": False},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_field_doc_policy_docstring(autodocument):
    kwargs = dict(object_path='target.configuration.FieldDocPolicy.field',
                  **KWARGS)

    result = [
        '',
        '.. py:pydantic_field:: FieldDocPolicy.field',
        '   :module: target.configuration',
        '   :type: int',
        '',
        '   Field.',
        ''
    ]

    # explict global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_doc_policy": "docstring"},
        **kwargs)
    assert result == actual

    # explicit local
    actual = autodocument(
        options_doc={"field-doc-policy": "docstring"},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_doc_policy": "both"},
        options_doc={"field-doc-policy": "docstring"},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_field_doc_policy_description(autodocument):
    kwargs = dict(object_path='target.configuration.FieldDocPolicy.field',
                  **KWARGS)

    result = [
        '',
        '.. py:pydantic_field:: FieldDocPolicy.field',
        '   :module: target.configuration',
        '   :type: int',
        '',
        '   Custom Desc.',
        ''
    ]

    # explict global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_doc_policy": "description"},
        **kwargs)
    assert result == actual

    # explicit local
    actual = autodocument(
        options_doc={"field-doc-policy": "description"},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_doc_policy": "both"},
        options_doc={"field-doc-policy": "description"},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_field_doc_policy_both(autodocument):
    kwargs = dict(object_path='target.configuration.FieldDocPolicy.field',
                  **KWARGS)

    result = [
        '',
        '.. py:pydantic_field:: FieldDocPolicy.field',
        '   :module: target.configuration',
        '   :type: int',
        '',
        '   Field.',
        '',
        '   Custom Desc.',
        ''
    ]

    # explict global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_doc_policy": "both"},
        **kwargs)
    assert result == actual

    # explicit local
    actual = autodocument(
        options_doc={"field-doc-policy": "both"},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_doc_policy": "docstring"},
        options_doc={"field-doc-policy": "both"},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_field_show_constraints_true(autodocument):
    kwargs = dict(
        object_path='target.configuration.FieldShowConstraints.field',
        **KWARGS)

    result = [
        '',
        '.. py:pydantic_field:: FieldShowConstraints.field',
        '   :module: target.configuration',
        '   :type: int',
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
        options_app={"autodoc_pydantic_field_show_constraints": True},
        **kwargs)
    assert result == actual

    # explicit local
    actual = autodocument(
        options_doc={"field-show-constraints": True},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_show_constraints": False},
        options_doc={"field-show-constraints": True},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_field_show_constraints_false(autodocument):
    kwargs = dict(
        object_path='target.configuration.FieldShowConstraints.field',
        **KWARGS)
    
    result = [
        '',
        '.. py:pydantic_field:: FieldShowConstraints.field',
        '   :module: target.configuration',
        '   :type: int',
        '',
        '   Field.',
        ''
    ]

    # explict global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_show_constraints": False},
        **kwargs)
    assert result == actual

    # explicit local
    actual = autodocument(
        options_doc={"field-show-constraints": False},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_show_constraints": True},
        options_doc={"field-show-constraints": False},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_field_show_alias_true(autodocument):
    kwargs = dict(
        object_path='target.configuration.FieldShowAlias.field',
        **KWARGS)

    result = [
        '',
        '.. py:pydantic_field:: FieldShowAlias.field',
        '   :module: target.configuration',
        '   :type: int',
        '   :alias: field2',
        '',
        '   Field.',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_show_alias": True},
        **kwargs)
    assert result == actual

    # explicit local
    actual = autodocument(
        options_doc={"field-show-alias": True},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_show_alias": False},
        options_doc={"field-show-alias": True},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_field_show_alias_false(autodocument):
    kwargs = dict(
        object_path='target.configuration.FieldShowAlias.field',
        **KWARGS)

    result = [
        '',
        '.. py:pydantic_field:: FieldShowAlias.field',
        '   :module: target.configuration',
        '   :type: int',
        '',
        '   Field.',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_show_alias": False},
        **kwargs)
    assert result == actual

    # explicit local
    actual = autodocument(
        options_doc={"field-show-alias": False},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_show_alias": True},
        options_doc={"field-show-alias": False},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_field_show_alias_true_directive(parse_rst):
    """Tests pydantic_validator directive.

    """

    default_value = desc_annotation_default_value("1")
    prefix = desc_annotation_directive_prefix("field")

    output_nodes = (
        index,
        [desc, ([desc_signature, ([desc_annotation, prefix],
                                  [desc_addname, "FieldShowAlias."],
                                  [desc_name, "field"],
                                  default_value,
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
        '   :alias: field2',
        ''
    ]

    doctree = parse_rst(input_rst)
    assert_node(doctree, output_nodes)

    # explicit local overwrite explict global
    doctree = parse_rst(input_rst,
                        conf={"autodoc_pydantic_field_show_alias": False})
    assert_node(doctree, output_nodes)

    doctree = parse_rst(input_rst,
                        conf={"autodoc_pydantic_field_show_alias": True})
    assert_node(doctree, output_nodes)


def test_autodoc_pydantic_field_show_alias_false_directive(parse_rst):
    """Tests pydantic_validator directive.

    """

    default_value = desc_annotation_default_value("1")
    prefix = desc_annotation_directive_prefix("field")

    output_nodes = (
        index,
        [desc, ([desc_signature, ([desc_annotation, prefix],
                                  [desc_addname, "FieldShowAlias."],
                                  [desc_name, "field"],
                                  default_value)],
                [desc_content, ()])
         ]
    )

    # explicit local
    input_rst = [
        '',
        '.. py:pydantic_field:: FieldShowAlias.field',
        '   :module: target.configuration',
        '   :value: 1',
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
                        conf={"autodoc_pydantic_field_show_alias": True})
    assert_node(doctree, output_nodes)


def test_autodoc_pydantic_field_show_default_true(autodocument):
    kwargs = dict(
        object_path='target.configuration.FieldShowDefault.field',
        **KWARGS)

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
        options_app={"autodoc_pydantic_field_show_default": True},
        **kwargs)
    assert result == actual

    # explicit local
    actual = autodocument(
        options_doc={"field-show-default": True},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_show_default": False},
        options_doc={"field-show-default": True},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_field_show_default_false(autodocument):
    kwargs = dict(
        object_path='target.configuration.FieldShowDefault.field',
        **KWARGS)

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
        options_app={"autodoc_pydantic_field_show_default": False},
        **kwargs)
    assert result == actual

    # explicit local
    actual = autodocument(
        options_doc={"field-show-default": False},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_show_default": True},
        options_doc={"field-show-default": False},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_field_signature_prefix(autodocument):
    kwargs = dict(
        object_path='target.configuration.FieldSignaturePrefix.field',
        **KWARGS)

    # default
    result = [
        '',
        ".. py:pydantic_field:: FieldSignaturePrefix.field",
        '   :module: target.configuration',
        '   :type: int',
        '',
        '   Field.',
        ''
    ]

    actual = autodocument(**kwargs)
    assert result == actual

    # explicit value
    result = [
        '',
        ".. py:pydantic_field:: FieldSignaturePrefix.field",
        '   :module: target.configuration',
        '   :type: int',
        '   :field-signature-prefix: foobar',
        '',
        '   Field.',
        ''
    ]

    actual = autodocument(
        options_doc={"field-signature-prefix": "foobar"},
        **kwargs)
    assert result == actual

    # explict empty
    result = [
        '',
        ".. py:pydantic_field:: FieldSignaturePrefix.field",
        '   :module: target.configuration',
        '   :type: int',
        '   :field-signature-prefix: ',
        '',
        '   Field.',
        ''
    ]

    actual = autodocument(
        options_doc={"field-signature-prefix": ""},
        **kwargs)
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
    prefix = desc_annotation_directive_prefix("field")
    assert_node(doctree[1][0][0], [desc_annotation, prefix])

    # empty
    doctree = parse_rst(input_rst,
                        conf={"autodoc_pydantic_field_signature_prefix": ""})
    prefix = desc_annotation_directive_prefix("attribute")
    assert_node(doctree[1][0][0], [desc_annotation, prefix])

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
    prefix = desc_annotation_directive_prefix("foobar")
    assert_node(doctree[1][0][0], [desc_annotation, prefix])


@pytest.mark.parametrize("field", ["field1", "field2", "field3"])
def test_autodoc_pydantic_field_show_required_true(field, autodocument):
    result = [
        f'',
        f'.. py:pydantic_field:: FieldShowRequired.{field}',
        '   :module: target.configuration',
        '   :type: int',
        '   :required:',
        f'',
        f'   {field}',
        f'',
    ]

    kwargs = dict(
        object_path=f'target.configuration.FieldShowRequired.{field}',
        **KWARGS
    )

    # explict global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_show_required": True},
        **kwargs)
    assert result == actual

    # explicit local
    actual = autodocument(options_doc={"field-show-required": True}, **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_show_required": False},
        options_doc={"field-show-required": True},
        **kwargs)
    assert result == actual


@pytest.mark.parametrize("field", ["field1", "field2", "field3"])
def test_autodoc_pydantic_field_show_required_false(field, autodocument):
    result = [
        '',
        f'.. py:pydantic_field:: FieldShowRequired.{field}',
        '   :module: target.configuration',
        '   :type: int',
        '',
        f'   {field}',
        '',
    ]

    kwargs = dict(
        object_path=f'target.configuration.FieldShowRequired.{field}',
        **KWARGS
    )

    # explict global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_show_required": False},
        **kwargs)
    assert result == actual

    # explicit local
    actual = autodocument(options_doc={"field-show-required": False}, **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_show_required": True},
        options_doc={"field-show-required": False},
        **kwargs)
    assert result == actual


@pytest.mark.parametrize(["field", "value"],
                         [("field1", "PydanticUndefined"),
                          ("field2", "Ellipsis"),
                          ("field3", "Ellipsis")])
def test_autodoc_pydantic_field_show_required_false_show_default_true(
        field, value, autodocument):
    if pydantic.VERSION < "1.8":
        value = "Ellipsis"

    result = [
        '',
        f'.. py:pydantic_field:: FieldShowRequired.{field}',
        '   :module: target.configuration',
        '   :type: int',
        f'   :value: {value}',
        '',
        f'   {field}',
        '',
    ]

    kwargs = dict(
        object_path=f'target.configuration.FieldShowRequired.{field}',
        **KWARGS
    )

    # explict global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_show_required": False,
                     "autodoc_pydantic_field_show_default": True},
        **kwargs)
    assert result == actual

    # explicit local
    actual = autodocument(options_doc={"field-show-required": False,
                                       "field-show-default": True},
                          **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_show_required": True,
                     "autodoc_pydantic_field_show_default": False},
        options_doc={"field-show-required": False,
                     "field-show-default": True},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_field_show_required_true_directive(parse_rst):
    """Tests pydantic_validator directive.

    """

    prefix = desc_annotation_directive_prefix("field")
    output_nodes = (
        index,
        [desc, ([desc_signature, ([desc_annotation, prefix],
                                  [desc_addname, "FieldShowRequired."],
                                  [desc_name, "field"],
                                  [desc_annotation, " [Required]"],
                                  [desc_annotation, " (alias 'field2')"])],
                [desc_content, ()])
         ]
    )

    # explicit local
    input_rst = [
        '',
        '.. py:pydantic_field:: FieldShowRequired.field',
        '   :module: target.configuration',
        '   :required:',
        '   :alias: field2',
        ''
    ]

    doctree = parse_rst(input_rst)
    assert_node(doctree, output_nodes)

    # explicit local overwrite explict global
    doctree = parse_rst(input_rst,
                        conf={"autodoc_pydantic_field_show_required": False})
    assert_node(doctree, output_nodes)


def test_autodoc_pydantic_field_show_required_false_directive(parse_rst):
    """Tests pydantic_validator directive.

    """

    prefix = desc_annotation_directive_prefix("field")
    output_nodes = (
        index,
        [desc, ([desc_signature, ([desc_annotation, prefix],
                                  [desc_addname, "FieldShowRequired."],
                                  [desc_name, "field"],
                                  [desc_annotation, " (alias 'field2')"])],
                [desc_content, ()])
         ]
    )

    # explicit local
    input_rst = [
        '',
        '.. py:pydantic_field:: FieldShowRequired.field',
        '   :module: target.configuration',
        '   :alias: field2',
        ''
    ]

    doctree = parse_rst(input_rst)
    assert_node(doctree, output_nodes)

    # explicit local overwrite explict global
    doctree = parse_rst(input_rst,
                        conf={"autodoc_pydantic_field_show_required": True})
    assert_node(doctree, output_nodes)
