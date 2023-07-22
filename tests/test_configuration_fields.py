"""This module contains tests for pydantic validator configurations.

"""

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
from .compatibility import desc_annotation_default_value, \
    desc_annotation_directive_prefix, convert_ellipsis_to_none, \
    TYPING_MODULE_PREFIX, OPTIONAL_INT

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
        '',
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
        '',
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
    """Ensure that constraints are properly show via the `Field` type
    annotation.

    """

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
        '      - **ge** = 0',
        '      - **le** = 100',
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


def test_autodoc_pydantic_field_show_constraints_native_int_type(autodocument):
    """Ensure that constraints are properly show via specialized constraint
    types.

    """

    kwargs = dict(
        object_path='target.configuration.FieldShowConstraintsNativeConstraintTypes.field_int',
        **KWARGS)

    result = [
        '',
        '.. py:pydantic_field:: FieldShowConstraintsNativeConstraintTypes.field_int',
        '   :module: target.configuration',
        '   :type: int',
        '',
        '   field_int',
        '',
        '   :Constraints:',
        '      - **strict** = True',
        '      - **ge** = 0',
        '      - **le** = 100',
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


def test_autodoc_pydantic_field_show_constraints_native_str_type(autodocument):
    """Ensure that constraints are properly show via specialized constraint
    types.

    """

    kwargs = dict(
        object_path='target.configuration.FieldShowConstraintsNativeConstraintTypes.field_str',
        **KWARGS)

    result = [
        '',
        '.. py:pydantic_field:: FieldShowConstraintsNativeConstraintTypes.field_str',
        '   :module: target.configuration',
        '   :type: str',
        '',
        '   field_str',
        '',
        '   :Constraints:',
        '      - **strict** = True',
        '      - **min_length** = 5',
        '      - **pattern** = [a-z]+',
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


def test_autodoc_pydantic_field_show_constraints_native_annotated_type(autodocument):
    """Ensure that constraints are properly show via specialized constraint
    types.

    """

    kwargs = dict(
        object_path='target.configuration.FieldShowConstraintsNativeConstraintTypes.field_annotated',
        **KWARGS)

    result = [
        '',
        '.. py:pydantic_field:: FieldShowConstraintsNativeConstraintTypes.field_annotated',
        '   :module: target.configuration',
        '   :type: float',
        '',
        '   field_annotated',
        '',
        '   :Constraints:',
        '      - **strict** = True',
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



def test_autodoc_pydantic_field_show_constraints_ignore_extra_kwargs(
        autodocument):
    """Ensure that additional keyword arguments passed to pydantic `Field` are
    not listed under the field's constraint documentation section.

    This relates to #110.

    """

    kwargs = dict(
        object_path='target.configuration.FieldShowConstraintsIgnoreExtraKwargs.field',
        **KWARGS)

    result = [
        '',
        '.. py:pydantic_field:: FieldShowConstraintsIgnoreExtraKwargs.field',
        '   :module: target.configuration',
        '   :type: int',
        '',
        '   Field.',
        '',
        '   :Constraints:',
        '      - **ge** = 0',
        '      - **le** = 100',
        ''
    ]

    actual = autodocument(
        options_app={"autodoc_pydantic_field_show_constraints": True},
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
        '   :field-show-alias: True',
        '',
        '   Field.',
        '',
    ]

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
    result = [
        '',
        '.. py:pydantic_field:: FieldShowAlias.field',
        '   :module: target.configuration',
        '   :type: int',
        '   :field-show-alias: False',
        '',
        '   Field.',
        '',
    ]

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


def test_autodoc_pydantic_field_show_alias_true_directive_local(parse_rst):
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
        '   :field-show-alias:',
        '   :alias: field2',
        ''
    ]

    doctree = parse_rst(input_rst)
    assert_node(doctree, output_nodes)

    # explicit local overwrite explict global
    doctree = parse_rst(input_rst,
                        conf={"autodoc_pydantic_field_show_alias": False})
    assert_node(doctree, output_nodes)


def test_autodoc_pydantic_field_show_alias_true_directive_global(parse_rst):
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

    # explicit local overwrite explict global
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
        '   :alias: foobar',
        '   :field-show-alias: False',
        ''
    ]

    doctree = parse_rst(input_rst)
    assert_node(doctree, output_nodes)

    # explicit local overwrite explict global
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


@pytest.mark.parametrize("expected",
                         [("field1", OPTIONAL_INT),
                          ("field2", OPTIONAL_INT),
                          ("field3", "int"),
                          ("field4", "int")])
def test_autodoc_pydantic_field_show_required_true_not(expected, autodocument):
    """Ensure that fields are not incorrectly tagged as required.

    This relates to #97.

    """

    field, field_type = expected

    result = [
        f'',
        f'.. py:pydantic_field:: FieldShowRequiredNot.{field}',
        '   :module: target.configuration',
        f'   :type: {field_type}',
        f'',
        f'   {field}',
        f'',
    ]

    kwargs = dict(
        object_path=f'target.configuration.FieldShowRequiredNot.{field}',
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


@pytest.mark.parametrize("field_values", (("field1", "int"),
                                          ("field2", "int"),
                                          ("field3", "int"),
                                          ("field4", OPTIONAL_INT)))
def test_autodoc_pydantic_field_show_required_false(field_values,
                                                    autodocument):
    """Ensure that the required marker is not shown if deactivated.

    """
    field_name, type_value = field_values
    result = [
        '',
        f'.. py:pydantic_field:: FieldShowRequired.{field_name}',
        '   :module: target.configuration',
        f'   :type: {type_value}',
        '',
        f'   {field_name}',
        '',
    ]

    kwargs = dict(
        object_path=f'target.configuration.FieldShowRequired.{field_name}',
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


@pytest.mark.parametrize("field_values", (("field1", "int"),
                                          ("field2", "int"),
                                          ("field3", "int"),
                                          ("field4", OPTIONAL_INT)))
def test_autodoc_pydantic_field_show_required_false_show_default_true(
        field_values, autodocument):
    """Ensure that the required marker is not shown while the default value
    is present.

    """

    field_name, type_value = field_values

    result = [
        '',
        f'.. py:pydantic_field:: FieldShowRequired.{field_name}',
        '   :module: target.configuration',
        f'   :type: {type_value}',
        f'   :value: PydanticUndefined',
        '',
        f'   {field_name}',
        '',
    ]

    kwargs = dict(
        object_path=f'target.configuration.FieldShowRequired.{field_name}',
        **KWARGS
    )

    # explict global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_show_required": False,
                     "autodoc_pydantic_field_show_default": True},
        **kwargs)
    assert result == convert_ellipsis_to_none(actual)

    # explicit local
    actual = autodocument(options_doc={"field-show-required": False,
                                       "field-show-default": True},
                          **kwargs)
    assert result == convert_ellipsis_to_none(actual)

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_show_required": True,
                     "autodoc_pydantic_field_show_default": False},
        options_doc={"field-show-required": False,
                     "field-show-default": True},
        **kwargs)
    assert result == convert_ellipsis_to_none(actual)


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
        '   :field-show-alias:',
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
        '   :field-show-alias:',
        '   :alias: field2',
        ''
    ]

    doctree = parse_rst(input_rst)
    assert_node(doctree, output_nodes)

    # explicit local overwrite explict global
    doctree = parse_rst(input_rst,
                        conf={"autodoc_pydantic_field_show_required": True})
    assert_node(doctree, output_nodes)


