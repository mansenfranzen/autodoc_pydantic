"""This module contains end to end example tests.

"""

def test_model_plain(autodocument):
    options_app = dict(autodoc_pydantic_model_show_json=False)
    actual = autodocument(documenter='pydantic_model',
                          object_path='target.examples.PlainModel',
                          options_app=options_app)

    assert actual == [
        '',
        '.. py:pydantic_model:: PlainModel',
        '   :module: target.examples',
        '',
        '   Model Plain.',
        ''
    ]

def test_model_with_field(autodocument):
    options_app = dict(autodoc_pydantic_model_show_json=False)
    options_doc = dict(members=None)
    actual = autodocument(documenter='pydantic_model',
                          object_path='target.examples.ModelWithField',
                          options_doc=options_doc,
                          options_app=options_app)

    assert actual == [
        '',
        '.. py:pydantic_model:: ModelWithField',
        '   :module: target.examples',
        '',
        '   Model With Field.',
        '',
        '   :Fields:',
        '      - :py:obj:`field (int) <target.examples.ModelWithField.field>`',
        '',
        '',
        '   .. py:pydantic_field:: ModelWithField.field',
        '      :module: target.examples',
        '      :type: int',
        '      :value: 1',
        '',
        '      Doc field',
        ''
    ]


def test_model_with_field_validator(autodocument):
    options_app = dict(autodoc_pydantic_model_show_json=False,
                       autodoc_pydantic_validator_list_fields=True)
    options_doc = dict(members=None)
    actual = autodocument(documenter='pydantic_model',
                          object_path='target.examples.ModelWithFieldValidator',
                          options_doc=options_doc,
                          options_app=options_app)

    assert actual == [
        '',
        '.. py:pydantic_model:: ModelWithFieldValidator',
        '   :module: target.examples',
        '',
        '   Model With Field Validator.',
        '',
        '   :Fields:',
        '      - :py:obj:`field (int) <target.examples.ModelWithFieldValidator.field>`',
        '',
        '   :Validators:',
        '      - :py:obj:`is_integer <target.examples.ModelWithFieldValidator.is_integer>` » :py:obj:`field <target.examples.ModelWithFieldValidator.field>`',
        '',
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
        '',
        '   .. py:pydantic_validator:: ModelWithFieldValidator.is_integer',
        '      :module: target.examples',
        '      :classmethod:',
        '',
        '      Doc validator.',
        '',
        '      :Validates:',
        '         - :py:obj:`field <target.examples.ModelWithFieldValidator.field>`',
        ''
    ]


def test_model_with_config(autodocument):
    options_app = dict(autodoc_pydantic_model_show_json=False,
                       autodoc_pydantic_model_show_config_member=True)
    options_doc = dict(members=None)
    actual = autodocument(documenter='pydantic_model',
                          object_path='target.examples.ModelWithConfig',
                          options_doc=options_doc,
                          options_app=options_app)

    assert actual == [
        '',
        '.. py:pydantic_model:: ModelWithConfig',
        '   :module: target.examples',
        '',
        '   Model with Config.',
        '',
        '   :Config:',
        '      - **frozen**: *bool = False*',
        '']


def test_model_plain_show_json(autodocument):
    actual = autodocument(documenter='pydantic_model',
                          object_path='target.examples.PlainModel')

    assert actual == [
        '',
        '.. py:pydantic_model:: PlainModel',
        '   :module: target.examples',
        '',
        '   Model Plain.',
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
