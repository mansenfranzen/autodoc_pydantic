from typing import Optional

from pydantic import BaseModel, Field


class RequiredOptionalField(BaseModel):
    """Outlines different representations of required/optional fields.

    """

    required_standard: int
    """No default value given."""

    required_with_none: Optional[int] = ...
    """Requires either integer or None."""

    required_with_none_field: Optional[int] = Field(...)
    """Requires either integer or None."""

    optional_standard: int = 1
    """Optional value. If not given, equals ``1``."""

    optional_none: Optional[int]
    """Optional value. If not given, equals ``None``."""

    optional_factory: Optional[int] = Field(default_factory=lambda x: 1)
    """Optional value. If not given, uses ``default_factory``."""
