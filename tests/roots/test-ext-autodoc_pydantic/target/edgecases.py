from pydantic import BaseModel


class NoJsonSerializer:
    foo = "bar"


class NotJsonCompliant(BaseModel):
    field: NoJsonSerializer = NoJsonSerializer()

    class Config:
        arbitrary_types_allowed = True
