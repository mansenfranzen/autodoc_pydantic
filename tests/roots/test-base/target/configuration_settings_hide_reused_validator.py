from pydantic import BaseModel, validator


def validation(name):
    return name


class SettingOne(BaseModel):
    name: str

    normalize_name = validator('name', allow_reuse=True)(validation)


class SettingTwo(BaseModel):
    name: str

    validation = validator('name', allow_reuse=True)(validation)
