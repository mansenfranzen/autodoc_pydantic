"""This module contains tests for edgecases.

"""
import copy

from sphinx.transforms.post_transforms import ReferencesResolver


def test_not_json_compliant(autodocument):
    actual = autodocument(
        documenter='pydantic_model',
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


def test_current_module_model(parse_rst):
    """Ensure that using current module does not break any features.

    This relates to issue #12.

    """

    input_rst = ['.. py:currentmodule:: target.example_model',
                 '',
                 '.. autopydantic_model:: ExampleModel',
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
