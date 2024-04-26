"""This module contains tests for pydantic model configurations."""

import pytest
from sphinx.addnodes import desc_annotation, desc_addname
from sphinx.testing.util import assert_node

from sphinxcontrib.autodoc_pydantic.directives.autodocumenters import (
    PydanticModelDocumenter,
)

from .compatibility import desc_annotation_directive_prefix

KWARGS = dict(documenter=PydanticModelDocumenter.objtype, deactivate_all=True)

SETTING_MEMBER_ORDER = {
    'autodoc_pydantic_model_members': True,
    'autodoc_pydantic_model_show_validator_members': True,
}


def test_autodoc_pydantic_model_show_json_true(autodocument):
    kwargs = dict(object_path='target.configuration.ModelShowJson', **KWARGS)

    result = [
        '',
        '.. py:pydantic_model:: ModelShowJson',
        '   :module: target.configuration',
        '',
        '   ModelShowJson.',
        '',
        '',
        '   .. raw:: html',
        '',
        '      <p><details  class="autodoc_pydantic_collapsable_json">',
        '      <summary>Show JSON schema</summary>',
        '',
        '   .. code-block:: json',
        '',
        '      {',
        '         "title": "ModelShowJson",',
        '         "description": "ModelShowJson.",',
        '         "type": "object",',
        '         "properties": {}',
        '      }',
        '',
        '   .. raw:: html',
        '',
        '      </details></p>',
        '',
        '',
    ]

    # explicit global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_show_json': True}, **kwargs
    )
    assert actual == result

    # explicit local
    actual = autodocument(options_doc={'model-show-json': True}, **kwargs)
    assert actual == result

    # explicit local overwrite global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_show_json': False},
        options_doc={'model-show-json': True},
        **kwargs,
    )
    assert actual == result


def test_autodoc_pydantic_model_show_json_false(autodocument):
    kwargs = dict(object_path='target.configuration.ModelShowJson', **KWARGS)

    result = [
        '',
        '.. py:pydantic_model:: ModelShowJson',
        '   :module: target.configuration',
        '',
        '   ModelShowJson.',
        '',
    ]

    # explicit global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_show_json': False}, **kwargs
    )
    assert actual == result

    # explicit local
    actual = autodocument(options_doc={'model-show-json': False}, **kwargs)
    assert actual == result

    # explicit local overwrite global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_show_json': True},
        options_doc={'model-show-json': False},
        **kwargs,
    )
    assert actual == result


def test_autodoc_pydantic_model_erdantic_figure_true(autodocument):
    pytest.importorskip('erdantic', minversion='1.0', reason='erdantic missing')

    kwargs = dict(object_path='target.configuration.ModelErdanticFigure', **KWARGS)

    result = [
        '',
        '.. py:pydantic_model:: ModelErdanticFigure',
        '   :module: target.configuration',
        '',
        '   ModelErdanticFigure.',
        '',
        '',
        '   .. raw:: html',
        '',
        '      <p><details  class="autodoc_pydantic_collapsable_erd">',
        '      <summary>Show Entity Relationship Diagram</summary>',
        '',
        '   .. graphviz::',
        '',
        '      digraph "Entity Relationship Diagram created by erdantic" {',
        '         graph [fontcolor=gray66,',
        '            fontname="Times New Roman,Times,Liberation Serif,serif",',
        '            fontsize=9,',
        '            nodesep=0.5,',
        '            rankdir=LR,',
        '            ranksep=1.5',
        '         ];',
        '         node [fontname="Times New Roman,Times,Liberation Serif,serif",',
        '            fontsize=14,',
        '            label="\\N",',
        '            shape=plain',
        '         ];',
        '         edge [dir=both];',
        '         "target.configuration.ModelErdanticFigure"   [label=<<table border="0" cellborder="1" cellspacing="0"><tr><td port="_root" colspan="2"><b>ModelErdanticFigure</b></td></tr><tr><td>field1</td><td port="field1">int</td></tr><tr><td>field2</td><td port="field2">str</td></tr><tr><td>related</td><td port="related">ModelErdanticFigureRelated</td></tr></table>>,',
        '            tooltip="target.configuration.ModelErdanticFigure&#xA;&#xA;ModelErdanticFigure.&#xA;"];',
        '         "target.configuration.ModelErdanticFigureRelated"   [label=<<table border="0" cellborder="1" cellspacing="0"><tr><td port="_root" colspan="2"><b>ModelErdanticFigureRelated</b></td></tr><tr><td>field1</td><td port="field1">int</td></tr><tr><td>field2</td><td port="field2">str</td></tr></table>>,',
        '            tooltip="target.configuration.ModelErdanticFigureRelated&#xA;&#xA;ModelErdanticFigureRelated.&#xA;"];',
        '         "target.configuration.ModelErdanticFigure":related:e -> "target.configuration.ModelErdanticFigureRelated":_root:w   [arrowhead=noneteetee,',
        '            arrowtail=nonenone];',
        '      }',
        '',
        '',
        '',
        '   .. raw:: html',
        '',
        '      </details></p>',
        '',
        '',
    ]
    # explicit global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_erdantic_figure': True}, **kwargs
    )
    assert actual == result

    # explicit local
    actual = autodocument(options_doc={'model-erdantic-figure': True}, **kwargs)
    assert actual == result

    # explicit local overwrite global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_erdantic_figure': False},
        options_doc={'model-erdantic-figure': True},
        **kwargs,
    )
    assert actual == result


