"""This module contains **autodoc_pydantic**'s autodocumenters.

"""

import json
from typing import Any, Optional, Dict, List, Iterable

import sphinx
from docutils.statemachine import StringList
from pydantic import BaseSettings
from sphinx.ext.autodoc import (
    MethodDocumenter,
    ClassDocumenter,
    AttributeDocumenter,
    Documenter
)

from sphinx.util.inspect import object_description
from sphinx.util.typing import get_type_hints, stringify

from sphinxcontrib.autodoc_pydantic.directives.options.enums import (
    OptionsJsonErrorStrategy,
    OptionsFieldDocPolicy,
    OptionsSummaryListOrder
)
from sphinxcontrib.autodoc_pydantic.directives.options.definition import (
    OPTIONS_MODEL,
    OPTIONS_SETTINGS,
    OPTIONS_FIELD,
    OPTIONS_VALIDATOR,
    OPTIONS_CONFIG,
    OPTIONS_MERGED
)
from sphinxcontrib.autodoc_pydantic.directives.templates import TPL_COLLAPSE
from sphinxcontrib.autodoc_pydantic.inspection import ModelInspector
from sphinxcontrib.autodoc_pydantic.directives.options.composites import (
    AutoDocOptions
)
from sphinxcontrib.autodoc_pydantic.directives.utility import NONE


class PydanticAutoDoc:
    """Composite to provide single namespace to access all **autodoc_pydantic**
    relevant documenter directive functionalities.

    """

    def __init__(self, documenter: Documenter, is_child: bool):
        self._documenter = documenter
        self._is_child = is_child
        self._inspect: Optional[ModelInspector] = None
        self._options = AutoDocOptions(self._documenter)

    @property
    def options(self) -> AutoDocOptions:
        """Provides access to :obj:`PydanticDocumenterOptions` to handle
        global and local configuration settings.

        """

        return self._options

    @property
    def inspect(self) -> ModelInspector:
        """Provides :obj:`ModelInspector` to access all inspection methods.
        You may wonder why this ``inspect`` is a property instead of a simple
        attribute being defined in the ``__init__`` method of this class. The
        reason is the following: auto-documenters do not have their ``object``
        attribute being correctly set after instantiation which typically holds
        a reference to the corresponding pydantic model and objects to be
        documented. Instead, ``object`` is ``None`` after plain instantiation
        (executing ``__init__``). However, this composite class is added during
        instantiation of the autodocumenter for consistency reasons. Therefore,
        ``ModelInspector`` can't be created at instantiation time of this class
        because the ``object`` is still ``None``. Hence, it is lazily created
        once the inspection methods are first required. At this point in time,
        it is guaranteed by the auto-documenter base class that ``object`` is
        then already correctly provided and the ``ModelInspector`` works as
        expected.

        """

        if self._inspect:
            return self._inspect

        if self._is_child:
            obj = self._documenter.parent
        else:
            obj = self._documenter.object

        self._inspect = ModelInspector(obj)
        return self._inspect


