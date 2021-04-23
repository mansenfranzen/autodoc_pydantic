"""This module contains the autodoc extension classes.

"""
import json
from typing import Any, Optional

import pydantic
from docutils.parsers.rst.directives import unchanged
from docutils.statemachine import StringList
from pydantic import BaseSettings
from pydantic.schema import get_field_schema_validations
from sphinx.ext.autodoc import (
    MethodDocumenter,
    ClassDocumenter,
    AttributeDocumenter,
    ALL)

from sphinx.util.inspect import object_description

from sphinxcontrib.autodoc_pydantic.inspection import (
    is_pydantic_model,
    is_validator_by_name,
    ModelWrapper
)
from sphinxcontrib.autodoc_pydantic.util import (
    option_members,
    option_one_of_factory,
    option_default_true,
    option_list_like,
    PydanticAutoDoc
)

OPTION_SPEC_FIELD = {
    "field-show-default": option_default_true,
    "field-signature-prefix": unchanged,
    "field-show-alias": option_default_true,
    "field-show-constraints": option_default_true,
    "field-list-validators": option_default_true,
    "__doc_disable_except__": option_list_like,
    "field-doc-policy": option_one_of_factory({"both",
                                               "docstring",
                                               "description"})}

OPTION_SPEC_VALIDATOR = {"validator-replace-signature": option_default_true,
                         "validator-list-fields": option_default_true,
                         "validator-signature-prefix": unchanged,
                         "__doc_disable_except__": option_list_like}

OPTION_SPEC_CONFIG = {"members": option_members,
                      "config-signature-prefix": unchanged,
                      "__doc_disable_except__": option_list_like}

OPTION_SPEC_MERGED = {**OPTION_SPEC_FIELD,
                      **OPTION_SPEC_VALIDATOR,
                      **OPTION_SPEC_CONFIG}

TPL_COLLAPSE = """
.. raw:: html

   <p><details  class="autodoc_pydantic_collapsable_json">
   <summary>Show JSON schema</summary>

.. code-block:: json

{}

.. raw:: html

   </details></p>
   
"""


class PydanticModelDocumenter(ClassDocumenter):
    """Represents specialized Documenter subclass for pydantic models.

    """

    objtype = 'pydantic_model'
    directivetype = 'pydantic_model'
    priority = 10 + ClassDocumenter.priority
    option_spec = ClassDocumenter.option_spec.copy()
    option_spec.update({"model-show-json": option_default_true,
                        "model-hide-paramlist": option_default_true,
                        "model-show-validator-members": option_default_true,
                        "model-show-validator-summary": option_default_true,
                        "model-show-config-member": option_default_true,
                        "model-show-config-summary": option_default_true,
                        "model-signature-prefix": unchanged,
                        "undoc-members": option_default_true,
                        "members": option_members,
                        "__doc_disable_except__": option_list_like,
                        **OPTION_SPEC_MERGED})

    pyautodoc_pass_to_directive = (
        "model-signature-prefix",
    )

    pyautodoc_set_default_option = (
        "member-order",
        "undoc-members"
    )

    pyautodoc_prefix = "model"

    def __init__(self, *args: Any) -> None:
        super().__init__(*args)
        self.pyautodoc = PydanticAutoDoc(self)

        self.pyautodoc.set_default_option_with_value("members", ALL)
        if self.options.get("undoc-members") is False:
            self.options.pop("undoc-members")

        if not self.pyautodoc.get_option_value("show-config-member", True):
            self.hide_config_member()

        if not self.pyautodoc.get_option_value("show-validator-members", True):
            self.hide_validator_members()

    def hide_config_member(self):
        """Add `Config` to `exclude_members` option.

        """

        if "exclude-members" not in self.options:
            self.options["exclude-members"] = {"Config"}
        else:
            self.options["exclude-members"].add("Config")

    def hide_validator_members(self):
        """Add validator names to `exclude_members`.

        """

        obj = self.pyautodoc.get_pydantic_object_from_name()

        validators = ModelWrapper(obj).get_validator_names()
        if "exclude-members" not in self.options:
            self.options["exclude-members"] = validators
        else:
            self.options["exclude-members"].update(validators)

    @classmethod
    def can_document_member(cls,
                            member: Any,
                            membername: str,
                            isattr: bool,
                            parent: Any) -> bool:
        """Filter only pydantic models.

        """

        is_val = super().can_document_member(member, membername, isattr,
                                             parent)
        is_model = is_pydantic_model(member)
        return is_val and is_model

    def format_signature(self, **kwargs) -> str:
        if self.pyautodoc.get_option_value("hide-paramlist", True):
            return ""
        else:
            return super().format_signature(**kwargs)

    def add_content(self,
                    more_content: Optional[StringList],
                    no_docstring: bool = False
                    ) -> None:
        super().add_content(more_content, no_docstring)

        if self.pyautodoc.get_option_value("show-json", True):
            self.add_collapsable_schema()

        if self.pyautodoc.get_option_value("show-config-summary", True):
            self.add_config_summary()

        if self.pyautodoc.get_option_value("show-validator-summary", True):
            self.add_validators_summary()

    def add_collapsable_schema(self):

        schema_json = self.object.schema_json()
        schema = json.dumps(json.loads(schema_json), default=str, indent=3)
        lines = [f"   {line}" for line in schema.split("\n")]
        lines = "\n".join(lines)
        lines = TPL_COLLAPSE.format(lines).split("\n")
        source_name = self.get_sourcename()

        for line in lines:
            self.add_line(line, source_name)

    def add_config_summary(self):
        """Adds summary section describing the model configuration.

        """

        cfg = self.object.Config
        is_main_config = cfg is pydantic.main.BaseConfig
        is_setting_config = cfg is pydantic.env_settings.BaseSettings.Config
        if is_main_config or is_setting_config:
            return

        values = {key: getattr(cfg, key) for key in dir(cfg)
                  if not key.startswith("_")}

        source_name = self.get_sourcename()
        self.add_line(":Config:", source_name)
        for name, value in values.items():
            line = f"   - **{name}**: *{type(value).__name__} = {value}*"
            self.add_line(line, source_name)
        self.add_line("", source_name)

    def add_validators_summary(self):
        """Adds summary section describing all validators with corresponding
        fields.

        """

        wrapper = ModelWrapper(self.object)
        validators = wrapper.get_named_references_for_validators()
        if validators:
            source_name = self.get_sourcename()
            self.add_line(":Validators:", source_name)

            for validator in validators:
                for field in wrapper.get_fields_for_validator(validator.name):
                    line = (f"   - "
                            f":py:obj:`{validator.name} <{validator.ref}>`"
                            f" » "
                            f":py:obj:`{field.name} <{field.ref}>`")
                    self.add_line(line, source_name)

            self.add_line("", source_name)


