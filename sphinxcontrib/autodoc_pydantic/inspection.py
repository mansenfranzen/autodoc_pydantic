"""This module contains inspection functionality for pydantic models.

"""
import functools
import pydoc
from collections import defaultdict
from itertools import chain
from typing import NamedTuple, Tuple, List, Dict, Any, Set, TypeVar

from pydantic import BaseModel, create_model
from pydantic.fields import ModelField, UndefinedType
from sphinx.addnodes import desc_signature


def is_pydantic_model(obj: Any) -> bool:
    """Determine if object is a valid pydantic model.

    """

    if isinstance(obj, type):
        return issubclass(obj, BaseModel)
    return False


def is_validator_by_name(name: str, obj: Any) -> bool:
    """Determine if a validator is present under provided `name` for given
    `model`.

    """

    if is_pydantic_model(obj):
        wrapper = ModelWrapper.factory(obj)
        return name in wrapper.get_validator_names()
    return False


def is_serializable(field: ModelField) -> bool:
    """Check of pydantic field is schema serializable.

    """

    class Cfg:
        arbitrary_types_allowed = True

    try:
        create_model("_", t=(field.type_, field.default), Config=Cfg).schema()
        return True
    except Exception:
        return False


class NamedRef(NamedTuple):
    """Contains the name and full path of an object.

    """

    name: str
    ref: str


class ValidatorFieldMap(NamedTuple):
    """Contains single mapping of a pydantic validator and field.

    """

    validator: NamedRef
    field: NamedRef
    is_asterisk: bool


