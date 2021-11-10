"""This module contains the inspection functionality for pydantic models. It
is used to retrieve relevant information about fields, validators, config and
schema of pydantical models.

"""

import pydoc
from itertools import chain
from typing import NamedTuple, List, Dict, Any, Set, TypeVar, Iterator, Type

import pydantic
from pydantic import BaseModel, create_model
from pydantic.class_validators import Validator
from pydantic.fields import ModelField, UndefinedType
from pydantic.schema import get_field_schema_validations
from sphinx.addnodes import desc_signature

ASTERISK_FIELD_NAME = "all fields"


class ValidatorFieldMap(NamedTuple):
    """Contains single mapping of a pydantic validator and field.

    """

    field_name: str
    """Name of the field."""

    validator_name: str
    """Name of the validator."""

    model_ref: str
    """Reference corresponding parent pydantic model."""

    def _get_ref(self, name: str) -> str:
        """Create reference for given `name` while prefixing it with model
        path.

        """

        return f"{self.model_ref}.{name}"

    @property
    def field_ref(self):
        """Reference to field..

        """

        return self._get_ref(self.field_name)

    @property
    def validator_ref(self):
        """Reference to validator.

        """

        return self._get_ref(self.validator_name)


class BaseInspectionComposite:
    """Serves as base class for inspector composites which are coupled to
    `ModelInspector` instances. Each composite provides a separate namespace to
    handle different areas of pydantic models (e.g. fields and validators).

    """

    def __init__(self, parent: 'ModelInspector'):
        self._parent = parent
        self.model = self._parent.model


class FieldInspector(BaseInspectionComposite):
    """Provide namespace for inspection methods for fields of pydantic models.

    """

    def __init__(self, parent: 'ModelInspector'):
        super().__init__(parent)
        self.attribute = self.model.__fields__

    @property
    def validator_names(self) -> Dict[str, Set[str]]:
        """Return mapping between all field names (keys) and their
        corresponding validator names (values).

        """

        standard = self.validator_names_standard
        root = self.validator_names_root

        # add root names
        complete = standard.copy()
        asterisk = complete.get("*", set()).union(root["*"])
        complete["*"] = asterisk

        return complete

    @property
    def validator_names_root(self) -> Dict[str, Set[str]]:
        """Return mapping between all field names (keys) and their
        corresponding validator names (values) for root validators only.

        """

        root_validator_names = self._parent.validators.names_root_validators
        return {"*": root_validator_names}

    @property
    def validator_names_standard(self) -> Dict[str, List[str]]:
        """Return mapping between all field names (keys) and their
        corresponding validator names (values) for standard validators only.

        Please be aware, the asterisk field name `*` is used to represent all
        fields.

        """

        validators_attribute = self._parent.validators.attribute
        name_getter = self._parent.validators.get_names_from_wrappers

        return {field: name_getter(validators)
                for field, validators in validators_attribute.items()}

    @property
    def names(self) -> List[str]:
        """Return field names while keeping ordering.

        """

        return list(self.attribute.keys())

    def get(self, name: str) -> ModelField:
        """Get the instance of `ModelField` for given field `name`.

        """

        return self.attribute[name]

    def get_property_from_field_info(self, field_name: str,
                                     property_name: str) -> Any:
        """Get specific property value from pydantic's field info.

        """

        field = self.get(field_name)
        return getattr(field.field_info, property_name, None)

    def get_constraints(self, field_name: str) -> Dict[str, Any]:
        """Get constraints for given `field_name`.

        """

        field = self.get(field_name)
        constraints = get_field_schema_validations(field)
        return {key: value for key, value in constraints.items()
                if key not in {"env_names", "env"}}

    def is_required(self, field_name: str) -> bool:
        """Check if a given pydantic field is required/mandatory. Returns True,
        if a value for this field needs to provided upon model creation.

        """

        types_to_check = (UndefinedType, type(...))
        default_value = self.get_property_from_field_info(
            field_name=field_name,
            property_name="default")

        return isinstance(default_value, types_to_check)

    def is_json_serializable(self, field_name: str) -> bool:
        """Check if given pydantic field is JSON serializable by calling
        pydantic's `model.json()` method. Custom objects might not be
        serializable and hence would break JSON schema generation.

        """

        field = self.get(field_name)

        class Cfg:
            arbitrary_types_allowed = True

        try:
            field_args = (field.type_, field.default)
            model = create_model("_", test_field=field_args, Config=Cfg)
            model.schema()
            return True
        except Exception:
            return False

    @property
    def non_json_serializable(self) -> List[str]:
        """Get all fields that can't be safely JSON serialized.

        """

        return [name for name in self.names
                if not self.is_json_serializable(name)]

    def __bool__(self):
        """Equals to False if no fields are present.

        """

        return bool(self.attribute)