def test_autodoc_pydantic_model_erdantic_figure_collapsed_false(autodocument):
    pytest.importorskip('erdantic', minversion='1.0', reason='erdantic missing')

    kwargs = dict(object_path='target.configuration.ModelErdanticFigure', **KWARGS)

    result = [
        '',
        '.. py:pydantic_model:: ModelErdanticFigure',
        '   :module: target.configuration',
        '',
        '   ModelErdanticFigure.',
        '',
        '   .. graphviz::',
        '',
        '      digraph "Entity Relationship Diagram created by erdantic" {',
        '         graph [fontcolor=gray66,',
        '            fontname="Times New Roman,Times,Liberation Serif,serif",',
        '            fontsize=9,',
        '            nodesep=0.5,',
        '            rankdir=LR,',
        '            ranksep=1.5',
        '         ];',
        '         node [fontname="Times New Roman,Times,Liberation Serif,serif",',
        '            fontsize=14,',
        '            label="\\N",',
        '            shape=plain',
        '         ];',
        '         edge [dir=both];',
        '         "target.configuration.ModelErdanticFigure"   [label=<<table border="0" cellborder="1" cellspacing="0"><tr><td port="_root" colspan="2"><b>ModelErdanticFigure</b></td></tr><tr><td>field1</td><td port="field1">int</td></tr><tr><td>field2</td><td port="field2">str</td></tr><tr><td>related</td><td port="related">ModelErdanticFigureRelated</td></tr></table>>,',
        '            tooltip="target.configuration.ModelErdanticFigure&#xA;&#xA;ModelErdanticFigure.&#xA;"];',
        '         "target.configuration.ModelErdanticFigureRelated"   [label=<<table border="0" cellborder="1" cellspacing="0"><tr><td port="_root" colspan="2"><b>ModelErdanticFigureRelated</b></td></tr><tr><td>field1</td><td port="field1">int</td></tr><tr><td>field2</td><td port="field2">str</td></tr></table>>,',
        '            tooltip="target.configuration.ModelErdanticFigureRelated&#xA;&#xA;ModelErdanticFigureRelated.&#xA;"];',
        '         "target.configuration.ModelErdanticFigure":related:e -> "target.configuration.ModelErdanticFigureRelated":_root:w   [arrowhead=noneteetee,',
        '            arrowtail=nonenone];',
        '      }',
        '',
        '',
    ]

    # explicit global
    actual = autodocument(
        options_app={
            'autodoc_pydantic_model_erdantic_figure': True,
            'autodoc_pydantic_model_erdantic_figure_collapsed': False,
        },
        **kwargs,
    )
    assert actual == result

    # explicit local
    actual = autodocument(
        options_doc={
            'model-erdantic-figure': True,
            'model-erdantic-figure-collapsed': False,
        },
        **kwargs,
    )
    assert actual == result

    # explicit local overwrite global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_erdantic_figure_collapsed': True},
        options_doc={
            'model-erdantic-figure': True,
            'model-erdantic-figure-collapsed': False,
        },
        **kwargs,
    )
    assert actual == result


def test_autodoc_pydantic_model_erdantic_figure_false(autodocument):
    pytest.importorskip('erdantic', minversion='1.0', reason='erdantic missing')

    kwargs = dict(object_path='target.configuration.ModelErdanticFigure', **KWARGS)

    result = [
        '',
        '.. py:pydantic_model:: ModelErdanticFigure',
        '   :module: target.configuration',
        '',
        '   ModelErdanticFigure.',
        '',
    ]

    # explicit global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_show_json': False}, **kwargs
    )
    assert actual == result

    # explicit local
    actual = autodocument(options_doc={'model-show-json': False}, **kwargs)
    assert actual == result

    # explicit local overwrite global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_show_json': True},
        options_doc={'model-show-json': False},
        **kwargs,
    )
    assert actual == result


def test_autodoc_pydantic_model_show_config_summary_summary_true(autodocument):
    kwargs = dict(object_path='target.configuration.ModelShowConfigSummary', **KWARGS)

    result = [
        '',
        '.. py:pydantic_model:: ModelShowConfigSummary',
        '   :module: target.configuration',
        '',
        '   ModelShowConfigSummary.',
        '',
        '   :Config:',
        '      - **frozen**: *bool = True*',
        '      - **title**: *str = FooBar*',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_show_config_summary': True}, **kwargs
    )
    assert actual == result

    # explict local
    actual = autodocument(options_doc={'model-show-config-summary': True}, **kwargs)
    assert actual == result

    # explicit local overwrite global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_show_config_summary': False},
        options_doc={'model-show-config-summary': True},
        **kwargs,
    )
    assert actual == result


def test_autodoc_pydantic_model_show_config_summary_false(autodocument):
    kwargs = dict(object_path='target.configuration.ModelShowConfigSummary', **KWARGS)

    result = [
        '',
        '.. py:pydantic_model:: ModelShowConfigSummary',
        '   :module: target.configuration',
        '',
        '   ModelShowConfigSummary.',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_show_config_summary': False}, **kwargs
    )
    assert actual == result

    # explict local
    actual = autodocument(options_doc={'model-show-config-summary': False}, **kwargs)
    assert actual == result

    # explicit local overwrite global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_show_config_summary': True},
        options_doc={'model-show-config-summary': False},
        **kwargs,
    )
    assert actual == result


