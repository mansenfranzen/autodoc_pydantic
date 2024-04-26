"""This module contains **autodoc_pydantic**'s directives."""

from __future__ import annotations

from typing import TYPE_CHECKING, Tuple

import sphinx
from docutils.nodes import Node, Text
from docutils.parsers.rst.directives import unchanged
from sphinx.addnodes import desc_annotation, desc_name, desc_signature, pending_xref
from sphinx.domains.python import PyAttribute, PyClasslike, PyMethod, py_sig_re

from sphinxcontrib.autodoc_pydantic.directives.options.composites import (
    DirectiveOptions,
)
from sphinxcontrib.autodoc_pydantic.directives.options.validators import (
    option_default_true,
    option_list_like,
)
from sphinxcontrib.autodoc_pydantic.directives.utility import (
    create_field_href,
    remove_node_by_tagname,
)
from sphinxcontrib.autodoc_pydantic.inspection import ModelInspector, ValidatorFieldMap

if TYPE_CHECKING:
    from sphinx.util.typing import OptionSpec

TUPLE_STR = Tuple[str, str]


class PydanticDirectiveMixin:
    """Base class for pydantic directive providing common functionality."""

    config_name: str

    def __init__(self, *args) -> None:  # noqa: ANN002
        super().__init__(*args)
        self.pyautodoc = DirectiveOptions(self)

    def get_signature_prefix(self, *_) -> list[Node]:  # noqa: ANN002
        """Overwrite original signature prefix with custom pydantic ones."""

        config_name = f'{self.config_name}-signature-prefix'
        prefix = self.pyautodoc.get_value(config_name)

        # empty prefix should not add any nodes
        if prefix == '':
            return []

        # account for changed signature in sphinx 4.3, see #62
        if sphinx.version_info < (4, 3):
            return f'{prefix} '  # type: ignore[return-value]

        from sphinx.addnodes import desc_sig_space

        return [Text(prefix), desc_sig_space()]


class PydanticModel(PydanticDirectiveMixin, PyClasslike):
    """Specialized directive for pydantic models."""

    option_spec: OptionSpec = PyClasslike.option_spec.copy()  # type: ignore[misc]
    option_spec.update(
        {
            '__doc_disable_except__': option_list_like,
            'model-signature-prefix': unchanged,
        }
    )

    config_name = 'model'


class PydanticSettings(PydanticDirectiveMixin, PyClasslike):
    """Specialized directive for pydantic settings."""

    option_spec: OptionSpec = PyClasslike.option_spec.copy()  # type: ignore[misc]
    option_spec.update(
        {
            '__doc_disable_except__': option_list_like,
            'settings-signature-prefix': unchanged,
        }
    )

    config_name = 'settings'