class ModelWrapper:
    """Wraps pydantic models and provides additional inspection functionality
    on top of it.

    Parameters
    ----------
    model: pydantic.BaseModel
        The pydantic model for which validators field validator_field_mappings
        will be extracted.

    """

    CACHED: Dict[int, "ModelWrapper"] = {}

    def __init__(self, model: BaseModel):
        self.model = model
        self.field_validator_names = self.get_field_validator_names()
        self.field_validator_mappings = self.generate_field_validator_map()

    def get_model_path(self) -> str:
        """Retrieve the full path to given model.

        """

        return f"{self.model.__module__}.{self.model.__name__}"

    def get_field_validator_names(self) -> Dict[str, List[str]]:
        """Retrieve function names from pydantic Validator wrapper objects.

        """

        def get_name(validators):
            return [validator.func.__name__ for validator in validators]

        validators = self.model.__validators__.items()
        field_names = {field: get_name(validators) for field, validators in
                       validators}

        field_names.setdefault("*", [])
        field_names["*"].extend(self.get_names_from_root_validators())
        return field_names

    def get_names_from_root_validators(self) -> List[str]:
        """Retrieve function names from pydantic root validator objects.

        """

        def get_name(validators):
            return [validator[1].__name__ for validator in validators]

        pre_root = get_name(self.model.__pre_root_validators__)
        post_root = get_name(self.model.__post_root_validators__)

        return pre_root + post_root

    def get_fields(self) -> Dict[str, ModelField]:
        """Retrieves all fields from pydantic model.

        """

        try:
            return self.model.__fields__
        except KeyError:
            return {}

    def get_validator_names(self) -> Set[str]:
        """Collect all names of the validator functions.

        """

        names = self.get_field_validator_names().values()
        return set(chain.from_iterable(names))

    def get_reference(self, name: str):
        """Create reference path to given name.

        """

        return f"{self.get_model_path()}.{name}"

    def generate_mappings_asterisk_validators(self) -> List[ValidatorFieldMap]:
        """Generate references between fields and asterisk validators.

        """

        mappings = []
        if "*" not in self.field_validator_names:
            return []

        fields = self.field_validator_names.keys()

        for name in self.field_validator_names["*"]:
            for field in fields:
                _validator = NamedRef(
                    name=name,
                    ref=self.get_reference(name))
                _field = NamedRef(
                    name=field,
                    ref=self.get_reference(field)
                )
                mapping = ValidatorFieldMap(
                    validator=_validator,
                    field=_field,
                    is_asterisk=True
                )
                mappings.append(mapping)

        return mappings

    def generate_mappings_standard_validators(self) -> List[ValidatorFieldMap]:
        """Generate references between fields and standard validators.

        """

        items = self.field_validator_names.items()
        standard_validators = {field: validator
                               for field, validator in items
                               if field != "*"}
        to_ignore = set(self.field_validator_names.get("*", []))

        mappings = []
        for field, validators in standard_validators.items():
            for name in validators:
                if name in to_ignore:
                    continue

                _validator = NamedRef(
                    name=name,
                    ref=self.get_reference(name))
                _field = NamedRef(
                    name=field,
                    ref=self.get_reference(field)
                )
                mapping = ValidatorFieldMap(
                    validator=_validator,
                    field=_field,
                    is_asterisk=False
                )
                mappings.append(mapping)

        return mappings

    def generate_field_validator_map(self) -> Tuple[ValidatorFieldMap]:
        """Inspects pydantic model and gathers all validator_field_mappings
        between validators and fields.

        """

        asterisk = self.generate_mappings_asterisk_validators()
        standard = self.generate_mappings_standard_validators()

        return tuple(asterisk + standard)

    @functools.lru_cache(maxsize=128)
    def get_asterisk_validators(self) -> Dict[str, ValidatorFieldMap]:
        """Get single validator field mapping per asterisk validator.

        """

        return {mapping.validator.name: mapping
                for mapping in self.field_validator_mappings
                if mapping.is_asterisk}

    @functools.lru_cache(maxsize=128)
    def get_standard_validators(self) -> Dict[str, List[ValidatorFieldMap]]:
        """Get all validator field validator_field_mappings for standard
        validators.

        """

        result = defaultdict(list)
        for mapping in self.field_validator_mappings:
            if mapping.is_asterisk:
                continue
            result[mapping.validator.name].append(mapping)

        return result

    @classmethod
    def factory(cls, model: BaseModel) -> "ModelWrapper":
        """Factory with caching ability to prevent recreation of new instances.

        """

        model_id = id(model)
        result = cls.CACHED.get(model_id)
        if result:
            return result

        mapping = ModelWrapper(model)
        cls.CACHED[model_id] = mapping
        return mapping

    @classmethod
    def from_signode(cls, signode: desc_signature) -> "ModelWrapper":
        """Create instance from a `signode` as used within sphinx directives.

        """

        model_name = signode["fullname"].split(".")[0]
        model = pydoc.locate(f"{signode['module']}.{model_name}")
        return cls.factory(model)

    def get_fields_for_validator(self,
                                 validator_name: str) -> List[NamedRef]:
        """Return all fields for a given validator.

        """

        asterisk = self.get_asterisk_validators().get(validator_name)
        if asterisk:
            return [NamedRef("all fields", self.get_model_path())]

        else:
            return [NamedRef(x.field.name, x.field.ref)
                    for x in self.get_standard_validators()[validator_name]]

    def get_validators_for_field(self, field_name: str) -> List[NamedRef]:
        """Return all validators for given field.

        """

        return [x.validator for x in self.field_validator_mappings
                if x.field.name == field_name]

    def get_named_references_for_validators(self) -> List[NamedRef]:
        """Return named references for all validators.

        """

        unique = {mapping.validator.name: mapping
                  for mapping in self.field_validator_mappings}

        return [NamedRef(mapping.validator.name, mapping.validator.ref)
                for mapping in unique.values()]

    def get_field_object_by_name(self, field_name: str) -> ModelField:
        """Return the field object for given field name.

        """

        return self.model.__dict__["__fields__"][field_name]

    def get_field_property(self, field_name: str, property_name: str) -> Any:
        """Return a property of a given field.

        """

        field = self.get_field_object_by_name(field_name)
        return getattr(field.field_info, property_name, None)

    def field_is_required(self, field_name: str) -> bool:
        """Check if a field is required.

        """

        types_to_check = (UndefinedType, type(...))
        default_value = self.get_field_property(field_name=field_name,
                                                property_name="default")
        return isinstance(default_value, types_to_check)

    def find_non_json_serializable_fields(self) -> List[str]:
        """Get all fields that can't be safely serialized.

        """

        return [key for key, value in self.model.__fields__.items()
                if not is_serializable(value)]

    def get_safe_schema_json(self) -> Tuple[Dict, List[str]]:
        """Get model's `schema_json` while handling non serializable fields.

        """

        try:
            return self.model.schema(), []
        except (TypeError, ValueError):
            invalid_fields = self.find_non_json_serializable_fields()
            new_model = self.copy_sanitized_model(invalid_fields)
            return new_model.schema(), invalid_fields

    def copy_sanitized_model(self, invalid_fields: List[str]) -> BaseModel:
        """Generates a new pydantic model from the original one while
        substituting invalid fields with typevars.

        """

        new = {name: (TypeVar(name), None) for name in invalid_fields}
        return create_model(self.model.__name__, __base__=self.model,  **new)
