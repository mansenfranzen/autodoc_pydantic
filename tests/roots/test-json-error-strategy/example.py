from pydantic import BaseModel, ConfigDict


class Custom:
    pass


class NonSerializable(BaseModel):
    """NonSerializable"""

    field: Custom
    """Field"""

    model_config = ConfigDict(arbitrary_types_allowed=True)
