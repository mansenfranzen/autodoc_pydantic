from pydantic import BaseModel, Field
from pydantic.json_schema import SkipJsonSchema


class Child(BaseModel):
    foo: int
    parent: SkipJsonSchema[Parent] = Field(exclude=True)


class Parent(BaseModel):
    child: Child = Field(exclude=True)