@pytest.mark.parametrize(["field", "typ"],
                         [("field1", OPTIONAL_INT),
                          ("field2", OPTIONAL_INT),
                          ("field3", "int"),
                          ("field4", "int")])
def test_autodoc_pydantic_field_show_optional_true_not(
        field, typ, autodocument):
    """Ensure that fields are not incorrectly tagged as optional.

    """

    result = [
        f'',
        f'.. py:pydantic_field:: FieldShowOptionalNot.{field}',
        '   :module: target.configuration',
        f'   :type: {typ}',
        f'',
        f'   {field}',
        f'',
    ]

    kwargs = dict(
        object_path=f'target.configuration.FieldShowOptionalNot.{field}',
        **KWARGS
    )

    # explict global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_show_optional": True},
        **kwargs)
    assert result == actual

    # explicit local
    actual = autodocument(options_doc={"field-show-optional": True}, **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_show_optional": False},
        options_doc={"field-show-optional": True},
        **kwargs)
    assert result == actual


@pytest.mark.parametrize(["field", "typ"],
                         [("field1", "int"),
                          ("field2", OPTIONAL_INT)])
def test_autodoc_pydantic_field_show_optional_true(field, typ, autodocument):
    kwargs = dict(
        object_path=f'target.configuration.FieldShowOptional.{field}',
        **KWARGS)

    result = [
        '',
        f'.. py:pydantic_field:: FieldShowOptional.{field}',
        '   :module: target.configuration',
        f'   :type: {typ}',
        '   :optional:',
        '',
        f'   {field}',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_show_optional": True},
        **kwargs)
    assert result == actual

    # explicit local
    actual = autodocument(
        options_doc={"field-show-optional": True},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_show_optional": False},
        options_doc={"field-show-optional": True},
        **kwargs)
    assert result == actual


