"""This module contains tests for pydantic settings configurations.

"""
import pydantic
from sphinx.addnodes import desc_annotation
from sphinx.testing.util import assert_node

SETTING_MEMBER_ORDER = {
    "autodoc_pydantic_settings_members": True,
    "autodoc_pydantic_settings_show_validator_members": True,
    "autodoc_pydantic_settings_show_config_member": True}


def test_autodoc_pydantic_settings_show_json_true(autodocument):
    result = [
        '',
        '.. py:pydantic_settings:: SettingsShowJson',
        '   :module: target.configuration',
        '',
        '   SettingsShowJson.',
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
        '         "title": "SettingsShowJson",',
        '         "description": "SettingsShowJson.",',
        '         "type": "object",',
        '         "properties": {},',
        '         "additionalProperties": false',
        '      }',
        '',
        '   .. raw:: html',
        '',
        '      </details></p>',
        '',
        '']

    # explicit global
    actual = autodocument(
        documenter='pydantic_settings',
        options_app={"autodoc_pydantic_settings_show_json": True},
        object_path='target.configuration.SettingsShowJson')
    assert actual == result

    # explicit local
    actual = autodocument(documenter='pydantic_settings',
                          options_doc={"settings-show-json": True},
                          object_path='target.configuration.SettingsShowJson')
    assert actual == result

    # explicit local overwrite global
    actual = autodocument(documenter='pydantic_settings',
                          options_app={
                              "autodoc_pydantic_settings_show_json": False},
                          options_doc={"settings-show-json": True},
                          object_path='target.configuration.SettingsShowJson')
    assert actual == result


def test_autodoc_pydantic_settings_show_json_false(autodocument):
    result = [
        '',
        '.. py:pydantic_settings:: SettingsShowJson',
        '   :module: target.configuration',
        '',
        '   SettingsShowJson.',
        ''
    ]

    # explicit global
    actual = autodocument(
        documenter='pydantic_settings',
        options_app={"autodoc_pydantic_settings_show_json": False},
        object_path='target.configuration.SettingsShowJson')
    assert actual == result

    # explicit local
    actual = autodocument(
        documenter='pydantic_settings',
        options_doc={"settings-show-json": False},
        object_path='target.configuration.SettingsShowJson')
    assert actual == result

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_settings',
        options_app={"autodoc_pydantic_settings_show_json": True},
        options_doc={"settings-show-json": False},
        object_path='target.configuration.SettingsShowJson')
    assert actual == result


def test_autodoc_pydantic_settings_show_config_summary_summary_true(autodocument):
    result = [
        '',
        '.. py:pydantic_settings:: SettingsShowConfigSummary',
        '   :module: target.configuration',
        '',
        '   SettingsShowConfigSummary.',
        '',
        '   :Config:',
        '      - **allow_mutation**: *bool = True*',
        '      - **title**: *str = FooBar*',
        '']

    # explict global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowConfigSummary',
        options_app={"autodoc_pydantic_settings_show_config_summary": True},
        deactivate_all=True)
    assert actual == result

    # explict local
    actual = autodocument(documenter='pydantic_settings',
                          object_path='target.configuration.SettingsShowConfigSummary',
                          options_doc={"settings-show-config-summary": True},
                          deactivate_all=True)
    assert actual == result

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowConfigSummary',
        options_app={"autodoc_pydantic_settings_show_config_summary": False},
        options_doc={"settings-show-config-summary": True},
        deactivate_all=True)
    assert actual == result


def test_autodoc_pydantic_settings_show_config_summary_false(autodocument):
    result = [
        '',
        '.. py:pydantic_settings:: SettingsShowConfigSummary',
        '   :module: target.configuration',
        '',
        '   SettingsShowConfigSummary.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowConfigSummary',
        options_app={"autodoc_pydantic_settings_show_config_summary": False},
        deactivate_all=True)
    assert actual == result

    # explict local
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowConfigSummary',
        options_doc={"settings-show-config-summary": False},
        deactivate_all=True)
    assert actual == result

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowConfigSummary',
        options_app={"autodoc_pydantic_settings_show_config_summary": True},
        options_doc={"settings-show-config-summary": False},
        deactivate_all=True)
    assert actual == result


