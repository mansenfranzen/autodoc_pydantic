"""This module contains tests for pydantic specific directives."""

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
    strong,
)
from sphinx.addnodes import (
    desc,
    desc_signature,
    desc_name,
    desc_content,
    desc_annotation,
    desc_addname,
    pending_xref,
    index,
)
from sphinx.testing.util import assert_node

from .compatibility import (
    desc_annotation_type_annotation,
    desc_annotation_default_value,
    desc_annotation_directive_prefix,
)


def test_example_model_with_field(parse_rst):
    """Tests plain minimal pydantic model with doc string. Ensure that
    annotation is correct.

    """

    input_rst = [
        '.. py:pydantic_model:: ModelWithField',
        '   :module: target.model',
        '',
        '   Model With Field.',
        '',
        '',
        '   .. py:pydantic_field:: ModelWithField.field',
        '      :module: target.model',
        '      :type: int',
        '      :value: 1',
        '',
        '      Doc field',
        '',
    ]

    type_annotation = desc_annotation_type_annotation('int')
    default_value = desc_annotation_default_value('1')
    prefix_field = desc_annotation_directive_prefix('field')
    field_node = [
        desc,
        (
            [
                desc_signature,
                (
                    [desc_annotation, prefix_field],
                    [desc_name, 'field'],
                    [desc_annotation, type_annotation],
                    default_value,
                ),
            ],
            [desc_content, ([paragraph, 'Doc field'])],
        ),
    ]

    prefix_model = desc_annotation_directive_prefix('pydantic model')
    output_nodes = (
        index,
        [
            desc,
            (
                [
                    desc_signature,
                    (
                        [desc_annotation, prefix_model],
                        [desc_addname, 'target.model.'],
                        [desc_name, 'ModelWithField'],
                    ),
                ],
                [desc_content, ([paragraph, 'Model With Field.'], index, field_node)],
            ),
        ],
    )

    doctree = parse_rst(input_rst)
    assert_node(doctree, output_nodes)


