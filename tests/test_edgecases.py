"""This module contains tests for edgecases.

"""
import copy

import pytest
import sphinx.errors
from sphinx.transforms.post_transforms import ReferencesResolver

from sphinxcontrib.autodoc_pydantic import PydanticModelDocumenter
from tests.compatibility import rst_alias_class_directive, \
    TYPEHINTS_PREFIX, TYPING_MODULE_PREFIX_V1, module_doc_string_tab


def test_not_json_compliant(autodocument):
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.edgecase_json_compliant.NotJsonCompliant',
        options_doc={"model-show-json": True},
        deactivate_all=True)

    assert actual == [
        '',
        '.. py:pydantic_model:: NotJsonCompliant',
        '   :module: target.edgecase_json_compliant',
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
        '         "title": "NotJsonCompliant",',
        '         "type": "object",',
        '         "properties": {',
        '            "field": {',
        '               "default": null,',
        '               "title": "Field"',
        '            }',
        '         }',
        '      }',
        '',
        '   .. raw:: html',
        '',
        '      </details></p>',
        '',
        ''
    ]


def test_current_module_model(parse_rst):
    """Ensure that using current module does not break any features.

    This relates to issue #12.

    """

    input_rst = ['.. py:currentmodule:: target.example_model',
                 '',
                 '.. autopydantic_model:: ExampleSettings',
                 '   :model-show-json: True',
                 '   :model-show-config-member: False',
                 '   :model-show-config-summary: True',
                 '   :model-show-validator-members: False',
                 '   :model-show-validator-summary: False',
                 '   :model-hide-paramlist: True',
                 '   :undoc-members: True',
                 '   :members: True',
                 '   :member-order: alphabetical',
                 '   :model-signature-prefix: pydantic_model',
                 '   :field-list-validators: True',
                 '   :field-doc-policy: both',
                 '   :field-show-constraints: True',
                 '   :field-show-alias: True',
                 '   :field-show-default: True',
                 '   :field-signature-prefix: field',
                 '   :validator-signature-prefix: validator',
                 '   :validator-replace-signature: True',
                 '   :validator-list-fields: True',
                 '   :config-signature-prefix: config',
                 '']

    parse_rst(input_rst,
              conf={"extensions": ["sphinxcontrib.autodoc_pydantic"]})


def test_current_module_settings(parse_rst):
    """Ensure that using current module does not break any features.

    This relates to issue #12.

    """

    input_rst = ['.. py:currentmodule:: target.example_setting',
                 '',
                 '.. autopydantic_settings:: ExampleSettings',
                 '   :settings-show-json: True',
                 '   :settings-show-config-member: False',
                 '   :settings-show-config-summary: True',
                 '   :settings-show-validator-members: False',
                 '   :settings-show-validator-summary: False',
                 '   :settings-hide-paramlist: True',
                 '   :undoc-members: True',
                 '   :members: True',
                 '   :member-order: alphabetical',
                 '   :settings-signature-prefix: pydantic_settings',
                 '   :field-list-validators: True',
                 '   :field-doc-policy: both',
                 '   :field-show-constraints: True',
                 '   :field-show-alias: True',
                 '   :field-show-default: True',
                 '   :field-signature-prefix: field',
                 '   :validator-signature-prefix: validator',
                 '   :validator-replace-signature: True',
                 '   :validator-list-fields: True',
                 '   :config-signature-prefix: config',
                 '']

    parse_rst(input_rst,
              conf={"extensions": ["sphinxcontrib.autodoc_pydantic"]})


def test_any_reference(test_app, monkeypatch):
    """Ensure that `:any:` reference does also work with directives provided
    by autodoc_pydantic.

    This relates to #3.

    """

    failed_targets = set()
    func = copy.deepcopy(ReferencesResolver.warn_missing_reference)

    def mock(self, refdoc, typ, target, node, domain):
        failed_targets.add(target)
        return func(self, refdoc, typ, target, node, domain)

    with monkeypatch.context() as ctx:
        ctx.setattr(ReferencesResolver, "warn_missing_reference", mock)
        app = test_app("edgecase-any-reference")
        app.build()

    assert "does.not.exist" in failed_targets
    assert "target.example_setting.ExampleSettings" not in failed_targets


