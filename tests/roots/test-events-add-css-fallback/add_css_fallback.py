from pydantic import BaseModel, Field, field_validator, ConfigDict
from pydantic_settings import BaseSettings


class AutoSummaryModel(BaseModel):
    """Document your project settings very conveniently. Applies like wise
    to pydantic models.

    """

    field_plain_with_validator: int = 200
    """Show standard field with type annotation."""

    field_with_validator_and_alias: str = Field("FooBar", alias="BarFoo")
    """Shows corresponding validator with link/anchor."""

    field_with_constraints_and_description: int = Field(
        default=5,
        ge=0,
        le=100,
        description="Shows constraints within doc string."
    )

    @field_validator("field_with_validator_and_alias", "field_plain_with_validator")
    def check_max_length_ten(cls, v):
        """Show corresponding field with link/anchor.

        """

        if not len(v) < 10:
            raise ValueError("No more than 10 characters allowed")

    model_config = ConfigDict(frozen=False)


class AutoSummarySettings(BaseSettings):
    """Some settings with pydantic."""

    field: int = 1
    """Doc field"""
