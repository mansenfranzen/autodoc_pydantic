from pydantic import BaseSettings, validator, Field


class ExampleSettings(BaseSettings):
    """Document your project settings very conveniently. Applies like wise
    to pydantic models.

    """

    field_with_constraints: int = Field(5, ge=0, le=100)
    """Shows constraints within doc string."""

    field_with_validator: str = "FooBar"
    """Shows corresponding validator with link/anchor."""

    @validator("field_with_validator")
    def check_max_length_ten(cls, v):
        """Show corresponding field with link/anchor.

        """

        if not len(v) < 10:
            raise ValueError("No more than 10 characters allowed")

    class Config:
        env_prefix = "foo_"