def test_autodoc_pydantic_model_show_validator_summary_true(autodocument):
    kwargs = dict(
        object_path='target.configuration.ModelShowValidatorsSummary', **KWARGS
    )

    result = [
        '',
        '.. py:pydantic_model:: ModelShowValidatorsSummary',
        '   :module: target.configuration',
        '',
        '   ModelShowValidatorsSummary.',
        '',
        '   :Validators:',
        '      - :py:obj:`check <target.configuration.ModelShowValidatorsSummary.check>` » :py:obj:`field <target.configuration.ModelShowValidatorsSummary.field>`',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_show_validator_summary': True}, **kwargs
    )
    assert result == actual

    # explict local
    actual = autodocument(options_doc={'model-show-validator-summary': True}, **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_show_validators_summary': False},
        options_doc={'model-show-validator-summary': True},
        **kwargs,
    )
    assert result == actual


def test_autodoc_pydantic_model_show_validator_summary_multiple_true(autodocument):
    kwargs = dict(
        object_path='target.configuration.ModelShowValidatorsSummaryMultipleFields',
        **KWARGS,
    )

    result = [
        '',
        '.. py:pydantic_model:: ModelShowValidatorsSummaryMultipleFields',
        '   :module: target.configuration',
        '',
        '   ModelShowValidatorsSummaryMultipleFields.',
        '',
        '   :Validators:',
        '      - :py:obj:`check <target.configuration.ModelShowValidatorsSummaryMultipleFields.check>` » :py:obj:`field1 <target.configuration.ModelShowValidatorsSummaryMultipleFields.field1>`',
        '      - :py:obj:`check <target.configuration.ModelShowValidatorsSummaryMultipleFields.check>` » :py:obj:`field2 <target.configuration.ModelShowValidatorsSummaryMultipleFields.field2>`',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_show_validator_summary': True}, **kwargs
    )
    assert result == actual

    # explict local
    actual = autodocument(options_doc={'model-show-validator-summary': True}, **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_show_validators_summary': False},
        options_doc={'model-show-validator-summary': True},
        **kwargs,
    )
    assert result == actual


def test_autodoc_pydantic_model_show_validator_summary_false(autodocument):
    kwargs = dict(
        object_path='target.configuration.ModelShowValidatorsSummary', **KWARGS
    )

    result = [
        '',
        '.. py:pydantic_model:: ModelShowValidatorsSummary',
        '   :module: target.configuration',
        '',
        '   ModelShowValidatorsSummary.',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_show_validator_summary': False}, **kwargs
    )
    assert result == actual

    # explict local
    actual = autodocument(options_doc={'model-show-validator-summary': False}, **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_show_validators_summary': True},
        options_doc={'model-show-validator-summary': False},
        **kwargs,
    )
    assert result == actual


def test_autodoc_pydantic_model_show_field_summary_true(autodocument):
    kwargs = dict(object_path='target.configuration.ModelShowFieldSummary', **KWARGS)

    result = [
        '',
        '.. py:pydantic_model:: ModelShowFieldSummary',
        '   :module: target.configuration',
        '',
        '   ModelShowFieldSummary.',
        '',
        '   :Fields:',
        '      - :py:obj:`field1 (int) <target.configuration.ModelShowFieldSummary.field1>`',
        '      - :py:obj:`field2 (str) <target.configuration.ModelShowFieldSummary.field2>`',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_show_field_summary': True}, **kwargs
    )
    assert result == actual

    # explict local
    actual = autodocument(options_doc={'model-show-field-summary': True}, **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_show_field_summary': False},
        options_doc={'model-show-field-summary': True},
        **kwargs,
    )
    assert result == actual


def test_autodoc_pydantic_model_show_field_summary_false(autodocument):
    kwargs = dict(object_path='target.configuration.ModelShowFieldSummary', **KWARGS)

    result = [
        '',
        '.. py:pydantic_model:: ModelShowFieldSummary',
        '   :module: target.configuration',
        '',
        '   ModelShowFieldSummary.',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_show_field_summary': False}, **kwargs
    )
    assert result == actual

    # explict local
    actual = autodocument(options_doc={'model-show-field-summary': False}, **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_show_field_summary': True},
        options_doc={'model-show-field-summary': False},
        **kwargs,
    )
    assert result == actual


def test_autodoc_pydantic_model_summary_list_order_alphabetical(autodocument):
    kwargs = dict(object_path='target.configuration.ModelSummaryListOrder', **KWARGS)
    enable = {
        'autodoc_pydantic_model_show_validator_summary': True,
        'autodoc_pydantic_model_show_field_summary': True,
    }

    result = [
        '',
        '.. py:pydantic_model:: ModelSummaryListOrder',
        '   :module: target.configuration',
        '',
        '   ModelSummaryListOrder.',
        '',
        '   :Fields:',
        '      - :py:obj:`field_a (int) <target.configuration.ModelSummaryListOrder.field_a>`',
        '      - :py:obj:`field_b (int) <target.configuration.ModelSummaryListOrder.field_b>`',
        '',
        '   :Validators:',
        '      - :py:obj:`validate_a <target.configuration.ModelSummaryListOrder.validate_a>` » :py:obj:`field_a <target.configuration.ModelSummaryListOrder.field_a>`',
        '      - :py:obj:`validate_b <target.configuration.ModelSummaryListOrder.validate_b>` » :py:obj:`field_b <target.configuration.ModelSummaryListOrder.field_b>`',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={
            'autodoc_pydantic_model_summary_list_order': 'alphabetical',
            **enable,
        },
        **kwargs,
    )
    assert result == actual

    # explict local
    actual = autodocument(
        options_app=enable,
        options_doc={'model-summary-list-order': 'alphabetical'},
        **kwargs,
    )
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_summary_list_order': 'bysource', **enable},
        options_doc={'model-summary-list-order': 'alphabetical'},
        **kwargs,
    )
    assert result == actual


