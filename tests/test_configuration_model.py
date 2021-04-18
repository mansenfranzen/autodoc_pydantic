"""This module contains tests for all configuration properties.

"""


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


def test_autodoc_pydantic_model_show_validators_summary_true(autodocument):
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
        options_app={"autodoc_pydantic_model_show_validators_summary": True},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowValidatorsSummary',
        options_doc={"model-show-validators-summary": True},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowValidatorsSummary',
        options_app={"autodoc_pydantic_model_show_validators_summary": False},
        options_doc={"model-show-validators-summary": True},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_model_show_validators_summary_false(autodocument):
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
        options_app={"autodoc_pydantic_model_show_validators_summary": False},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowValidatorsSummary',
        options_doc={"model-show-validators-summary": False},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowValidatorsSummary',
        options_app={"autodoc_pydantic_model_show_validators_summary": True},
        options_doc={"model-show-validators-summary": False},
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
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelMemberOrder',
        options_app={"autodoc_pydantic_model_members": True,
                     "autodoc_pydantic_validator_show": True,
                     "autodoc_pydantic_config_show": True,
                     "autodoc_pydantic_model_member_order": "groupwise"},
        deactivate_all=True)
    assert result == actual


    # explict local
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelMemberOrder',
        options_app={"autodoc_pydantic_model_members": True,
                     "autodoc_pydantic_validator_show": True,
                     "autodoc_pydantic_config_show": True},
        options_doc={"member-order": "groupwise"},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelMemberOrder',
        options_app={"autodoc_pydantic_model_members": True,
                     "autodoc_pydantic_validator_show": True,
                     "autodoc_pydantic_config_show": True,
                     "autodoc_pydantic_model_member_order": "bysource"},
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
        options_app={"autodoc_pydantic_model_members": True,
                     "autodoc_pydantic_validator_show": True,
                     "autodoc_pydantic_config_show": True,
                     "autodoc_pydantic_model_member_order": "bysource"},
        deactivate_all=True)
    assert result == actual


    # explict local
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelMemberOrder',
        options_app={"autodoc_pydantic_model_members": True,
                     "autodoc_pydantic_validator_show": True,
                     "autodoc_pydantic_config_show": True},
        options_doc={"member-order": "bysource"},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelMemberOrder',
        options_app={"autodoc_pydantic_model_members": True,
                     "autodoc_pydantic_validator_show": True,
                     "autodoc_pydantic_config_show": True,
                     "autodoc_pydantic_model_member_order": "groupwise"},
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
        options_app={"autodoc_pydantic_model_members": True,
                     "autodoc_pydantic_validator_show": True,
                     "autodoc_pydantic_config_show": True,
                     "autodoc_pydantic_model_member_order": "alphabetical"},
        deactivate_all=True)
    assert result == actual


    # explict local
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelMemberOrder',
        options_app={"autodoc_pydantic_model_members": True,
                     "autodoc_pydantic_validator_show": True,
                     "autodoc_pydantic_config_show": True},
        options_doc={"member-order": "alphabetical"},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelMemberOrder',
        options_app={"autodoc_pydantic_model_members": True,
                     "autodoc_pydantic_validator_show": True,
                     "autodoc_pydantic_config_show": True,
                     "autodoc_pydantic_model_member_order": "groupwise"},
        options_doc={"member-order": "alphabetical"},
        deactivate_all=True)
    assert result == actual