class PydanticSettingsDocumenter(PydanticModelDocumenter):
    objtype = 'pydantic_settings'
    directivetype = 'pydantic_settings'

    priority = 10 + ClassDocumenter.priority
    option_spec = ClassDocumenter.option_spec.copy()
    option_spec.update({"settings-show-json": option_default_true,
                        "settings-hide-paramlist": option_default_true,
                        "settings-show-validator-members": option_default_true,
                        "settings-show-validator-summary": option_default_true,
                        "settings-show-config-member": option_default_true,
                        "settings-show-config-summary": option_default_true,
                        "settings-signature-prefix": unchanged,
                        "undoc-members": option_default_true,
                        "members": option_members,
                        "__doc_disable_except__": option_list_like,
                        **OPTION_SPEC_MERGED})

    pyautodoc_pass_to_directive = (
        "settings-signature-prefix",
    )

    pyautodoc_set_default_option = (
        "member-order",
        "undoc-members"
    )

    pyautodoc_prefix = "settings"

    @classmethod
    def can_document_member(cls,
                            member: Any,
                            membername: str,
                            isattr: bool,
                            parent: Any) -> bool:
        """Filter only pydantic models.

        """

        is_val = super().can_document_member(member,
                                             membername,
                                             isattr,
                                             parent)
        if is_val:
            return issubclass(member, BaseSettings)
        else:
            return False


