from typing import Optional

from pydantic import BaseModel, field_validator, Field, model_validator, ConfigDict, root_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class ModelShowJson(BaseModel):
    """ModelShowJson."""


class ModelShowConfigSummary(BaseModel):
    """ModelShowConfigSummary."""

    model_config = ConfigDict(title="FooBar", frozen=False)


class ModelShowValidatorsSummary(BaseModel):
    """ModelShowValidatorsSummary."""

    field: int = 1

    @field_validator("field")
    def check(cls, v) -> str:
        return v


class ModelShowValidatorsSummaryInherited(ModelShowValidatorsSummary):
    """ModelShowValidatorsSummaryInherited."""

    @field_validator("field")
    def check_inherited(cls, v) -> str:
        return v


class ModelShowValidatorsSummaryMultipleFields(BaseModel):
    """ModelShowValidatorsSummaryMultipleFields."""

    field1: int = 1

    field2: int = 2

    @field_validator("field1", "field2")
    def check(cls, v) -> str:
        return v



class ModelShowFieldSummary(BaseModel):
    """ModelShowFieldSummary."""

    field1: int = 5
    field2: str = "FooBar"


class ModelShowFieldSummaryInherited(ModelShowFieldSummary):
    """ModelShowFieldSummaryInherited."""

    field3: int = 5


class ModelSummaryListOrder(BaseModel):
    """ModelSummaryListOrder."""

    field_b: int = 1
    field_a: int = 1

    @field_validator("field_b")
    def validate_b(cls, v):
        return v

    @field_validator("field_a")
    def validate_a(cls, v):
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

    @field_validator("field")
    def dummy(cls, v) -> str:
        """Check."""
        return v

    model_config = ConfigDict(frozen=False)

    field: int = 1
    """Field."""


class ModelShowValidatorMembers(BaseModel):
    """ModelShowValidatorMembers."""

    field: int = 1
    """Field."""

    @field_validator("field")
    def dummy(cls, v) -> str:
        """Check."""
        return v


class ModelShowConfigMember(BaseModel):
    """ModelShowConfigMember."""

    field: int = 1
    """Field."""

    model_config = ConfigDict(frozen=False)


class ModelSignaturePrefix(BaseModel):
    """ModelSignaturePrefix."""


class ModelWithFieldSwapNameAndAlias(BaseModel):
    """ModelWithFieldSwapNameAndAlias."""

    field1: int = Field(default=5, alias="field1 alias")
    """Field1"""
    field2: str = Field(default="FooBar", alias="field2 alias")
    """Field2"""

    @field_validator("field1")
    def check(cls, v) -> str:
        """Check."""
        return v


class SettingsShowJson(BaseSettings):
    """SettingsShowJson."""


class SettingsShowConfigSummary(BaseSettings):
    """SettingsShowConfigSummary."""

    model_config = SettingsConfigDict(title="FooBar", frozen=False)


class SettingsShowValidatorsSummary(BaseSettings):
    """SettingsShowValidatorsSummary."""

    field: int = 1

    @field_validator("field")
    def check(cls, v) -> str:
        return v


class SettingsShowFieldSummary(BaseSettings):
    """SettingsShowFieldSummary."""

    field1: int = 5
    """Field1."""
    field2: str = "FooBar"
    """Field2."""


class SettingsSummaryListOrder(BaseSettings):
    """SettingsSummaryListOrder."""

    field_b: int = 1
    field_a: int = 1

    @field_validator("field_b")
    def validate_b(cls, v):
        return v

    @field_validator("field_a")
    def validate_a(cls, v):
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

    @field_validator("field")
    def dummy(cls, v) -> str:
        """Check."""
        return v

    model_config = SettingsConfigDict(frozen=False)

    field: int = 1
    """Field."""


class SettingsShowValidatorMembers(BaseSettings):
    """SettingsShowValidatorMembers."""

    field: int = 1
    """Field."""

    @field_validator("field")
    def dummy(cls, v) -> str:
        """Check."""
        return v


class SettingsShowConfigMember(BaseSettings):
    """SettingsShowConfigMember."""

    field: int = 1
    """Field."""

    model_config = SettingsConfigDict(frozen=False)


class SettingsSignaturePrefix(BaseSettings):
    """SettingsSignaturePrefix."""


class ConfigMembers(BaseModel):
    """ConfigUndocMembers."""

    class Config:
        frozen = False
        title = "FooBar"


