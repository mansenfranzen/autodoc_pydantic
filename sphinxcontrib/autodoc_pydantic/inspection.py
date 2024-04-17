"""This module contains the inspection functionality for pydantic models. It
is used to retrieve relevant information about fields, validators, config and
schema of pydantical models.

"""

from __future__ import annotations

import inspect
import itertools
import pydoc
import warnings
from collections import defaultdict
from typing import TYPE_CHECKING, Any, Callable, NamedTuple, TypeGuard, TypeVar

from pydantic import BaseModel, ConfigDict, PydanticInvalidForJsonSchema, create_model
from pydantic_settings import BaseSettings

ASTERISK_FIELD_NAME = 'all fields'

if TYPE_CHECKING:
    from pydantic.fields import FieldInfo
    from sphinx.addnodes import desc_signature


class ValidatorAdapter(NamedTuple):
    """Provide standardized interface to pydantic's validator objects with
    additional metadata (e.g. root validator) for internal usage in
    autodoc_pydantic.

    """

    func: Callable

    @property
    def name(self) -> str:
        """Return the validators function name."""
        return self.func.__name__

    @property
    def class_name(self) -> str | None:
        """Return the validators class name. It might be None if validator
        is not bound to a class.

        """

        qualname = self.func.__qualname__.split('.')
        if len(qualname) > 1:
            return qualname[-2]

        return None

    @property
    def module(self) -> str:
        """Return the validators module name."""

        return self.func.__module__

    @property
    def object_path(self) -> str:
        """Return the fully qualified object path of the validators function."""

        return f'{self.func.__module__}.{self.func.__qualname__}'

    def __hash__(self) -> int:
        return id(f'{self}')


class ValidatorFieldMap(NamedTuple):
    """Contains single mapping of a pydantic validator and field."""

    field_name: str
    """Name of the field."""

    validator_name: str
    """Name of the validator."""

    field_ref: str
    """Reference to field."""

    validator_ref: str
    """Reference to validataor."""


class BaseInspectionComposite:
    """Serves as base class for inspector composites which are coupled to
    `ModelInspector` instances. Each composite provides a separate namespace to
    handle different areas of pydantic models (e.g. fields and validators).

    """

    def __init__(self, parent: ModelInspector) -> None:
        self._parent: ModelInspector = parent
        self.model = self._parent.model


class FieldInspector(BaseInspectionComposite):
    """Provide namespace for inspection methods for fields of pydantic models."""

    def __init__(self, parent: ModelInspector) -> None:
        super().__init__(parent)
        # json schema can reliably be created only at model level
        self.attribute = self.model.model_fields

    @property
    def names(self) -> list[str]:
        """Return field names while keeping ordering."""

        return list(self.attribute.keys())

    def get(self, name: str) -> FieldInfo:
        """Get the instance of `FieldInfo` for given field `name`."""

        return self.attribute[name]

    def get_alias_or_name(self, field_name: str) -> str:
        """Get the alias of a pydantic field if given. Otherwise, return the
        field name.

        """

        if field_name == ASTERISK_FIELD_NAME:
            return field_name

        alias = self.get(field_name).alias
        if alias is not None:
            return alias

        return field_name

    def get_property_from_field_info(self, field_name: str, property_name: str) -> Any:  # noqa: ANN401
        """Get specific property value from pydantic's field info."""

        field = self.get(field_name)
        return getattr(field, property_name, None)

    @staticmethod
    def _get_meta_items(meta_class: Any) -> dict[str, str]:  # noqa: ANN401
        """Helper method to extract constraint names and values from different
        pydantic Metadata objects such as `pydantic.types.Strict`.

        """

        try:
            return meta_class.__dataclass_fields__
        except AttributeError:
            return meta_class.__dict__

    def get_constraints(self, field_name: str) -> dict[str, Any]:
        """Get constraints for given `field_name`."""

        metadata = self.model.model_fields[field_name].metadata
        available = [meta for meta in metadata if meta is not None]

        return {
            key: getattr(meta, key)
            for meta in available
            for key, value in self._get_meta_items(meta).items()
            if getattr(meta, key) is not None
        }

    def is_required(self, field_name: str) -> bool:
        """Check if a given pydantic field is required/mandatory. Returns True,
        if a value for this field needs to provided upon model creation.

        """

        return self.get(field_name).is_required()

    def has_default_factory(self, field_name: str) -> bool:
        """Check if field has a `default_factory` being set. This information
        is used to determine if a pydantic field is optional or not.

        """

        return self.get(field_name).default_factory is not None

    def is_json_serializable(self, field_name: str) -> bool:
        """Check if given pydantic field is JSON serializable by calling
        pydantic's `model.schema()` method. Custom objects might not be
        serializable and hence would break JSON schema generation.

        """

        field = self.get(field_name)
        return self._is_json_serializable(field)

    @classmethod
    def _is_json_serializable(cls, field: FieldInfo) -> bool:
        """Ensure JSON serializability for given pydantic `FieldInfo`."""
        # hide user warnings in sphinx output
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            return cls._test_field_serializabiltiy(field)

    @staticmethod
    def _test_field_serializabiltiy(field: FieldInfo) -> bool:
        """Test JSON serializability for given pydantic `FieldInfo`."""

        model_config = ConfigDict(arbitrary_types_allowed=True)

        try:
            field_args = (field.annotation, field.default)
            model = create_model('_', __config__=model_config, test_field=field_args)
            model.model_json_schema()

        except Exception:  # noqa: BLE001
            return False

        else:
            return True

    @property
    def non_json_serializable(self) -> list[str]:
        """Get all fields that can't be safely JSON serialized."""

        return [name for name in self.names if not self.is_json_serializable(name)]

    def __bool__(self) -> bool:
        """Equals to False if no fields are present."""

        return bool(self.attribute)