class PydanticFieldDocumenter(AttributeDocumenter):
    objtype = 'pydantic_field'
    directivetype = 'pydantic_field'
    priority = 10 + AttributeDocumenter.priority
    option_spec = dict(AttributeDocumenter.option_spec)
    option_spec.update(OPTION_SPEC_FIELD)
    member_order = 0

    pyautodoc_pass_to_directive = (
        "field-show-alias",
        "field-signature-prefix"
    )

    def __init__(self, *args):
        super().__init__(*args)
        self.pyautodoc = PydanticAutoDoc(self)

    @classmethod
    def can_document_member(cls,
                            member: Any,
                            membername: str,
                            isattr: bool,
                            parent: Any) -> bool:
        """Filter only pydantic fields.

        """

        is_val = super().can_document_member(member, membername, isattr, parent)
        is_parent_model = is_pydantic_model(parent.object)
        return is_val and is_parent_model and isattr

    def add_directive_header(self, sig: str) -> None:
        """Add default value to header.

        """

        super().add_directive_header(sig)
        if self.pyautodoc.get_option_value("field-show-default"):
            self.add_default_value()

    def add_default_value(self):
        """Adds default value.

        """

        name = self.objpath[-1]
        wrapper = ModelWrapper(self.parent)
        default = wrapper.get_field_properties_by_name(name).get("default")
        if default is not None:
            value = object_description(default)
            sourcename = self.get_sourcename()
            self.add_line('   :value: ' + value, sourcename)

    def add_content(self,
                    more_content: Optional[StringList],
                    no_docstring: bool = False
                    ) -> None:

        doc_policy = self.pyautodoc.get_option_value("field-doc-policy")
        if doc_policy in ("docstring", "both", None):
            super().add_content(more_content, no_docstring)
        if doc_policy in ("both", "description"):
            self.add_description()

        if self.pyautodoc.get_option_value("field-show-constraints"):
            self.add_constraints()

        if self.pyautodoc.get_option_value("field-list-validators"):
            self.add_validators()

    def add_constraints(self):
        """Adds section showing all defined constraints.

        """

        name = self.objpath[-1]
        wrapper = ModelWrapper(self.parent)
        field = wrapper.get_field_object_by_name(name)

        constraints = get_field_schema_validations(field)
        constraints = {key: value for key, value in constraints.items()
                       if key not in {"env_names"}}

        if constraints:
            source_name = self.get_sourcename()
            self.add_line(":Constraints:", source_name)
            for key, value in constraints.items():
                line = f"   - **{key}** = {value}"
                self.add_line(line, source_name)

            self.add_line("", source_name)

    def add_description(self):
        """Adds description from schema if present.

        """

        name = self.objpath[-1]
        wrapper = ModelWrapper(self.parent)
        properties = wrapper.get_field_properties_by_name(name)

        description = properties.get("description")
        if description is not None:
            source_name = self.get_sourcename()
            self.add_line(description, source_name)
            self.add_line("", source_name)

    def add_validators(self):
        """Add section with all validators that process this field.

        """

        name = self.objpath[-1]
        wrapper = ModelWrapper(self.parent)

        validators = wrapper.get_validators_for_field(name)
        if validators:
            source_name = self.get_sourcename()
            self.add_line(":Validated by:", source_name)
            for validator in validators:
                line = f"   - :py:obj:`{validator.name} <{validator.ref}>`"
                self.add_line(line, source_name)

            self.add_line("", source_name)


class PydanticValidatorDocumenter(MethodDocumenter):
    """Represents specialized Documenter subclass for pydantic validators.

    """

    objtype = 'pydantic_validator'
    directivetype = 'pydantic_validator'
    member_order = 50
    priority = 10 + MethodDocumenter.priority
    option_spec = MethodDocumenter.option_spec.copy()
    option_spec.update(OPTION_SPEC_VALIDATOR)

    pyautodoc_pass_to_directive = (
        "validator-signature-prefix",
        "validator-replace-signature"
    )

    def __init__(self, *args: Any) -> None:
        super().__init__(*args)
        self.pyautodoc = PydanticAutoDoc(self)

    @classmethod
    def can_document_member(cls,
                            member: Any,
                            membername: str,
                            isattr: bool,
                            parent: Any) -> bool:
        """Filter only pydantic validators.

        """

        is_val = super().can_document_member(member, membername, isattr,
                                             parent)
        is_validator = is_validator_by_name(membername, parent.object)
        return is_val and is_validator

    def format_args(self, **kwargs: Any) -> str:

        if self.pyautodoc.get_option_value("validator-replace-signature"):
            return ''
        else:
            return super().format_args(**kwargs)

    def add_content(self,
                    more_content: Optional[StringList],
                    no_docstring: bool = False
                    ) -> None:
        """Optionally show validator content.

        """

        super().add_content(more_content, no_docstring)

        if self.pyautodoc.get_option_value("validator-list-fields"):
            self.add_field_list()

    def add_field_list(self):
        """Adds a field list with all fields that are validated by this
        validator.

        """

        wrapper = ModelWrapper(self.parent)
        fields = wrapper.get_fields_for_validator(self.object_name)

        if not fields:
            return

        source_name = self.get_sourcename()
        self.add_line(":Validates:", source_name)

        for field in fields:
            line = f"   - :py:obj:`{field.name} <{field.ref}>`"
            self.add_line(line, source_name)

        self.add_line("", source_name)


class PydanticConfigClassDocumenter(ClassDocumenter):
    """Represents specialized Documenter subclass for pydantic model
    configuration.

    """

    objtype = 'pydantic_config'
    directivetype = 'pydantic_config'
    option_spec = ClassDocumenter.option_spec.copy()
    option_spec.update(OPTION_SPEC_CONFIG)
    member_order = 100
    priority = 10 + ClassDocumenter.priority

    pyautodoc_pass_to_directive = (
        "config-signature-prefix",
    )

    def __init__(self, *args: Any) -> None:
        super().__init__(*args)
        self.pyautodoc = PydanticAutoDoc(self)

        self.pyautodoc.set_default_option_with_value("members", ALL)
        if self.options.get("members"):
            self.options["undoc-members"] = True

    @classmethod
    def can_document_member(cls,
                            member: Any,
                            membername: str,
                            isattr: bool,
                            parent: Any) -> bool:
        """Filter only pydantic model configurations.

        """

        is_val = super().can_document_member(member, membername, isattr,
                                             parent)
        is_parent_model = is_pydantic_model(parent.object)
        is_config = membername == "Config"
        is_class = isinstance(member, type)
        return is_val and is_parent_model and is_config and is_class
