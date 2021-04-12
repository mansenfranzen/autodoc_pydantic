"""This module contains end to end example tests.

"""

def test_model_plain(autodocument):
    options_app = dict(autodoc_pydantic_model_show_json=False)
    actual = autodocument(documenter='pydantic_model',
                          object_path='target.model.PlainModel',
                          options_app=options_app)

    assert actual == [
        '',
        '.. py:pydantic_model:: PlainModel',
        '   :module: target.model',
        '',
        '   Model Plain.',
        ''
    ]

def test_model_with_field(autodocument):
    options_app = dict(autodoc_pydantic_model_show_json=False)
    options_doc = dict(members=None)
    actual = autodocument(documenter='pydantic_model',
                          object_path='target.model.ModelWithField',
                          options_doc=options_doc,
                          options_app=options_app)

    assert actual == [
        '',
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
        ''
    ]


def test_model_with_field_validator(autodocument):
    options_app = dict(autodoc_pydantic_model_show_json=False)
    options_doc = dict(members=None)
    actual = autodocument(documenter='pydantic_model',
                          object_path='target.model.ModelWithFieldValidator',
                          options_doc=options_doc,
                          options_app=options_app)

    assert actual == [
        '',
        '.. py:pydantic_model:: ModelWithFieldValidator',
        '   :module: target.model',
        '',
        '   Model With Field Validator.',
        '',
        '   :Validators:',
        '      - :py:obj:`is_integer <target.model.ModelWithFieldValidator.is_integer>` » :py:obj:`field <target.model.ModelWithFieldValidator.field>`',
        '',
        '   .. py:pydantic_field:: ModelWithFieldValidator.field',
        '      :module: target.model',
        '      :type: int',
        '      :value: 1',
        '',
        '      Doc field',
        '',
        '      :Validated by:',
        '         - :py:obj:`is_integer <target.model.ModelWithFieldValidator.is_integer>`',
        '',
        '   .. py:pydantic_validator:: ModelWithFieldValidator.is_integer',
        '      :module: target.model',
        '      :classmethod:',
        '',
        '      Doc validator.',
        '',
        '      :Validates:',
        '         - :py:obj:`field <target.model.ModelWithFieldValidator.field>`',
        ''
    ]


def test_model_with_config(autodocument):
    options_app = dict(autodoc_pydantic_model_show_json=False)
    options_doc = dict(members=None)
    actual = autodocument(documenter='pydantic_model',
                          object_path='target.model.ModelWithConfig',
                          options_doc=options_doc,
                          options_app=options_app)

    assert actual == [
        '',
        '.. py:pydantic_model:: ModelWithConfig',
        '   :module: target.model',
        '',
        '   Model with Config.',
        '',
        '   :Config:',
        '      - **allow_mutation**: *bool = True*',
        '',
        '',
        '   .. py:pydantic_config:: ModelWithConfig.Config()',
        '      :module: target.model',
        '',
        '      With Doc String.',
        '',
        '',
        '      .. py:attribute:: ModelWithConfig.Config.allow_mutation',
        '         :module: target.model',
        '         :value: True',
        '',
        '         FooBar.',
        '']


def test_model_plain_show_json(autodocument):
    actual = autodocument(documenter='pydantic_model',
                          object_path='target.model.PlainModel')

    assert actual == [
        '',
        '.. py:pydantic_model:: PlainModel',
        '   :module: target.model',
        '',
        '   Model Plain.',
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
        '         "title": "PlainModel",',
        '         "description": "Model Plain.",',
        '         "type": "object",',
        '         "properties": {}',
        '      }',
        '',
        '   .. raw:: html',
        '',
        '      </details></p>',
        '',
        '']