def test_autodoc_member_order(autodocument):
    """Ensure that member order does not change when pydantic models are used.

    This relates to #21.

    """

    actual = autodocument(
        documenter='module',
        object_path='target.edgecase_member_order',
        options_app={"autodoc_member_order": "bysource"},
        options_doc={"members": None},
        deactivate_all=True)

    assert actual == [
        '',
        '.. py:module:: target.edgecase_member_order',
        '',
        f'{module_doc_string_tab()}Module doc string.',
        '',
        '',
        '.. py:pydantic_model:: C',
        '   :module: target.edgecase_member_order',
        '',
        '   Class C',
        '',
        '',
        '.. py:class:: D()',
        '   :module: target.edgecase_member_order',
        '',
        '   Class D',
        '',
        '',
        '.. py:pydantic_model:: A',
        '   :module: target.edgecase_member_order',
        '',
        '   Class A',
        '',
        '',
        '.. py:class:: B()',
        '   :module: target.edgecase_member_order',
        '',
        '   Class B',
        '']


def test_typed_field_reference(test_app, monkeypatch):
    """Ensure that typed fields within doc strings successfully reference
    pydantic models/settings.

    This relates to #27.

    """

    failed_targets = set()
    func = copy.deepcopy(ReferencesResolver.warn_missing_reference)

    def mock(self, refdoc, typ, target, node, domain):
        failed_targets.add(target)
        return func(self, refdoc, typ, target, node, domain)

    with monkeypatch.context() as ctx:
        ctx.setattr(ReferencesResolver, "warn_missing_reference", mock)
        app = test_app("edgecase-typed-field-reference")
        app.build()


def test_json_error_strategy_raise(test_app):
    """Confirm that a non serializable field raises an exception if strategy
    is to raise.

    This relates to #28.

    """

    with pytest.raises(sphinx.errors.ExtensionError):
        conf = {"autodoc_pydantic_model_show_json_error_strategy": "raise"}
        app = test_app("json-error-strategy", conf=conf)
        app.build()


def test_json_error_strategy_coerce(test_app, log_capturer):
    """Confirm that a non serializable field triggers no warning during build
    process but is coerced.

    This relates to #28.

    """

    conf = {"autodoc_pydantic_model_show_json_error_strategy": "coerce"}

    with log_capturer() as logs:
        app = test_app("json-error-strategy-coerce", conf=conf)
        app.build()

    message = (
        "JSON schema can't be generated for 'example.NonSerializable' "
        "because the following pydantic fields can't be serialized properly: "
        "['field']."
    )

    assert not [log for log in logs if log.msg == message]


def test_json_error_strategy_warn(test_app, log_capturer):
    """Confirm that a non serializable field triggers a warning during build
    process.

    This relates to #28.

    """

    conf = {"autodoc_pydantic_model_show_json_error_strategy": "warn"}

    with log_capturer() as logs:
        app = test_app("json-error-strategy", conf=conf)
        app.build()

    message = (
        "JSON schema can't be generated for 'example.NonSerializable' "
        "because the following pydantic fields can't be serialized properly: "
        "['field']."
    )

    assert [log for log in logs if log.msg == message]


