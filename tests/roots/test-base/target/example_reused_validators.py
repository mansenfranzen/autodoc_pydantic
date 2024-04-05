from pydantic import BaseModel, field_validator


def normalize(name: str) -> str:
    """Normalize docstring."""
    return ' '.join((word.capitalize()) for word in name.split(' '))


class Producer(BaseModel):
    name: str

    # validators
    normalize_name = field_validator('name')(normalize)


class Consumer(BaseModel):
    name: str

    # validators
    normalize_name = field_validator('name')(normalize)
