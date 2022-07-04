from pydantic import BaseModel, validator


def validation(name):
    return name


class ModelOne(BaseModel):
    name: str

    normalize_name = validator('name', allow_reuse=True)(validation)


class ModelTwo(BaseModel):
    name: str

    validation = validator('name', allow_reuse=True)(validation)