class PydanticModelDocumenter(ClassDocumenter):
    """Represents specialized Documenter subclass for pydantic models.

    """

    objtype = 'pydantic_model'
    directivetype = 'pydantic_model'
    priority = 10 + ClassDocumenter.priority
    option_spec = ClassDocumenter.option_spec.copy()
    option_spec.update({**OPTIONS_MODEL, **OPTIONS_MERGED})

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
        is_model = ModelInspector.static.is_pydantic_model(member)
        return is_val and is_model

    def __init__(self, *args: Any) -> None:
        super().__init__(*args)
        self.pydantic = PydanticAutoDoc(self, is_child=False)

    def document_members(self, *args, **kwargs):
        """Modify member options before starting to document members.

        """

        self.pydantic.options.set_members_all()
        if self.options.get("undoc-members") is False:
            self.options.pop("undoc-members")

        if self.pydantic.options.is_false("show-config-member", True):
            self.hide_config_member()

        if self.pydantic.options.is_false("show-validator-members", True):
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

        validators = self.pydantic.inspect.validators.names
        if "exclude-members" not in self.options:
            self.options["exclude-members"] = validators
        else:
            self.options["exclude-members"].update(validators)

    def format_signature(self, **kwargs) -> str:
        """If parameter list is to be hidden, return only empty signature.

        """

        if self.pydantic.options.is_true("hide-paramlist", True):
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

        # do not provide any additional info if documented as attribute
        if self.doc_as_attr:
            return

        if self.pydantic.options.is_true("show-json", True):
            self.add_collapsable_schema()

        if self.pydantic.options.is_true("show-config-summary", True):
            self.add_config_summary()

        if self.pydantic.options.is_true("show-field-summary", True):
            self.add_field_summary()

        if self.pydantic.options.is_true("show-validator-summary", True):
            self.add_validators_summary()

    def add_collapsable_schema(self):
        """Adds collapse code block containing JSON schema.

        """

        schema = self.pydantic.inspect.schema.sanitized
        non_serializable = self.pydantic.inspect.fields.non_json_serializable

        # handle non serializable fields
        strategy = self.pydantic.options.get_value("show-json-error-strategy")
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

        schema_rest = self._convert_json_schema_to_rest(schema)
        source_name = self.get_sourcename()

        for line in schema_rest:
            self.add_line(line, source_name)

    def add_config_summary(self):
        """Adds summary section describing the model configuration.

        """

        if not self.pydantic.inspect.config.is_configured:
            return

        cfg_items = self.pydantic.inspect.config.items

        source_name = self.get_sourcename()
        self.add_line(":Config:", source_name)
        for name, value in cfg_items.items():
            line = f"   - **{name}**: *{type(value).__name__} = {value}*"
            self.add_line(line, source_name)
        self.add_line("", source_name)

    def add_validators_summary(self):
        """Adds summary section describing all validators with corresponding
        fields.

        """

        if not self.pydantic.inspect.validators:
            return

        references = self.pydantic.inspect.references.mappings
        valid_members = self.pydantic.options.get_filtered_member_names()
        filtered_references = {reference.validator_name: reference
                               for reference in references
                               if reference.validator_name in valid_members}

        # get correct sort order
        validator_names = filtered_references.keys()
        sorted_validator_names = self._sort_summary_list(validator_names)

        source_name = self.get_sourcename()
        self.add_line(":Validators:", source_name)
        for validator_name in sorted_validator_names:
            ref = filtered_references[validator_name]
            line = (f"   - "
                    f":py:obj:`{ref.validator_name} <{ref.validator_ref}>`"
                    f" » "
                    f":py:obj:`{ref.field_name} <{ref.field_ref}>`")
            self.add_line(line, source_name)

        self.add_line("", source_name)

    def add_field_summary(self):
        """Adds summary section describing all fields.

        """

        if not self.pydantic.inspect.fields:
            return

        fields = self.pydantic.inspect.fields.names
        valid_members = self.pydantic.options.get_filtered_member_names()
        filtered_fields = [field for field in fields
                           if field in valid_members]
        sorted_fields = self._sort_summary_list(filtered_fields)

        source_name = self.get_sourcename()
        self.add_line(":Fields:", source_name)
        for field_name in sorted_fields:
            line = self._get_field_summary_line(field_name)
            self.add_line(line, source_name)

        self.add_line("", source_name)

    def _sort_summary_list(self, names: Iterable[str]) -> List[str]:
        """Sort member names according to given sort order
        `OptionsSummaryListOrder`.

        """

        sort_order = self.pydantic.options.get_value(name="summary-list-order",
                                                     prefix=True,
                                                     force_availability=True)

        if sort_order == OptionsSummaryListOrder.ALPHABETICAL:
            def sort_func(name: str):
                return name
        elif sort_order == OptionsSummaryListOrder.BYSOURCE:
            def sort_func(name: str):
                name_with_class = f"{self.object_name}.{name}"
                return self.analyzer.tagorder.get(name_with_class)
        else:
            raise ValueError(
                f"Invalid value `{sort_order}` provided for "
                f"`summary_list_order`. Valid options are: "
                f"{OptionsSummaryListOrder.values()}")

        return sorted(names, key=sort_func)

    def _get_field_summary_line(self, field_name: str) -> str:
        """Get reST for field summary for given `member_name`.

        """

        ref_func = self.pydantic.inspect.references.create_model_reference
        ref = ref_func(field_name)
        typ = self._stringify_type(field_name)
        return f"   - :py:obj:`{field_name} ({typ}) <{ref}>`"

    def _stringify_type(self, field_name: str) -> str:
        """Get proper string representation of type for given `member_nane`
        relying on sphinx functionality.

        """

        type_aliases = self.config.autodoc_type_aliases
        annotations = get_type_hints(self.object, None, type_aliases)
        return stringify(annotations.get(field_name, ""))

    @staticmethod
    def _convert_json_schema_to_rest(schema: Dict) -> List[str]:
        """Convert model's schema dict into reST.

        """

        schema = json.dumps(schema, default=str, indent=3)
        lines = [f"   {line}" for line in schema.split("\n")]
        lines = "\n".join(lines)
        lines = TPL_COLLAPSE.format(lines).split("\n")

        return lines


