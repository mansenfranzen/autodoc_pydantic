from pydantic import BaseSettings


class TestSettingsExternal(BaseSettings):
    """External Model"""

    a: str
    """Dummy Doc String"""