class ValidatorInspector(BaseInspectionComposite):
    """Provide namespace for inspection methods for validators of pydantic
    models.

    """

    def __init__(self, parent: ModelInspector) -> None:
        super().__init__(parent)

    @property
    def values(self) -> set[ValidatorAdapter]:
        """Returns set of all available validators."""

        all_validators = self._parent.field_validator_mappings.values()
        flattened = itertools.chain.from_iterable(all_validators)
        return set(flattened)

    def get_reused_validators_names(self) -> list[str]:
        """Identify all reused validators. This is done implicitly by relying
        on the fact the reused validators are registered as unbound functions
        instead of bound methods.

        """

        validators = self.model.__pydantic_decorators__.field_validators
        return [
            x.cls_var_name for x in validators.values() if inspect.isfunction(x.func)
        ]

    @property
    def names(self) -> set[str]:
        """Return names of all validators of pydantic model."""

        return {validator.name for validator in self.values}

    def __bool__(self) -> bool:
        """Equals to False if no validators are present."""

        return bool(self.values)


class ConfigInspector(BaseInspectionComposite):
    """Provide namespace for inspection methods for config class of pydantic
    models.

    """

    def __init__(self, parent: ModelInspector) -> None:
        super().__init__(parent)
        self.items = self._get_values_per_type()

    def _get_values_per_type(self) -> dict[str, Any]:
        """Get the configuration values from any pydantic model.

        Behavior of configuration values varies between `BaseModel` and
        BaseSettings`. For `BaseModel`, if no configs are provided, then
        model_config` is empty. However, for `BaseSettings`, `model_config`
        contains a predefined set of values. This needs to be handled properly
        otherwise the `BaseSettings` always show up a lot of irrelevant default
        values. Hence, the default values are removed.

        """

        cfg = self.model.model_config

        if issubclass(self.model, BaseSettings):
            default = tuple(BaseSettings.model_config.items())
            available = tuple(cfg.items())
            result = [given for given in available if given not in default]
            values = dict(result)
        else:
            values = dict(cfg)

        return values

    @property
    def is_configured(self) -> bool:
        """Check if pydantic model config was explicitly configured."""

        return bool(self.items)


class ReferenceInspector(BaseInspectionComposite):
    """Provide namespace for inspection methods for creating references
    mainly between pydantic fields and validators.

    Importantly, `mappings` provides the set of all `ValidatorFieldMap`
    instances which contain all references between fields and validators.

    """

    def __init__(self, *args, **kwargs) -> None:  # noqa: ANN002, ANN003
        super().__init__(*args, **kwargs)
        self.mappings = self._create_mappings()

    @property
    def model_path(self) -> str:
        """Retrieve the full path of the model."""

        return f'{self.model.__module__}.{self.model.__name__}'

    def create_model_reference(self, name: str) -> str:
        """Create reference for given attribute `name` returning full path
        including the model path.

        """

        return f'{self.model_path}.{name}'

    def _create_mappings(self) -> set[ValidatorFieldMap]:
        """Generate reference mappings between validators and corresponding
        fields.

        """
        mappings = set()

        for field, validators in self._parent.field_validator_mappings.items():
            is_aserisk = field == '*'
            field_name = ASTERISK_FIELD_NAME if is_aserisk else field

            for validator in validators:
                mapping = ValidatorFieldMap(
                    field_name=field_name,
                    field_ref=f'{self.model_path}.{field_name}',
                    validator_name=validator.name,
                    validator_ref=validator.object_path,
                )
                mappings.add(mapping)

        return mappings

    def filter_by_validator_name(self, name: str) -> list[ValidatorFieldMap]:
        """Return mappings for given validator `name`."""

        return [mapping for mapping in self.mappings if mapping.validator_name == name]

    def filter_by_field_name(self, name: str) -> list[ValidatorFieldMap]:
        """Return mappings for given field `name`."""

        return [
            mapping
            for mapping in self.mappings
            if mapping.field_name in (name, ASTERISK_FIELD_NAME)
        ]


