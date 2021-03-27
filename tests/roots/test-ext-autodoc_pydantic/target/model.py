from pydantic import BaseModel, validator


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
