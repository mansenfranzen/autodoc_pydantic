from pydantic import BaseModel, field_validator


class Base(BaseModel):
    """MyBase"""

    field_on_base: str
    """Base Field"""

    @field_validator('field_on_base')
    def validate_field_on_base(cls, v):
        """Validate field_on_base"""
        return v


class WithoutInheritedMembers(Base):
    """Without `:inherited-members: BaseModel`"""

    field_on_subclass: str
    """Subclass field"""

    @field_validator('field_on_subclass')
    def validate_field_on_subclass(cls, v):
        """Validate field_on_subclass"""
        return v


class WithInheritedMembers(Base):
    """With `:inherited-members: BaseModel`"""

    field_on_subclass: str
    """Subclass field"""

    @field_validator('field_on_subclass')
    def validate_field_on_subclass(cls, v):
        """Validate field_on_subclass"""
        return v
