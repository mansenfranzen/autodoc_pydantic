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