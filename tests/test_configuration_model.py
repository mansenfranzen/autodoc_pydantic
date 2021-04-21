"""This module contains tests for pydantic model configurations.

"""

from docutils.nodes import paragraph
from sphinx.addnodes import index, desc, desc_signature, desc_annotation, \
    desc_addname, desc_name, desc_content
from sphinx.testing.util import assert_node

SETTING_MEMBER_ORDER = {
    "autodoc_pydantic_model_members": True,
    "autodoc_pydantic_model_show_validator_members": True,
    "autodoc_pydantic_model_show_config_member": True}


def test_autodoc_pydantic_model_show_json_true(autodocument):
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
        '      <p><details>',
        '      <summary><a>Show JSON schema</a></summary>',
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
        '']

    # explicit global
    actual = autodocument(
        documenter='pydantic_model',
        options_app={"autodoc_pydantic_model_show_json": True},
        object_path='target.configuration.ModelShowJson')
    assert actual == result

    # explicit local
    actual = autodocument(documenter='pydantic_model',
                          options_doc={"model-show-json": True},
                          object_path='target.configuration.ModelShowJson')
    assert actual == result

    # explicit local overwrite global
    actual = autodocument(documenter='pydantic_model',
                          options_app={
                              "autodoc_pydantic_model_show_json": False},
                          options_doc={"model-show-json": True},
                          object_path='target.configuration.ModelShowJson')
    assert actual == result


def test_autodoc_pydantic_model_show_json_false(autodocument):
    result = [
        '',
        '.. py:pydantic_model:: ModelShowJson',
        '   :module: target.configuration',
        '',
        '   ModelShowJson.',
        ''
    ]

    # explicit global
    actual = autodocument(
        documenter='pydantic_model',
        options_app={"autodoc_pydantic_model_show_json": False},
        object_path='target.configuration.ModelShowJson')
    assert actual == result

    # explicit local
    actual = autodocument(
        documenter='pydantic_model',
        options_doc={"model-show-json": False},
        object_path='target.configuration.ModelShowJson')
    assert actual == result

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        options_app={"autodoc_pydantic_model_show_json": True},
        options_doc={"model-show-json": False},
        object_path='target.configuration.ModelShowJson')
    assert actual == result


def test_autodoc_pydantic_model_show_config_summary_summary_true(autodocument):
    result = [
        '',
        '.. py:pydantic_model:: ModelShowConfigSummary',
        '   :module: target.configuration',
        '',
        '   ModelShowConfigSummary.',
        '',
        '   :Config:',
        '      - **allow_mutation**: *bool = True*',
        '      - **title**: *str = FooBar*',
        '']

    # explict global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowConfigSummary',
        options_app={"autodoc_pydantic_model_show_config_summary": True},
        deactivate_all=True)
    assert actual == result

    # explict local
    actual = autodocument(documenter='pydantic_model',
                          object_path='target.configuration.ModelShowConfigSummary',
                          options_doc={"model-show-config-summary": True},
                          deactivate_all=True)
    assert actual == result

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowConfigSummary',
        options_app={"autodoc_pydantic_model_show_config_summary": False},
        options_doc={"model-show-config-summary": True},
        deactivate_all=True)
    assert actual == result


def test_autodoc_pydantic_model_show_config_summary_false(autodocument):
    result = [
        '',
        '.. py:pydantic_model:: ModelShowConfigSummary',
        '   :module: target.configuration',
        '',
        '   ModelShowConfigSummary.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowConfigSummary',
        options_app={"autodoc_pydantic_model_show_config_summary": False},
        deactivate_all=True)
    assert actual == result

    # explict local
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowConfigSummary',
        options_doc={"model-show-config-summary": False},
        deactivate_all=True)
    assert actual == result

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowConfigSummary',
        options_app={"autodoc_pydantic_model_show_config_summary": True},
        options_doc={"model-show-config-summary": False},
        deactivate_all=True)
    assert actual == result