@pytest.mark.parametrize(["field", "typ"],
                         [("field1", "int"),
                          ("field2", OPTIONAL_INT)])
def test_autodoc_pydantic_field_show_optional_false(field, typ, autodocument):
    kwargs = dict(
        object_path=f'target.configuration.FieldShowOptional.{field}',
        **KWARGS)

    result = [
        '',
        f'.. py:pydantic_field:: FieldShowOptional.{field}',
        '   :module: target.configuration',
        f'   :type: {typ}',
        '',
        f'   {field}',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_show_optional": False},
        **kwargs)
    assert result == actual

    # explicit local
    actual = autodocument(
        options_doc={"field-show-optional": False},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_show_optional": True},
        options_doc={"field-show-optional": False},
        **kwargs)
    assert result == actual


@pytest.mark.parametrize("field", ["field1", "field2"])
def test_autodoc_pydantic_field_show_optional_true_directive(field, parse_rst):
    prefix = desc_annotation_directive_prefix("field")
    output_nodes = (
        index,
        [desc, ([desc_signature, ([desc_annotation, prefix],
                                  [desc_addname, "FieldShowOptional."],
                                  [desc_name, field],
                                  [desc_annotation, " [Optional]"])],
                [desc_content, ()])
         ]
    )

    # explicit local
    input_rst = [
        '',
        f'.. py:pydantic_field:: FieldShowOptional.{field}',
        '   :module: target.configuration',
        '   :optional:',
        ''
    ]

    doctree = parse_rst(input_rst)
    assert_node(doctree, output_nodes)

    # explicit local overwrite explict global
    doctree = parse_rst(input_rst,
                        conf={"autodoc_pydantic_field_show_optional": False})
    assert_node(doctree, output_nodes)


def test_autodoc_pydantic_field_swap_name_and_alias_with_alias(autodocument):
    kwargs = dict(
        object_path=f'target.configuration.FieldSwapNameAndAlias.field1',
        **KWARGS)

    result = [
        '',
        '.. py:pydantic_field:: FieldSwapNameAndAlias.field1',
        '   :module: target.configuration',
        '   :type: int',
        '   :alias: field 1 alias',
        '   :field-show-alias: True',
        '   :field-swap-name-and-alias: True',
        '',
        '   Field1',
        '',
    ]

    # explicit local
    actual = autodocument(
        options_doc={"field-swap-name-and-alias": True,
                     "field-show-alias": True},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_swap_name_and_alias": False,
                     "autodoc_pydantic_field_show_alias": False},
        options_doc={"field-swap-name-and-alias": True,
                     "field-show-alias": True},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_field_swap_name_and_alias_with_alias_directive_local(
        parse_rst):
    prefix = desc_annotation_directive_prefix("field")
    output_nodes = (
        index,
        [desc, ([desc_signature, ([desc_annotation, prefix],
                                  [desc_addname, "FieldSwapNameAndAlias."],
                                  [desc_name, "field 1 alias"],
                                  [desc_annotation, " (name 'field1')"])],
                [desc_content, ()])
         ]
    )

    # explicit local
    input_rst = [
        '',
        '.. py:pydantic_field:: FieldSwapNameAndAlias.field1',
        '   :module: target.configuration',
        '   :field-swap-name-and-alias:',
        '   :field-show-alias:',
        '   :alias: field 1 alias',
        ''
    ]

    doctree = parse_rst(input_rst)
    assert_node(doctree, output_nodes)

    # explicit local overwrite explict global
    doctree = parse_rst(
        input_rst,
        conf={"autodoc_pydantic_field_swap_name_and_alias": False})
    assert_node(doctree, output_nodes)


def test_autodoc_pydantic_field_swap_name_and_alias_with_alias_directive_global(
        parse_rst):
    prefix = desc_annotation_directive_prefix("field")
    output_nodes = (
        index,
        [desc, ([desc_signature, ([desc_annotation, prefix],
                                  [desc_addname, "FieldSwapNameAndAlias."],
                                  [desc_name, "field 1 alias"],
                                  [desc_annotation, " (name 'field1')"])],
                [desc_content, ()])
         ]
    )

    # explicit local
    input_rst = [
        '',
        '.. py:pydantic_field:: FieldSwapNameAndAlias.field1',
        '   :module: target.configuration',
        '   :alias: field 1 alias',
        ''
    ]

    # explicit local overwrite explict global
    doctree = parse_rst(
        input_rst,
        conf={"autodoc_pydantic_field_swap_name_and_alias": True,
              "autodoc_pydantic_field_show_alias": True})
    assert_node(doctree, output_nodes)