def test_example_model_with_field_and_validator(parse_rst):
    """Tests more complex pydantic model with validators and fields including
    corresponding referencing.

    """

    input_rst = [
        '',
        '.. py:pydantic_model:: ModelWithFieldValidator',
        '   :module: target.examples',
        '',
        '   Model With Field Validator.',
        '',
        '   :Validators:',
        '      - :py:obj:`is_integer <target.examples.ModelWithFieldValidator.is_integer>` » :py:obj:`field <target.examples.ModelWithFieldValidator.field>`',
        '',
        '   .. py:pydantic_field:: ModelWithFieldValidator.field',
        '      :module: target.examples',
        '      :type: int',
        '      :value: 1',
        '',
        '      Doc field',
        '',
        '      :Validated by:',
        '         - :py:obj:`is_integer <target.examples.ModelWithFieldValidator.is_integer>`',
        '',
        '   .. py:pydantic_validator:: ModelWithFieldValidator.is_integer',
        '      :module: target.examples',
        '      :classmethod:',
        '',
        '      Doc validator.',
        '',
        '      :Validates:',
        '         - :py:obj:`field <target.examples.ModelWithFieldValidator.field>`',
        '',
    ]

    field_validated_node = [
        field_list,
        (
            [
                field,
                (
                    [field_name, 'Validated by'],
                    [
                        field_body,
                        (
                            [
                                bullet_list,
                                (
                                    [
                                        list_item,
                                        (
                                            [
                                                paragraph,
                                                (
                                                    [
                                                        pending_xref,
                                                        ([literal, 'is_integer']),
                                                    ]
                                                ),
                                            ]
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    ],
                ),
            ]
        ),
    ]

    type_annotation = desc_annotation_type_annotation('int')
    default_value = desc_annotation_default_value('1')
    prefix_field = desc_annotation_directive_prefix('field')
    field_node = [
        desc,
        (
            [
                desc_signature,
                (
                    [desc_annotation, prefix_field],
                    [desc_name, 'field'],
                    [desc_annotation, type_annotation],
                    default_value,
                ),
            ],
            [desc_content, ([paragraph, 'Doc field'], field_validated_node)],
        ),
    ]

    validator_validates_node = [
        field_list,
        (
            [
                field,
                (
                    [field_name, 'Validates'],
                    [
                        field_body,
                        (
                            [
                                bullet_list,
                                (
                                    [
                                        list_item,
                                        (
                                            [
                                                paragraph,
                                                ([pending_xref, ([literal, 'field'])]),
                                            ]
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    ],
                ),
            ]
        ),
    ]

    prefix_validator = desc_annotation_directive_prefix('validator')
    validator_node = [
        desc,
        (
            [
                desc_signature,
                (
                    [desc_annotation, prefix_validator],
                    [desc_name, 'is_integer'],
                    [desc_annotation, '  »  '],
                    [pending_xref, ([emphasis, 'field'])],
                ),
            ],
            [desc_content, ([paragraph, 'Doc validator.'], validator_validates_node)],
        ),
    ]

    model_validator_node = [
        field_list,
        (
            [
                field,
                (
                    [field_name, 'Validators'],
                    [
                        field_body,
                        (
                            [
                                bullet_list,
                                (
                                    [
                                        list_item,
                                        (
                                            [
                                                paragraph,
                                                (
                                                    [
                                                        pending_xref,
                                                        ([literal, 'is_integer']),
                                                    ],
                                                    ' » ',
                                                    [
                                                        pending_xref,
                                                        ([literal, 'field']),
                                                    ],
                                                ),
                                            ]
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    ],
                ),
            ]
        ),
    ]

    prefix_model = desc_annotation_directive_prefix('pydantic model')
    output_nodes = (
        index,
        [
            desc,
            (
                [
                    desc_signature,
                    (
                        [desc_annotation, prefix_model],
                        [desc_addname, 'target.examples.'],
                        [desc_name, 'ModelWithFieldValidator'],
                    ),
                ],
                [
                    desc_content,
                    (
                        [paragraph, 'Model With Field Validator.'],
                        model_validator_node,
                        index,
                        field_node,
                        index,
                        validator_node,
                    ),
                ],
            ),
        ],
    )

    doctree = parse_rst(input_rst)
    assert_node(doctree, output_nodes)


def test_pydantic_model(parse_rst):
    """Tests pydantic_model directive."""

    input_rst = [
        '.. py:pydantic_model:: PlainModel',
        '   :module: target.examples',
        '',
        '   Model Plain.',
        '',
    ]

    prefix_model = desc_annotation_directive_prefix('pydantic model')
    output_nodes = (
        index,
        [
            desc,
            (
                [
                    desc_signature,
                    (
                        [desc_annotation, prefix_model],
                        [desc_addname, 'target.examples.'],
                        [desc_name, 'PlainModel'],
                    ),
                ],
                [desc_content, ([paragraph, 'Model Plain.'])],
            ),
        ],
    )

    doctree = parse_rst(input_rst)
    assert_node(doctree, output_nodes)


def test_pydantic_settings(parse_rst):
    """Tests pydantic_settings directive."""

    input_rst = [
        '.. py:pydantic_settings:: PlainSettings',
        '   :module: target.examples',
        '',
        '   Settings Plain.',
        '',
    ]

    prefix_settings = desc_annotation_directive_prefix('pydantic settings')
    output_nodes = (
        index,
        [
            desc,
            (
                [
                    desc_signature,
                    (
                        [desc_annotation, prefix_settings],
                        [desc_addname, 'target.examples.'],
                        [desc_name, 'PlainSettings'],
                    ),
                ],
                [desc_content, ([paragraph, 'Settings Plain.'])],
            ),
        ],
    )

    doctree = parse_rst(input_rst)
    assert_node(doctree, output_nodes)


def test_pydantic_validator(parse_rst):
    """Tests pydantic_validator directive."""

    input_rst = [
        '.. py:pydantic_validator:: ModelWithFieldValidator.is_integer',
        '   :module: target.examples',
        '',
        '   Validator Plain.',
        '',
    ]

    prefix_validator = desc_annotation_directive_prefix('validator')
    output_nodes = (
        index,
        [
            desc,
            (
                [
                    desc_signature,
                    (
                        [desc_annotation, prefix_validator],
                        [desc_addname, 'ModelWithFieldValidator.'],
                        [desc_name, 'is_integer'],
                        [desc_annotation, '  »  '],
                        [pending_xref, ([emphasis, 'field'])],
                    ),
                ],
                [desc_content, ([paragraph, 'Validator Plain.'])],
            ),
        ],
    )

    doctree = parse_rst(input_rst)
    assert_node(doctree, output_nodes)


def test_pydantic_field_with_default_value(parse_rst):
    """Tests pydantic_field directive."""

    input_rst = [
        '.. py:pydantic_field:: ModelWithAlias.field',
        '   :module: target.examples',
        '   :value: 5',
        '   :type: int',
        '   :alias: aliased',
        '',
        '   Alias Plain.',
        '',
    ]

    type_annotation = desc_annotation_type_annotation('int')
    default_value = desc_annotation_default_value('5')
    prefix_field = desc_annotation_directive_prefix('field')
    output_nodes = (
        index,
        [
            desc,
            (
                [
                    desc_signature,
                    (
                        [desc_annotation, prefix_field],
                        [desc_addname, 'ModelWithAlias.'],
                        [desc_name, 'field'],
                        [desc_annotation, type_annotation],
                        default_value,
                        [desc_annotation, " (alias 'aliased')"],
                    ),
                ],
                [desc_content, ([paragraph, 'Alias Plain.'])],
            ),
        ],
    )

    doctree = parse_rst(input_rst)
    assert_node(doctree, output_nodes)


def test_pydantic_field_with_required(parse_rst):
    """Tests pydantic_field directive."""

    input_rst = [
        '.. py:pydantic_field:: ModelWithAlias.field',
        '   :module: target.examples',
        '   :type: int',
        '   :required:',
        '   :alias: Alias',
        '',
        '   Required.',
        '',
    ]

    type_annotation = desc_annotation_type_annotation('int')
    prefix_field = desc_annotation_directive_prefix('field')
    output_nodes = (
        index,
        [
            desc,
            (
                [
                    desc_signature,
                    (
                        [desc_annotation, prefix_field],
                        [desc_addname, 'ModelWithAlias.'],
                        [desc_name, 'field'],
                        [desc_annotation, type_annotation],
                        [desc_annotation, ' [Required]'],
                        [desc_annotation, " (alias 'Alias')"],
                    ),
                ],
                [desc_content, ([paragraph, 'Required.'])],
            ),
        ],
    )

    doctree = parse_rst(input_rst)
    assert_node(doctree, output_nodes)