def test_autodoc_pydantic_model_show_validator_summary_true(autodocument):
    result = [
        '',
        '.. py:pydantic_model:: ModelShowValidatorsSummary',
        '   :module: target.configuration',
        '',
        '   ModelShowValidatorsSummary.',
        '',
        '   :Validators:',
        '      - :py:obj:`check <target.configuration.ModelShowValidatorsSummary.check>` » :py:obj:`field <target.configuration.ModelShowValidatorsSummary.field>`',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowValidatorsSummary',
        options_app={"autodoc_pydantic_model_show_validator_summary": True},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowValidatorsSummary',
        options_doc={"model-show-validator-summary": True},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowValidatorsSummary',
        options_app={"autodoc_pydantic_model_show_validators_summary": False},
        options_doc={"model-show-validator-summary": True},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_model_show_validator_summary_false(autodocument):
    result = [
        '',
        '.. py:pydantic_model:: ModelShowValidatorsSummary',
        '   :module: target.configuration',
        '',
        '   ModelShowValidatorsSummary.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowValidatorsSummary',
        options_app={"autodoc_pydantic_model_show_validator_summary": False},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowValidatorsSummary',
        options_doc={"model-show-validator-summary": False},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowValidatorsSummary',
        options_app={"autodoc_pydantic_model_show_validators_summary": True},
        options_doc={"model-show-validator-summary": False},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_model_hide_paramlist_false(autodocument):
    result = [
        '',
        ".. py:pydantic_model:: ModelHideParamList(*, field1: int = 5, field2: str = 'FooBar')",
        '   :module: target.configuration',
        '',
        '   ModelHideParamList.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelHideParamList',
        options_app={"autodoc_pydantic_model_hide_paramlist": False},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelHideParamList',
        options_doc={"model-hide-paramlist": False},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelHideParamList',
        options_app={"autodoc_pydantic_model_hide_paramlist": True},
        options_doc={"model-hide-paramlist": False},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_model_hide_paramlist_true(autodocument):
    result = [
        '',
        '.. py:pydantic_model:: ModelHideParamList',
        '   :module: target.configuration',
        '',
        '   ModelHideParamList.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelHideParamList',
        options_app={"autodoc_pydantic_model_hide_paramlist": True},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelHideParamList',
        options_doc={"model-hide-paramlist": True},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelHideParamList',
        options_app={"autodoc_pydantic_model_hide_paramlist": False},
        options_doc={"model-hide-paramlist": True},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_model_undoc_members_true(autodocument):
    result = [
        '',
        ".. py:pydantic_model:: ModelUndocMembers",
        '   :module: target.configuration',
        '',
        '   ModelUndocMembers.',
        '',
        '',
        '   .. py:pydantic_field:: ModelUndocMembers.field1',
        '      :module: target.configuration',
        '      :type: int',
        '      :value: 5',
        '',
        '',
        '   .. py:pydantic_field:: ModelUndocMembers.field2',
        '      :module: target.configuration',
        '      :type: str',
        "      :value: 'FooBar'",
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelUndocMembers',
        options_app={"autodoc_pydantic_model_undoc_members": True,
                     "autodoc_pydantic_model_members": True},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelUndocMembers',
        options_app={"autodoc_pydantic_model_members": True},
        options_doc={"undoc-members": None},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelUndocMembers',
        options_app={"autodoc_pydantic_model_undoc_members": False,
                     "autodoc_pydantic_model_members": True},
        options_doc={"undoc-members": None},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_model_undoc_members_false(autodocument):
    result = [
        '',
        ".. py:pydantic_model:: ModelUndocMembers",
        '   :module: target.configuration',
        '',
        '   ModelUndocMembers.',
        '',
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelUndocMembers',
        options_app={"autodoc_pydantic_model_undoc_members": False,
                     "autodoc_pydantic_model_members": True},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_model_members_true(autodocument):
    result = [
        '',
        ".. py:pydantic_model:: ModelMembers",
        '   :module: target.configuration',
        '',
        '   ModelMembers.',
        '',
        '',
        '   .. py:pydantic_field:: ModelMembers.field1',
        '      :module: target.configuration',
        '      :type: int',
        '      :value: 5',
        '',
        '      Doc field 1',
        '',
        '',
        '   .. py:pydantic_field:: ModelMembers.field2',
        '      :module: target.configuration',
        '      :type: str',
        "      :value: 'FooBar'",
        '',
        '      Doc field 2',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelMembers',
        options_app={"autodoc_pydantic_model_members": True},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelMembers',
        options_doc={"members": None},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelMembers',
        options_app={"autodoc_pydantic_model_members": False},
        options_doc={"members": None},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_model_members_false(autodocument):
    result = [
        '',
        ".. py:pydantic_model:: ModelMembers",
        '   :module: target.configuration',
        '',
        '   ModelMembers.',
        '',
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelMembers',
        options_app={"autodoc_pydantic_model_members": False},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelMembers',
        options_doc={"members": "False"},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelMembers',
        options_app={"autodoc_pydantic_model_members": True},
        options_doc={"members": "False"},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_model_member_order_groupwise(autodocument):
    result = [
        '',
        ".. py:pydantic_model:: ModelMemberOrder",
        '   :module: target.configuration',
        '',
        '   ModelMemberOrder.',
        '',
        '',
        '   .. py:pydantic_field:: ModelMemberOrder.field',
        '      :module: target.configuration',
        '      :type: int',
        '      :value: 1',
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
        '',
        '   .. py:pydantic_config:: ModelMemberOrder.Config()',
        '      :module: target.configuration',
        '',
        '      Config.',
        '',
        '',
        '      .. py:attribute:: ModelMemberOrder.Config.allow_mutation',
        '         :module: target.configuration',
        '         :value: True',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelMemberOrder',
        options_app={"autodoc_pydantic_model_member_order": "groupwise",
                     **SETTING_MEMBER_ORDER},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelMemberOrder',
        options_app=SETTING_MEMBER_ORDER,
        options_doc={"member-order": "groupwise"},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelMemberOrder',
        options_app={"autodoc_pydantic_model_member_order": "bysource",
                     **SETTING_MEMBER_ORDER},
        options_doc={"member-order": "groupwise"},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_model_member_order_bysource(autodocument):
    result = [
        '',
        ".. py:pydantic_model:: ModelMemberOrder",
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
        '   .. py:pydantic_config:: ModelMemberOrder.Config()',
        '      :module: target.configuration',
        '',
        '      Config.',
        '',
        '',
        '      .. py:attribute:: ModelMemberOrder.Config.allow_mutation',
        '         :module: target.configuration',
        '         :value: True',
        '',
        '',
        '   .. py:pydantic_field:: ModelMemberOrder.field',
        '      :module: target.configuration',
        '      :type: int',
        '      :value: 1',
        '',
        '      Field.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelMemberOrder',
        options_app={"autodoc_pydantic_model_member_order": "bysource",
                     **SETTING_MEMBER_ORDER},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelMemberOrder',
        options_app=SETTING_MEMBER_ORDER,
        options_doc={"member-order": "bysource"},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelMemberOrder',
        options_app={"autodoc_pydantic_model_member_order": "groupwise",
                     **SETTING_MEMBER_ORDER},
        options_doc={"member-order": "bysource"},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_model_member_order_alphabetical(autodocument):
    result = [
        '',
        ".. py:pydantic_model:: ModelMemberOrder",
        '   :module: target.configuration',
        '',
        '   ModelMemberOrder.',
        '',
        '',
        '   .. py:pydantic_config:: ModelMemberOrder.Config()',
        '      :module: target.configuration',
        '',
        '      Config.',
        '',
        '',
        '      .. py:attribute:: ModelMemberOrder.Config.allow_mutation',
        '         :module: target.configuration',
        '         :value: True',
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
        '      :value: 1',
        '',
        '      Field.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelMemberOrder',
        options_app={"autodoc_pydantic_model_member_order": "alphabetical",
                     **SETTING_MEMBER_ORDER},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelMemberOrder',
        options_app=SETTING_MEMBER_ORDER,
        options_doc={"member-order": "alphabetical"},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelMemberOrder',
        options_app={"autodoc_pydantic_model_member_order": "groupwise",
                     **SETTING_MEMBER_ORDER},
        options_doc={"member-order": "alphabetical"},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_model_show_validator_members_true(autodocument):
    result = [
        '',
        ".. py:pydantic_model:: ModelShowValidatorMembers",
        '   :module: target.configuration',
        '',
        '   ModelShowValidatorMembers.',
        '',
        '',
        '   .. py:pydantic_field:: ModelShowValidatorMembers.field',
        '      :module: target.configuration',
        '      :type: int',
        '      :value: 1',
        '',
        '      Field.',
        '',
        '',
        '   .. py:pydantic_validator:: ModelShowValidatorMembers.dummy',
        '      :module: target.configuration',
        '      :classmethod:',
        '',
        '      Check.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowValidatorMembers',
        options_app={"autodoc_pydantic_model_members": True,
                     "autodoc_pydantic_model_show_validator_members": True},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowValidatorMembers',
        options_app={"autodoc_pydantic_model_members": True},
        options_doc={"model-show-validator-members": True},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowValidatorMembers',
        options_app={"autodoc_pydantic_model_members": True,
                     "autodoc_pydantic_model_show_validator_members": False},
        options_doc={"model-show-validator-members": True},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_model_show_validator_members_false(autodocument):
    result = [
        '',
        ".. py:pydantic_model:: ModelShowValidatorMembers",
        '   :module: target.configuration',
        '',
        '   ModelShowValidatorMembers.',
        '',
        '',
        '   .. py:pydantic_field:: ModelShowValidatorMembers.field',
        '      :module: target.configuration',
        '      :type: int',
        '      :value: 1',
        '',
        '      Field.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowValidatorMembers',
        options_app={"autodoc_pydantic_model_members": True,
                     "autodoc_pydantic_model_show_validator_members": False},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowValidatorMembers',
        options_app={"autodoc_pydantic_model_members": True},
        options_doc={"model-show-validator-members": False},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowValidatorMembers',
        options_app={"autodoc_pydantic_model_members": True,
                     "autodoc_pydantic_model_show_validator_members": True},
        options_doc={"model-show-validator-members": False},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_model_show_config_members_true(autodocument):
    result = [
        '',
        ".. py:pydantic_model:: ModelShowConfigMember",
        '   :module: target.configuration',
        '',
        '   ModelShowConfigMember.',
        '',
        '',
        '   .. py:pydantic_field:: ModelShowConfigMember.field',
        '      :module: target.configuration',
        '      :type: int',
        '      :value: 1',
        '',
        '      Field.',
        '',
        '',
        '   .. py:pydantic_config:: ModelShowConfigMember.Config()',
        '      :module: target.configuration',
        '',
        '      Config.',
        '',
        '',
        '      .. py:attribute:: ModelShowConfigMember.Config.allow_mutation',
        '         :module: target.configuration',
        '         :value: True',
        '']

    # explict global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowConfigMember',
        options_app={"autodoc_pydantic_model_members": True,
                     "autodoc_pydantic_model_show_config_member": True},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowConfigMember',
        options_app={"autodoc_pydantic_model_members": True},
        options_doc={"model-show-config-member": True},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowConfigMember',
        options_app={"autodoc_pydantic_model_members": True,
                     "autodoc_pydantic_model_show_config_member": False},
        options_doc={"model-show-config-member": True},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_model_show_config_members_false(autodocument):
    result = [
        '',
        ".. py:pydantic_model:: ModelShowConfigMember",
        '   :module: target.configuration',
        '',
        '   ModelShowConfigMember.',
        '',
        '',
        '   .. py:pydantic_field:: ModelShowConfigMember.field',
        '      :module: target.configuration',
        '      :type: int',
        '      :value: 1',
        '',
        '      Field.',
        '',
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowConfigMember',
        options_app={"autodoc_pydantic_model_members": True,
                     "autodoc_pydantic_model_show_config_member": False},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowConfigMember',
        options_app={"autodoc_pydantic_model_members": True},
        options_doc={"model-show-config-member": False},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowConfigMember',
        options_app={"autodoc_pydantic_model_members": True,
                     "autodoc_pydantic_model_show_config_member": True},
        options_doc={"model-show-config-member": False},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_model_signature_prefix(autodocument, parse_rst):
    """Tests pydantic_model directive.

    """

    # default
    result = [
        '',
        ".. py:pydantic_model:: ModelSignaturePrefix",
        '   :module: target.configuration',
        '',
        '   ModelSignaturePrefix.',
        ''
    ]

    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelSignaturePrefix',
        deactivate_all=True)
    assert result == actual

    # explicit value
    result = [
        '',
        ".. py:pydantic_model:: ModelSignaturePrefix",
        '   :module: target.configuration',
        '   :model-signature-prefix: foobar ',
        '',
        '   ModelSignaturePrefix.',
        ''
    ]

    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelSignaturePrefix',
        options_doc={"model-signature-prefix": "foobar "},
        deactivate_all=True)
    assert result == actual

    # explict empty
    result = [
        '',
        ".. py:pydantic_model:: ModelSignaturePrefix",
        '   :module: target.configuration',
        '   :model-signature-prefix: ',
        '',
        '   ModelSignaturePrefix.',
        ''
    ]

    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelSignaturePrefix',
        options_doc={"model-signature-prefix": ""},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_model_signature_prefix_directive(parse_rst):
    """Tests pydantic_model directive.

    """

    # default
    input_rst = [
        '',
        ".. py:pydantic_model:: ModelSignaturePrefix",
        '   :module: target.configuration',
        '',
        '   ModelSignaturePrefix.',
        ''
    ]

    doctree = parse_rst(input_rst)
    assert_node(doctree[1][0][0], [desc_annotation, "pydantic model "])

    # empty
    doctree = parse_rst(input_rst,
                        conf={"autodoc_pydantic_model_signature_prefix": ""})
    assert_node(doctree[1][0][0], [desc_annotation, "class "])

    # custom
    input_rst = [
        '',
        ".. py:pydantic_model:: ModelSignaturePrefix",
        '   :module: target.configuration',
        '   :model-signature-prefix: foobar',
        '',
        '   ModelSignaturePrefix.',
        ''
    ]

    doctree = parse_rst(input_rst)
    assert_node(doctree[1][0][0], [desc_annotation, "foobar "])