def test_autodoc_pydantic_model_show_field_summary_not_inherited(autodocument):
    """Ensure that autodoc pydantic respects `:inherited-members:` option when
    listing fields in model/settings. More concretely, fields from base classes
    should not be listed be default.

    This relates to #32.

    """

    result = [
        '',
        '.. py:pydantic_model:: ModelShowFieldSummaryInherited',
        '   :module: target.configuration',
        '',
        '   ModelShowFieldSummaryInherited.',
        '',
        '   :Fields:',
        '      - :py:obj:`field3 (int) <target.configuration.ModelShowFieldSummaryInherited.field3>`',
        ''
    ]

    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowFieldSummaryInherited',
        options_app={"autodoc_pydantic_model_show_field_summary": True},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_model_show_field_summary_inherited(autodocument):
    """Ensure that autodoc pydantic respects `:inherited-members:` option when
    listing fields in model/settings. More concretely, fields from base classes
    should be listed if `:inherited-members:` is given.

    This relates to #32.

    """
    result = [
        '',
        '.. py:pydantic_model:: ModelShowFieldSummaryInherited',
        '   :module: target.configuration',
        '',
        '   ModelShowFieldSummaryInherited.',
        '',
        '   :Fields:',
        '      - :py:obj:`field1 (int) <target.configuration.ModelShowFieldSummaryInherited.field1>`',
        '      - :py:obj:`field2 (str) <target.configuration.ModelShowFieldSummaryInherited.field2>`',
        '      - :py:obj:`field3 (int) <target.configuration.ModelShowFieldSummaryInherited.field3>`',
        ''
    ]

    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowFieldSummaryInherited',
        options_app={"autodoc_pydantic_model_show_field_summary": True,
                     "autodoc_pydantic_model_members": True},
        options_doc={"inherited-members": "BaseModel"},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_model_show_validator_summary_inherited_with_inherited(
        autodocument):
    """Ensure that references to inherited validators point to child class
    when `inherited-members` is given.

    Relates to #122.

    """

    result = [
        '',
        '.. py:pydantic_model:: ModelShowValidatorsSummaryInherited',
        '   :module: target.configuration',
        '',
        '   ModelShowValidatorsSummaryInherited.',
        '',
        '   :Validators:',
        '      - :py:obj:`check <target.configuration.ModelShowValidatorsSummaryInherited.check>` » :py:obj:`field <target.configuration.ModelShowValidatorsSummaryInherited.field>`',
        '      - :py:obj:`check_inherited <target.configuration.ModelShowValidatorsSummaryInherited.check_inherited>` » :py:obj:`field <target.configuration.ModelShowValidatorsSummaryInherited.field>`',
        ''
    ]

    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowValidatorsSummaryInherited',
        options_app={"autodoc_pydantic_model_show_validator_summary": True,
                     "autodoc_pydantic_model_members": True},
        options_doc={"inherited-members": "BaseModel"},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_model_show_validator_summary_inherited_without_inherited(
        autodocument):
    """Ensure that references to inherited validators point to parent class
    when `inherited-members` is not given.

    Relates to #122.

    """

    result = [
        '',
        '.. py:pydantic_model:: ModelShowValidatorsSummaryInherited',
        '   :module: target.configuration',
        '',
        '   ModelShowValidatorsSummaryInherited.',
        '',
        '   :Validators:',
        '      - :py:obj:`check_inherited <target.configuration.ModelShowValidatorsSummaryInherited.check_inherited>` » :py:obj:`field <target.configuration.ModelShowValidatorsSummaryInherited.field>`',
        ''
    ]

    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowValidatorsSummaryInherited',
        options_app={"autodoc_pydantic_model_show_validator_summary": True,
                     "autodoc_pydantic_model_members": True},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_field_list_validators_inherited_with_inherited(
        autodocument):
    """Ensure that references to inherited validators point to child class
    when `inherited-members` is given.

    Relates to #122.

    """

    result = [
        '',
        '.. py:pydantic_model:: FieldListValidatorsInherited',
        '   :module: target.configuration',
        '',
        '   FieldListValidatorsInherited.',
        '',
        '',
        '   .. py:pydantic_field:: FieldListValidatorsInherited.field',
        '      :module: target.configuration',
        '      :type: int',
        '',
        '      Field.',
        '',
        '      :Validated by:',
        '         - :py:obj:`check <target.configuration.FieldListValidatorsInherited.check>`',
        '         - :py:obj:`check_inherited <target.configuration.FieldListValidatorsInherited.check_inherited>`',
        ''
    ]

    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.FieldListValidatorsInherited',
        options_app={"autodoc_pydantic_field_list_validators": True,
                     "autodoc_pydantic_model_members": True,
                     "autodoc_pydantic_model_undoc_members": True},
        options_doc={"inherited-members": "BaseModel"},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_field_list_validators_inherited_without_inherited(
        autodocument):
    """Ensure that references to inherited validators point to parent class
    when `inherited-members` is not given.

    Relates to #122.

    """

    result = [
        '',
        '.. py:pydantic_model:: FieldListValidatorsInherited',
        '   :module: target.configuration',
        '',
        '   FieldListValidatorsInherited.',
        '',
        '',
        '   .. py:pydantic_field:: FieldListValidatorsInherited.field',
        '      :module: target.configuration',
        '      :type: int',
        '',
        '      Field.',
        '',
        '      :Validated by:',
        '         - :py:obj:`check <target.configuration.FieldListValidators.check>`',
        '         - :py:obj:`check_inherited <target.configuration.FieldListValidatorsInherited.check_inherited>`',
        ''
    ]

    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.FieldListValidatorsInherited',
        options_app={"autodoc_pydantic_field_list_validators": True,
                     "autodoc_pydantic_model_members": True,
                     "autodoc_pydantic_model_undoc_members": True},
        deactivate_all=True)
    assert result == actual


