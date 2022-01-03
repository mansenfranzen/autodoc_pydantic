from pydantic import BaseModel, validator


class Model(BaseModel):
    """Model Doc String."""

    field: int
    """Field Doc String"""

    field2: str
    """Field2 Doc String"""

    @validator("field")
    def validate(cls, v):
        """Dummy validator"""
        return v


class Container:
    """Container Doc String"""

    TEST_MODEL = Model
