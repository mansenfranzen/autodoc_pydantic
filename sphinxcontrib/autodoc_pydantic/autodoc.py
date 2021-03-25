"""This module contains the autodoc extension classes.

"""
import json
from typing import Any, Optional

import pydantic
from docutils.statemachine import StringList
from pydantic import BaseSettings
from pydantic.schema import get_field_schema_validations
from sphinx.ext.autodoc import MethodDocumenter, ClassDocumenter, \
    AttributeDocumenter
from sphinx.util.inspect import object_description

from sphinxcontrib.autodoc_pydantic.inspection import is_pydantic_model, \
    is_validator_by_name, ModelWrapper

tpl_collapse = """
.. raw:: html

   <p><details>
   <summary><a>Show JSON schema</a></summary>

.. code-block:: json

{}

.. raw:: html

   </details></p>
   
"""


class PydanticFieldDocumenter(AttributeDocumenter):
    objtype = 'pydantic_field'
    directivetype = 'pydantic_field'
    priority = 10 + AttributeDocumenter.priority
    option_spec = dict(AttributeDocumenter.option_spec)
    member_order = 0

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

        cfg = self.env.config["autodoc_pydantic_field_doc_policy"]
        if cfg in ("docstring", "both"):
            super().add_content(more_content, no_docstring)
        if cfg in ("both", "description"):
            self.add_description()

        if self.env.config["autodoc_pydantic_field_show_constraints"]:
            self.add_constraints()

        if self.env.config["autodoc_pydantic_field_list_validators"]:
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


class PydanticConfigClassDocumenter(ClassDocumenter):
    """Represents specialized Documenter subclass for pydantic model
    configuration.

    """

    objtype = 'pydantic_config_class'
    directivetype = 'pydantic_config_class'
    member_order = 100
    priority = 10 + ClassDocumenter.priority

    def __init__(self, *args: Any) -> None:
        super().__init__(*args)
        self.options["undoc-members"] = True

    @classmethod
    def can_document_member(cls,
                            member: Any,
                            membername: str,
                            isattr: bool,
                            parent: Any) -> bool:
        """Filter only pydantic model configurations.

        """

        is_val = super().can_document_member(member, membername, isattr, parent)
        is_parent_model = is_pydantic_model(parent.object)
        is_config = membername == "Config"
        is_class = isinstance(member, type)
        return is_val and is_parent_model and is_config and is_class

    def add_content(self,
                    more_content: Optional[StringList],
                    no_docstring: bool = False
                    ) -> None:
        """Optionally show model configuration or not.

        """

        if self.env.config["autodoc_pydantic_show_config"]:
            super().add_content(more_content, no_docstring)

    def add_directive_header(self, sig: str) -> None:
        """Optionally show model configuration or not.

        """

        if self.env.config["autodoc_pydantic_show_config"]:
            super().add_directive_header(sig)


class PydanticModelDocumenter(ClassDocumenter):
    """Represents specialized Documenter subclass for pydantic models.

    """

    objtype = 'pydantic_model'
    directivetype = 'pydantic_model'
    priority = 10 + ClassDocumenter.priority

    def __init__(self, *args: Any) -> None:
        super().__init__(*args)
        member_order = self.env.config["autodoc_pydantic_model_member_order"]
        self.options["member-order"] = member_order

    @classmethod
    def can_document_member(cls,
                            member: Any,
                            membername: str,
                            isattr: bool,
                            parent: Any) -> bool:
        """Filter only pydantic models.

        """

        is_val = super().can_document_member(member, membername, isattr, parent)
        is_model = is_pydantic_model(member)
        return is_val and is_model

    def add_content(self,
                    more_content: Optional[StringList],
                    no_docstring: bool = False
                    ) -> None:
        super().add_content(more_content, no_docstring)

        if self.env.config["autodoc_pydantic_model_show_schema"]:
            self.add_collapsable_schema()

        if self.env.config["autodoc_pydantic_model_show_config"]:
            self.add_config()

        if self.env.config["autodoc_pydantic_model_show_validators"]:
            self.add_validators()

    def add_collapsable_schema(self):

        schema_json = self.object.schema_json()
        schema = json.dumps(json.loads(schema_json), default=str, indent=3)
        lines = [f"   {line}" for line in schema.split("\n")]
        lines = "\n".join(lines)
        lines = tpl_collapse.format(lines).split("\n")
        source_name = self.get_sourcename()

        for line in lines:
            self.add_line(line, source_name)


    def add_config(self):
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

    def add_validators(self):
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


class PydanticSettingsDocumenter(PydanticModelDocumenter):

    objtype = 'pydantic_settings'
    directivetype = 'pydantic_settings'
    priority = 10 + PydanticModelDocumenter.priority

    @classmethod
    def can_document_member(cls,
                            member: Any,
                            membername: str,
                            isattr: bool,
                            parent: Any) -> bool:
        """Filter only pydantic models.

        """

        is_val = super().can_document_member(member, membername, isattr, parent)
        if is_val:
            return issubclass(member, BaseSettings)
        else:
            return False


class PydanticValidatorDocumenter(MethodDocumenter):
    """Represents specialized Documenter subclass for pydantic validators.

    """

    objtype = 'pydantic_validator'
    directivetype = 'pydantic_validator'
    member_order = 50
    priority = 10 + MethodDocumenter.priority

    @classmethod
    def can_document_member(cls,
                            member: Any,
                            membername: str,
                            isattr: bool,
                            parent: Any) -> bool:
        """Filter only pydantic validators.

        """

        is_val = super().can_document_member(member, membername, isattr, parent)
        is_validator = is_validator_by_name(membername, parent.object)
        return is_val and is_validator

    def add_directive_header(self, sig: str) -> None:
        """Optionally show validator header.

        """

        if self.env.config["autodoc_pydantic_show_validators"]:
            super().add_directive_header(sig)

    def add_content(self,
                    more_content: Optional[StringList],
                    no_docstring: bool = False
                    ) -> None:
        """Optionally show validator content.

        """

        if self.env.config["autodoc_pydantic_show_validators"]:
            super().add_content(more_content, no_docstring)

            if self.env.config["autodoc_pydantic_validator_list_fields"]:
                self.add_field_list()

    def add_field_list(self):
        """Adds a field list with all fields that are validated by this
        validator.

        """

        source_name = self.get_sourcename()
        self.add_line(":Validates:", source_name)

        wrapper = ModelWrapper(self.parent)
        fields = wrapper.get_fields_for_validator(self.object_name)
        for field in fields:
            line = f"   - :py:obj:`{field.name} <{field.ref}>`"
            self.add_line(line, source_name)
