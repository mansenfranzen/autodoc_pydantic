from pydantic_settings import BaseSettings


class TestSettingsExternal(BaseSettings):
    """External Model"""

    a: str
    """Dummy Doc String"""
