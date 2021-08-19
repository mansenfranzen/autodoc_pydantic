"""This module contains the autodoc extension classes.

"""

import json
from typing import Any, Optional, Dict

import pydantic
import sphinx
from docutils.parsers.rst.directives import unchanged
from docutils.statemachine import StringList
from pydantic import BaseSettings
from pydantic.schema import get_field_schema_validations
from sphinx.ext.autodoc import (
    MethodDocumenter,
    ClassDocumenter,
    AttributeDocumenter)

from sphinx.util.inspect import object_description
from sphinx.util.typing import get_type_hints, stringify

from sphinxcontrib.autodoc_pydantic.inspection import (
    is_pydantic_model,
    is_validator_by_name,
    ModelWrapper
)
from sphinxcontrib.autodoc_pydantic.composites import (
    option_members,
    option_one_of_factory,
    option_default_true,
    option_list_like,
    PydanticAutoDoc,
    NONE
)
from sphinxcontrib.autodoc_pydantic.utility import CustomEnum


class OptionsJsonErrorStrategy(CustomEnum):
    RAISE = "raise"
    COERCE = "coerce"
    WARN = "warn"


class OptionsFieldDocPolicy(CustomEnum):
    BOTH = "both"
    DOCSTRING = "docstring"
    DESCRIPTION = "description"


OPTION_SPEC_FIELD = {
    "field-show-default": option_default_true,
    "field-show-required": option_default_true,
    "field-signature-prefix": unchanged,
    "field-show-alias": option_default_true,
    "field-show-constraints": option_default_true,
    "field-list-validators": option_default_true,
    "__doc_disable_except__": option_list_like,
    "field-doc-policy": option_one_of_factory(OptionsFieldDocPolicy.values())}

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

OPTION_SPEC_MODEL = {
    "model-show-json": option_default_true,
    "model-show-json-error-strategy": option_one_of_factory(
        OptionsJsonErrorStrategy.values()
    ),
    "model-hide-paramlist": option_default_true,
    "model-show-validator-members": option_default_true,
    "model-show-validator-summary": option_default_true,
    "model-show-field-summary": option_default_true,
    "model-show-config-member": option_default_true,
    "model-show-config-summary": option_default_true,
    "model-signature-prefix": unchanged,
    "undoc-members": option_default_true,
    "members": option_members,
    "__doc_disable_except__": option_list_like}

OPTION_SPEC_SETTINGS = {
    "settings-show-json": option_default_true,
    "settings-show-json-error-strategy": option_one_of_factory(
        OptionsJsonErrorStrategy.values()
    ),
    "settings-hide-paramlist": option_default_true,
    "settings-show-validator-members": option_default_true,
    "settings-show-validator-summary": option_default_true,
    "settings-show-field-summary": option_default_true,
    "settings-show-config-member": option_default_true,
    "settings-show-config-summary": option_default_true,
    "settings-signature-prefix": unchanged,
    "undoc-members": option_default_true,
    "members": option_members,
    "__doc_disable_except__": option_list_like}

TPL_COLLAPSE = """
.. raw:: html

   <p><details  class="autodoc_pydantic_collapsable_json">
   <summary>Show JSON schema</summary>

.. code-block:: json

{}

.. raw:: html

   </details></p>

"""


def convert_json_schema_to_rest(schema: Dict) -> str:
    """Convert model's schema dict into reST.

    """

    schema = json.dumps(schema, default=str, indent=3)
    lines = [f"   {line}" for line in schema.split("\n")]
    lines = "\n".join(lines)
    lines = TPL_COLLAPSE.format(lines).split("\n")

    return lines