def test_autodoc_pydantic_model_summary_list_order_bysource(autodocument):
    kwargs = dict(object_path='target.configuration.ModelSummaryListOrder', **KWARGS)
    enable = {
        'autodoc_pydantic_model_show_validator_summary': True,
        'autodoc_pydantic_model_show_field_summary': True,
    }

    result = [
        '',
        '.. py:pydantic_model:: ModelSummaryListOrder',
        '   :module: target.configuration',
        '',
        '   ModelSummaryListOrder.',
        '',
        '   :Fields:',
        '      - :py:obj:`field_b (int) <target.configuration.ModelSummaryListOrder.field_b>`',
        '      - :py:obj:`field_a (int) <target.configuration.ModelSummaryListOrder.field_a>`',
        '',
        '   :Validators:',
        '      - :py:obj:`validate_b <target.configuration.ModelSummaryListOrder.validate_b>` » :py:obj:`field_b <target.configuration.ModelSummaryListOrder.field_b>`',
        '      - :py:obj:`validate_a <target.configuration.ModelSummaryListOrder.validate_a>` » :py:obj:`field_a <target.configuration.ModelSummaryListOrder.field_a>`',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_summary_list_order': 'bysource', **enable},
        **kwargs,
    )
    assert result == actual

    # explict local
    actual = autodocument(
        options_app=enable,
        options_doc={'model-summary-list-order': 'bysource'},
        **kwargs,
    )
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={
            'autodoc_pydantic_model_summary_list_order': 'alphabetical',
            **enable,
        },
        options_doc={'model-summary-list-order': 'bysource'},
        **kwargs,
    )
    assert result == actual


def test_autodoc_pydantic_model_summary_list_order_bysource_inherited_shown(
    autodocument,
):
    """Test that you can order the output when in an inherited model, showing inherited fields/validators"""
    kwargs = dict(
        object_path='target.configuration.ModelSummaryListOrderInherited', **KWARGS
    )
    enable = {
        'autodoc_pydantic_model_show_validator_summary': True,
        'autodoc_pydantic_model_show_field_summary': True,
    }

    local_bysource = {'model-summary-list-order': 'bysource'}
    show_inherited = {'inherited-members': 'BaseModel'}

    result = [
        '',
        '.. py:pydantic_model:: ModelSummaryListOrderInherited',
        '   :module: target.configuration',
        '',
        '   ModelSummaryListOrderInherited.',
        '',
        '   :Fields:',
        '      - :py:obj:`field_b (int) <target.configuration.ModelSummaryListOrderInherited.field_b>`',
        '      - :py:obj:`field_a (int) <target.configuration.ModelSummaryListOrderInherited.field_a>`',
        '      - :py:obj:`field_c (int) <target.configuration.ModelSummaryListOrderInherited.field_c>`',
        '',
        '   :Validators:',
        '      - :py:obj:`validate_b <target.configuration.ModelSummaryListOrderInherited.validate_b>` » :py:obj:`field_b <target.configuration.ModelSummaryListOrderInherited.field_b>`',
        '      - :py:obj:`validate_a <target.configuration.ModelSummaryListOrderInherited.validate_a>` » :py:obj:`field_a <target.configuration.ModelSummaryListOrderInherited.field_a>`',
        '      - :py:obj:`validate_c <target.configuration.ModelSummaryListOrderInherited.validate_c>` » :py:obj:`field_c <target.configuration.ModelSummaryListOrderInherited.field_c>`',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_summary_list_order': 'bysource', **enable},
        options_doc=show_inherited,
        **kwargs,
    )
    assert result == actual

    # explict local
    actual = autodocument(
        options_app=enable,
        options_doc=dict(**local_bysource, **show_inherited),
        **kwargs,
    )
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={
            'autodoc_pydantic_model_summary_list_order': 'alphabetical',
            **enable,
        },
        options_doc=dict(**local_bysource, **show_inherited),
        **kwargs,
    )
    assert result == actual


def test_autodoc_pydantic_model_summary_list_order_bysource_inherited_not_shown(
    autodocument,
):
    kwargs = dict(
        object_path='target.configuration.ModelSummaryListOrderInherited', **KWARGS
    )
    enable = {
        'autodoc_pydantic_model_show_validator_summary': True,
        'autodoc_pydantic_model_show_field_summary': True,
    }

    local_bysource = {'model-summary-list-order': 'bysource'}

    result = [
        '',
        '.. py:pydantic_model:: ModelSummaryListOrderInherited',
        '   :module: target.configuration',
        '',
        '   ModelSummaryListOrderInherited.',
        '',
        '   :Fields:',
        '      - :py:obj:`field_c (int) <target.configuration.ModelSummaryListOrderInherited.field_c>`',
        '',
        '   :Validators:',
        '      - :py:obj:`validate_c <target.configuration.ModelSummaryListOrderInherited.validate_c>` » :py:obj:`field_c <target.configuration.ModelSummaryListOrderInherited.field_c>`',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_summary_list_order': 'bysource', **enable},
        **kwargs,
    )
    assert result == actual

    # explict local
    actual = autodocument(options_app=enable, options_doc=local_bysource, **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={
            'autodoc_pydantic_model_summary_list_order': 'alphabetical',
            **enable,
        },
        options_doc=local_bysource,
        **kwargs,
    )
    assert result == actual