def test_model_as_attr(autodocument):
    """Ensure that additional information provided by autodoc_pydantic like
    field/validator summary are hidden when model/settings are documented as
    an attribute.

    This relates to #78.

    """

    actual = autodocument(
        documenter='class',
        object_path='target.edgecase_model_as_attr.Container',
        options_doc={"members": "TEST_MODEL"},
        deactivate_all=False)

    rst_class = rst_alias_class_directive()

    assert actual == [
        '',
        '.. py:class:: Container()',
        '   :module: target.edgecase_model_as_attr',
        '',
        '   Container Doc String',
        '',
        '',
        '   .. py:attribute:: Container.TEST_MODEL',
        '      :module: target.edgecase_model_as_attr',
        '',
        f'      alias of {rst_class}`{TYPEHINTS_PREFIX}target.edgecase_model_as_attr.Model`'
    ]


def test_model_as_attr_sort_order_bysource_exception(autodocument):
    """Resembles a bug that occurred while documenting models as attributes
    and having model summary list order set to `bysource`. Test that no
    exception is raised.

    This relates to #78.

    """

    autodocument(
        documenter='class',
        object_path='target.edgecase_model_as_attr.Container',
        options_doc={"members": "TEST_MODEL"},
        options_app={"autodoc_pydantic_model_summary_list_order": "bysource"},
        deactivate_all=False)


def test_field_description_correct_rst_rendering(autodocument):
    """Ensure that pydantic `Field`s description attribute's content is
    correctly rendered as reST in the same way as common class/function
    docstrings are rendered.

    This relates to #91

    """

    result = [
        '',
        '.. py:pydantic_model:: FieldDocRender',
        '   :module: target.edgecase_field_doc_render_rst',
        '',
        '   Doc String.',
        '',
        '   :any:`FieldDocRender` *italic*',
        '',
        '   :fieldlist: item',
        '',
        '',
        '   .. py:pydantic_field:: FieldDocRender.field',
        '      :module: target.edgecase_field_doc_render_rst',
        '      :type: int',
        '',
        '      Doc String.',
        '',
        '      :any:`FieldDocRender` *italic*',
        '',
        '      :fieldlist: item',
        '',
        ''
    ]

    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.edgecase_field_doc_render_rst.FieldDocRender',
        options_app={"autodoc_pydantic_model_members": True,
                     "autodoc_pydantic_model_undoc_members": True},
        deactivate_all=True)
    assert result == actual


