from pydantic import BaseModel, validator, Field


class SwapFieldWithAlias(BaseModel):
    """SwapFieldWithAlias."""

    field1: int = Field(default=5, alias="field1 alias")
    """Field1"""

    @validator("field1")
    def check(cls, v) -> str:
        """Check."""
        return v