def test_autodoc_pydantic_model_hide_paramlist_false(autodocument):
    kwargs = dict(object_path='target.configuration.ModelHideParamList', **KWARGS)

    result = [
        '',
        ".. py:pydantic_model:: ModelHideParamList(*, field1: int = 5, field2: str = 'FooBar')",
        '   :module: target.configuration',
        '',
        '   ModelHideParamList.',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_hide_paramlist': False}, **kwargs
    )
    assert result == actual

    # explict local
    actual = autodocument(options_doc={'model-hide-paramlist': False}, **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_hide_paramlist': True},
        options_doc={'model-hide-paramlist': False},
        **kwargs,
    )
    assert result == actual


def test_autodoc_pydantic_model_hide_paramlist_true(autodocument):
    kwargs = dict(object_path='target.configuration.ModelHideParamList', **KWARGS)

    result = [
        '',
        '.. py:pydantic_model:: ModelHideParamList',
        '   :module: target.configuration',
        '',
        '   ModelHideParamList.',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_hide_paramlist': True}, **kwargs
    )
    assert result == actual

    # explict local
    actual = autodocument(options_doc={'model-hide-paramlist': True}, **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_hide_paramlist': False},
        options_doc={'model-hide-paramlist': True},
        **kwargs,
    )
    assert result == actual


def test_autodoc_pydantic_model_undoc_members_true(autodocument):
    kwargs = dict(object_path='target.configuration.ModelUndocMembers', **KWARGS)
    enable = {'autodoc_pydantic_model_members': True}

    result = [
        '',
        '.. py:pydantic_model:: ModelUndocMembers',
        '   :module: target.configuration',
        '',
        '   ModelUndocMembers.',
        '',
        '',
        '   .. py:pydantic_field:: ModelUndocMembers.field1',
        '      :module: target.configuration',
        '      :type: int',
        '',
        '',
        '   .. py:pydantic_field:: ModelUndocMembers.field2',
        '      :module: target.configuration',
        '      :type: str',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_undoc_members': True, **enable}, **kwargs
    )
    assert result == actual

    # explict local
    actual = autodocument(
        options_app=enable, options_doc={'undoc-members': None}, **kwargs
    )
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_undoc_members': False, **enable},
        options_doc={'undoc-members': None},
        **kwargs,
    )
    assert result == actual


def test_autodoc_pydantic_model_undoc_members_false(autodocument):
    kwargs = dict(object_path='target.configuration.ModelUndocMembers', **KWARGS)
    enable = {'autodoc_pydantic_model_members': True}

    result = [
        '',
        '.. py:pydantic_model:: ModelUndocMembers',
        '   :module: target.configuration',
        '',
        '   ModelUndocMembers.',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_undoc_members': False, **enable}, **kwargs
    )
    assert result == actual


def test_autodoc_pydantic_model_members_true(autodocument):
    kwargs = dict(object_path='target.configuration.ModelMembers', **KWARGS)

    result = [
        '',
        '.. py:pydantic_model:: ModelMembers',
        '   :module: target.configuration',
        '',
        '   ModelMembers.',
        '',
        '',
        '   .. py:pydantic_field:: ModelMembers.field1',
        '      :module: target.configuration',
        '      :type: int',
        '',
        '      Doc field 1',
        '',
        '',
        '   .. py:pydantic_field:: ModelMembers.field2',
        '      :module: target.configuration',
        '      :type: str',
        '',
        '      Doc field 2',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_members': True}, **kwargs
    )
    assert result == actual

    # explict local
    actual = autodocument(options_doc={'members': None}, **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_members': False},
        options_doc={'members': None},
        **kwargs,
    )
    assert result == actual


def test_autodoc_pydantic_model_members_false(autodocument):
    kwargs = dict(object_path='target.configuration.ModelMembers', **KWARGS)

    result = [
        '',
        '.. py:pydantic_model:: ModelMembers',
        '   :module: target.configuration',
        '',
        '   ModelMembers.',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_members': False}, **kwargs
    )
    assert result == actual

    # explict local
    actual = autodocument(options_doc={'members': 'False'}, **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={'autodoc_pydantic_model_members': True},
        options_doc={'members': 'False'},
        **kwargs,
    )
    assert result == actual


def test_autodoc_pydantic_model_member_order_groupwise(autodocument):
    kwargs = dict(object_path='target.configuration.ModelMemberOrder', **KWARGS)

    result = [
        '',
        '.. py:pydantic_model:: ModelMemberOrder',
        '   :module: target.configuration',
        '',
        '   ModelMemberOrder.',
        '',
        '',
        '   .. py:pydantic_field:: ModelMemberOrder.field',
        '      :module: target.configuration',
        '      :type: int',
        '',
        '      Field.',
        '',
        '',
        '   .. py:pydantic_validator:: ModelMemberOrder.dummy',
        '      :module: target.configuration',
        '      :classmethod:',
        '',
        '      Check.',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={
            'autodoc_pydantic_model_member_order': 'groupwise',
            **SETTING_MEMBER_ORDER,
        },
        **kwargs,
    )
    assert result == actual

    # explict local
    actual = autodocument(
        options_app=SETTING_MEMBER_ORDER,
        options_doc={'member-order': 'groupwise'},
        **kwargs,
    )
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={
            'autodoc_pydantic_model_member_order': 'bysource',
            **SETTING_MEMBER_ORDER,
        },
        options_doc={'member-order': 'groupwise'},
        **kwargs,
    )
    assert result == actual


