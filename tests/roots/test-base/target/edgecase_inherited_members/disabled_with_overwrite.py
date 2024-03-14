from pydantic import BaseModel, field_validator


class Parent(BaseModel):
    """Base"""

    field_on_parent: str
    """field_on_parent"""

    @field_validator("field_on_parent")
    def validate_field_on_parent(cls, v):
        """Validate field_on_parent"""
        return v


class Child(Parent):
    """Child"""

    field_on_child: str
    """field_on_child"""

    @field_validator("field_on_child")
    def validate_field_on_child(cls, v):
        """Validate field_on_child"""
        return v


class ChildWithOverwrite(Parent):
    """ChildWithOverwrite"""

    field_on_parent: str
    """overwritten field_on_parent"""

    field_on_child: str
    """field_on_child"""

    @field_validator("field_on_child")
    def validate_field_on_child(cls, v):
        """Validate field_on_child"""
        return v
