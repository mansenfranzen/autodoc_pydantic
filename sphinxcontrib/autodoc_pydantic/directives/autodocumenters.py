"""This module contains **autodoc_pydantic**'s autodocumenters."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Callable, ClassVar, Iterable

import sphinx
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from sphinx.ext.autodoc import (
    AttributeDocumenter,
    ClassDocumenter,
    Documenter,
    MethodDocumenter,
)
from sphinx.util.docstrings import prepare_docstring
from sphinx.util.inspect import object_description
from sphinx.util.typing import OptionSpec, get_type_hints

try:
    from sphinx.util.typing import stringify_annotation
except ImportError:
    # fall back to older name for older versions of Sphinx
    from sphinx.util.typing import (  # type: ignore[no-redef]
        stringify as stringify_annotation,
    )

from sphinxcontrib.autodoc_pydantic.directives.options.composites import AutoDocOptions
from sphinxcontrib.autodoc_pydantic.directives.options.definition import (
    OPTIONS_FIELD,
    OPTIONS_MERGED,
    OPTIONS_MODEL,
    OPTIONS_SETTINGS,
    OPTIONS_VALIDATOR,
)
from sphinxcontrib.autodoc_pydantic.directives.options.enums import (
    OptionsFieldDocPolicy,
    OptionsJsonErrorStrategy,
    OptionsSummaryListOrder,
)
from sphinxcontrib.autodoc_pydantic.directives.templates import to_collapsable
from sphinxcontrib.autodoc_pydantic.directives.utility import (
    intercept_type_annotations_py_gt_39,
)
from sphinxcontrib.autodoc_pydantic.inspection import (
    ASTERISK_FIELD_NAME,
    ModelInspector,
    ValidatorFieldMap,
)

if TYPE_CHECKING:
    from docutils.statemachine import StringList
    from pydantic import BaseModel


class PydanticAutoDoc:
    """Composite to provide single namespace to access all **autodoc_pydantic**
    relevant documenter directive functionalities.

    """

    def __init__(self, documenter: Documenter, is_child: bool) -> None:  # noqa: FBT001
        self._documenter = documenter
        self._is_child = is_child
        self._inspect: ModelInspector | None = None
        self._options = AutoDocOptions(self._documenter)
        self._model: type[BaseModel] | None = None

    @property
    def model(self) -> type[BaseModel]:
        """Lazily load pydantic model after initialization. For more, please
        read `inspect` doc string.

        """

        if self._model is not None:
            return self._model

        if self._is_child:
            self._model = self._documenter.parent
        else:
            self._model = self._documenter.object

        return self._model

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

        obj = self._documenter.parent if self._is_child else self._documenter.object

        self._inspect = ModelInspector(obj)
        return self._inspect

    def get_field_name_or_alias(self, field_name: str) -> str:
        """If `field-swap-name-and-alias` is enabled, provide alias (if
        present) for given field.

        """

        if self.options.is_true('field-swap-name-and-alias'):
            return self.inspect.fields.get_alias_or_name(field_name)

        return field_name

    def get_non_inherited_members(self) -> set[str]:
        """Return all member names of autodocumented object which are
        prefiltered to exclude inherited members.

        """
        object_members = self._documenter.get_object_members(want_all=True)[1]
        return {x.__name__ for x in object_members}  # type: ignore[union-attr]

    def get_base_class_names(self) -> list[str]:
        return [x.__name__ for x in self.model.__mro__]

    def resolve_inherited_validator_reference(self, ref: str) -> str:
        """Provide correct validator reference in case validator is inherited
        and explicitly shown in docs via directive option
        `inherited-members`.

        More concretely, inherited validators are not shown from parent class
        unless directive option `inherited-members` is used. The validator
        references may either point to the parent class or the child class.
        This logic is implemented here.

        """
        ref_parts = ref.split('.')
        class_name = ref_parts[-2]

        # early exit if ref class name equals model name -> no inheritance
        if class_name == self.model.__name__:
            return ref

        validator_name = ref_parts[-1]
        base_class_names = self.get_base_class_names()

        is_base_class = class_name in base_class_names
        is_inherited = self.options.exists('inherited-members')
        is_member = validator_name in self.inspect.validators.names

        if is_member and is_base_class and is_inherited:
            ref_parts[-2] = self.model.__name__
            return '.'.join(ref_parts)
        return ref


class PydanticModelDocumenter(ClassDocumenter):
    """Represents specialized Documenter subclass for pydantic models."""

    objtype = 'pydantic_model'
    directivetype = 'pydantic_model'
    priority = 10 + ClassDocumenter.priority
    option_spec = ClassDocumenter.option_spec.copy()
    option_spec.update({**OPTIONS_MODEL, **OPTIONS_MERGED})

    pyautodoc_pass_to_directive = ('model-signature-prefix',)

    pyautodoc_set_default_option = (
        'member-order',
        'undoc-members',
    )

    pyautodoc_prefix = 'model'

    @classmethod
    def can_document_member(
        cls,
        member: Any,  # noqa: ANN401
        membername: str,
        isattr: bool,  # noqa: FBT001
        parent: Any,  # noqa: ANN401
    ) -> bool:
        """Filter only pydantic models."""

        is_val = super().can_document_member(member, membername, isattr, parent)
        is_model = ModelInspector.static.is_pydantic_model(member)
        return is_val and is_model

    def __init__(self, *args) -> None:  # noqa: ANN002
        super().__init__(*args)
        exclude_members = self.options.setdefault('exclude-members', set())
        exclude_members.add('model_fields')
        exclude_members.add('model_config')
        exclude_members.add('model_computed_fields')
        self.pydantic = PydanticAutoDoc(self, is_child=False)

    def document_members(self, *args, **kwargs) -> None:  # noqa: ANN002, ANN003
        """Modify member options before starting to document members."""

        self.pydantic.options.set_members_all()
        if self.options.get('undoc-members') is False:
            self.options.pop('undoc-members')

        if self.pydantic.options.is_false('show-validator-members', prefix=True):
            self.hide_validator_members()

        if self.pydantic.options.is_true('hide-reused-validator', prefix=True):
            self.hide_reused_validators()

        if self.pydantic.options.exists('inherited-members'):
            self.hide_inherited_members()

        super().document_members(*args, **kwargs)

    def hide_inherited_members(self) -> None:
        """If inherited-members is set, make sure that these are excluded from
        the class documenter, too"""

        exclude_members = self.options['exclude-members']
        squash_set = self.options['inherited-members']
        for cl in self.pydantic.model.__mro__:
            if cl.__name__ in squash_set:
                for item in dir(cl):
                    exclude_members.add(item)

    def hide_validator_members(self) -> None:
        """Add validator names to `exclude_members`."""
        validators = self.pydantic.inspect.validators.names
        exclude_members = self.options['exclude-members']
        exclude_members.update(validators)

    def hide_reused_validators(self) -> None:
        """Add reused validators to `exclude_members` option."""

        validators = self.pydantic.inspect.validators
        reused_validators = validators.get_reused_validators_names()
        exclude_members = self.options['exclude-members']
        exclude_members.update(reused_validators)

    def format_signature(self, **kwargs) -> str:  # noqa: ANN003
        """If parameter list is to be hidden, return only empty signature."""

        if self.pydantic.options.is_true('hide-paramlist', prefix=True):
            return ''

        return super().format_signature(**kwargs)

    def add_content(
        self,
        more_content: StringList | None,
        **kwargs,  # noqa: ANN003
    ) -> None:
        """Delegate additional content creation."""
        super().add_content(more_content, **kwargs)

        # do not provide any additional info if documented as attribute
        if self.doc_as_attr:
            return

        if self.pydantic.options.is_true('erdantic-figure', prefix=True):
            self.add_erdantic_figure()

        if self.pydantic.options.is_true('show-json', prefix=True):
            self.add_collapsable_schema()

        if self.pydantic.options.is_true('show-config-summary', prefix=True):
            self.add_config_summary()

        if self.pydantic.options.is_true('show-field-summary', prefix=True):
            self.add_field_summary()

        if self.pydantic.options.is_true('show-validator-summary', prefix=True):
            self.add_validators_summary()

    def add_collapsable_schema(self) -> None:
        """Adds collapse code block containing JSON schema."""

        non_serializable = self.pydantic.inspect.fields.non_json_serializable

        # handle non serializable fields
        strategy = self.pydantic.options.get_value('show-json-error-strategy')
        if non_serializable:
            error_msg = (
                f"JSON schema can't be generated for '{self.fullname}' "
                f"because the following pydantic fields can't be serialized "
                f'properly: {non_serializable}.'
            )

            if strategy == OptionsJsonErrorStrategy.WARN:
                logger = sphinx.util.logging.getLogger(__name__)
                logger.warning(error_msg, location='autodoc_pydantic')
            elif strategy == OptionsJsonErrorStrategy.RAISE:
                raise sphinx.errors.ExtensionError(error_msg)
            elif strategy != OptionsJsonErrorStrategy.COERCE:
                error_msg = (
                    f"Invalid option provided for 'show-json-error-strategy'. "
                    f'Allowed values are f{OptionsJsonErrorStrategy.values()}'
                )
                raise sphinx.errors.ExtensionError(error_msg)

        schema = self.pydantic.inspect.schema.sanitized
        schema_rest = self._convert_json_schema_to_rest(schema)
        source_name = self.get_sourcename()
        for line in schema_rest:
            self.add_line(line, source_name)

    def add_erdantic_figure(self) -> None:
        """Adds an erdantic entity relation diagram to the doc of an
        pydantic model.

        """

        try:
            import erdantic as erd
        except ImportError as e:
            error_msg = (
                'erdantic is not installed, you need to install it before '
                'creating an Entity Relationship Diagram for '
                'f{self.fullname}. See '
                'https://autodoc-pydantic.readthedocs.io/'
                'en/stable/users/installation.html'
            )
            raise ImportError(error_msg) from e

        source_name = self.get_sourcename()
        # Graphviz [DOT language](https://graphviz.org/doc/info/lang.html)
        figure_dot = (
            erd.to_dot(self.object, graph_attr={'label': ''})
            .replace('\t', '   ')
            .split('\n')
        )
        lines_dot = ['   ' + line for line in figure_dot]
        lines = ['.. graphviz::', '', *lines_dot, '']

        if self.pydantic.options.is_true('erdantic-figure-collapsed', prefix=True):
            lines = to_collapsable(
                lines,
                'Show Entity Relationship Diagram',
                'autodoc_pydantic_collapsable_erd',
            )
        for line in lines:
            self.add_line(line, source_name)

    def add_config_summary(self) -> None:
        """Adds summary section describing the model configuration."""

        if not self.pydantic.inspect.config.is_configured:
            return

        cfg_items = self.pydantic.inspect.config.items

        source_name = self.get_sourcename()
        self.add_line(':Config:', source_name)
        for name, value in cfg_items.items():
            line = f'   - **{name}**: *{type(value).__name__} = {value}*'
            self.add_line(line, source_name)
        self.add_line('', source_name)

    def _get_idx_mappings(self, members: Iterable[str]) -> dict[str, int]:
        """Get index positions for given members while respecting
        `OptionsSummaryListOrder`.

        """

        sorted_members = self._sort_summary_list(members)
        return {name: idx for idx, name in enumerate(sorted_members)}

    def _get_reference_sort_func(self, references: list[ValidatorFieldMap]) -> Callable:
        """Helper function to create sorting function for instances of
        `ValidatorFieldMap` which first sorts by validator name and second by
        field name while respecting `OptionsSummaryListOrder`.

        This is used for validator summary section.

        """

        all_fields = [ref.field_name for ref in references]
        all_validators = [ref.validator_name for ref in references]

        idx_validators = self._get_idx_mappings(all_validators)
        idx_fields = self._get_idx_mappings(all_fields)

        def sort_func(reference: ValidatorFieldMap) -> tuple[int, int]:
            return (
                idx_validators.get(reference.validator_name, -1),
                idx_fields.get(reference.field_name, -1),
            )

        return sort_func

    def _get_validator_summary_references(self) -> list[ValidatorFieldMap]:
        """Filter and sort validator-field mappings for validator summary
        section.

        """

        base_class_validators = self._get_base_model_validators()
        inherited_validators = self._get_inherited_validators()
        references = base_class_validators + inherited_validators

        sort_func = self._get_reference_sort_func(references)
        return sorted(references, key=sort_func)

    def _build_validator_summary_rest_line(self, reference: ValidatorFieldMap) -> str:
        """Generates reST line for validator-field mapping with references for
        validator summary section.

        """

        name = self.pydantic.get_field_name_or_alias(reference.field_name)
        validator_ref = self.pydantic.resolve_inherited_validator_reference(
            reference.validator_ref,
        )

        return (
            f'   - '
            f':py:obj:`{reference.validator_name} <{validator_ref}>`'
            f' » '
            f':py:obj:`{name} <{reference.field_ref}>`'
        )

    def add_validators_summary(self) -> None:
        """Adds summary section describing all validators with corresponding
        fields.

        """

        if not self.pydantic.inspect.validators:
            return

        sorted_references = self._get_validator_summary_references()

        source_name = self.get_sourcename()
        self.add_line(':Validators:', source_name)
        for ref in sorted_references:
            line = self._build_validator_summary_rest_line(ref)
            self.add_line(line, source_name)

        self.add_line('', source_name)

    def _get_base_model_validators(self) -> list[ValidatorFieldMap]:
        """Return the validators on the model being documented"""

        result = []

        base_model_fields = set(self._get_base_model_fields())
        base_object = self.object_name
        references = self.pydantic.inspect.references.mappings

        # The validator is considered part of the base_object if
        # the field that is being validated is on the object being
        # documented, if the method that is doing the validating
        # is on that object (even if that method is validating
        # an inherited field)
        for ref in references:
            if ref.field_name in base_model_fields:
                result.append(ref)
            else:
                validator_class = ref.validator_ref.split('.')[-2]
                if validator_class == base_object:
                    result.append(ref)
        return result

    def _get_inherited_validators(self) -> list[ValidatorFieldMap]:
        """Return the validators on inherited fields to be documented,
        if any"""

        if not self.pydantic.options.exists('inherited-members'):
            return []

        squash_set = self.options['inherited-members']
        references = self.pydantic.inspect.references.mappings
        base_object = self.object_name
        already_documented = self._get_base_model_validators()

        result = []
        for ref in references:
            if ref in already_documented:
                continue

            validator_class = ref.validator_ref.split('.')[-2]
            foreign_validator = validator_class != base_object
            not_ignored = validator_class not in squash_set

            if foreign_validator and not_ignored:
                result.append(ref)

        return result

    def add_field_summary(self) -> None:
        """Adds summary section describing all fields."""
        if not self.pydantic.inspect.fields:
            return

        base_class_fields = self._get_base_model_fields()
        inherited_fields = self._get_inherited_fields()
        valid_fields = base_class_fields + inherited_fields

        sorted_fields = self._sort_summary_list(valid_fields)

        source_name = self.get_sourcename()
        self.add_line(':Fields:', source_name)
        for field_name in sorted_fields:
            line = self._get_field_summary_line(field_name)
            self.add_line(line, source_name)

        self.add_line('', source_name)

    def _get_base_model_fields(self) -> list[str]:
        """Returns all field names that are valid members of pydantic model."""

        fields = self.pydantic.inspect.fields.names
        valid_members = self.pydantic.get_non_inherited_members()
        return [field for field in fields if field in valid_members]

    def _get_inherited_fields(self) -> list[str]:
        """Return the inherited fields if inheritance is enabled"""

        if not self.pydantic.options.exists('inherited-members'):
            return []

        fields = self.pydantic.inspect.fields.names
        base_class_fields = self.pydantic.get_non_inherited_members()
        return [field for field in fields if field not in base_class_fields]

    def _get_tagorder(self, name: str) -> int | None:
        """Get tagorder for given `name`."""

        if self.analyzer is None:
            return None

        if name in self.analyzer.tagorder:
            return self.analyzer.tagorder.get(name)

        for base in self.pydantic.get_base_class_names():
            name_with_class = f'{base}.{name}'
            if name_with_class in self.analyzer.tagorder:
                return self.analyzer.tagorder.get(name_with_class)

        if name == ASTERISK_FIELD_NAME:
            return -1

        return None

    def _sort_summary_list(self, names: Iterable[str]) -> list[str]:
        """Sort member names according to given sort order
        `OptionsSummaryListOrder`.

        """
        sort_order = self.pydantic.options.get_value(
            name='summary-list-order', prefix=True, force_availability=True
        )

        if sort_order == OptionsSummaryListOrder.ALPHABETICAL:

            def sort_func(name: str) -> str:
                return name
        elif sort_order == OptionsSummaryListOrder.BYSOURCE:

            def sort_func(name: str) -> int:  # type: ignore[misc]
                tagorder = self._get_tagorder(name)

                # catch cases where field is not found in tagorder
                if tagorder is None:
                    return max(self.analyzer.tagorder.values()) + 1

                return tagorder

        try:
            return sorted(names, key=sort_func)
        except TypeError as e:
            msg = (
                f'Uncaught exception while sorting fields for model '
                f'{self.name} with sort order {sort_order}.'
            )
            raise ValueError(msg).with_traceback(e.__traceback__) from e

    def _get_field_summary_line(self, field_name: str) -> str:
        """Get reST for field summary for given `member_name`."""

        ref_func = self.pydantic.inspect.references.create_model_reference
        name = self.pydantic.get_field_name_or_alias(field_name)
        ref = ref_func(field_name)
        typ = self._stringify_type(field_name)
        return f'   - :py:obj:`{name} ({typ}) <{ref}>`'

    def _stringify_type(self, field_name: str) -> str:
        """Get proper string representation of type for given `member_nane`
        relying on sphinx functionality.

        """

        type_aliases = self.config.autodoc_type_aliases
        annotations = get_type_hints(self.object, None, type_aliases)
        return stringify_annotation(annotations.get(field_name, ''))

    @staticmethod
    def _convert_json_schema_to_rest(schema: dict) -> list[str]:
        """Convert model's schema dict into reST."""
        schema_str = json.dumps(schema, default=str, indent=3)
        lines = [f'   {line}' for line in schema_str.split('\n')]
        lines = ['.. code-block:: json', '', *lines]
        return to_collapsable(
            lines,
            'Show JSON schema',
            'autodoc_pydantic_collapsable_json',
        )


