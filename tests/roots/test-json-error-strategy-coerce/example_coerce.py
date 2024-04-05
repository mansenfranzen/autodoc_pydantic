from pydantic import BaseModel, ConfigDict


class CustomCoerce:
    pass


class NonSerializableCoerce(BaseModel):
    """NonSerializable"""

    test_me: CustomCoerce
    """Field"""

    model_config = ConfigDict(arbitrary_types_allowed=True)