class PydanticModelDocumenter(ClassDocumenter):
    """Represents specialized Documenter subclass for pydantic models.

    """

    objtype = 'pydantic_model'
    directivetype = 'pydantic_model'
    priority = 10 + ClassDocumenter.priority
    option_spec = ClassDocumenter.option_spec.copy()
    option_spec.update({**OPTION_SPEC_MODEL, **OPTION_SPEC_MERGED})

    pyautodoc_pass_to_directive = (
        "model-signature-prefix",
    )

    pyautodoc_set_default_option = (
        "member-order",
        "undoc-members"
    )

    pyautodoc_prefix = "model"

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

    def __init__(self, *args: Any) -> None:
        super().__init__(*args)
        self.pyautodoc = PydanticAutoDoc(self)

    def document_members(self, *args, **kwargs):
        """Modify member options before starting to document members.

        """

        self.pyautodoc.set_members_all()
        if self.options.get("undoc-members") is False:
            self.options.pop("undoc-members")

        if self.pyautodoc.option_is_false("show-config-member", True):
            self.hide_config_member()

        if self.pyautodoc.option_is_false("show-validator-members", True):
            self.hide_validator_members()

        super().document_members(*args, **kwargs)

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

        validators = ModelWrapper(self.object).get_validator_names()
        if "exclude-members" not in self.options:
            self.options["exclude-members"] = validators
        else:
            self.options["exclude-members"].update(validators)

    def format_signature(self, **kwargs) -> str:
        """If parameter list is to be hidden, return only empty signature.

        """

        if self.pyautodoc.option_is_true("hide-paramlist", True):
            return ""
        else:
            return super().format_signature(**kwargs)

    def add_content(self,
                    more_content: Optional[StringList],
                    no_docstring: bool = False
                    ) -> None:
        """Delegate additional content creation.

        """

        super().add_content(more_content, no_docstring)

        if self.pyautodoc.option_is_true("show-json", True):
            self.add_collapsable_schema()

        if self.pyautodoc.option_is_true("show-config-summary", True):
            self.add_config_summary()

        if self.pyautodoc.option_is_true("show-field-summary", True):
            self.add_field_summary()

        if self.pyautodoc.option_is_true("show-validator-summary", True):
            self.add_validators_summary()

    def add_collapsable_schema(self):
        """Adds collapse code block containing JSON schema.

        """

        wrapper = ModelWrapper(self.object)
        schema, non_serializable = wrapper.get_safe_schema_json()

        # handle non serializable fields
        strategy = self.pyautodoc.get_option_value("show-json-error-strategy")
        if non_serializable:
            error_msg = (
                f"JSON schema can't be generated for '{self.fullname}' "
                f"because the following pydantic fields can't be serialized "
                f"properly: {non_serializable}."
            )

            if strategy == OptionsJsonErrorStrategy.WARN:
                logger = sphinx.util.logging.getLogger(__name__)
                logger.warning(error_msg, location="autodoc_pydantic")
            elif strategy == OptionsJsonErrorStrategy.RAISE:
                raise sphinx.errors.ExtensionError(error_msg)
            elif strategy != OptionsJsonErrorStrategy.COERCE:
                raise sphinx.errors.ExtensionError(
                    f"Invalid option provided for 'show-json-error-strategy'. "
                    f"Allowed values are f{OptionsJsonErrorStrategy.values()}"
                )

        schema_rest = convert_json_schema_to_rest(schema)
        source_name = self.get_sourcename()

        for line in schema_rest:
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
            valid_members = self.pyautodoc.get_filtered_member_names()
            filtered_members = [validator for validator in validators
                                if validator.name in valid_members]

            self.add_line(":Validators:", source_name)
            for validator in filtered_members:
                for field in wrapper.get_fields_for_validator(validator.name):
                    line = (f"   - "
                            f":py:obj:`{validator.name} <{validator.ref}>`"
                            f" » "
                            f":py:obj:`{field.name} <{field.ref}>`")
                    self.add_line(line, source_name)

            self.add_line("", source_name)

    def add_field_summary(self):
        """Adds summary section describing all fields.

        """

        wrapper = ModelWrapper(self.object)
        fields = wrapper.get_fields()

        if fields:
            source_name = self.get_sourcename()
            type_aliases = self.config.autodoc_type_aliases
            valid_members = self.pyautodoc.get_filtered_member_names()
            filtered_members = [field for field in fields
                                if field in valid_members]

            self.add_line(":Fields:", source_name)
            for member_name in filtered_members:
                ref = wrapper.get_reference(member_name)
                annotations = get_type_hints(self.object, None, type_aliases)
                typ = stringify(annotations.get(member_name, ""))

                line = (f"   - :py:obj:`{member_name} ({typ}) <{ref}>`")
                self.add_line(line, source_name)

            self.add_line("", source_name)


