from pydantic import BaseModel, validator, Field


class PlainModel(BaseModel):
    """Model Plain."""


class ModelWithField(BaseModel):
    """Model With Field."""

    field: int = 1
    """Doc field"""


class ModelWithFieldValidator(BaseModel):
    """Model With Field Validator."""

    field: int = 1
    """Doc field"""

    @validator("field")
    def is_integer(cls, v) -> str:
        """Doc validator."""
        return v


class ModelWithConfig(BaseModel):
    """Model with Config."""

    class Config:
        """With Doc String."""
        allow_mutation = True
        """FooBar."""


class ModelWithAlias(BaseModel):
    """Model with Alias."""

    field: int = Field(5, alias="aliased")
    """FooBar."""