def test_autodoc_pydantic_field_swap_name_and_alias_true(autodocument):
    kwargs = dict(
        object_path=f'target.configuration.FieldSwapNameAndAlias.field1',
        **KWARGS)

    result = [
        '',
        '.. py:pydantic_field:: FieldSwapNameAndAlias.field1',
        '   :module: target.configuration',
        '   :type: int',
        '   :alias: field 1 alias',
        '   :field-swap-name-and-alias: True',
        '',
        '   Field1',
        '',
    ]

    # explicit local
    actual = autodocument(
        options_doc={"field-swap-name-and-alias": True},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_swap_name_and_alias": False},
        options_doc={"field-swap-name-and-alias": True},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_field_swap_name_and_alias_false(autodocument):
    kwargs = dict(
        object_path=f'target.configuration.FieldSwapNameAndAlias.field1',
        **KWARGS)

    result = [
        '',
        '.. py:pydantic_field:: FieldSwapNameAndAlias.field1',
        '   :module: target.configuration',
        '   :type: int',
        '   :field-swap-name-and-alias: False',
        '',
        '   Field1',
        '',
    ]

    # explicit local
    actual = autodocument(
        options_doc={"field-swap-name-and-alias": False},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_field_swap_name_and_alias": True},
        options_doc={"field-swap-name-and-alias": False},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_field_swap_name_and_alias_true_directive_local(
        parse_rst):
    prefix = desc_annotation_directive_prefix("field")
    output_nodes = (
        index,
        [desc, ([desc_signature, ([desc_annotation, prefix],
                                  [desc_addname, "FieldSwapNameAndAlias."],
                                  [desc_name, "field 1 alias"])],
                [desc_content, ()])
         ]
    )

    # explicit local
    input_rst = [
        '',
        '.. py:pydantic_field:: FieldSwapNameAndAlias.field1',
        '   :module: target.configuration',
        '   :field-swap-name-and-alias:',
        '   :field-show-alias: False',
        '   :alias: field 1 alias',
        ''
    ]

    doctree = parse_rst(input_rst)
    assert_node(doctree, output_nodes)

    # explicit local overwrite explict global
    doctree = parse_rst(
        input_rst,
        conf={"autodoc_pydantic_field_swap_name_and_alias": False})
    assert_node(doctree, output_nodes)


def test_autodoc_pydantic_field_swap_name_and_alias_false_directive_local(
        parse_rst):
    prefix = desc_annotation_directive_prefix("field")
    output_nodes = (
        index,
        [desc, ([desc_signature, ([desc_annotation, prefix],
                                  [desc_addname, "FieldSwapNameAndAlias."],
                                  [desc_name, "field1"])],
                [desc_content, ()])
         ]
    )

    # explicit local
    input_rst = [
        '',
        '.. py:pydantic_field:: FieldSwapNameAndAlias.field1',
        '   :module: target.configuration',
        '   :field-swap-name-and-alias: False',
        '   :field-show-alias: False',
        '   :alias: field 1 alias',
        ''
    ]

    doctree = parse_rst(input_rst)
    assert_node(doctree, output_nodes)

    # explicit local overwrite explict global
    doctree = parse_rst(
        input_rst,
        conf={"autodoc_pydantic_field_swap_name_and_alias": True})
    assert_node(doctree, output_nodes)


def test_autodoc_pydantic_field_swap_name_and_alias_true_directive_global(
        parse_rst):
    prefix = desc_annotation_directive_prefix("field")
    output_nodes = (
        index,
        [desc, ([desc_signature, ([desc_annotation, prefix],
                                  [desc_addname, "FieldSwapNameAndAlias."],
                                  [desc_name, "field 1 alias"])],
                [desc_content, ()])
         ]
    )

    # explicit local
    input_rst = [
        '',
        '.. py:pydantic_field:: FieldSwapNameAndAlias.field1',
        '   :module: target.configuration',
        '   :alias: field 1 alias',
        ''
    ]

    doctree = parse_rst(
        input_rst,
        conf={"autodoc_pydantic_field_swap_name_and_alias": True,
              "autodoc_pydantic_field_show_alias": False})
    assert_node(doctree, output_nodes)