class PydanticSettingsDocumenter(PydanticModelDocumenter):
    """Represents specialized Documenter subclass for pydantic settings.

    """

    objtype = 'pydantic_settings'
    directivetype = 'pydantic_settings'

    priority = 10 + ClassDocumenter.priority
    option_spec = ClassDocumenter.option_spec.copy()
    option_spec.update({**OPTION_SPEC_SETTINGS, **OPTION_SPEC_MERGED})

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
    """Represents specialized Documenter subclass for pydantic fields.

    """

    objtype = 'pydantic_field'
    directivetype = 'pydantic_field'
    priority = 10 + AttributeDocumenter.priority
    option_spec = dict(AttributeDocumenter.option_spec)
    option_spec.update(OPTION_SPEC_FIELD)
    member_order = 0

    pyautodoc_pass_to_directive = (
        "field-signature-prefix",
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

        is_val = super().can_document_member(member, membername, isattr,
                                             parent)
        is_parent_model = is_pydantic_model(parent.object)
        return is_val and is_parent_model and isattr

    def add_directive_header(self, sig: str) -> None:
        """Delegate header options.

        """

        super().add_directive_header(sig)

        self.add_default_value_or_required()

        if self.pyautodoc.option_is_true("field-show-alias"):
            self.add_alias()

    def add_default_value_or_required(self):
        """Adds default value or required marker.

        """

        field_name = self.objpath[-1]
        wrapper = ModelWrapper(self.parent)

        show_default = self.pyautodoc.option_is_true("field-show-default")
        show_required = self.pyautodoc.option_is_true("field-show-required")
        is_required = wrapper.field_is_required(field_name)

        if show_required and is_required:
            sourcename = self.get_sourcename()
            self.add_line('   :required:', sourcename)

        elif show_default:
            default = wrapper.get_field_property(field_name, "default")
            value = object_description(default)
            sourcename = self.get_sourcename()
            self.add_line('   :value: ' + value, sourcename)

    def add_alias(self):
        """Adds alias directive option.

        """

        field_name = self.objpath[-1]
        wrapper = ModelWrapper(self.parent)
        alias = wrapper.get_field_object_by_name(field_name).alias

        if alias != field_name:
            sourcename = self.get_sourcename()
            self.add_line('   :alias: ' + alias, sourcename)

    def add_content(self,
                    more_content: Optional[StringList],
                    no_docstring: bool = False
                    ) -> None:
        """Delegate additional content creation.

        """

        doc_policy = self.pyautodoc.get_option_value("field-doc-policy")
        if doc_policy in (OptionsFieldDocPolicy.DOCSTRING,
                          OptionsFieldDocPolicy.BOTH,
                          None, NONE):
            super().add_content(more_content, no_docstring)
        if doc_policy in (OptionsFieldDocPolicy.BOTH,
                          OptionsFieldDocPolicy.DESCRIPTION):
            self.add_description()

        if self.pyautodoc.option_is_true("field-show-constraints"):
            self.add_constraints()

        if self.pyautodoc.option_is_true("field-list-validators"):
            self.add_validators()

    def add_constraints(self):
        """Adds section showing all defined constraints.

        """

        field_name = self.objpath[-1]
        wrapper = ModelWrapper(self.parent)
        field = wrapper.get_field_object_by_name(field_name)

        constraints = get_field_schema_validations(field)
        constraints = {key: value for key, value in constraints.items()
                       if key not in {"env_names", "env"}}

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
        description = wrapper.get_field_property(name, "description")

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
        """Return empty arguments if validator should be replaced.

        """

        if self.pyautodoc.option_is_true("validator-replace-signature"):
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

        if self.pyautodoc.option_is_true("validator-list-fields"):
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

    def document_members(self, *args, **kwargs):
        """Modify member options before starting to document members.

        """

        self.pyautodoc.set_members_all()
        if self.options.get("members"):
            self.options["undoc-members"] = True

        # handle special case when Config is documented as an attribute
        # in which case `all_members` defaults to True which has to be
        # overruled by `autodoc_pydantic_config_members` app cfg
        hide_members = self.pyautodoc.get_app_cfg_by_name("members") is False
        no_members = bool(self.options.get("members")) is False

        if hide_members and no_members:
            super().document_members(all_members=False, **kwargs)
        else:
            super().document_members(*args, **kwargs)
