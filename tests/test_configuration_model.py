import pytest
from conftest import do_autodoc


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