class PydanticSettingsDocumenter(PydanticModelDocumenter):
    """Represents specialized Documenter subclass for pydantic settings.

    """

    objtype = 'pydantic_settings'
    directivetype = 'pydantic_settings'

    priority = 10 + ClassDocumenter.priority
    option_spec = ClassDocumenter.option_spec.copy()
    option_spec.update({**OPTIONS_SETTINGS, **OPTIONS_MERGED})

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
    option_spec.update(OPTIONS_FIELD)
    member_order = 0

    pyautodoc_pass_to_directive = (
        "field-signature-prefix",
    )

    def __init__(self, *args):
        super().__init__(*args)
        self.pydantic = PydanticAutoDoc(self, is_child=True)

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
        is_parent_model = ModelInspector.static.is_pydantic_model(
            parent.object)
        return is_val and is_parent_model and isattr

    @property
    def pydantic_field_name(self) -> str:
        """Provide the pydantic field name which refers to the member name of
        the parent pydantic model.

        """

        return self.objpath[-1]

    def add_directive_header(self, sig: str) -> None:
        """Delegate header options.

        """

        super().add_directive_header(sig)

        self.add_default_value_or_required()

        if self.pydantic.options.is_true("field-show-alias"):
            self.add_alias()

    def add_default_value_or_required(self):
        """Adds default value or required marker.

        """

        field_name = self.pydantic_field_name
        is_required = self.pydantic.inspect.fields.is_required(field_name)
        show_default = self.pydantic.options.is_true("field-show-default")
        show_required = self.pydantic.options.is_true("field-show-required")

        if show_required and is_required:
            sourcename = self.get_sourcename()
            self.add_line('   :required:', sourcename)

        elif show_default:
            func = self.pydantic.inspect.fields.get_property_from_field_info
            default = func(field_name, "default")
            value = object_description(default)
            sourcename = self.get_sourcename()
            self.add_line('   :value: ' + value, sourcename)

    def add_alias(self):
        """Adds alias directive option.

        """

        field_name = self.pydantic_field_name
        field = self.pydantic.inspect.fields.get(field_name)

        if field.alias != field_name:
            sourcename = self.get_sourcename()
            self.add_line('   :alias: ' + field.alias, sourcename)

    def add_content(self,
                    more_content: Optional[StringList],
                    no_docstring: bool = False
                    ) -> None:
        """Delegate additional content creation.

        """

        doc_policy = self.pydantic.options.get_value("field-doc-policy")
        if doc_policy in (OptionsFieldDocPolicy.DOCSTRING,
                          OptionsFieldDocPolicy.BOTH,
                          None, NONE):
            super().add_content(more_content, no_docstring)
        if doc_policy in (OptionsFieldDocPolicy.BOTH,
                          OptionsFieldDocPolicy.DESCRIPTION):
            self.add_description()

        if self.pydantic.options.is_true("field-show-constraints"):
            self.add_constraints()

        if self.pydantic.options.is_true("field-list-validators"):
            self.add_validators()

    def add_constraints(self):
        """Adds section showing all defined constraints.

        """

        field_name = self.pydantic_field_name
        constraints = self.pydantic.inspect.fields.get_constraints(field_name)

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

        field_name = self.pydantic_field_name
        func = self.pydantic.inspect.fields.get_property_from_field_info
        description = func(field_name, "description")

        if description is not None:
            source_name = self.get_sourcename()
            self.add_line(description, source_name)
            self.add_line("", source_name)

    def add_validators(self):
        """Add section with all validators that process this field.

        """

        field_name = self.pydantic_field_name
        func = self.pydantic.inspect.references.filter_by_field_name
        references = func(field_name)

        if not references:
            return

        source_name = self.get_sourcename()
        self.add_line(":Validated by:", source_name)
        for reference in references:
            field_name = reference.validator_name
            ref = reference.validator_ref
            line = f"   - :py:obj:`{field_name} <{ref}>`"
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
    option_spec.update(OPTIONS_VALIDATOR)

    pyautodoc_pass_to_directive = (
        "validator-signature-prefix",
        "validator-replace-signature"
    )

    def __init__(self, *args: Any) -> None:
        super().__init__(*args)
        self.pydantic = PydanticAutoDoc(self, is_child=True)

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
        is_validator = ModelInspector.static.is_validator_by_name(
            membername,
            parent.object)
        return is_val and is_validator

    def format_args(self, **kwargs: Any) -> str:
        """Return empty arguments if validator should be replaced.

        """

        if self.pydantic.options.is_true("validator-replace-signature"):
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

        if self.pydantic.options.is_true("validator-list-fields"):
            self.add_field_list()

    def add_field_list(self):
        """Adds a field list with all fields that are validated by this
        validator.

        """

        func = self.pydantic.inspect.references.filter_by_validator_name
        references = func(self.object_name)

        if not references:
            return

        source_name = self.get_sourcename()
        self.add_line(":Validates:", source_name)

        for reference in references:
            line = f"   - :py:obj:" \
                   f"`{reference.field_name} " \
                   f"<{reference.field_ref}>`"
            self.add_line(line, source_name)

        self.add_line("", source_name)