class PydanticSettingsDocumenter(PydanticModelDocumenter):
    """Represents specialized Documenter subclass for pydantic settings."""

    objtype = 'pydantic_settings'
    directivetype = 'pydantic_settings'

    priority = 10 + ClassDocumenter.priority
    option_spec = ClassDocumenter.option_spec.copy()
    option_spec.update({**OPTIONS_SETTINGS, **OPTIONS_MERGED})

    pyautodoc_pass_to_directive = ('settings-signature-prefix',)

    pyautodoc_set_default_option = (
        'member-order',
        'undoc-members',
    )

    pyautodoc_prefix = 'settings'

    def __init__(self, *args) -> None:  # noqa: ANN002
        super().__init__(*args)
        self.options['exclude-members'].add('settings_customise_sources')

    @classmethod
    def can_document_member(
        cls,
        member: Any,  # noqa: ANN401
        membername: str,
        isattr: bool,  # noqa: FBT001
        parent: Any,  # noqa: ANN401
    ) -> bool:
        """Filter only pydantic models."""

        is_val = super().can_document_member(member, membername, isattr, parent)
        if is_val:
            return issubclass(member, BaseSettings)

        return False


class PydanticFieldDocumenter(AttributeDocumenter):
    """Represents specialized Documenter subclass for pydantic fields."""

    objtype = 'pydantic_field'
    directivetype = 'pydantic_field'
    priority = 10 + AttributeDocumenter.priority
    option_spec: ClassVar[OptionSpec] = dict(AttributeDocumenter.option_spec)
    option_spec.update(OPTIONS_FIELD)
    member_order = 0

    pyautodoc_pass_to_directive = (
        'field-signature-prefix',
        'field-show-alias',
        'field-swap-name-and-alias',
    )

    def __init__(self, *args) -> None:  # noqa: ANN002
        super().__init__(*args)
        self.pydantic = PydanticAutoDoc(self, is_child=True)

    @classmethod
    def can_document_member(
        cls,
        member: Any,  # noqa: ANN401
        membername: str,
        isattr: bool,  # noqa: FBT001
        parent: Any,  # noqa: ANN401
    ) -> bool:
        """Filter only pydantic fields."""

        is_valid = super().can_document_member(member, membername, isattr, parent)

        is_field = ModelInspector.static.is_pydantic_field(
            parent=parent.object,
            field_name=membername,
        )

        return is_valid and is_field and isattr

    @property
    def pydantic_field_name(self) -> str:
        """Provide the pydantic field name which refers to the member name of
        the parent pydantic model.

        """

        return self.objpath[-1]

    def add_directive_header(self, sig: str) -> None:
        """Delegate header options."""
        super().add_directive_header(sig)

        self.add_default_value_or_marker()
        self.add_alias()

    @property
    def needs_required_marker(self) -> bool:
        """Indicate if field should be marked as required."""

        field_name = self.pydantic_field_name
        is_required = self.pydantic.inspect.fields.is_required(field_name)
        show_required = self.pydantic.options.is_true('field-show-required')

        return is_required and show_required

    @property
    def needs_optional_marker(self) -> bool:
        """Indicate if field should be marked as optional."""

        field_name = self.pydantic_field_name
        check_func = self.pydantic.inspect.fields.has_default_factory
        has_default_factory = check_func(field_name)
        show_optional = self.pydantic.options.is_true('field-show-optional')

        return has_default_factory and show_optional

    def get_default_value(self) -> str:
        """Gets the default value of pydantic field as reST."""

        field_name = self.pydantic_field_name
        default = self.pydantic.inspect.fields.get(field_name).default
        value = object_description(default)

        return f'   :value: {value}'

    def add_default_value_or_marker(self) -> None:
        """Adds default value or a marker for field being required or optional."""

        sourcename = self.get_sourcename()

        show_default = self.pydantic.options.is_true('field-show-default')
        if self.needs_required_marker:
            self.add_line('   :required:', sourcename)

        elif self.needs_optional_marker:
            self.add_line('   :optional:', sourcename)

        elif show_default:
            self.add_line(self.get_default_value(), sourcename)

    def add_alias(self) -> None:
        """Adds alias directive option."""

        field_name = self.pydantic_field_name
        field = self.pydantic.inspect.fields.get(field_name)
        alias_given = field.alias and field.alias != field_name

        show_alias = self.pydantic.options.is_true('field-show-alias')
        swap = self.pydantic.options.is_true('field-swap-name-and-alias')
        alias_required = show_alias or swap

        if alias_given and alias_required:
            sourcename = self.get_sourcename()
            self.add_line(f'   :alias: {field.alias}', sourcename)

    @property
    def needs_doc_string(self) -> bool:
        """Indicate if docstring from attribute should be added to field."""

        doc_policy = self.pydantic.options.get_value('field-doc-policy')
        return doc_policy != OptionsFieldDocPolicy.DESCRIPTION

    @property
    def needs_description(self) -> bool:
        """Indicate if pydantic field description should be added to field."""

        doc_policy = self.pydantic.options.get_value('field-doc-policy')
        is_enabled = doc_policy in (
            OptionsFieldDocPolicy.BOTH,
            OptionsFieldDocPolicy.DESCRIPTION,
        )

        description = self._get_field_description()
        has_description = bool(description)

        identical_doc = description == self._get_pydantic_sanitized_doc_string()
        is_duplicated = identical_doc and self.needs_doc_string

        return is_enabled and has_description and not is_duplicated

    def add_content(
        self,
        more_content: StringList | None,
        **kwargs,  # noqa: ANN003
    ) -> None:
        """Delegate additional content creation."""

        if self.needs_doc_string:
            super().add_content(more_content, **kwargs)
        if self.needs_description:
            self.add_description()

        if self.pydantic.options.is_true('field-show-constraints'):
            self.add_constraints()

        if self.pydantic.options.is_true('field-list-validators'):
            self.add_validators()

    def add_constraints(self) -> None:
        """Adds section showing all defined constraints."""

        field_name = self.pydantic_field_name
        constraints = self.pydantic.inspect.fields.get_constraints(field_name)

        if constraints:
            source_name = self.get_sourcename()
            self.add_line(':Constraints:', source_name)
            for key, value in constraints.items():
                line = f'   - **{key}** = {value}'
                self.add_line(line, source_name)

            self.add_line('', source_name)

    def _get_field_description(self) -> str:
        """Get field description from schema if present."""

        field_name = self.pydantic_field_name
        func = self.pydantic.inspect.fields.get_property_from_field_info
        return func(field_name, 'description')

    def _get_pydantic_sanitized_doc_string(self) -> str:
        """Helper to get sanitized docstring for pydantic field that
        uses same formatting as pydantic's method to extract the doc
        string for automated field description provisioning.

        """

        docstrings = self.get_doc()
        if not docstrings:
            return ''

        docstring = docstrings[0]  # first element is always the docstring
        without_last = docstring[:-1]  # last element is always empty
        substitute_linebreaks = ['\n\n' if x == '' else x for x in without_last]
        return ''.join(substitute_linebreaks)

    def add_description(self) -> None:
        """Adds description from schema if present."""

        description = self._get_field_description()

        tabsize = self.directive.state.document.settings.tab_width
        lines = prepare_docstring(description, tabsize=tabsize)
        source_name = self.get_sourcename()
        for line in lines:
            self.add_line(line, source_name)

    def add_validators(self) -> None:
        """Add section with all validators that process this field."""

        field_name = self.pydantic_field_name
        func = self.pydantic.inspect.references.filter_by_field_name
        references = func(field_name)
        sorted_references = sorted(references, key=lambda x: x.validator_name)

        if not references:
            return

        source_name = self.get_sourcename()
        self.add_line(':Validated by:', source_name)
        for reference in sorted_references:
            resolver = self.pydantic.resolve_inherited_validator_reference
            ref = resolver(reference.validator_ref)
            line = f'   - :py:obj:`{reference.validator_name} <{ref}>`'
            self.add_line(line, source_name)

        self.add_line('', source_name)

    def add_line(self, line: str, source: str, *lineno: int) -> None:
        """Intercept added rst lines to handle edge cases such as correct
        string representation for annotated types in python < 3.9.

        """

        line = intercept_type_annotations_py_gt_39(line)
        super().add_line(line, source, *lineno)


