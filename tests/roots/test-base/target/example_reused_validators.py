from pydantic import BaseModel, validator


def normalize(name: str) -> str:
    """Normalize docstring."""
    return ' '.join((word.capitalize()) for word in name.split(' '))


class Producer(BaseModel):
    name: str

    # validators
    normalize_name = validator('name', allow_reuse=True)(normalize)


class Consumer(BaseModel):
    name: str

    # validators
    normalize_name = validator('name', allow_reuse=True)(normalize)