class PydanticConfigClassDocumenter(ClassDocumenter):
    """Represents specialized Documenter subclass for pydantic model
    configuration.

    """

    objtype = 'pydantic_config'
    directivetype = 'pydantic_config'
    option_spec = ClassDocumenter.option_spec.copy()
    option_spec.update(OPTIONS_CONFIG)
    member_order = 100
    priority = 10 + ClassDocumenter.priority

    pyautodoc_pass_to_directive = (
        "config-signature-prefix",
    )

    def __init__(self, *args: Any) -> None:
        super().__init__(*args)
        self.pydantic = PydanticAutoDoc(self, is_child=True)

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
        is_parent_model = ModelInspector.static.is_pydantic_model(
            parent.object)
        is_config = membername == "Config"
        is_class = isinstance(member, type)
        return is_val and is_parent_model and is_config and is_class

    def document_members(self, *args, **kwargs):
        """Modify member options before starting to document members.

        """

        self.pydantic.options.set_members_all()
        if self.options.get("members"):
            self.options["undoc-members"] = True

        # handle special case when Config is documented as an attribute
        # in which case `all_members` defaults to True which has to be
        # overruled by `autodoc_pydantic_config_members` app cfg
        app_cfg = self.pydantic.options.get_app_cfg_by_name("members")
        hide_members = app_cfg is False
        no_members = bool(self.options.get("members")) is False

        if hide_members and no_members:
            super().document_members(all_members=False, **kwargs)
        else:
            super().document_members(*args, **kwargs)
