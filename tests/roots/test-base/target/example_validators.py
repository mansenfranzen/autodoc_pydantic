from pydantic import BaseModel, field_validator, model_validator


class ExampleValidators(BaseModel):
    """Show usage of asterisk and root validators.

    """

    name: str
    email: str

    @field_validator("*")
    def check_non_whitespaces(cls, v):
        """Confirm that string contains non whitespace characters.

        """

        stripped = v.strip()
        if stripped:
            return v
        else:
            raise ValueError("String contains only whitespace characters.")

    @model_validator(mode="after")
    def check_contains_letters(cls, values):
        """Confirm that string contains at least one letter.

        """

        for key, value in values.items():
            has_letter = any(x.isalpha() for x in value)
            if not has_letter:
                raise ValueError(f"Field '{key}' does not contain a letter.")

        return values
