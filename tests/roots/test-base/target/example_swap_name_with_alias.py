from pydantic import BaseModel, field_validator, Field


class SwapFieldWithAlias(BaseModel):
    """SwapFieldWithAlias."""

    field_with_alias: int = Field(default=5, alias='aliased_field')
    """Field with alias."""

    field_without_alias: int = 5
    """Field without alias."""

    @field_validator('field_with_alias', 'field_without_alias')
    def check(cls, v) -> str:
        """Check."""
        return v
