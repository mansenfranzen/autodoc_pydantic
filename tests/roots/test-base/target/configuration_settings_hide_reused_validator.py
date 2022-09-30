from pydantic import BaseModel, validator


def validation(name):
    """Validation function."""
    return name


class SettingOne(BaseModel):
    name: str
    """Name"""

    normalize_name = validator('name', allow_reuse=True)(validation)
    """Reused validator class method."""

