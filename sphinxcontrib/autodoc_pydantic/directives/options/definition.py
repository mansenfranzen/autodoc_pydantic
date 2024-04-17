"""This module contains the autodocumenter's option definitions."""

from __future__ import annotations

from typing import Callable

from docutils.parsers.rst.directives import unchanged

from sphinxcontrib.autodoc_pydantic.directives.options.enums import (
    OptionsFieldDocPolicy,
    OptionsJsonErrorStrategy,
    OptionsSummaryListOrder,
)
from sphinxcontrib.autodoc_pydantic.directives.options.validators import (
    option_default_true,
    option_list_like,
    option_members,
    option_one_of_factory,
)

OPTIONS_FIELD: dict[str, Callable] = {
    'field-show-default': option_default_true,
    'field-show-required': option_default_true,
    'field-show-optional': option_default_true,
    'field-signature-prefix': unchanged,
    'field-show-alias': option_default_true,
    'field-show-constraints': option_default_true,
    'field-list-validators': option_default_true,
    'field-swap-name-and-alias': option_default_true,
    'field-doc-policy': option_one_of_factory(OptionsFieldDocPolicy.values()),
    '__doc_disable_except__': option_list_like,
}
"""Represents added directive options for :class:`PydanticFieldDocumenter`."""

OPTIONS_VALIDATOR: dict[str, Callable] = {
    'validator-replace-signature': option_default_true,
    'validator-list-fields': option_default_true,
    'validator-signature-prefix': unchanged,
    'field-swap-name-and-alias': option_default_true,
    '__doc_disable_except__': option_list_like,
}
"""Represents added directive options for :class:`PydanticValidatorDocumenter`.
"""

OPTIONS_MERGED: dict[str, Callable] = {**OPTIONS_FIELD, **OPTIONS_VALIDATOR}

OPTIONS_MODEL: dict[str, Callable] = {
    'model-show-json': option_default_true,
    'model-show-json-error-strategy': option_one_of_factory(
        OptionsJsonErrorStrategy.values(),
    ),
    'model-hide-paramlist': option_default_true,
    'model-hide-reused-validator': option_default_true,
    'model-show-validator-members': option_default_true,
    'model-show-validator-summary': option_default_true,
    'model-show-field-summary': option_default_true,
    'model-summary-list-order': option_one_of_factory(
        OptionsSummaryListOrder.values(),
    ),
    'model-show-config-member': option_default_true,
    'model-show-config-summary': option_default_true,
    'model-erdantic-figure': option_default_true,
    'model-erdantic-figure-collapsed': option_default_true,
    'model-signature-prefix': unchanged,
    'undoc-members': option_default_true,
    'members': option_members,
    '__doc_disable_except__': option_list_like,
}
"""Represents added directive options for :class:`PydanticModelDocumenter`."""

OPTIONS_SETTINGS: dict[str, Callable] = {
    'settings-show-json': option_default_true,
    'settings-show-json-error-strategy': option_one_of_factory(
        OptionsJsonErrorStrategy.values(),
    ),
    'settings-hide-paramlist': option_default_true,
    'settings-hide-reused-validator': option_default_true,
    'settings-show-validator-members': option_default_true,
    'settings-show-validator-summary': option_default_true,
    'settings-show-field-summary': option_default_true,
    'settings-summary-list-order': option_one_of_factory(
        OptionsSummaryListOrder.values(),
    ),
    'settings-show-config-member': option_default_true,
    'settings-show-config-summary': option_default_true,
    'settings-signature-prefix': unchanged,
    'undoc-members': option_default_true,
    'members': option_members,
    '__doc_disable_except__': option_list_like,
}
"""Represents added directive options for :class:`PydanticSettingsDocumenter`.
"""