class PydanticValidatorDocumenter(MethodDocumenter):
    """Represents specialized Documenter subclass for pydantic validators."""

    objtype = 'pydantic_validator'
    directivetype = 'pydantic_validator'
    member_order = 50
    priority = 10 + MethodDocumenter.priority
    option_spec = MethodDocumenter.option_spec.copy()
    option_spec.update(OPTIONS_VALIDATOR)

    pyautodoc_pass_to_directive = (
        'validator-signature-prefix',
        'validator-replace-signature',
        'field-swap-name-and-alias',
    )

    def __init__(self, *args: Any) -> None:  # noqa: ANN401
        super().__init__(*args)
        self.pydantic = PydanticAutoDoc(self, is_child=True)

    @classmethod
    def can_document_member(
        cls,
        member: Any,  # noqa: ANN401
        membername: str,
        isattr: bool,  # noqa: FBT001
        parent: Any,  # noqa: ANN401
    ) -> bool:
        """Filter only pydantic validators."""

        is_val = super().can_document_member(member, membername, isattr, parent)
        is_validator = ModelInspector.static.is_validator_by_name(
            membername, parent.object
        )
        return is_val and is_validator

    def format_args(self, **kwargs: Any) -> str:  # noqa: ANN401
        """Return empty arguments if validator should be replaced."""

        if self.pydantic.options.is_true('validator-replace-signature'):
            return ''

        return super().format_args(**kwargs)

    def add_content(
        self,
        more_content: StringList | None,
        **kwargs,  # noqa: ANN003
    ) -> None:
        """Optionally show validator content."""

        super().add_content(more_content, **kwargs)

        if self.pydantic.options.is_true('validator-list-fields'):
            self.add_field_list()

    def _build_field_list_rest_line(self, reference: ValidatorFieldMap) -> str:
        """Generates reST line for field reference for field list section."""

        name = self.pydantic.get_field_name_or_alias(reference.field_name)
        return f'   - :py:obj:' f'`{name} ' f'<{reference.field_ref}>`'

    def add_field_list(self) -> None:
        """Adds a field list with all fields that are validated by this
        validator.

        """

        func = self.pydantic.inspect.references.filter_by_validator_name
        references = func(self.object_name)

        if not references:
            return

        source_name = self.get_sourcename()
        self.add_line(':Validates:', source_name)

        for reference in references:
            line = self._build_field_list_rest_line(reference)
            self.add_line(line, source_name)

        self.add_line('', source_name)
