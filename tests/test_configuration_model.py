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


def test_autodoc_pydantic_model_show_config_true(autodocument):
    result = [
        '',
        '.. py:pydantic_model:: ModelShowConfig',
        '   :module: target.configuration',
        '',
        '   ModelShowConfig.',
        '',
        '   :Config:',
        '      - **allow_mutation**: *bool = True*',
        '      - **title**: *str = FooBar*',
        '']

    # explict global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowConfig',
        options_app={"autodoc_pydantic_model_show_config": True},
        deactivate_all=True)
    assert actual == result

    # explict local
    actual = autodocument(documenter='pydantic_model',
                          object_path='target.configuration.ModelShowConfig',
                          options_doc={"model-show-config": True},
                          deactivate_all=True)
    assert actual == result

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowConfig',
        options_app={"autodoc_pydantic_model_show_config": False},
        options_doc={"model-show-config": True},
        deactivate_all=True)
    assert actual == result


def test_autodoc_pydantic_model_show_config_false(autodocument):
    result = [
        '',
        '.. py:pydantic_model:: ModelShowConfig',
        '   :module: target.configuration',
        '',
        '   ModelShowConfig.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowConfig',
        options_app={"autodoc_pydantic_model_show_config": False},
        deactivate_all=True)
    assert actual == result

    # explict local
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowConfig',
        options_doc={"model-show-config": False},
        deactivate_all=True)
    assert actual == result

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowConfig',
        options_app={"autodoc_pydantic_model_show_config": True},
        options_doc={"model-show-config": False},
        deactivate_all=True)
    assert actual == result


def test_autodoc_pydantic_model_show_validators_true(autodocument):
    result = [
        '',
        '.. py:pydantic_model:: ModelShowValidators',
        '   :module: target.configuration',
        '',
        '   ModelShowValidators.',
        '',
        '   :Validators:',
        '      - :py:obj:`check <target.configuration.ModelShowValidators.check>` » :py:obj:`field <target.configuration.ModelShowValidators.field>`',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowValidators',
        options_app={"autodoc_pydantic_model_show_validators": True},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowValidators',
        options_doc={"model-show-validators": True},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowValidators',
        options_app={"autodoc_pydantic_model_show_validators": False},
        options_doc={"model-show-validators": True},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_model_show_validators_false(autodocument):
    result = [
        '',
        '.. py:pydantic_model:: ModelShowValidators',
        '   :module: target.configuration',
        '',
        '   ModelShowValidators.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowValidators',
        options_app={"autodoc_pydantic_model_show_validators": False},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowValidators',
        options_doc={"model-show-validators": False},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowValidators',
        options_app={"autodoc_pydantic_model_show_validators": True},
        options_doc={"model-show-validators": False},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_model_show_paramlist_true(autodocument):
    result = [
        '',
        ".. py:pydantic_model:: ModelShowParamList(*, field1: int = 5, field2: str = 'FooBar')",
        '   :module: target.configuration',
        '',
        '   ModelShowParamList.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowParamList',
        options_app={"autodoc_pydantic_model_show_paramlist": True},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowParamList',
        options_doc={"model-show-paramlist": True},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowParamList',
        options_app={"autodoc_pydantic_model_show_paramlist": False},
        options_doc={"model-show-paramlist": True},
        deactivate_all=True)
    assert result == actual


def test_autodoc_pydantic_model_show_paramlist_false(autodocument):
    result = [
        '',
        '.. py:pydantic_model:: ModelShowParamList',
        '   :module: target.configuration',
        '',
        '   ModelShowParamList.',
        ''
    ]

    # explict global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowParamList',
        options_app={"autodoc_pydantic_model_show_paramlist": False},
        deactivate_all=True)
    assert result == actual

    # explict local
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowParamList',
        options_doc={"model-show-paramlist": False},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelShowParamList',
        options_app={"autodoc_pydantic_model_show_paramlist": True},
        options_doc={"model-show-paramlist": False},
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
        options_doc={"hide-members": True},
        deactivate_all=True)
    assert result == actual

    # explicit local overwrite global
    actual = autodocument(
        documenter='pydantic_model',
        object_path='target.configuration.ModelMembers',
        options_app={"autodoc_pydantic_model_members": True},
        options_doc={"hide-members": True},
        deactivate_all=True)
    assert result == actual