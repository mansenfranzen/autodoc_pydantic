from pydantic import BaseModel, ConfigDict


class NoJsonSerializer:
    foo = 'bar'


class NotJsonCompliant(BaseModel):
    field: NoJsonSerializer = NoJsonSerializer()

    model_config = ConfigDict(arbitrary_types_allowed=True)
