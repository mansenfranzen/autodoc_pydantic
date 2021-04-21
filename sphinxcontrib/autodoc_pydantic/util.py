"""This module contains directive utilities like option validation functions
and the PyAutoDoc composite class.

"""
import functools
import pydoc
from typing import Any, Union, List, Set, Callable, Optional

from docutils.nodes import emphasis, Node
from docutils.parsers.rst import Directive
from sphinx.addnodes import pending_xref
from sphinx.environment import BuildEnvironment
from sphinx.ext.autodoc import ALL, Documenter

from sphinxcontrib.autodoc_pydantic.inspection import NamedReference

NONE = object()


def create_href(text, target, env) -> pending_xref:
    # create the reference node
    options = {'refdoc': env.docname,
               'refdomain': "py",
               'reftype': "obj",
               'reftarget': target}
    refnode = pending_xref(text, **options)
    classes = ['xref', "py", '%s-%s' % ("py", "obj")]
    refnode += emphasis(text, text, classes=classes)
    return refnode


def create_field_href(reference: NamedReference,
                      env: BuildEnvironment) -> pending_xref:
    return create_href(text=reference.name,
                       target=reference.ref,
                       env=env)


def remove_node_by_tagname(nodes: List, tagname: str):
    """Removes node from list of `nodes` with given `tagname` in place.

    """

    for remove in [node for node in nodes if node.tagname == tagname]:
        nodes.remove(remove)



def option_members(arg: Any) -> Union[object, List[str]]:
    """Used to convert the :members: option to auto directives."""
    if isinstance(arg, str):
        sanitized = arg.lower()
        if sanitized == "true":
            return ALL
        elif sanitized == "false":
            return None

    if arg in (None, True):
        return ALL
    elif arg is False:
        return None
    else:
        return [x.strip() for x in arg.split(',') if x.strip()]


def option_one_of_factory(choices: Set[Any]) -> Callable:
    """Create a option validation function which allows only one value
    of given set of provided `choices`.

    """

    def option_func(value: Any):
        if value not in choices:
            raise ValueError(f"Option value has to be on of {choices}")
        return value

    return option_func


def option_default_true(arg: Any) -> bool:
    """Used to define boolean options with default to True if no argument
    is passed.

    """

    if isinstance(arg, bool):
        return arg

    if arg is None:
        return True

    sanitized = arg.strip().lower()

    if sanitized == "true":
        return True
    elif sanitized == "false":
        return False
    else:
        raise ValueError(f"Directive option argument '{arg}' is not valid. "
                         f"Valid arguments are 'true' or 'false'.")


def option_list_like(arg: Any) -> Set[str]:
    """Used to define a set of items.

    """

    if not arg:
        return set()
    else:
        return {x.strip() for x in arg.split(",")}


class PydanticAutoDirective:
    """Composite class providing methods to handle getting and setting
    directive option values.

    """

    def __init__(self, parent: Union[Documenter, Directive]):
        self.parent = parent
        self.add_default_options()

    def add_default_options(self):
        """Adds all default options.

        """

        options = getattr(self.parent, "pyautodoc_set_default_option", [])
        for option in options:
            self.set_default_option(option)


    def get_configuration_option_name(self, name: str) -> str:
        """Provide full app environment configuration name for given option
        name.

        Parameters
        ----------
        name: str
            Name of the option.

        Returns
        -------
        full_name: str
            Full app environment configuration name.

        """

        sanitized = name.replace("-", "_")

        return f"autodoc_pydantic_{sanitized}"

    def is_available(self, name: str) -> bool:
        """Check if option is usable.

        """

        available = self.parent.options.get("__doc_disable_except__")
        if available is None:
            return True
        else:
            return name in available

    def get_option_value(self, name: str, prefix: bool = False) -> Any:
        """Get option value for given `name`. First, looks for explicit
        directive option values (e.g. :member-order:) which have highest
        priority. Second, if no directive option is given, get the default
        option value provided via the app environment configuration.

        Parameters
        ----------
        name: str
            Name of the option.
        prefix: bool
            If True, add `pyautodoc_prefix` to name.

        """

        if prefix:
            name = f"{self.parent.pyautodoc_prefix}-{name}"

        if name in self.parent.options:
            return self.parent.options[name]
        elif self.is_available(name):
            config_name = self.get_configuration_option_name(name)
            return self.parent.env.config[config_name]

    def set_default_option(self, name: str):
        """Set default option value for given `name` from app environment
        configuration if an explicit directive option was not provided.

        Parameters
        ----------
        name: str
            Name of the option.

        """

        if (name not in self.parent.options) and (self.is_available(name)):
            config_name = self.get_configuration_option_name(name)
            value = self.parent.env.config[config_name]
            self.parent.options[name] = value

    def set_default_option_with_value(self, name: str,
                                      value_true: Any,
                                      value_false: Optional[Any] = NONE):
        """Set option value for given `name`. Depending on app environment
        configuration boolean value choose either `value_true` or `value_false`.
        This is only relevant if option value has not been set, yet.

        Parameters
        ----------
        name: str
            Name of the option.
        value_true:
            Value to be set if True.
        value_false:
            Value to be set if False.

        """

        value = self.parent.options.get(name)

        if value is not None and self.is_available(name):
            config_name = self.get_configuration_option_name(name)
            if self.parent.env.config[config_name]:
                self.parent.options[name] = value_true
            elif value_false is not NONE:
                self.parent.options[name] = value_false


class PydanticAutoDoc(PydanticAutoDirective):
    """Composite class providing methods to handle getting and setting
    autodoc directive option values.

    """

    def __init__(self, *args):
        super().__init__(*args)
        self.add_pass_through_to_directive()

    def get_configuration_option_name(self, name: str) -> str:
        """Provide full app environment configuration name for given option
        name.

        Parameters
        ----------
        name: str
            Name of the option.

        Returns
        -------
        full_name: str
            Full app environment configuration name.

        """

        sanitized = name.replace("-", "_")
        prefix = self.parent.objtype.split("_")[-1]

        if prefix not in sanitized:
            sanitized = f"{prefix}_{sanitized}"

        return f"autodoc_pydantic_{sanitized}"

    def get_pydantic_object_from_name(self) -> Any:
        """Return the object referenced by name.

        """

        obj = pydoc.locate(self.parent.name)

        if obj is None:
            raise ValueError(f"Could not locate object from path "
                             f"`{self.parent.name}` for "
                             f"`{self.parent.object}`.")
        else:
            return obj

    def add_pass_through_to_directive(self):
        """Intercepts documenters `add_directive_header` and adds pass through.

        """

        func = self.parent.add_directive_header

        pass_through = ["__doc_disable_except__"]
        specific = getattr(self.parent, "pyautodoc_pass_to_directive", [])
        pass_through.extend(specific)

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            for option in pass_through:
                self.pass_option_to_directive(option)

            return result

        self.parent.add_directive_header = wrapped


    def pass_option_to_directive(self, name: str):
        """Pass an autodoc option through to the generated directive.

        """

        if name in self.parent.options:
            source_name = self.parent.get_sourcename()
            value = self.parent.options[name]

            if isinstance("value", set):
                value = ", ".join(value)

            self.parent.add_line(f"   :{name}: {value}", source_name)