class SchemaInspector(BaseInspectionComposite):
    """Provide namespace for inspection methods for general properties of
    pydantic models.

    """

    @property
    def sanitized(self) -> dict:
        """Get model's `schema` while handling non serializable fields. Such
        fields will be replaced by TypeVars.

        """

        try:
            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                schema = self.model.model_json_schema()

        except (TypeError, ValueError, PydanticInvalidForJsonSchema):
            new_model = self.create_sanitized_model()
            schema = new_model.model_json_schema()

        keys_order = ['title', 'description', 'type', 'properties']
        reordered_schema = {k: schema[k] for k in keys_order if k in schema}
        reordered_schema.update(schema)
        return reordered_schema

    def create_sanitized_model(self) -> type[BaseModel]:
        """Generates a new pydantic model from the original one while
        substituting invalid fields with typevars.

        """

        invalid_fields = self._parent.fields.non_json_serializable
        new: dict[str, Any] = {name: (TypeVar(name), None) for name in invalid_fields}
        return create_model(self.model.__name__, __base__=self.model, **new)


class StaticInspector:
    """Namespace under `ModelInspector` for static methods."""

    @staticmethod
    def is_pydantic_model(obj: Any) -> TypeGuard[type[BaseModel]]:  # noqa: ANN401
        """Determine if object is a valid pydantic model."""

        try:
            return issubclass(obj, BaseModel)
        except TypeError:
            return False

    @classmethod
    def is_pydantic_field(cls, parent: Any, field_name: str) -> bool:  # noqa: ANN401
        """Determine if given `field` is a pydantic field."""

        if not cls.is_pydantic_model(parent):
            return False

        return field_name in parent.model_fields

    @classmethod
    def is_validator_by_name(cls, name: str, obj: Any) -> bool:  # noqa: ANN401
        """Determine if a validator is present under provided `name` for given
        `model`.

        """

        if cls.is_pydantic_model(obj):
            inspector = ModelInspector(obj)
            return name in inspector.validators.names
        return False


class ModelInspector:
    """Provides inspection functionality for pydantic models."""

    static = StaticInspector

    def __init__(self, model: type[BaseModel]) -> None:
        self.model = model
        self.field_validator_mappings = self.get_field_validator_mapping()

        self.config = ConfigInspector(self)
        self.schema = SchemaInspector(self)
        self.fields = FieldInspector(self)
        self.validators = ValidatorInspector(self)
        self.references = ReferenceInspector(self)

    def get_field_validator_mapping(self) -> dict[str, list[ValidatorAdapter]]:
        """Collect all available validators keyed by their corresponding
        fields including post/pre root validators.

        Validators are wrapped into `ValidatorAdapters` to provide uniform
        interface within autodoc_pydantic.

        """

        mapping: dict[str, list[Any]] = defaultdict(list)
        decorators = self.model.__pydantic_decorators__

        # field validators
        for field_validator in decorators.field_validators.values():
            for field in field_validator.info.fields:
                mapping[field].append(ValidatorAdapter(func=field_validator.func))

        # model validators
        for model_validator in decorators.model_validators.values():
            mapping['*'].append(ValidatorAdapter(func=model_validator.func))

        return mapping

    @classmethod
    def from_child_signode(cls, signode: desc_signature) -> ModelInspector:
        """Create instance from a child `signode` as used within sphinx
        directives.

        """

        model_path_parts = signode['fullname'].split('.')[:-1]
        model_path = '.'.join(model_path_parts)
        model = pydoc.locate(f"{signode['module']}.{model_path}")

        if not cls.static.is_pydantic_model(model):
            err = (
                f"Signode with full name {signode['fullname']} and extracted "
                f"model path does reference pydantic model. "
            )

            raise ValueError(err)

        return cls(model)
