from pydantic import BaseModel, field_validator


def validation(name):
    """Validation function."""
    return name


class SettingOne(BaseModel):
    name: str
    """Name"""

    normalize_name = field_validator('name')(validation)
    """Reused validator class method."""