class PydanticField(PydanticDirectiveMixin, PyAttribute):
    """Specialized directive for pydantic fields."""

    option_spec: OptionSpec = PyAttribute.option_spec.copy()  # type: ignore[misc]
    option_spec.update(
        {
            'alias': unchanged,
            'field-show-alias': option_default_true,
            'field-swap-name-and-alias': option_default_true,
            'required': option_default_true,
            'optional': option_default_true,
            '__doc_disable_except__': option_list_like,
            'field-signature-prefix': unchanged,
        }
    )

    config_name = 'field'

    def get_field_name(self, sig: str) -> str:
        """Get field name from signature. Borrows implementation from
        `PyObject.handle_signature`.

        """

        result = py_sig_re.match(sig)
        if not result:
            msg = f'Cannot find field name in signature: {sig} for {self.name}'
            raise ValueError(msg)

        return result.groups()[1]

    def add_required(self, signode: desc_signature) -> None:
        """Add `[Required]` if directive option `required` is set."""

        if self.options.get('required'):
            signode += desc_annotation('', ' [Required]')

    def add_optional(self, signode: desc_signature) -> None:
        """Add `[Optional]` if directive option `optional` is set."""

        if self.options.get('optional'):
            signode += desc_annotation('', ' [Optional]')

    def add_alias_or_name(self, sig: str, signode: desc_signature) -> None:
        """Add alias or name to signature.

        Alias is added if `show-alias` is enabled. Name is added if both
        `show-alias` and `swap-name-and-alias` is enabled.

        """

        if not self.pyautodoc.get_value('field-show-alias'):
            return

        if self.pyautodoc.is_true('field-swap-name-and-alias'):
            prefix = 'name'
            value = self.get_field_name(sig)
        else:
            prefix = 'alias'
            value = self.options.get('alias', '')

        signode += desc_annotation('', f" ({prefix} '{value}')")

    def _find_desc_name_node(self, sig: str, signode: desc_signature) -> Node | None:
        """Return `desc_name` node  from `signode` that contains the field
        name. This is used to replace the name with the alias.

        """

        name = self.get_field_name(sig)

        for node in signode.children:
            has_correct_text = node.astext() == name
            is_desc_name = isinstance(node, desc_name)
            if has_correct_text and is_desc_name:
                return node

        return None

    def swap_name_and_alias(self, sig: str, signode: desc_signature) -> None:
        """Replaces name with alias if `swap-name-and-alias` is enabled.

        Requires to replace existing `addnodes.desc_name` because name node is
        added within `handle_signature` and this can't be intercepted or
        overwritten otherwise.

        """

        if not self.pyautodoc.get_value('field-swap-name-and-alias'):
            return

        name_node = self._find_desc_name_node(sig, signode)

        if not name_node:
            logger = sphinx.util.logging.getLogger(__name__)
            logger.warning(
                "Field's `desc_name` node can't be located to " 'swap name with alias.',
                location='autodoc_pydantic',
            )
        else:
            text_node = Text(self.options.get('alias', ''))
            text_node.parent = name_node
            name_node.children = [text_node]

    def handle_signature(self, sig: str, signode: desc_signature) -> TUPLE_STR:
        """Optionally call add alias method."""

        fullname, prefix = super().handle_signature(sig, signode)
        self.add_required(signode)
        self.add_optional(signode)

        if self.options.get('alias') is not None:
            self.add_alias_or_name(sig, signode)
            self.swap_name_and_alias(sig, signode)

        return fullname, prefix


class PydanticValidator(PydanticDirectiveMixin, PyMethod):
    """Specialized directive for pydantic validators."""

    option_spec: OptionSpec = PyMethod.option_spec.copy()  # type: ignore[misc]
    option_spec.update(
        {
            'validator-replace-signature': option_default_true,
            '__doc_disable_except__': option_list_like,
            'validator-signature-prefix': unchanged,
            'field-swap-name-and-alias': option_default_true,
        }
    )

    config_name = 'validator'

    def get_field_href_from_mapping(
        self, inspector: ModelInspector, mapping: ValidatorFieldMap
    ) -> pending_xref:
        """Generate the field reference node aka `pending_xref` from given
        validator-field `mapping` while respecting field name/alias swap
        possibility.

        """

        name = mapping.field_name
        if self.pyautodoc.is_true('field-swap-name-and-alias'):
            name = inspector.fields.get_alias_or_name(mapping.field_name)

        return create_field_href(name=name, ref=mapping.field_ref, env=self.env)

    def replace_return_node(self, signode: desc_signature) -> None:
        """Replaces the return node with references to validated fields."""

        remove_node_by_tagname(signode.children, 'desc_parameterlist')

        # replace nodes
        class_name = 'autodoc_pydantic_validator_arrow'
        signode += desc_annotation('', '  »  ', classes=[class_name])

        # get imports, names and fields of validator
        name = signode['fullname'].split('.')[-1]
        inspector = ModelInspector.from_child_signode(signode)
        mappings = inspector.references.filter_by_validator_name(name)

        # add field reference nodes
        signode += self.get_field_href_from_mapping(
            inspector=inspector, mapping=mappings[0]
        )
        for mapping in mappings[1:]:
            signode += desc_annotation('', ', ')
            signode += self.get_field_href_from_mapping(
                inspector=inspector, mapping=mapping
            )

    def handle_signature(self, sig: str, signode: desc_signature) -> TUPLE_STR:
        """Optionally call replace return node method."""

        fullname, prefix = super().handle_signature(sig, signode)

        if self.pyautodoc.get_value('validator-replace-signature'):
            self.replace_return_node(signode)

        return fullname, prefix
