"""This module contains tests for edgecases.

"""


def test_not_json_compliant(autodocument):
    actual = autodocument(documenter='pydantic_model',
                          object_path='target.edgecases.NotJsonCompliant',
                          options_app={"autodoc_pydantic_model_show_config_member": False,
                                       "autodoc_pydantic_model_show_config_summary": False})

    assert actual == [
        '',
        '.. py:pydantic_model:: NotJsonCompliant',
        '   :module: target.edgecases',
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
        '               "title": "Field",',
        '               "default": "ERROR: Not serializable",',
        '               "type": "string"',
        '            }',
        '         }',
        '      }',
        '',
        '   .. raw:: html',
        '',
        '      </details></p>',
        '',
        '',
        '',
        '   .. py:pydantic_field:: NotJsonCompliant.field',
        '      :module: target.edgecases',
        '      :type: target.edgecases.NoJsonSerializer',
        '      :value: <target.edgecases.NoJsonSerializer object>',
        ''
    ]