class ConfigSignaturePrefix(BaseModel):
    """ConfigSignaturePrefix."""

    model_config = ConfigDict()


class ValidatorReplaceSignature(BaseModel):
    """ValidatorReplaceSignature."""

    field: int = 1

    @field_validator("field")
    def check(cls, v) -> str:
        """Check."""
        return v


class ValidatorReplaceSignatureWithSwapNameAndAlias(BaseModel):
    """ValidatorReplaceSignatureWithSwapNameAndAlias."""

    field1: int = Field(default=5, alias="field1 alias")
    """Field1"""

    @field_validator("field1")
    def check(cls, v) -> str:
        """Check."""
        return v


class ValidatorListFields(BaseModel):
    """ValidatorListFields."""

    field: int = 1

    @field_validator("field")
    def check(cls, v) -> str:
        """Check."""
        return v


class ValidatorListFieldsWithFieldSwapNameAndAlias(BaseModel):
    """ValidatorListFieldsWithFieldSwapNameAndAlias."""

    field: int = Field(1, alias="field_alias")

    @field_validator("field")
    def check(cls, v) -> str:
        """Check."""
        return v


class ValidatorSignaturePrefix(BaseModel):
    """ValidatorSignaturePrefix."""

    field: int = 1

    @field_validator("field")
    def check(cls, v) -> str:
        """Check."""
        return v


class ValidatorAsteriskRootValidator(BaseModel):
    """ValidatorAsteriskRootValidator"""

    field: int = 1

    @field_validator("*")
    def check(cls, v):
        """Check."""
        return v

    @root_validator(skip_on_failure=True)
    def check_root(cls, values):
        """Check root."""
        return values

    @model_validator(mode="before")
    def check_root_pre(cls, values):
        """Check root pre."""
        return values


class FieldListValidators(BaseModel):
    """FieldListValidators."""

    field: int = 1
    """Field."""

    @field_validator("field")
    def check(cls, v) -> str:
        """Check."""
        return v


class FieldListValidatorsInherited(FieldListValidators):
    """FieldListValidatorsInherited."""

    @field_validator("field")
    def check_inherited(cls, v) -> str:
        """Check inherited."""
        return v


class FieldDocPolicy(BaseModel):
    """FieldDocPolicy."""

    field: int = Field(1, description="Custom Desc.")
    """Field."""


class FieldShowConstraints(BaseModel):
    """FieldShowConstraints."""

    field: int = Field(1, ge=0, le=100)
    """Field."""


class FieldShowConstraintsIgnoreExtraKwargs(BaseModel):
    """FieldShowConstraints."""

    field: int = Field(1, ge=0, le=100, non_existing_kwarg=1)
    """Field."""


class FieldShowAlias(BaseModel):
    """FieldShowAlias."""

    field: int = Field(1, alias="field2")
    """Field."""


class FieldShowDefault(BaseModel):
    """FieldShowDefault."""

    field: int = 1
    """Field."""


class FieldSignaturePrefix(BaseModel):
    """FieldSignaturePrefix."""

    field: int = 1
    """Field."""


class FieldShowRequired(BaseModel):
    """FieldShowRequired."""

    field1: int
    """field1"""
    field2: int = ...
    """field2"""
    field3: int = Field(default=...)
    """field3"""


class FieldShowRequiredNot(BaseModel):
    """FieldShowRequiredNot"""

    field1: Optional[int]
    """field1"""

    field2: Optional[int] = 0
    """field2"""

    field3: int = 0
    """field3"""

    field4: int = Field(default=0)
    """field4"""


class FieldShowOptional(BaseModel):
    """FieldShowOptional"""

    field1: int = Field(default_factory=lambda: 1)
    """field1"""

    field2: Optional[int] = Field(default_factory=lambda: 1)
    """field2"""


class FieldShowOptionalNot(BaseModel):
    """FieldShowOptionalNot"""

    field1: Optional[int]
    """field1"""

    field2: Optional[int] = 0
    """field2"""

    field3: int = 0
    """field3"""

    field4: int = Field(default=0)
    """field4"""


class FieldSwapNameAndAlias(BaseModel):
    """FieldSwapNameAndAlias"""

    field1: int = Field(default=1, alias="field 1 alias")
    """Field1"""


class ModelErdanticFigureRelated(ModelShowFieldSummary):
    """ModelErdanticFigureRelated."""


class ModelErdanticFigure(ModelShowFieldSummary):
    """ModelErdanticFigure."""
    related: ModelErdanticFigureRelated
