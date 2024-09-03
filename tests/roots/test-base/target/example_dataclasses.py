from pydantic import Field
from pydantic.dataclasses import dataclass


@dataclass
class ExampleDataclass:
    """An example Pydantic dataclass."""

    name: str = Field(description="The name of the object")
    age: int = Field(5, description="The age of the object")