def test_autodoc_pydantic_model_member_order_bysource(autodocument):
    kwargs = dict(object_path='target.configuration.ModelMemberOrder', **KWARGS)

    result = [
        '',
        '.. py:pydantic_model:: ModelMemberOrder',
        '   :module: target.configuration',
        '',
        '   ModelMemberOrder.',
        '',
        '',
        '   .. py:pydantic_validator:: ModelMemberOrder.dummy',
        '      :module: target.configuration',
        '      :classmethod:',
        '',
        '      Check.',
        '',
        '',
        '   .. py:pydantic_field:: ModelMemberOrder.field',
        '      :module: target.configuration',
        '      :type: int',
        '',
        '      Field.',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={
            'autodoc_pydantic_model_member_order': 'bysource',
            **SETTING_MEMBER_ORDER,
        },
        **kwargs,
    )
    assert result == actual

    # explict local
    actual = autodocument(
        options_app=SETTING_MEMBER_ORDER,
        options_doc={'member-order': 'bysource'},
        **kwargs,
    )
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={
            'autodoc_pydantic_model_member_order': 'groupwise',
            **SETTING_MEMBER_ORDER,
        },
        options_doc={'member-order': 'bysource'},
        **kwargs,
    )
    assert result == actual


def test_autodoc_pydantic_model_member_order_alphabetical(autodocument):
    kwargs = dict(object_path='target.configuration.ModelMemberOrder', **KWARGS)

    result = [
        '',
        '.. py:pydantic_model:: ModelMemberOrder',
        '   :module: target.configuration',
        '',
        '   ModelMemberOrder.',
        '',
        '',
        '   .. py:pydantic_validator:: ModelMemberOrder.dummy',
        '      :module: target.configuration',
        '      :classmethod:',
        '',
        '      Check.',
        '',
        '',
        '   .. py:pydantic_field:: ModelMemberOrder.field',
        '      :module: target.configuration',
        '      :type: int',
        '',
        '      Field.',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={
            'autodoc_pydantic_model_member_order': 'alphabetical',
            **SETTING_MEMBER_ORDER,
        },
        **kwargs,
    )
    assert result == actual

    # explict local
    actual = autodocument(
        options_app=SETTING_MEMBER_ORDER,
        options_doc={'member-order': 'alphabetical'},
        **kwargs,
    )
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={
            'autodoc_pydantic_model_member_order': 'groupwise',
            **SETTING_MEMBER_ORDER,
        },
        options_doc={'member-order': 'alphabetical'},
        **kwargs,
    )
    assert result == actual


def test_autodoc_pydantic_model_show_validator_members_true(autodocument):
    kwargs = dict(
        object_path='target.configuration.ModelShowValidatorMembers', **KWARGS
    )

    result = [
        '',
        '.. py:pydantic_model:: ModelShowValidatorMembers',
        '   :module: target.configuration',
        '',
        '   ModelShowValidatorMembers.',
        '',
        '',
        '   .. py:pydantic_field:: ModelShowValidatorMembers.field',
        '      :module: target.configuration',
        '      :type: int',
        '',
        '      Field.',
        '',
        '',
        '   .. py:pydantic_validator:: ModelShowValidatorMembers.dummy',
        '      :module: target.configuration',
        '      :classmethod:',
        '',
        '      Check.',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={
            'autodoc_pydantic_model_members': True,
            'autodoc_pydantic_model_show_validator_members': True,
        },
        **kwargs,
    )
    assert result == actual

    # explict local
    actual = autodocument(
        options_app={'autodoc_pydantic_model_members': True},
        options_doc={'model-show-validator-members': True},
        **kwargs,
    )
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={
            'autodoc_pydantic_model_members': True,
            'autodoc_pydantic_model_show_validator_members': False,
        },
        options_doc={'model-show-validator-members': True},
        **kwargs,
    )
    assert result == actual


def test_autodoc_pydantic_model_show_validator_members_false(autodocument):
    kwargs = dict(
        object_path='target.configuration.ModelShowValidatorMembers', **KWARGS
    )

    result = [
        '',
        '.. py:pydantic_model:: ModelShowValidatorMembers',
        '   :module: target.configuration',
        '',
        '   ModelShowValidatorMembers.',
        '',
        '',
        '   .. py:pydantic_field:: ModelShowValidatorMembers.field',
        '      :module: target.configuration',
        '      :type: int',
        '',
        '      Field.',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={
            'autodoc_pydantic_model_members': True,
            'autodoc_pydantic_model_show_validator_members': False,
        },
        **kwargs,
    )
    assert result == actual

    # explict local
    actual = autodocument(
        options_app={'autodoc_pydantic_model_members': True},
        options_doc={'model-show-validator-members': False},
        **kwargs,
    )
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={
            'autodoc_pydantic_model_members': True,
            'autodoc_pydantic_model_show_validator_members': True,
        },
        options_doc={'model-show-validator-members': False},
        **kwargs,
    )
    assert result == actual


