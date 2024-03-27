from pydantic import BaseModel, field_validator


def validation(name):
    """Validation function."""
    return name


class ModelOne(BaseModel):
    name: str
    """Name"""

    validation = field_validator('name')(validation)
    """Reused validator class method."""
