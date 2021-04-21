from pydantic import BaseModel, validator, Field, BaseSettings


class ModelShowJson(BaseModel):
    """ModelShowJson."""


class ModelShowConfigSummary(BaseModel):
    """ModelShowConfigSummary."""

    class Config:
        title: str = "FooBar"
        allow_mutation: bool = True


class ModelShowValidatorsSummary(BaseModel):
    """ModelShowValidatorsSummary."""

    field: int = 1

    @validator("field")
    def check(cls, v) -> str:
        return v


class ModelHideParamList(BaseModel):
    """ModelHideParamList."""

    field1: int = 5
    field2: str = "FooBar"


class ModelUndocMembers(BaseModel):
    """ModelUndocMembers."""

    field1: int = 5
    field2: str = "FooBar"


class ModelMembers(BaseModel):
    """ModelMembers."""

    field1: int = 5
    """Doc field 1"""

    field2: str = "FooBar"
    """Doc field 2"""


class ModelMemberOrder(BaseModel):
    """ModelMemberOrder."""

    @validator("field")
    def dummy(cls, v) -> str:
        """Check."""
        return v

    class Config:
        """Config."""
        allow_mutation = True

    field: int = 1
    """Field."""


class ModelShowValidatorMembers(BaseModel):
    """ModelShowValidatorMembers."""

    field: int = 1
    """Field."""

    @validator("field")
    def dummy(cls, v) -> str:
        """Check."""
        return v


class ModelShowConfigMember(BaseModel):
    """ModelShowConfigMember."""

    field: int = 1
    """Field."""

    class Config:
        """Config."""
        allow_mutation = True


class ModelSignaturePrefix(BaseModel):
    """ModelSignaturePrefix."""

class SettingsShowJson(BaseSettings):
    """SettingsShowJson."""


class SettingsShowConfigSummary(BaseSettings):
    """SettingsShowConfigSummary."""

    class Config:
        title: str = "FooBar"
        allow_mutation: bool = True


class SettingsShowValidatorsSummary(BaseSettings):
    """SettingsShowValidatorsSummary."""

    field: int = 1

    @validator("field")
    def check(cls, v) -> str:
        return v


class SettingsHideParamList(BaseSettings):
    """SettingsHideParamList."""

    field1: int = 5
    field2: str = "FooBar"


class SettingsUndocMembers(BaseSettings):
    """SettingsUndocMembers."""

    field1: int = 5
    field2: str = "FooBar"


class SettingsMembers(BaseSettings):
    """SettingsMembers."""

    field1: int = 5
    """Doc field 1"""

    field2: str = "FooBar"
    """Doc field 2"""


class SettingsMemberOrder(BaseSettings):
    """SettingsMemberOrder."""

    @validator("field")
    def dummy(cls, v) -> str:
        """Check."""
        return v

    class Config:
        """Config."""
        allow_mutation = True

    field: int = 1
    """Field."""


class SettingsShowValidatorMembers(BaseSettings):
    """SettingsShowValidatorMembers."""

    field: int = 1
    """Field."""

    @validator("field")
    def dummy(cls, v) -> str:
        """Check."""
        return v


class SettingsShowConfigMember(BaseSettings):
    """SettingsShowConfigMember."""

    field: int = 1
    """Field."""

    class Config:
        """Config."""
        allow_mutation = True


class SettingsSignaturePrefix(BaseSettings):
    """SettingsSignaturePrefix."""


class ConfigMembers(BaseModel):
    """ConfigUndocMembers."""

    class Config:
        allow_mutation = True
        """Allow Mutation."""
        title = "foobar"


class ConfigSignaturePrefix(BaseModel):
    """ConfigSignaturePrefix."""

    class Config:
        """Config."""