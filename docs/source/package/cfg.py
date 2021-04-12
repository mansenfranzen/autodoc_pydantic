from pydantic import BaseModel, validator, Field


class ShowConfig(BaseModel):
    """Example showing model configuration."""

    class Config:
        title = "FooBar"
        allow_mutation = True

class ShowJson(BaseModel):
    """Exmaple showing json representation."""

    field: int = 5

class ShowValidators(BaseModel):
    """Exmaple showing validators."""

    field1: int = 5
    field2: str = "FooBar"

    @validator("field1")
    def check1(cls, v):
        return v

    @validator("field2")
    def check2(cls, v):
        return v

