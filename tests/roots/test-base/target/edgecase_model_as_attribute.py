import pydantic


class Foo:
    """Foo class"""

    class Bar(pydantic.BaseModel):
        """Bar class"""

        x: str

        @pydantic.validator('x')
        def do_nothing(cls, value):
            """Foo"""
            return value
