from pydantic import BaseModel


class Custom:
    def __init__(self):
        self.field = "foobar"

class NonSerializable(BaseModel):
    """NonSerializable

    """

    field: Custom = Custom()
    """Field"""

    class Config:
        arbitrary_types_allowed = True