def test_non_field_attributes(autodocument):
    """Ensure that attributes which are not pydantic fields are correctly
    ignored.

    This relates to #123

    """

    result = [
        '',
        '.. py:pydantic_model:: ClassAttribute',
        '   :module: target.edgecase_non_field_attribute',
        '',
        '   FooBar.',
        '',
        '',
        '',
        '',
        '   .. py:attribute:: ClassAttribute.class_attribute',
        '      :module: target.edgecase_non_field_attribute',
        f'      :type: {TYPING_MODULE_PREFIX_V1}ClassVar[str]',
        '      :value: None',
        '',
        '      Dummy',
        '']

    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.edgecase_non_field_attribute.ClassAttribute',
        options_app={"autodoc_pydantic_model_show_json": False},
        deactivate_all=False)

    assert result == actual


def test_non_field_attributes(autodocument):
    """Ensure that pydantic models can be documented as class attributes.

    This relates to #129.

    """

    result = [
        '',
        '.. py:module:: target.edgecase_model_as_attribute',
        '',
        '',
        '.. py:class:: Foo()',
        '   :module: target.edgecase_model_as_attribute',
        '',
        '   Foo class',
        '',
        '',
        '   .. py:pydantic_model:: Foo.Bar',
        '      :module: target.edgecase_model_as_attribute',
        '',
        '      Bar class',
        '',
        '',
        '      .. py:pydantic_validator:: Foo.Bar.do_nothing',
        '         :module: target.edgecase_model_as_attribute',
        '         :classmethod:',
        '',
        '         Foo',
        ''
    ]

    actual = autodocument(
        documenter='module',
        object_path='target.edgecase_model_as_attribute',
        options_doc={"members": None},
        options_app={"autodoc_pydantic_model_show_validator_members": True},
        deactivate_all=True)

    assert result == actual


def test_autodoc_pydantic_model_hide_reused_validator_true_identical_names(
        autodocument):
    """Ensure that class attributes of reused validators are hidden and the
    actual validator reference point to the correct function when the function
    name is identical to validator/method name.

    This relates to #122.

    """

    kwargs = dict(
        object_path='target.edgecase_reused_validator_identical_names.ModelOne',
        documenter=PydanticModelDocumenter.objtype,
        deactivate_all=True
    )

    result = [
        '',
        '.. py:pydantic_model:: ModelOne',
        '   :module: target.edgecase_reused_validator_identical_names',
        '',
        '   :Validators:',
        '      - :py:obj:`validation <target.edgecase_reused_validator_identical_names.validation>` » :py:obj:`name <target.edgecase_reused_validator_identical_names.ModelOne.name>`',
        '',
        '',
        '   .. py:pydantic_field:: ModelOne.name',
        '      :module: target.edgecase_reused_validator_identical_names',
        '      :type: str',
        '',
        '      Name',
        '',
        '      :Validated by:',
        '         - :py:obj:`validation <target.edgecase_reused_validator_identical_names.validation>`',
        ''
    ]

    # explict global
    actual = autodocument(
        options_app={"autodoc_pydantic_model_hide_reused_validator": True,
                     "autodoc_pydantic_model_show_validator_summary": True,
                     "autodoc_pydantic_field_list_validators": True},
        options_doc={"members": None,
                     "undoc-members": None},
        **kwargs)
    assert result == actual

    # explict local
    actual = autodocument(
        options_doc={"model-hide-reused-validator": True,
                     "members": None,
                     "undoc-members": None},
        options_app={"autodoc_pydantic_model_show_validator_summary": True,
                     "autodoc_pydantic_field_list_validators": True},
        **kwargs)
    assert result == actual

    # explict global
    actual = autodocument(
        options_app={"autodoc_pydantic_model_hide_reused_validator": False,
                     "autodoc_pydantic_model_show_validator_summary": True,
                     "autodoc_pydantic_field_list_validators": True},
        options_doc={"model-hide-reused-validator": True,
                     "members": None,
                     "undoc-members": None},
        **kwargs)
    assert result == actual
