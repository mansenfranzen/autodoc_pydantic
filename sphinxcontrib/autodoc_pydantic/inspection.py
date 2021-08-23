"""This module contains inspection functionality for pydantic models.

"""
import functools
import pydoc
from collections import defaultdict
from itertools import chain
from typing import NamedTuple, Tuple, List, Dict, Any, Set, TypeVar, Iterator

from pydantic import BaseModel, create_model
from pydantic.class_validators import Validator
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


class ValidatorFieldMap(NamedTuple):
    """Contains single mapping of a pydantic validator and field.

    """

    field: str
    validator: str
    is_asterisk: bool
    model_path: str

    def _get_ref(self, name: str) -> str:
        """Create reference for given `name` while prefixing it with model
        path.

        """

        return f"{self.model_path}.{name}"

    @property
    def field_ref(self):
        """Create reference to field object.

        """

        if self.is_asterisk:
            return self.model_path

        return self._get_ref(self.field)

    @property
    def validator_ref(self):
        """Create reference to validator object.

        """

        return self._get_ref(self.validator)


class ValidatorFieldMappings:
    """Represents a container of `ValidatorFieldMap` instances with
    convenient accessor methods.

    """

    def __init__(self, mappings: List[ValidatorFieldMap]):
        self.mappings = mappings

    def filter_by_validator_name(self, name: str) -> List[ValidatorFieldMap]:
        """Return mappings for given validator `name`.

        """

        return [mapping for mapping in self.mappings
                if mapping.validator == name]

    def filter_by_field_name(self, name: str) -> List[ValidatorFieldMap]:
        """Return mappings for given field `name`.

        """

        return [mapping for mapping in self.mappings
                if mapping.field in (name, "all fields")]

    def __bool__(self):
        """Equals to `True` if not empty.

        """

        return bool(self.mappings)

    def __iter__(self):
        """Allow iteration over mappings.

        """

        return iter(self.mappings)


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

        def get_name_from_root(validators):
            return {validator[1].__name__ for validator in validators}

        pre_root = get_name_from_root(self.model.__pre_root_validators__)
        post_root = get_name_from_root(self.model.__post_root_validators__)

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


class PropertyInspector(BaseInspectionComposite):
    """Provide namespace for inspection methods for general properties of
    pydantic models.

    """


class ReferenceInspector(BaseInspectionComposite):
    """Provide namespace for inspection methods for creating references
    mainly between pydantic fields and validators.

    """

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

        return {ValidatorFieldMap(field="all fields",
                                  validator=validator,
                                  is_asterisk=True,
                                  model_path=model_path)
                for validator in asterisk_validators}

    def _create_mappings_standard(self) -> Set[ValidatorFieldMap]:
        """Generate `ValidatorFieldMap` instances for asterisk validators.

        """

        is_asterisk = self._parent.validators.is_asterisk
        field_validator_names = self._parent.fields.validator_names
        model_path = self.model_path

        references = set()
        for field, validators in field_validator_names.items():
            refs = {ValidatorFieldMap(field=field,
                                      validator=validator,
                                      is_asterisk=False,
                                      model_path=model_path)
                    for validator in validators
                    if not is_asterisk(validator)}
            references.update(refs)

        return references

    @property
    def mapping(self) -> ValidatorFieldMappings:
        """"""
        mappings_asterisk = self._create_mappings_asterisk()
        mappings_standard = self._create_mappings_standard()
        mappings = mappings_standard.union(mappings_asterisk)

        return ValidatorFieldMappings(mappings)


class ModelInspector:
    """Provides inspection functionality for pydantic models.

    """

    def __init__(self, model: BaseModel):
        self.model = model
        self.fields = FieldInspector(self)
        self.validators = ValidatorInspector(self)
        self.properties = PropertyInspector(self)
        self.references = ReferenceInspector(self)


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
        self.wrapper = ModelInspector(model)

    def get_model_path(self) -> str:  # DONE
        """Retrieve the full path to given model.

        """

        return self.wrapper.references.model_path

    def get_field_validator_names(self) -> Dict[str, Set[str]]:  # DONE
        """Retrieve function names from pydantic Validator wrapper objects.

        """

        return self.wrapper.fields.validator_names

    def get_fields(self) -> List[str]:  # Done
        """Retrieves all fields from pydantic model.

        """

        return self.wrapper.fields.names

    def get_validator_names(self) -> Set[str]:  # Done
        """Collect all names of the validator functions.

        """

        return self.wrapper.validators.names

    def get_reference(self, name: str):  # Done
        """Create reference path to given name.

        """

        return self.wrapper.references.create_model_reference(name)

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
                                 validator_name: str) -> List[
        ValidatorFieldMap]:
        """Return all fields for a given validator.

        """

        return self.wrapper.references.mapping.filter_by_validator_name(
            validator_name)

    def get_validators_for_field(self, field_name: str) -> List[
        ValidatorFieldMap]:
        """Return all validators for given field.

        """

        return self.wrapper.references.mapping.filter_by_field_name(
            field_name)


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
        return create_model(self.model.__name__, __base__=self.model, **new)
