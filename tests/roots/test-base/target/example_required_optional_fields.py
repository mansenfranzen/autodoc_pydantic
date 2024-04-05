from typing import Optional

from pydantic import BaseModel, Field


class RequiredOptionalField(BaseModel):
    """Outlines different representations of required/optional fields."""

    required_standard: int
    """No default value given:
    
    :code:`required_standard: int`
    """

    required_optional_with_ellipsis: Optional[int] = ...
    """Requires either integer or None:
    
    :code:`required_optional_with_ellipsis: Optional[int] = ...`
    """

    required_optional_with_field: Optional[int] = Field(...)
    """Requires either integer or None:
    
    :code:`required_optional_with_field: Optional[int] = Field(...)`
    """

    optional_standard: int = 1
    """Optional value with default value *1*:
    
    :code:`optional_standard: int = 1`
    """

    optional_with_optional: Optional[int]
    """Optional value with default value *None*:
    
    :code:`optional_with_optional: Optional[int]`"""

    optional_with_default_factory: int = Field(default_factory=lambda: 1)
    """Optional value with default factory:
    
    :code:`optional_with_default_factory: int = Field(default_factory=lambda: 1)`
    """
