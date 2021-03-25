"""This module contains pydantic specific directives.

"""
from typing import Tuple
import importlib

from docutils.nodes import literal, Element
from sphinx.addnodes import desc_signature, pending_xref, desc_sig_element, \
    desc_sig_punctuation, desc_annotation
from sphinx.domains.python import PyMethod, PyAttribute, PyClasslike
from sphinx.environment import BuildEnvironment

from sphinxcontrib.autodoc_pydantic.inspection import ModelWrapper, \
    ValidatorFieldMapping, NamedReference


def create_href(text, target, env) -> pending_xref:
    # create the reference node
    options = {'refdoc': env.docname,
               'refdomain': "py",
               'reftype': "obj",
               'reftarget': target}
    refnode = pending_xref(text, **options)
    classes = ['xref', "py", '%s-%s' % ("py", "obj")]
    refnode += literal(text, text, classes=classes)
    return refnode


def create_field_href(reference: NamedReference,
                      env: BuildEnvironment) -> pending_xref:
    return create_href(text=reference.name,
                       target=reference.ref,
                       env=env)


def remove_nodes_by_tagname(parent: Element, tagname: str):
    """Removes all nodes with given `tagname` from `parent` node. Modifes parent
    node in place.

    """

    nodes = [node for node in parent
             if node.tagname == tagname]

    for node in nodes:
        parent.remove(node)

class PydanticValidator(PyMethod):
    """Description of a method."""

    def replace_return_node(self, signode: desc_signature):
        """Replaces the return node with references to validated fields.

        """

        # replace nodes
        remove_nodes_by_tagname(signode, "desc_returns")
        signode += desc_sig_element("", " » ")

        # get imports, names and fields of validator
        module = importlib.import_module(name=signode['module'])
        model_name, validator_name = signode["fullname"].split(".")
        model = getattr(module, model_name)
        wrapper = ModelWrapper.factory(model)
        fields = wrapper.get_fields_for_validator(validator_name)

        # add field reference nodes
        first_field = fields[0]
        signode += create_field_href(first_field, env=self.env)
        for field in fields[1:]:
            signode += desc_sig_element("", ", ")
            signode += create_field_href(field, self.env)

    def handle_signature(self, sig: str, signode: desc_signature) -> Tuple[
        str, str]:
        fullname, prefix = super().handle_signature(sig, signode)

        if not self.env.config["autodoc_pydantic_validator_show_paramlist"]:
            remove_nodes_by_tagname(signode, "desc_parameterlist")

        if self.env.config["autodoc_pydantic_validator_replace_retann"]:
            self.replace_return_node(signode)

        return fullname, prefix

    def get_signature_prefix(self, sig: str) -> str:
        return "validator "


class PydanticField(PyAttribute):
    """Description of an attribute."""

    def get_signature_prefix(self, sig: str) -> str:
        return "field "

    def add_alias(self, signode: desc_signature):
        """Replaces the return node with references to validated fields.

        """

        # get imports, names and fields of validator
        module = importlib.import_module(name=signode['module'])
        model_name, field_name = signode["fullname"].split(".")
        model = getattr(module, model_name)
        wrapper = ModelWrapper.factory(model)
        field = wrapper.get_field_object_by_name(field_name)
        alias = field.alias

        if alias != field_name:
            signode += desc_sig_punctuation("", f" (alias '{alias}')")

    def handle_signature(self, sig: str, signode: desc_signature) -> Tuple[
        str, str]:
        fullname, prefix = super().handle_signature(sig, signode)

        if self.env.config["autodoc_pydantic_field_show_alias"]:
            self.add_alias(signode)

        return fullname, prefix




class PydanticModel(PyClasslike):
    """Description of an attribute."""

    def handle_signature(self, sig: str, signode: desc_signature) -> Tuple[
        str, str]:
        fullname, prefix = super().handle_signature(sig, signode)

        if not self.env.config["autodoc_pydantic_model_show_paramlist"]:
            remove_nodes_by_tagname(signode, "desc_parameterlist")

        return fullname, prefix

    def get_signature_prefix(self, sig: str) -> str:
        return "pydantic model "

class PydanticSettings(PydanticModel):
    """Description of an attribute."""

    def get_signature_prefix(self, sig: str) -> str:
        return "pydantic settings "


class PydanticConfigClass(PyClasslike):
    """Description of an attribute."""

    def get_signature_prefix(self, sig: str) -> str:
        return "model "
