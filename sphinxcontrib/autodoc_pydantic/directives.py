"""This module contains pydantic specific directives.

"""
from typing import Tuple

from docutils.parsers.rst.directives import unchanged
from sphinx.addnodes import (
    desc_signature,
    desc_annotation
)
from sphinx.domains.python import PyMethod, PyAttribute, PyClasslike
from sphinxcontrib.autodoc_pydantic.inspection import ModelWrapper
from sphinxcontrib.autodoc_pydantic.util import (
    PydanticAutoDirective,
    option_default_true,
    option_list_like,
    create_field_href, remove_node_by_tagname
)


class PydanticValidator(PyMethod):
    """Description of pydantic validator.

    """

    option_spec = PyMethod.option_spec.copy()
    option_spec.update({"validator-replace-signature": option_default_true,
                        "__doc_disable_except__": option_list_like,
                        "validator-signature-prefix": unchanged})

    def __init__(self, *args):
        super().__init__(*args)
        self.pyautodoc = PydanticAutoDirective(self)

    def replace_return_node(self, signode: desc_signature):
        """Replaces the return node with references to validated fields.

        """

        remove_node_by_tagname(signode.children, "desc_parameterlist")

        # replace nodes
        class_name = "autodoc_pydantic_validator_arrow"
        signode += desc_annotation("", "  »  ", classes=[class_name])

        # get imports, names and fields of validator
        validator_name = signode["fullname"].split(".")[-1]
        wrapper = ModelWrapper.from_signode(signode)
        fields = wrapper.get_fields_for_validator(validator_name)

        # add field reference nodes
        first_field = fields[0]
        signode += create_field_href(first_field, env=self.env)
        for field in fields[1:]:
            signode += desc_annotation("", ", ")
            signode += create_field_href(field, self.env)

    def handle_signature(self, sig: str, signode: desc_signature) -> Tuple[
        str, str]:
        fullname, prefix = super().handle_signature(sig, signode)

        if self.pyautodoc.get_option_value("validator-replace-signature"):
            self.replace_return_node(signode)

        return fullname, prefix

    def get_signature_prefix(self, sig: str) -> str:
        """Overwrite original signature prefix with custom pydantic ones.

        """

        prefix = self.pyautodoc.get_option_value("validator-signature-prefix")
        value = prefix or "classmethod"
        return f"{value} "


class PydanticField(PyAttribute):
    """Description of pydantic field.

    """

    option_spec = PyAttribute.option_spec.copy()
    option_spec.update({"field-show-alias": option_default_true,
                        "__doc_disable_except__": option_list_like,
                        "field-signature-prefix": unchanged})

    def __init__(self, *args):
        super().__init__(*args)
        self.pyautodoc = PydanticAutoDirective(self)

    def get_signature_prefix(self, sig: str) -> str:
        """Overwrite original signature prefix with custom pydantic ones.

        """

        prefix = self.pyautodoc.get_option_value("field-signature-prefix")
        value = prefix or "attribute"
        return f"{value} "

    def add_alias(self, signode: desc_signature):
        """Replaces the return node with references to validated fields.

        """

        # get imports, names and fields of validator
        field_name = signode["fullname"].split(".")[-1]
        wrapper = ModelWrapper.from_signode(signode)
        field = wrapper.get_field_object_by_name(field_name)
        alias = field.alias

        if alias != field_name:
            signode += desc_annotation("", f" (alias '{alias}')")

    def handle_signature(self, sig: str, signode: desc_signature) -> Tuple[
        str, str]:
        fullname, prefix = super().handle_signature(sig, signode)

        if self.pyautodoc.get_option_value("field-show-alias"):
            self.add_alias(signode)

        return fullname, prefix


class PydanticModel(PyClasslike):
    """Description of pydantic model.

    """

    option_spec = PyClasslike.option_spec.copy()
    option_spec.update({"__doc_disable_except__": option_list_like,
                        "model-signature-prefix": unchanged})

    def __init__(self, *args):
        super().__init__(*args)
        self.pyautodoc = PydanticAutoDirective(self)

    def get_signature_prefix(self, sig: str) -> str:
        """Overwrite original signature prefix with custom pydantic ones.

        """

        prefix = self.pyautodoc.get_option_value("model-signature-prefix")
        value = prefix or "class"
        return f"{value} "


class PydanticSettings(PyClasslike):
    """Description of pydantic settings.

    """

    option_spec = PyClasslike.option_spec.copy()
    option_spec.update({"__doc_disable_except__": option_list_like,
                        "settings-signature-prefix": unchanged})

    def __init__(self, *args):
        super().__init__(*args)
        self.pyautodoc = PydanticAutoDirective(self)

    def get_signature_prefix(self, sig: str) -> str:
        """Overwrite original signature prefix with custom pydantic ones.

        """

        prefix = self.pyautodoc.get_option_value("settings-signature-prefix")
        value = prefix or "class"
        return f"{value} "


class PydanticConfigClass(PyClasslike):
    """Description of pydantic model/settings config class."""

    option_spec = PyClasslike.option_spec.copy()
    option_spec.update({"__doc_disable_except__": option_list_like,
                        "config-signature-prefix": unchanged})

    def __init__(self, *args):
        super().__init__(*args)
        self.pyautodoc = PydanticAutoDirective(self)

    def get_signature_prefix(self, sig: str) -> str:
        """Overwrite original signature prefix with custom pydantic ones.

        """

        prefix = self.pyautodoc.get_option_value("config-signature-prefix")
        value = prefix or "class"
        return f"{value} "
