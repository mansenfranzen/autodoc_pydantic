from pydantic import BaseModel, field_validator, Field, ConfigDict
from pydantic.dataclasses import dataclass


class PlainModel(BaseModel):
    """Model Plain."""


class ModelWithField(BaseModel):
    """Model With Field."""

    field: int = 1
    """Doc field"""


@dataclass
class DataclassWithField:
    """Dataclass With Field."""
    field: int = Field(5, description="The Field")


class ModelWithFieldValidator(BaseModel):
    """Model With Field Validator."""

    field: int = 1
    """Doc field"""

    @field_validator('field')
    def is_integer(cls, v):
        """Doc validator."""
        return v


class ModelWithConfig(BaseModel):
    """Model with Config."""

    """With Doc String."""
    model_config = ConfigDict(frozen=False)


class ModelWithAlias(BaseModel):
    """Model with Alias."""

    field: int = Field(5, alias='aliased')
    """FooBar."""
