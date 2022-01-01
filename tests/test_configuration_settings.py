"""This module contains tests for pydantic model configurations.

"""
import pydantic
from sphinx.addnodes import desc_annotation
from sphinx.testing.util import assert_node

from sphinxcontrib.autodoc_pydantic import PydanticSettingsDocumenter
from .compatability import desc_annotation_directive_prefix

KWARGS = dict(documenter=PydanticSettingsDocumenter.objtype,
              deactivate_all=True)

SETTING_MEMBER_ORDER = {
    "autodoc_pydantic_settings_members": True,
    "autodoc_pydantic_settings_show_validator_members": True,
    "autodoc_pydantic_settings_show_config_member": True}


def test_autodoc_pydantic_settings_show_json_true(autodocument):
    kwargs = dict(object_path='target.configuration.SettingsShowJson',
                  **KWARGS)

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
        options_app={"autodoc_pydantic_settings_show_json": True},
        **kwargs)
    assert actual == result

    # explicit local
    actual = autodocument(
        options_doc={"settings-show-json": True},
        **kwargs)
    assert actual == result

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_show_json": False},
        options_doc={"settings-show-json": True},
        **kwargs)
    assert actual == result


def test_autodoc_pydantic_settings_show_json_false(autodocument):
    kwargs = dict(object_path='target.configuration.SettingsShowJson',
                  **KWARGS)

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
        options_app={"autodoc_pydantic_settings_show_json": False},
        **kwargs)
    assert actual == result

    # explicit local
    actual = autodocument(
        options_doc={"settings-show-json": False},
        **kwargs)
    assert actual == result

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_show_json": True},
        options_doc={"settings-show-json": False},
        **kwargs)
    assert actual == result


def test_autodoc_pydantic_settings_show_config_summary_summary_true(autodocument):
    kwargs = dict(object_path='target.configuration.SettingsShowConfigSummary',
                  **KWARGS)

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
        options_app={"autodoc_pydantic_settings_show_config_summary": True},
        **kwargs)
    assert actual == result

    # explict local
    actual = autodocument(
        options_doc={"settings-show-config-summary": True},
        **kwargs)
    assert actual == result

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_show_config_summary": False},
        options_doc={"settings-show-config-summary": True},
        **kwargs)
    assert actual == result


def test_autodoc_pydantic_settings_show_config_summary_false(autodocument):
    kwargs = dict(object_path='target.configuration.SettingsShowConfigSummary',
                  **KWARGS)

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
        options_app={"autodoc_pydantic_settings_show_config_summary": False},
        **kwargs)
    assert actual == result

    # explict local
    actual = autodocument(
        options_doc={"settings-show-config-summary": False},
        **kwargs)
    assert actual == result

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_show_config_summary": True},
        options_doc={"settings-show-config-summary": False},
        **kwargs)
    assert actual == result


