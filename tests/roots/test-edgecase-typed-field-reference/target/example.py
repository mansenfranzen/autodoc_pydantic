from pydantic import BaseModel
from .external import TestSettingsExternal


class TestClass:
    """Test Class

    Attributes:
        model (TestModel): Model
        model2 (target.external.TestSettingsExternal): Model

    """

    def __init__(self):
        self.model = TestModel()
        self.model2 = TestSettingsExternal()


class TestModel(BaseModel):
    """Test Model"""

    a: str
    """Dummy Doc String"""
