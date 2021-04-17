from pydantic import BaseModel, validator, Field


class ModelShowJson(BaseModel):
    """ModelShowJson."""


class ModelShowConfig(BaseModel):
    """ModelShowConfig."""

    class Config:
        title: str = "FooBar"
        allow_mutation: bool = True


class ModelShowValidators(BaseModel):
    """ModelShowValidators."""

    field: int = 1

    @validator("field")
    def check(cls, v) -> str:
        return v


class ModelHideParamList(BaseModel):
    """ModelHideParamList."""

    field1: int = 5
    field2: str = "FooBar"


class ModelUndocMembers(BaseModel):
    """ModelUndocMembers."""

    field1: int = 5
    field2: str = "FooBar"


class ModelMembers(BaseModel):
    """ModelMembers."""

    field1: int = 5
    """Doc field 1"""

    field2: str = "FooBar"
    """Doc field 2"""


class ModelMemberOrder(BaseModel):
    """ModelMemberOrder."""

    @validator("field")
    def dummy(cls, v) -> str:
        """Check."""
        return v

    class Config:
        """Config."""
        allow_mutation = True

    field: int = 1
    """Field."""