def test_autodoc_pydantic_settings_show_validator_summary_true(autodocument):
    result = [
        '',
        '.. py:pydantic_settings:: SettingsShowValidatorsSummary',
        '   :module: target.configuration',
        '',
        '   SettingsShowValidatorsSummary.',
        '',
        '   :Validators:',
        '      - :py:obj:`check <target.configuration.SettingsShowValidatorsSummary.check>` » :py:obj:`field <target.configuration.SettingsShowValidatorsSummary.field>`',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowValidatorsSummary',
        options_app={"autodoc_pydantic_settings_show_validator_summary": True},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowValidatorsSummary',
        options_doc={"settings-show-validator-summary": True},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowValidatorsSummary',
        options_app={"autodoc_pydantic_settings_show_validators_summary": False},
        options_doc={"settings-show-validator-summary": True},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_settings_show_validator_summary_false(autodocument):
    result = [
        '',
        '.. py:pydantic_settings:: SettingsShowValidatorsSummary',
        '   :module: target.configuration',
        '',
        '   SettingsShowValidatorsSummary.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowValidatorsSummary',
        options_app={"autodoc_pydantic_settings_show_validator_summary": False},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowValidatorsSummary',
        options_doc={"settings-show-validator-summary": False},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowValidatorsSummary',
        options_app={"autodoc_pydantic_settings_show_validators_summary": True},
        options_doc={"settings-show-validator-summary": False},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_settings_show_field_summary_true(autodocument):
    result = [
        '',
        '.. py:pydantic_settings:: SettingsShowFieldSummary',
        '   :module: target.configuration',
        '',
        '   SettingsShowFieldSummary.',
        '',
        '   :Fields:',
        '      - :py:obj:`field1 (int) <target.configuration.SettingsShowFieldSummary.field1>`',
        '      - :py:obj:`field2 (str) <target.configuration.SettingsShowFieldSummary.field2>`',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowFieldSummary',
        options_app={"autodoc_pydantic_settings_show_field_summary": True},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowFieldSummary',
        options_doc={"settings-show-field-summary": True},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowFieldSummary',
        options_app={"autodoc_pydantic_settings_show_field_summary": False},
        options_doc={"settings-show-field-summary": True},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_settings_show_field_summary_false(autodocument):
    result = [
        '',
        '.. py:pydantic_settings:: SettingsShowFieldSummary',
        '   :module: target.configuration',
        '',
        '   SettingsShowFieldSummary.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowFieldSummary',
        options_app={"autodoc_pydantic_settings_show_field_summary": False},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowFieldSummary',
        options_doc={"settings-show-field-summary": False},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowFieldSummary',
        options_app={"autodoc_pydantic_settings_show_field_summary": True},
        options_doc={"settings-show-field-summary": False},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_settings_hide_paramlist_false(autodocument):

    params = [
        "_env_file: Optional[Union[pathlib.Path, str]] = '<object object>', ",
        "_env_file_encoding: Optional[str] = None, ",
        "_secrets_dir: Optional[Union[pathlib.Path, str]] = None, ",
        "*, field1: int = 5, field2: str = 'FooBar'"]

    if pydantic.version.VERSION[:3] <= "1.6":
        params.remove("_secrets_dir: Optional[Union[pathlib.Path, str]] = None, ")

    if pydantic.version.VERSION[:3] <= "1.5":
        params.remove("_env_file_encoding: Optional[str] = None, ")

    params = "".join(params)

    result = [
        '',
        f".. py:pydantic_settings:: SettingsHideParamList({params})",
        '   :module: target.configuration',
        '',
        '   SettingsHideParamList.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsHideParamList',
        options_app={"autodoc_pydantic_settings_hide_paramlist": False},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsHideParamList',
        options_doc={"settings-hide-paramlist": False},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsHideParamList',
        options_app={"autodoc_pydantic_settings_hide_paramlist": True},
        options_doc={"settings-hide-paramlist": False},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_settings_hide_paramlist_true(autodocument):
    result = [
        '',
        '.. py:pydantic_settings:: SettingsHideParamList',
        '   :module: target.configuration',
        '',
        '   SettingsHideParamList.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsHideParamList',
        options_app={"autodoc_pydantic_settings_hide_paramlist": True},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsHideParamList',
        options_doc={"settings-hide-paramlist": True},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsHideParamList',
        options_app={"autodoc_pydantic_settings_hide_paramlist": False},
        options_doc={"settings-hide-paramlist": True},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_settings_undoc_members_true(autodocument):
    result = [
        '',
        ".. py:pydantic_settings:: SettingsUndocMembers",
        '   :module: target.configuration',
        '',
        '   SettingsUndocMembers.',
        '',
        '',
        '   .. py:pydantic_field:: SettingsUndocMembers.field1',
        '      :module: target.configuration',
        '      :type: int',
        '      :value: 5',
        '',
        '',
        '   .. py:pydantic_field:: SettingsUndocMembers.field2',
        '      :module: target.configuration',
        '      :type: str',
        "      :value: 'FooBar'",
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsUndocMembers',
        options_app={"autodoc_pydantic_settings_undoc_members": True,
                     "autodoc_pydantic_settings_members": True},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsUndocMembers',
        options_app={"autodoc_pydantic_settings_members": True},
        options_doc={"undoc-members": None},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsUndocMembers',
        options_app={"autodoc_pydantic_settings_undoc_members": False,
                     "autodoc_pydantic_settings_members": True},
        options_doc={"undoc-members": None},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_settings_undoc_members_false(autodocument):
    result = [
        '',
        ".. py:pydantic_settings:: SettingsUndocMembers",
        '   :module: target.configuration',
        '',
        '   SettingsUndocMembers.',
        '',
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsUndocMembers',
        options_app={"autodoc_pydantic_settings_undoc_members": False,
                     "autodoc_pydantic_settings_members": True},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_settings_members_true(autodocument):
    result = [
        '',
        ".. py:pydantic_settings:: SettingsMembers",
        '   :module: target.configuration',
        '',
        '   SettingsMembers.',
        '',
        '',
        '   .. py:pydantic_field:: SettingsMembers.field1',
        '      :module: target.configuration',
        '      :type: int',
        '      :value: 5',
        '',
        '      Doc field 1',
        '',
        '',
        '   .. py:pydantic_field:: SettingsMembers.field2',
        '      :module: target.configuration',
        '      :type: str',
        "      :value: 'FooBar'",
        '',
        '      Doc field 2',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsMembers',
        options_app={"autodoc_pydantic_settings_members": True},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsMembers',
        options_doc={"members": None},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsMembers',
        options_app={"autodoc_pydantic_settings_members": False},
        options_doc={"members": None},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_settings_members_false(autodocument):
    result = [
        '',
        ".. py:pydantic_settings:: SettingsMembers",
        '   :module: target.configuration',
        '',
        '   SettingsMembers.',
        '',
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsMembers',
        options_app={"autodoc_pydantic_settings_members": False},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsMembers',
        options_doc={"members": "False"},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsMembers',
        options_app={"autodoc_pydantic_settings_members": True},
        options_doc={"members": "False"},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_settings_member_order_groupwise(autodocument):
    result = [
        '',
        ".. py:pydantic_settings:: SettingsMemberOrder",
        '   :module: target.configuration',
        '',
        '   SettingsMemberOrder.',
        '',
        '',
        '   .. py:pydantic_field:: SettingsMemberOrder.field',
        '      :module: target.configuration',
        '      :type: int',
        '      :value: 1',
        '',
        '      Field.',
        '',
        '',
        '   .. py:pydantic_validator:: SettingsMemberOrder.dummy',
        '      :module: target.configuration',
        '      :classmethod:',
        '',
        '      Check.',
        '',
        '',
        '   .. py:pydantic_config:: SettingsMemberOrder.Config()',
        '      :module: target.configuration',
        '',
        '      Config.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsMemberOrder',
        options_app={"autodoc_pydantic_settings_member_order": "groupwise",
                     **SETTING_MEMBER_ORDER},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsMemberOrder',
        options_app=SETTING_MEMBER_ORDER,
        options_doc={"member-order": "groupwise"},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsMemberOrder',
        options_app={"autodoc_pydantic_settings_member_order": "bysource",
                     **SETTING_MEMBER_ORDER},
        options_doc={"member-order": "groupwise"},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_settings_member_order_bysource(autodocument):
    result = [
        '',
        ".. py:pydantic_settings:: SettingsMemberOrder",
        '   :module: target.configuration',
        '',
        '   SettingsMemberOrder.',
        '',
        '',
        '   .. py:pydantic_validator:: SettingsMemberOrder.dummy',
        '      :module: target.configuration',
        '      :classmethod:',
        '',
        '      Check.',
        '',
        '',
        '   .. py:pydantic_config:: SettingsMemberOrder.Config()',
        '      :module: target.configuration',
        '',
        '      Config.',
        '',
        '',
        '   .. py:pydantic_field:: SettingsMemberOrder.field',
        '      :module: target.configuration',
        '      :type: int',
        '      :value: 1',
        '',
        '      Field.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsMemberOrder',
        options_app={"autodoc_pydantic_settings_member_order": "bysource",
                     **SETTING_MEMBER_ORDER},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsMemberOrder',
        options_app=SETTING_MEMBER_ORDER,
        options_doc={"member-order": "bysource"},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsMemberOrder',
        options_app={"autodoc_pydantic_settings_member_order": "groupwise",
                     **SETTING_MEMBER_ORDER},
        options_doc={"member-order": "bysource"},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_settings_member_order_alphabetical(autodocument):
    result = [
        '',
        ".. py:pydantic_settings:: SettingsMemberOrder",
        '   :module: target.configuration',
        '',
        '   SettingsMemberOrder.',
        '',
        '',
        '   .. py:pydantic_config:: SettingsMemberOrder.Config()',
        '      :module: target.configuration',
        '',
        '      Config.',
        '',
        '',
        '   .. py:pydantic_validator:: SettingsMemberOrder.dummy',
        '      :module: target.configuration',
        '      :classmethod:',
        '',
        '      Check.',
        '',
        '',
        '   .. py:pydantic_field:: SettingsMemberOrder.field',
        '      :module: target.configuration',
        '      :type: int',
        '      :value: 1',
        '',
        '      Field.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsMemberOrder',
        options_app={"autodoc_pydantic_settings_member_order": "alphabetical",
                     **SETTING_MEMBER_ORDER},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsMemberOrder',
        options_app=SETTING_MEMBER_ORDER,
        options_doc={"member-order": "alphabetical"},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsMemberOrder',
        options_app={"autodoc_pydantic_settings_member_order": "groupwise",
                     **SETTING_MEMBER_ORDER},
        options_doc={"member-order": "alphabetical"},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_settings_show_validator_members_true(autodocument):
    result = [
        '',
        ".. py:pydantic_settings:: SettingsShowValidatorMembers",
        '   :module: target.configuration',
        '',
        '   SettingsShowValidatorMembers.',
        '',
        '',
        '   .. py:pydantic_field:: SettingsShowValidatorMembers.field',
        '      :module: target.configuration',
        '      :type: int',
        '      :value: 1',
        '',
        '      Field.',
        '',
        '',
        '   .. py:pydantic_validator:: SettingsShowValidatorMembers.dummy',
        '      :module: target.configuration',
        '      :classmethod:',
        '',
        '      Check.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowValidatorMembers',
        options_app={"autodoc_pydantic_settings_members": True,
                     "autodoc_pydantic_settings_show_validator_members": True},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowValidatorMembers',
        options_app={"autodoc_pydantic_settings_members": True},
        options_doc={"settings-show-validator-members": True},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowValidatorMembers',
        options_app={"autodoc_pydantic_settings_members": True,
                     "autodoc_pydantic_settings_show_validator_members": False},
        options_doc={"settings-show-validator-members": True},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_settings_show_validator_members_false(autodocument):
    result = [
        '',
        ".. py:pydantic_settings:: SettingsShowValidatorMembers",
        '   :module: target.configuration',
        '',
        '   SettingsShowValidatorMembers.',
        '',
        '',
        '   .. py:pydantic_field:: SettingsShowValidatorMembers.field',
        '      :module: target.configuration',
        '      :type: int',
        '      :value: 1',
        '',
        '      Field.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowValidatorMembers',
        options_app={"autodoc_pydantic_settings_members": True,
                     "autodoc_pydantic_settings_show_validator_members": False},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowValidatorMembers',
        options_app={"autodoc_pydantic_settings_members": True},
        options_doc={"settings-show-validator-members": False},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowValidatorMembers',
        options_app={"autodoc_pydantic_settings_members": True,
                     "autodoc_pydantic_settings_show_validator_members": True},
        options_doc={"settings-show-validator-members": False},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_settings_show_config_members_true(autodocument):
    result = [
        '',
        ".. py:pydantic_settings:: SettingsShowConfigMember",
        '   :module: target.configuration',
        '',
        '   SettingsShowConfigMember.',
        '',
        '',
        '   .. py:pydantic_field:: SettingsShowConfigMember.field',
        '      :module: target.configuration',
        '      :type: int',
        '      :value: 1',
        '',
        '      Field.',
        '',
        '',
        '   .. py:pydantic_config:: SettingsShowConfigMember.Config()',
        '      :module: target.configuration',
        '',
        '      Config.',
        '',
        '',
        '      .. py:attribute:: SettingsShowConfigMember.Config.allow_mutation',
        '         :module: target.configuration',
        '         :value: True',
        '']

    # explict global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowConfigMember',
        options_app={"autodoc_pydantic_settings_members": True,
                     "autodoc_pydantic_settings_show_config_member": True,
                     "autodoc_pydantic_config_members": True},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowConfigMember',
        options_app={"autodoc_pydantic_settings_members": True,
                     "autodoc_pydantic_config_members": True},
        options_doc={"settings-show-config-member": True},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowConfigMember',
        options_app={"autodoc_pydantic_settings_members": True,
                     "autodoc_pydantic_settings_show_config_member": False,
                     "autodoc_pydantic_config_members": True},
        options_doc={"settings-show-config-member": True},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_settings_show_config_members_false(autodocument):
    result = [
        '',
        ".. py:pydantic_settings:: SettingsShowConfigMember",
        '   :module: target.configuration',
        '',
        '   SettingsShowConfigMember.',
        '',
        '',
        '   .. py:pydantic_field:: SettingsShowConfigMember.field',
        '      :module: target.configuration',
        '      :type: int',
        '      :value: 1',
        '',
        '      Field.',
        '',
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowConfigMember',
        options_app={"autodoc_pydantic_settings_members": True,
                     "autodoc_pydantic_settings_show_config_member": False},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowConfigMember',
        options_app={"autodoc_pydantic_settings_members": True},
        options_doc={"settings-show-config-member": False},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsShowConfigMember',
        options_app={"autodoc_pydantic_settings_members": True,
                     "autodoc_pydantic_settings_show_config_member": True},
        options_doc={"settings-show-config-member": False},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_settings_signature_prefix(autodocument, parse_rst):
    """Tests pydantic_settings directive.

    """

    # default
    result = [
        '',
        ".. py:pydantic_settings:: SettingsSignaturePrefix",
        '   :module: target.configuration',
        '',
        '   SettingsSignaturePrefix.',
        ''
    ]

    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsSignaturePrefix',
        deactivate_all=True)
    assert result == actual

    # explicit value
    result = [
        '',
        ".. py:pydantic_settings:: SettingsSignaturePrefix",
        '   :module: target.configuration',
        '   :settings-signature-prefix: foobar ',
        '',
        '   SettingsSignaturePrefix.',
        ''
    ]

    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsSignaturePrefix',
        options_doc={"settings-signature-prefix": "foobar "},
        deactivate_all=True)
    assert result == actual

    # explict empty
    result = [
        '',
        ".. py:pydantic_settings:: SettingsSignaturePrefix",
        '   :module: target.configuration',
        '   :settings-signature-prefix: ',
        '',
        '   SettingsSignaturePrefix.',
        ''
    ]

    actual = autodocument(
        documenter='pydantic_settings',
        object_path='target.configuration.SettingsSignaturePrefix',
        options_doc={"settings-signature-prefix": ""},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_settings_signature_prefix_directive(parse_rst):
    """Tests pydantic_settings directive.

    """

    # default
    input_rst = [
        '',
        ".. py:pydantic_settings:: SettingsSignaturePrefix",
        '   :module: target.configuration',
        '',
        '   SettingsSignaturePrefix.',
        ''
    ]

    doctree = parse_rst(input_rst)
    assert_node(doctree[1][0][0], [desc_annotation, "pydantic settings "])

    # empty
    doctree = parse_rst(input_rst,
                        conf={"autodoc_pydantic_settings_signature_prefix": ""})
    assert_node(doctree[1][0][0], [desc_annotation, "class "])

    # custom
    input_rst = [
        '',
        ".. py:pydantic_settings:: SettingsSignaturePrefix",
        '   :module: target.configuration',
        '   :settings-signature-prefix: foobar',
        '',
        '   SettingsSignaturePrefix.',
        ''
    ]

    doctree = parse_rst(input_rst)
    assert_node(doctree[1][0][0], [desc_annotation, "foobar "])