def test_autodoc_pydantic_model_signature_prefix(autodocument, parse_rst):
    """Tests pydantic_model directive."""
    kwargs = dict(object_path='target.configuration.ModelSignaturePrefix', **KWARGS)

    # default
    result = [
        '',
        '.. py:pydantic_model:: ModelSignaturePrefix',
        '   :module: target.configuration',
        '',
        '   ModelSignaturePrefix.',
        '',
    ]

    actual = autodocument(**kwargs)
    assert result == actual

    # explicit value
    result = [
        '',
        '.. py:pydantic_model:: ModelSignaturePrefix',
        '   :module: target.configuration',
        '   :model-signature-prefix: foobar ',
        '',
        '   ModelSignaturePrefix.',
        '',
    ]

    actual = autodocument(options_doc={'model-signature-prefix': 'foobar '}, **kwargs)
    assert result == actual

    # explict empty
    result = [
        '',
        '.. py:pydantic_model:: ModelSignaturePrefix',
        '   :module: target.configuration',
        '   :model-signature-prefix: ',
        '',
        '   ModelSignaturePrefix.',
        '',
    ]

    actual = autodocument(options_doc={'model-signature-prefix': ''}, **kwargs)
    assert result == actual


def test_autodoc_pydantic_model_signature_prefix_directive(parse_rst):
    """Tests pydantic_model directive."""

    # default
    input_rst = [
        '',
        '.. py:pydantic_model:: ModelSignaturePrefix',
        '   :module: target.configuration',
        '',
        '   ModelSignaturePrefix.',
        '',
    ]

    doctree = parse_rst(input_rst)
    prefix = desc_annotation_directive_prefix('pydantic model')
    assert_node(doctree[1][0][0], [desc_annotation, prefix])

    # empty
    doctree = parse_rst(input_rst, conf={'autodoc_pydantic_model_signature_prefix': ''})
    assert_node(doctree[1][0][0], [desc_addname, 'target.configuration.'])

    # custom
    input_rst = [
        '',
        '.. py:pydantic_model:: ModelSignaturePrefix',
        '   :module: target.configuration',
        '   :model-signature-prefix: foobar',
        '',
        '   ModelSignaturePrefix.',
        '',
    ]

    doctree = parse_rst(input_rst)
    prefix = desc_annotation_directive_prefix('foobar')
    assert_node(doctree[1][0][0], [desc_annotation, prefix])


def test_autodoc_pydantic_model_show_field_summary_with_swap_name_and_alias(
    autodocument,
):
    kwargs = dict(
        object_path='target.configuration.ModelWithFieldSwapNameAndAlias', **KWARGS
    )

    result = [
        '',
        '.. py:pydantic_model:: ModelWithFieldSwapNameAndAlias',
        '   :module: target.configuration',
        '',
        '   ModelWithFieldSwapNameAndAlias.',
        '',
        '   :Fields:',
        '      - :py:obj:`field1 alias (int) <target.configuration.ModelWithFieldSwapNameAndAlias.field1>`',
        '      - :py:obj:`field2 alias (str) <target.configuration.ModelWithFieldSwapNameAndAlias.field2>`',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={
            'autodoc_pydantic_model_show_field_summary': True,
            'autodoc_pydantic_field_swap_name_and_alias': True,
        },
        **kwargs,
    )
    assert result == actual

    # explict local
    actual = autodocument(
        options_doc={
            'model-show-field-summary': True,
            'field-swap-name-and-alias': True,
        },
        **kwargs,
    )
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={
            'autodoc_pydantic_model_show_field_summary': False,
            'autodoc_pydantic_field_swap_name_and_alias': False,
        },
        options_doc={
            'model-show-field-summary': True,
            'field-swap-name-and-alias': True,
        },
        **kwargs,
    )
    assert result == actual


def test_autodoc_pydantic_model_show_validator_summary_with_swap_name_and_alias(
    autodocument,
):
    kwargs = dict(
        object_path='target.configuration.ModelWithFieldSwapNameAndAlias', **KWARGS
    )

    result = [
        '',
        '.. py:pydantic_model:: ModelWithFieldSwapNameAndAlias',
        '   :module: target.configuration',
        '',
        '   ModelWithFieldSwapNameAndAlias.',
        '',
        '   :Validators:',
        '      - :py:obj:`check <target.configuration.ModelWithFieldSwapNameAndAlias.check>` » :py:obj:`field1 alias <target.configuration.ModelWithFieldSwapNameAndAlias.field1>`',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={
            'autodoc_pydantic_field_swap_name_and_alias': True,
            'autodoc_pydantic_model_show_validator_summary': True,
        },
        **kwargs,
    )
    assert result == actual

    # explict local
    actual = autodocument(
        options_doc={
            'model-show-validator-summary': True,
            'field-swap-name-and-alias': True,
        },
        **kwargs,
    )
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={
            'autodoc_pydantic_model_show_validator_summary': False,
            'autodoc_pydantic_field_swap_name_and_alias': False,
        },
        options_doc={
            'model-show-validator-summary': True,
            'field-swap-name-and-alias': True,
        },
        **kwargs,
    )
    assert result == actual


