from pydantic import BaseModel, validator, Field


class ModelShowConfig(BaseModel):
    """Example showing model configuration."""

    class Config:
        title = "FooBar"
        allow_mutation = True


class ModelShowJson(BaseModel):
    """Exmaple showing json representation."""

    field: int = 5


class ModelShowValidators(BaseModel):
    """Exmaple showing validators."""

    field1: int = 5
    field2: str = "FooBar"

    @validator("field1")
    def check1(cls, v):
        return v

    @validator("field2")
    def check2(cls, v):
        return v


class ModelShowParamList(BaseModel):
    """Example showing param list."""

    field1: int = 5
    field2: str = "FooBar"


class ModelUndocMembers(BaseModel):
    """Example showing undoc members."""

    field1: int = 5
    field2: str = "FooBar"


class ModelMembers(BaseModel):
    """Example showing members."""

    field1: int = 5
    """Doc field 1"""

    field2: str = "FooBar"
    """Doc field 2"""