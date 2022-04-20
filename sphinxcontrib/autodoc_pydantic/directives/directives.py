"""This module contains **autodoc_pydantic**'s directives.

"""

from typing import Tuple, Union, List

import sphinx
from docutils.nodes import Text
from docutils.parsers.rst.directives import unchanged
from sphinx.addnodes import (
    desc_signature,
    desc_annotation, desc_name
)
from sphinx.domains.python import PyMethod, PyAttribute, PyClasslike, py_sig_re
from sphinxcontrib.autodoc_pydantic.inspection import ModelInspector
from sphinxcontrib.autodoc_pydantic.directives.options.composites import (
    DirectiveOptions
)
from sphinxcontrib.autodoc_pydantic.directives.utility import \
    create_field_href, remove_node_by_tagname
from sphinxcontrib.autodoc_pydantic.directives.options.validators import \
    option_default_true, option_list_like

TUPLE_STR = Tuple[str, str]


class PydanticDirectiveBase:
    """Base class for pydantic directive providing common functionality.

    """

    config_name: str
    default_prefix: str

    def __init__(self, *args):
        super().__init__(*args)
        self.pyautodoc = DirectiveOptions(self)

    def get_signature_prefix(self, sig: str) -> Union[str, List[Text]]:
        """Overwrite original signature prefix with custom pydantic ones.

        """

        config_name = f"{self.config_name}-signature-prefix"
        prefix = self.pyautodoc.get_value(config_name)
        value = prefix or self.default_prefix

        if sphinx.version_info < (4, 3):
            return f"{value} "
        from sphinx.addnodes import desc_sig_space
        return [Text(value), desc_sig_space()]


class PydanticModel(PydanticDirectiveBase, PyClasslike):
    """Specialized directive for pydantic models.

    """

    option_spec = PyClasslike.option_spec.copy()
    option_spec.update({"__doc_disable_except__": option_list_like,
                        "model-signature-prefix": unchanged})

    config_name = "model"
    default_prefix = "class"


class PydanticSettings(PydanticDirectiveBase, PyClasslike):
    """Specialized directive for pydantic settings.

    """

    option_spec = PyClasslike.option_spec.copy()
    option_spec.update({"__doc_disable_except__": option_list_like,
                        "settings-signature-prefix": unchanged})

    config_name = "settings"
    default_prefix = "class"


class PydanticField(PydanticDirectiveBase, PyAttribute):
    """Specialized directive for pydantic fields.

    """

    option_spec = PyAttribute.option_spec.copy()
    option_spec.update({"alias": unchanged,
                        "field-show-alias": option_default_true,
                        "field-swap-name-and-alias": option_default_true,
                        "required": option_default_true,
                        "optional": option_default_true,
                        "__doc_disable_except__": option_list_like,
                        "field-signature-prefix": unchanged})

    config_name = "field"
    default_prefix = "attribute"

    def get_field_name(self, sig: str) -> str:
        """Get field name from signature. Borrows implementation from
        `PyObject.handle_signature`.

        """

        return py_sig_re.match(sig).groups()[1]

    def add_required(self, signode: desc_signature):
        """Add `[Required]` if directive option `required` is set.

        """

        if self.options.get("required"):
            signode += desc_annotation("", " [Required]")

    def add_optional(self, signode: desc_signature):
        """Add `[Optional]` if directive option `optional` is set.

        """

        if self.options.get("optional"):
            signode += desc_annotation("", " [Optional]")

    def add_alias_or_name(self, sig: str, signode: desc_signature):
        """Add alias or name to signature.

         Alias is added if `show-alias` is enabled. Name is added if both
         `show-alias` and `swap-name-and-alias` is enabled.

        """

        if not self.pyautodoc.get_value("field-show-alias"):
            return

        elif self.pyautodoc.is_true("field-swap-name-and-alias"):
            prefix = "name"
            value = self.get_field_name(sig)

        else:
            prefix = "alias"
            value = self.options.get("alias")

        signode += desc_annotation("", f" ({prefix} '{value}')")

    def _find_desc_name_node(self,
                             sig: str,
                             signode: desc_signature) -> desc_name:
        """Return `desc_name` node  from `signode` that contains the field
        name. This is used to replace the name with the alias.

        """

        name = self.get_field_name(sig)

        for node in signode.children:
            has_correct_text = node.astext() == name
            is_desc_name = isinstance(node, desc_name)

            if has_correct_text and is_desc_name:
                return node

    def swap_name_and_alias(self, sig: str, signode: desc_signature):
        """Replaces name with alias if `swap-name-and-alias` is enabled.

        Requires to replace existing `addnodes.desc_name` because name node is
        added within `handle_signature` and this can't be intercepted or
        overwritten otherwise.

        """

        if not self.pyautodoc.get_value("field-swap-name-and-alias"):
            return

        if name_node := self._find_desc_name_node(sig, signode):
            text_node = Text(self.options.get("alias"))
            text_node.parent = name_node
            name_node.children[0] = text_node
        else:
            logger = sphinx.util.logging.getLogger(__name__)
            logger.warning("Field's `desc_name` node can't be located to "
                           "swap name with alias.",
                           location="autodoc_pydantic")

    def handle_signature(self, sig: str, signode: desc_signature) -> TUPLE_STR:
        """Optionally call add alias method.

        """

        fullname, prefix = super().handle_signature(sig, signode)
        self.add_required(signode)
        self.add_optional(signode)

        if self.options.get("alias") is not None:
            self.add_alias_or_name(sig, signode)
            self.swap_name_and_alias(sig, signode)

        return fullname, prefix


class PydanticValidator(PydanticDirectiveBase, PyMethod):
    """Specialized directive for pydantic validators.

    """

    option_spec = PyMethod.option_spec.copy()
    option_spec.update({"validator-replace-signature": option_default_true,
                        "__doc_disable_except__": option_list_like,
                        "validator-signature-prefix": unchanged})

    config_name = "validator"
    default_prefix = "classmethod"

    def replace_return_node(self, signode: desc_signature):
        """Replaces the return node with references to validated fields.

        """

        remove_node_by_tagname(signode.children, "desc_parameterlist")

        # replace nodes
        class_name = "autodoc_pydantic_validator_arrow"
        signode += desc_annotation("", "  »  ", classes=[class_name])

        # get imports, names and fields of validator
        name = signode["fullname"].split(".")[-1]
        inspector = ModelInspector.from_signode(signode)
        mappings = inspector.references.filter_by_validator_name(name)

        # add field reference nodes
        mapping_first = mappings[0]
        signode += create_field_href(name=mapping_first.field_name,
                                     ref=mapping_first.field_ref,
                                     env=self.env)
        for mapping in mappings[1:]:
            signode += desc_annotation("", ", ")
            signode += create_field_href(name=mapping.field_name,
                                         ref=mapping.field_ref,
                                         env=self.env)

    def handle_signature(self, sig: str, signode: desc_signature) -> TUPLE_STR:
        """Optionally call replace return node method.

        """

        fullname, prefix = super().handle_signature(sig, signode)

        if self.pyautodoc.get_value("validator-replace-signature"):
            self.replace_return_node(signode)

        return fullname, prefix


class PydanticConfigClass(PydanticDirectiveBase, PyClasslike):
    """Specialized directive for pydantic config class.

    """

    option_spec = PyClasslike.option_spec.copy()
    option_spec.update({"__doc_disable_except__": option_list_like,
                        "config-signature-prefix": unchanged})

    config_name = "config"
    default_prefix = "class"