def test_autodoc_pydantic_model_validator_signature_with_swap_name_and_alias(
    autodocument,
):
    """Ensure that directive option `:field-swap-name-and-alias:` is passed to
    `py:pydantic_validator`.

    This relates to ##99.

    """

    kwargs = dict(
        object_path='target.configuration.ModelWithFieldSwapNameAndAlias', **KWARGS
    )

    result = [
        '',
        '.. py:pydantic_model:: ModelWithFieldSwapNameAndAlias',
        '   :module: target.configuration',
        '',
        '   ModelWithFieldSwapNameAndAlias.',
        '',
        '',
        '   .. py:pydantic_field:: ModelWithFieldSwapNameAndAlias.field1',
        '      :module: target.configuration',
        '      :type: int',
        '      :alias: field1 alias',
        '      :field-swap-name-and-alias: True',
        '',
        '      Field1',
        '',
        '',
        '   .. py:pydantic_field:: ModelWithFieldSwapNameAndAlias.field2',
        '      :module: target.configuration',
        '      :type: str',
        '      :alias: field2 alias',
        '      :field-swap-name-and-alias: True',
        '',
        '      Field2',
        '',
        '',
        '   .. py:pydantic_validator:: ModelWithFieldSwapNameAndAlias.check',
        '      :module: target.configuration',
        '      :classmethod:',
        '      :field-swap-name-and-alias: True',
        '',
        '      Check.',
        '',
    ]

    # explict local
    actual = autodocument(
        options_doc={
            'model-show-validator-members': True,
            'field-swap-name-and-alias': True,
            'members': None,
        },
        **kwargs,
    )
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={
            'autodoc_pydantic_model_show_validator_members': False,
            'autodoc_pydantic_field_swap_name_and_alias': False,
            'autodoc_pydantic_model_members': False,
        },
        options_doc={
            'model-show-validator-members': True,
            'field-swap-name-and-alias': True,
            'members': None,
        },
        **kwargs,
    )
    assert result == actual


def test_autodoc_pydantic_model_hide_reused_validator_true(autodocument):
    """Ensure that class attributes of reused validators are hidden and the
    actual validator reference point to the correct function.

    This relates to #122.

    """

    kwargs = dict(
        object_path='target.configuration_model_hide_reused_validator.ModelOne',
        **KWARGS,
    )

    result = [
        '',
        '.. py:pydantic_model:: ModelOne',
        '   :module: target.configuration_model_hide_reused_validator',
        '',
        '   :Validators:',
        '      - :py:obj:`validation <target.configuration_model_hide_reused_validator.validation>` » :py:obj:`name <target.configuration_model_hide_reused_validator.ModelOne.name>`',
        '',
        '',
        '   .. py:pydantic_field:: ModelOne.name',
        '      :module: target.configuration_model_hide_reused_validator',
        '      :type: str',
        '',
        '      Name',
        '',
        '      :Validated by:',
        '         - :py:obj:`validation <target.configuration_model_hide_reused_validator.validation>`',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={
            'autodoc_pydantic_model_hide_reused_validator': True,
            'autodoc_pydantic_model_show_validator_summary': True,
            'autodoc_pydantic_field_list_validators': True,
        },
        options_doc={'members': None, 'undoc-members': None},
        **kwargs,
    )
    assert result == actual

    # explict local
    actual = autodocument(
        options_doc={
            'model-hide-reused-validator': True,
            'members': None,
            'undoc-members': None,
        },
        options_app={
            'autodoc_pydantic_model_show_validator_summary': True,
            'autodoc_pydantic_field_list_validators': True,
        },
        **kwargs,
    )
    assert result == actual

    # explict global
    actual = autodocument(
        options_app={
            'autodoc_pydantic_model_hide_reused_validator': False,
            'autodoc_pydantic_model_show_validator_summary': True,
            'autodoc_pydantic_field_list_validators': True,
        },
        options_doc={
            'model-hide-reused-validator': True,
            'members': None,
            'undoc-members': None,
        },
        **kwargs,
    )
    assert result == actual


def test_autodoc_pydantic_model_hide_reused_validator_false(autodocument):
    """Ensure that class attributes of reused validators are not hidden and the
    actual validator reference point to the correct function.

    This relates to #122.

    """

    kwargs = dict(
        object_path='target.configuration_model_hide_reused_validator.ModelOne',
        **KWARGS,
    )

    result = [
        '',
        '.. py:pydantic_model:: ModelOne',
        '   :module: target.configuration_model_hide_reused_validator',
        '',
        '   :Validators:',
        '      - :py:obj:`validation <target.configuration_model_hide_reused_validator.validation>` » :py:obj:`name <target.configuration_model_hide_reused_validator.ModelOne.name>`',
        '',
        '',
        '   .. py:pydantic_field:: ModelOne.name',
        '      :module: target.configuration_model_hide_reused_validator',
        '      :type: str',
        '',
        '      Name',
        '',
        '      :Validated by:',
        '         - :py:obj:`validation <target.configuration_model_hide_reused_validator.validation>`',
        '',
        '',
        '   .. py:method:: ModelOne.normalize_name()',
        '      :module: target.configuration_model_hide_reused_validator',
        '',
        '      Reused validator class method.',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={
            'autodoc_pydantic_model_hide_reused_validator': False,
            'autodoc_pydantic_model_show_validator_summary': True,
            'autodoc_pydantic_field_list_validators': True,
        },
        options_doc={'members': None, 'undoc-members': None},
        **kwargs,
    )
    assert result == actual

    # explict local
    actual = autodocument(
        options_doc={
            'model-hide-reused-validator': False,
            'members': None,
            'undoc-members': None,
        },
        options_app={
            'autodoc_pydantic_model_show_validator_summary': True,
            'autodoc_pydantic_field_list_validators': True,
        },
        **kwargs,
    )
    assert result == actual

    # explict global
    actual = autodocument(
        options_app={
            'autodoc_pydantic_model_hide_reused_validator': True,
            'autodoc_pydantic_model_show_validator_summary': True,
            'autodoc_pydantic_field_list_validators': True,
        },
        options_doc={
            'model-hide-reused-validator': False,
            'members': None,
            'undoc-members': None,
        },
        **kwargs,
    )
    assert result == actual
