from pydantic import field_validator, BaseModel


class Foo:
    """Foo class"""

    class Bar(BaseModel):
        """Bar class"""

        x: str

        @field_validator('x')
        def do_nothing(cls, value):
            """Foo"""
            return value
