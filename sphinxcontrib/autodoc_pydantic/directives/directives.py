"""This module contains **autodoc_pydantic**'s directives.

"""

from typing import Tuple, Union, List

import sphinx
from docutils.nodes import Text
from docutils.parsers.rst.directives import unchanged
from sphinx.addnodes import (
    desc_signature,
    desc_annotation
)
from sphinx.domains.python import PyMethod, PyAttribute, PyClasslike
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

        # account for changed signature in sphinx 4.3, see #62
        if sphinx.version_info >= (4, 3):
            from sphinx.addnodes import desc_sig_space
            return [Text(value), desc_sig_space()]
        else:
            return f"{value} "


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
                        "required": option_default_true,
                        "__doc_disable_except__": option_list_like,
                        "field-signature-prefix": unchanged})

    config_name = "field"
    default_prefix = "attribute"

    def add_required(self, signode: desc_signature):
        """Add `[Required]` if directive option `required` is set.

        """

        if self.options.get("required"):
            signode += desc_annotation("", " [Required]")

    def add_alias(self, signode: desc_signature):
        """Add alias to signature if alias is provided via directive option.

        """

        alias = self.options.get("alias")
        if alias:
            signode += desc_annotation("", f" (alias '{alias}')")

    def handle_signature(self, sig: str, signode: desc_signature) -> TUPLE_STR:
        """Optionally call add alias method.

        """

        fullname, prefix = super().handle_signature(sig, signode)
        self.add_required(signode)
        self.add_alias(signode)

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