def test_autodoc_pydantic_settings_show_validator_summary_true(autodocument):
    kwargs = dict(
        object_path='target.configuration.SettingsShowValidatorsSummary',
        **KWARGS)

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
        options_app={"autodoc_pydantic_settings_show_validator_summary": True},
        **kwargs)
    assert result == actual

    # explict local
    actual = autodocument(
        options_doc={"settings-show-validator-summary": True},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_show_validators_summary": False},
        options_doc={"settings-show-validator-summary": True},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_settings_show_validator_summary_false(autodocument):
    kwargs = dict(
        object_path='target.configuration.SettingsShowValidatorsSummary',
        **KWARGS)

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
        options_app={"autodoc_pydantic_settings_show_validator_summary": False},
        **kwargs)
    assert result == actual

    # explict local
    actual = autodocument(
        options_doc={"settings-show-validator-summary": False},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_show_validators_summary": True},
        options_doc={"settings-show-validator-summary": False},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_settings_show_field_summary_true(autodocument):
    kwargs = dict(object_path='target.configuration.SettingsShowFieldSummary',
                  **KWARGS)

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
        options_app={"autodoc_pydantic_settings_show_field_summary": True},
        **kwargs)
    assert result == actual

    # explict local
    actual = autodocument(
        options_doc={"settings-show-field-summary": True},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_show_field_summary": False},
        options_doc={"settings-show-field-summary": True},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_settings_show_field_summary_false(autodocument):
    kwargs = dict(object_path='target.configuration.SettingsShowFieldSummary',
                  **KWARGS)

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
        options_app={"autodoc_pydantic_settings_show_field_summary": False},
        **kwargs)
    assert result == actual

    # explict local
    actual = autodocument(
        options_doc={"settings-show-field-summary": False},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_show_field_summary": True},
        options_doc={"settings-show-field-summary": False},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_settings_summary_list_order_alphabetical(
        autodocument):
    kwargs = dict(object_path='target.configuration.SettingsSummaryListOrder',
                  **KWARGS)
    enable = {"autodoc_pydantic_settings_show_validator_summary": True,
              "autodoc_pydantic_settings_show_field_summary": True}

    result = [
        '',
        '.. py:pydantic_settings:: SettingsSummaryListOrder',
        '   :module: target.configuration',
        '',
        '   SettingsSummaryListOrder.',
        '',
        '   :Fields:',
        '      - :py:obj:`field_a (int) <target.configuration.SettingsSummaryListOrder.field_a>`',
        '      - :py:obj:`field_b (int) <target.configuration.SettingsSummaryListOrder.field_b>`',
        '',
        '   :Validators:',
        '      - :py:obj:`validate_a <target.configuration.SettingsSummaryListOrder.validate_a>` » :py:obj:`field_a <target.configuration.SettingsSummaryListOrder.field_a>`',
        '      - :py:obj:`validate_b <target.configuration.SettingsSummaryListOrder.validate_b>` » :py:obj:`field_b <target.configuration.SettingsSummaryListOrder.field_b>`',
        ''
    ]

    # explict global
    actual = autodocument(
        options_app={
            "autodoc_pydantic_settings_summary_list_order": "alphabetical",
            **enable},
        **kwargs)
    assert result == actual

    # explict local
    actual = autodocument(
        options_app=enable,
        options_doc={"settings-summary-list-order": "alphabetical"},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_summary_list_order": "bysource",
                     **enable},
        options_doc={"settings-summary-list-order": "alphabetical"},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_settings_summary_list_order_bysource(autodocument):
    kwargs = dict(object_path='target.configuration.SettingsSummaryListOrder',
                  **KWARGS)
    enable = {"autodoc_pydantic_settings_show_validator_summary": True,
              "autodoc_pydantic_settings_show_field_summary": True}

    result = [
        '',
        '.. py:pydantic_settings:: SettingsSummaryListOrder',
        '   :module: target.configuration',
        '',
        '   SettingsSummaryListOrder.',
        '',
        '   :Fields:',
        '      - :py:obj:`field_b (int) <target.configuration.SettingsSummaryListOrder.field_b>`',
        '      - :py:obj:`field_a (int) <target.configuration.SettingsSummaryListOrder.field_a>`',
        '',
        '   :Validators:',
        '      - :py:obj:`validate_b <target.configuration.SettingsSummaryListOrder.validate_b>` » :py:obj:`field_b <target.configuration.SettingsSummaryListOrder.field_b>`',
        '      - :py:obj:`validate_a <target.configuration.SettingsSummaryListOrder.validate_a>` » :py:obj:`field_a <target.configuration.SettingsSummaryListOrder.field_a>`',

        ''
    ]

    # explict global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_summary_list_order": "bysource",
                     **enable},
        **kwargs)
    assert result == actual

    # explict local
    actual = autodocument(
        options_app=enable,
        options_doc={"settings-summary-list-order": "bysource"},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={
            "autodoc_pydantic_settings_summary_list_order": "alphabetical",
            **enable},
        options_doc={"settings-summary-list-order": "bysource"},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_settings_hide_paramlist_false(autodocument):
    kwargs = dict(object_path='target.configuration.SettingsHideParamList',
                  **KWARGS)

    if pydantic.version.VERSION[:3] >= "1.9":
        path_type = "Union[str, os.PathLike]"
    else:
        path_type = "Union[pathlib.Path, str]"

    env_file = f"_env_file: Optional[{path_type}] = '<object object>', "
    env_file_encoding = "_env_file_encoding: Optional[str] = None, "
    env_nested_delimiter = "_env_nested_delimiter: Optional[str] = None, "
    secret_dir = f"_secrets_dir: Optional[{path_type}] = None, "
    remaining = "*, field1: int = 5, field2: str = 'FooBar'"

    params = [env_file,
              env_file_encoding,
              env_nested_delimiter,
              secret_dir,
              remaining]

    if pydantic.version.VERSION[:3] <= "1.8":
        params.remove(env_nested_delimiter)

    if pydantic.version.VERSION[:3] <= "1.6":
        params.remove(secret_dir)

    if pydantic.version.VERSION[:3] <= "1.5":
        params.remove(env_file_encoding)

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
        options_app={"autodoc_pydantic_settings_hide_paramlist": False},
        **kwargs)
    assert result == actual

    # explict local
    actual = autodocument(
        options_doc={"settings-hide-paramlist": False},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_hide_paramlist": True},
        options_doc={"settings-hide-paramlist": False},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_settings_hide_paramlist_true(autodocument):
    kwargs = dict(object_path='target.configuration.SettingsHideParamList',
                  **KWARGS)

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
        options_app={"autodoc_pydantic_settings_hide_paramlist": True},
        **kwargs)
    assert result == actual

    # explict local
    actual = autodocument(
        options_doc={"settings-hide-paramlist": True},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_hide_paramlist": False},
        options_doc={"settings-hide-paramlist": True},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_settings_undoc_members_true(autodocument):
    kwargs = dict(object_path='target.configuration.SettingsUndocMembers',
                  **KWARGS)
    enable = {"autodoc_pydantic_settings_members": True}

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
        '',
        '',
        '   .. py:pydantic_field:: SettingsUndocMembers.field2',
        '      :module: target.configuration',
        '      :type: str',
        ''
    ]

    # explict global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_undoc_members": True, **enable},
        **kwargs)
    assert result == actual

    # explict local
    actual = autodocument(
        options_app=enable,
        options_doc={"undoc-members": None},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_undoc_members": False, **enable},
        options_doc={"undoc-members": None},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_settings_undoc_members_false(autodocument):
    kwargs = dict(object_path='target.configuration.SettingsUndocMembers',
                  **KWARGS)
    enable = {"autodoc_pydantic_settings_members": True}

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
        options_app={"autodoc_pydantic_settings_undoc_members": False, **enable},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_settings_members_true(autodocument):
    kwargs = dict(object_path='target.configuration.SettingsMembers',
                  **KWARGS)

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
        '',
        '      Doc field 1',
        '',
        '',
        '   .. py:pydantic_field:: SettingsMembers.field2',
        '      :module: target.configuration',
        '      :type: str',
        '',
        '      Doc field 2',
        ''
    ]

    # explict global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_members": True},
        **kwargs)
    assert result == actual

    # explict local
    actual = autodocument(
        options_doc={"members": None},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_members": False},
        options_doc={"members": None},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_settings_members_false(autodocument):
    kwargs = dict(object_path='target.configuration.SettingsMembers',
                  **KWARGS)

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
        options_app={"autodoc_pydantic_settings_members": False},
        **kwargs)
    assert result == actual

    # explict local
    actual = autodocument(
        options_doc={"members": "False"},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_members": True},
        options_doc={"members": "False"},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_settings_member_order_groupwise(autodocument):
    kwargs = dict(object_path='target.configuration.SettingsMemberOrder',
                  **KWARGS)

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
        options_app={"autodoc_pydantic_settings_member_order": "groupwise",
                     **SETTING_MEMBER_ORDER},
        **kwargs)
    assert result == actual

    # explict local
    actual = autodocument(
        options_app=SETTING_MEMBER_ORDER,
        options_doc={"member-order": "groupwise"},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_member_order": "bysource",
                     **SETTING_MEMBER_ORDER},
        options_doc={"member-order": "groupwise"},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_settings_member_order_bysource(autodocument):
    kwargs = dict(object_path='target.configuration.SettingsMemberOrder',
                  **KWARGS)

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
        '',
        '      Field.',
        ''
    ]

    # explict global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_member_order": "bysource",
                     **SETTING_MEMBER_ORDER},
        **kwargs)
    assert result == actual

    # explict local
    actual = autodocument(
        options_app=SETTING_MEMBER_ORDER,
        options_doc={"member-order": "bysource"},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_member_order": "groupwise",
                     **SETTING_MEMBER_ORDER},
        options_doc={"member-order": "bysource"},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_settings_member_order_alphabetical(autodocument):
    kwargs = dict(object_path='target.configuration.SettingsMemberOrder',
                  **KWARGS)

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
        '',
        '      Field.',
        ''
    ]

    # explict global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_member_order": "alphabetical",
                     **SETTING_MEMBER_ORDER},
        **kwargs)
    assert result == actual

    # explict local
    actual = autodocument(
        options_app=SETTING_MEMBER_ORDER,
        options_doc={"member-order": "alphabetical"},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_member_order": "groupwise",
                     **SETTING_MEMBER_ORDER},
        options_doc={"member-order": "alphabetical"},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_settings_show_validator_members_true(autodocument):
    kwargs = dict(object_path='target.configuration.SettingsShowValidatorMembers',
                  **KWARGS)

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
        options_app={"autodoc_pydantic_settings_members": True,
                     "autodoc_pydantic_settings_show_validator_members": True},
        **kwargs)
    assert result == actual

    # explict local
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_members": True},
        options_doc={"settings-show-validator-members": True},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_members": True,
                     "autodoc_pydantic_settings_show_validator_members": False},
        options_doc={"settings-show-validator-members": True},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_settings_show_validator_members_false(autodocument):
    kwargs = dict(object_path='target.configuration.SettingsShowValidatorMembers',
                  **KWARGS)

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
        '',
        '      Field.',
        ''
    ]

    # explict global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_members": True,
                     "autodoc_pydantic_settings_show_validator_members": False},
        **kwargs)
    assert result == actual

    # explict local
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_members": True},
        options_doc={"settings-show-validator-members": False},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_members": True,
                     "autodoc_pydantic_settings_show_validator_members": True},
        options_doc={"settings-show-validator-members": False},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_settings_show_config_members_true(autodocument):
    kwargs = dict(object_path='target.configuration.SettingsShowConfigMember',
                  **KWARGS)
    enable = {"autodoc_pydantic_settings_members": True,
              "autodoc_pydantic_config_members": True}

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
        options_app={"autodoc_pydantic_settings_show_config_member": True,
                     **enable},
        **kwargs)
    assert result == actual

    # explict local
    actual = autodocument(
        options_app=enable,
        options_doc={"settings-show-config-member": True},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_show_config_member": False,
                     **enable},
        options_doc={"settings-show-config-member": True},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_settings_show_config_members_false(autodocument):
    kwargs = dict(object_path='target.configuration.SettingsShowConfigMember',
                  **KWARGS)
    enable = {"autodoc_pydantic_settings_members": True,
              "autodoc_pydantic_config_members": True}

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
        '',
        '      Field.',
        '',
    ]

    # explict global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_show_config_member": False,
                     **enable},
        **kwargs)
    assert result == actual

    # explict local
    actual = autodocument(
        options_app=enable,
        options_doc={"settings-show-config-member": False},
        **kwargs)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        options_app={"autodoc_pydantic_settings_show_config_member": True,
                     **enable},
        options_doc={"settings-show-config-member": False},
        **kwargs)
    assert result == actual


def test_autodoc_pydantic_settings_signature_prefix(autodocument, parse_rst):
    """Tests pydantic_settings directive.

    """
    kwargs = dict(object_path='target.configuration.SettingsSignaturePrefix',
                  **KWARGS)

    # default
    result = [
        '',
        ".. py:pydantic_settings:: SettingsSignaturePrefix",
        '   :module: target.configuration',
        '',
        '   SettingsSignaturePrefix.',
        ''
    ]

    actual = autodocument(**kwargs)
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
        options_doc={"settings-signature-prefix": "foobar "},
        **kwargs)
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
        options_doc={"settings-signature-prefix": ""},
        **kwargs)
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
    prefix = desc_annotation_directive_prefix("pydantic settings")
    assert_node(doctree[1][0][0], [desc_annotation, prefix])

    # empty
    doctree = parse_rst(input_rst,
                        conf={"autodoc_pydantic_settings_signature_prefix": ""})
    prefix = desc_annotation_directive_prefix("class")
    assert_node(doctree[1][0][0], [desc_annotation, prefix])

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
    prefix = desc_annotation_directive_prefix("foobar")
    assert_node(doctree[1][0][0], [desc_annotation, prefix])