class ValidatorInspector(BaseInspectionComposite):
    """Provide namespace for inspection methods for validators of pydantic
    models.

    """

    def __init__(self, parent: 'ModelInspector'):
        super().__init__(parent)
        self.attribute: Dict = self.model.__validators__

    @staticmethod
    def get_names_from_wrappers(validators: Iterator[Validator]) -> Set[str]:
        """Return the actual validator names as defined in the class body from
        list of pydantic validator wrappers.

        Parameters
        ----------
        validators: list
            Wrapper objects for pydantic validators.

        """

        return {validator.func.__name__ for validator in validators}

    @property
    def names_root_validators(self) -> Set[str]:
        """Return all names of root validators.

        """

        def get_name_pre_root(validators):
            return {validator.__name__ for validator in validators}

        def get_name_post_root(validators):
            return {validator[1].__name__ for validator in validators}

        pre_root = get_name_pre_root(self.model.__pre_root_validators__)
        post_root = get_name_post_root(self.model.__post_root_validators__)

        return pre_root.union(post_root)

    @property
    def names_asterisk_validators(self) -> Set[str]:
        """Return all names of asterisk validators. Asterisk are defined as
        validators, that process all availble fields. They consist of root
        validators and validators with the `*` field target.

        """

        asterisk_validators = self.attribute.get("*", [])
        asterisk = self.get_names_from_wrappers(asterisk_validators)
        return asterisk.union(self.names_root_validators)

    @property
    def names_standard_validators(self) -> Set[str]:
        """Return all names of standard validators which do not process all
        fields at once (in contrast to asterisk validators).

        """

        validator_wrappers = chain.from_iterable(self.attribute.values())
        names_all_validators = self.get_names_from_wrappers(validator_wrappers)
        return names_all_validators.difference(self.names_asterisk_validators)

    @property
    def names(self) -> Set[str]:
        """Return names of all validators of pydantic model.

        """

        asterisks = self.names_asterisk_validators
        standard = self.names_standard_validators

        return asterisks.union(standard)

    def is_asterisk(self, name: str) -> bool:
        """Check if provided validator `name` references an asterisk validator.

        Parameters
        ----------
        name: str
            Name of the validator.

        """

        return name in self.names_asterisk_validators

    def __bool__(self):
        """Equals to False if no validators are present.

        """

        return bool(self.attribute)


class ConfigInspector(BaseInspectionComposite):
    """Provide namespace for inspection methods for config class of pydantic
    models.

    """

    def __init__(self, parent: 'ModelInspector'):
        super().__init__(parent)
        self.attribute: Dict = self.model.Config

    @property
    def is_configured(self) -> bool:
        """Check if pydantic model config was explicitly configured. If not,
        it defaults to the standard configuration provided by pydantic and
        typically does not required documentation.

        """

        cfg = self.attribute

        is_main_config = cfg is pydantic.main.BaseConfig
        is_setting_config = cfg is pydantic.env_settings.BaseSettings.Config
        is_default_config = is_main_config or is_setting_config

        return not is_default_config

    @property
    def items(self) -> Dict:
        """Return all non private (without leading underscore `_`) items of
        pydantic configuration class.

        """

        return {key: getattr(self.attribute, key)
                for key in dir(self.attribute)
                if not key.startswith("_")}


