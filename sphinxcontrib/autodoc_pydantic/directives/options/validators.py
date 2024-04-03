"""This module contains custom directive option validator functions."""

from __future__ import annotations

from typing import Any, Callable

from sphinx.ext.autodoc import ALL


def option_members(arg: Any) -> list[str] | Any:  # noqa: ANN401
    """Option validator function used to convert the ``:members:`` option for
    auto directives.

    """

    if isinstance(arg, str):
        sanitized = arg.lower()
        if sanitized == 'true':
            return ALL
        if sanitized == 'false':
            return None

    if arg in (None, True):
        return ALL
    if arg is False:
        return None

    return [x.strip() for x in arg.split(',') if x.strip()]


def option_one_of_factory(choices: set[Any]) -> Callable:
    """Option validator factory to create a option validation function which
    allows only one value of given set of provided `choices`.

    """

    def option_func(value: str) -> str:
        if value not in choices:
            err = f'Option value {value} has to be on of {choices}'
            raise ValueError(err)
        return value

    return option_func


def option_default_true(arg: str | None) -> bool:
    """Option validator used to define boolean options with default to True if
    no argument is passed.

    """

    if isinstance(arg, bool):
        return arg

    if arg is None:
        return True

    sanitized = arg.strip().lower()
    if sanitized == 'true':
        return True
    if sanitized == 'false':
        return False

    err = (
        f"Directive option argument '{arg}' is not valid. "
        f"Valid arguments are 'true' or 'false'."
    )
    raise ValueError(err)


def option_list_like(arg: str | None) -> set[str]:
    """Option validator used to define a set of items."""

    if not arg:
        return set()

    return {x.strip() for x in arg.split(',')}