class ReferenceInspector(BaseInspectionComposite):
    """Provide namespace for inspection methods for creating references
    mainly between pydantic fields and validators.

    Importantly, `mappings` provides the set of all `ValidatorFieldMap`
    instances which contain all references between fields and validators.

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        mappings_asterisk = self._create_mappings_asterisk()
        mappings_standard = self._create_mappings_standard()
        self.mappings = mappings_standard.union(mappings_asterisk)

    @property
    def model_path(self) -> str:
        """Retrieve the full path of the model.

        """

        return f"{self.model.__module__}.{self.model.__name__}"

    def create_model_reference(self, name: str) -> str:
        """Create reference for given attribute `name` returning full path
        including the model path.

        """

        return f"{self.model_path}.{name}"

    def _create_mappings_asterisk(self) -> Set[ValidatorFieldMap]:
        """Generate `ValidatorFieldMap` instances for asterisk validators.

        """

        field_validator_names = self._parent.fields.validator_names
        asterisk_validators = field_validator_names.pop("*")
        model_path = self.model_path

        return {ValidatorFieldMap(field_name=ASTERISK_FIELD_NAME,
                                  validator_name=validator,
                                  model_ref=model_path)
                for validator in asterisk_validators}

    def _create_mappings_standard(self) -> Set[ValidatorFieldMap]:
        """Generate `ValidatorFieldMap` instances for asterisk validators.

        """

        is_asterisk = self._parent.validators.is_asterisk
        field_validator_names = self._parent.fields.validator_names
        model_path = self.model_path

        references = set()
        for field, validators in field_validator_names.items():
            refs = {ValidatorFieldMap(field_name=field,
                                      validator_name=validator,
                                      model_ref=model_path)
                    for validator in validators
                    if not is_asterisk(validator)}
            references.update(refs)

        return references

    def filter_by_validator_name(self, name: str) -> List[ValidatorFieldMap]:
        """Return mappings for given validator `name`.

        """

        return [mapping for mapping in self.mappings
                if mapping.validator_name == name]

    def filter_by_field_name(self, name: str) -> List[ValidatorFieldMap]:
        """Return mappings for given field `name`.

        """

        return [mapping for mapping in self.mappings
                if mapping.field_name in (name, ASTERISK_FIELD_NAME)]


class SchemaInspector(BaseInspectionComposite):
    """Provide namespace for inspection methods for general properties of
    pydantic models.

    """

    @property
    def sanitized(self) -> Dict:
        """Get model's `schema` while handling non serializable fields. Such
        fields will be replaced by TypeVars.

        """

        try:
            return self.model.schema()
        except (TypeError, ValueError):
            new_model = self.create_sanitized_model()
            return new_model.schema()

    def create_sanitized_model(self) -> BaseModel:
        """Generates a new pydantic model from the original one while
        substituting invalid fields with typevars.

        """

        invalid_fields = self._parent.fields.non_json_serializable
        new = {name: (TypeVar(name), None) for name in invalid_fields}
        return create_model(self.model.__name__, __base__=self.model, **new)


class StaticInspector:
    """Namespace under `ModelInspector` for static methods.

    """

    @staticmethod
    def is_pydantic_model(obj: Any) -> bool:
        """Determine if object is a valid pydantic model.

        """

        try:
            return issubclass(obj, BaseModel)
        except TypeError:
            return False

    @classmethod
    def is_validator_by_name(cls, name: str, obj: Any) -> bool:
        """Determine if a validator is present under provided `name` for given
        `model`.

        """

        if cls.is_pydantic_model(obj):
            inspector = ModelInspector(obj)
            return name in inspector.validators.names
        return False


class ModelInspector:
    """Provides inspection functionality for pydantic models.

    """

    static = StaticInspector

    def __init__(self, model: Type[BaseModel]):
        self.model = model
        self.config = ConfigInspector(self)
        self.schema = SchemaInspector(self)
        self.fields = FieldInspector(self)
        self.validators = ValidatorInspector(self)
        self.references = ReferenceInspector(self)

    @classmethod
    def from_signode(cls, signode: desc_signature) -> "ModelInspector":
        """Create instance from a `signode` as used within sphinx directives.

        """

        model_name = signode["fullname"].split(".")[0]
        model = pydoc.locate(f"{signode['module']}.{model_name}")
        return cls(model)
