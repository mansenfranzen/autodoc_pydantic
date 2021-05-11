"""This module contains directive utilities like option validation functions
and the PyAutoDoc composite class.

"""
import functools
from typing import Any, Union, List, Set, Callable, Optional

from docutils.nodes import emphasis
from docutils.parsers.rst import Directive
from sphinx.addnodes import pending_xref
from sphinx.environment import BuildEnvironment
from sphinx.ext.autodoc import ALL, Documenter

from sphinxcontrib.autodoc_pydantic.inspection import NamedReference


class NullType:
    """Helper class to present a Null value which is not the same
    as python's `None`. This represents a missing value, or no
    value at all by convention. It should be used as a singleton.

    """

    def __bool__(self):
        return False

NONE = NullType()


def create_field_href(reference: NamedReference,
                      env: BuildEnvironment) -> pending_xref:
    """Create `pending_xref` node with link to given `reference`.

    """

    text = reference.name
    options = {'refdoc': env.docname,
               'refdomain': "py",
               'reftype': "obj",
               'reftarget': reference.ref}

    refnode = pending_xref(reference.name, **options)
    classes = ['xref', "py", '%s-%s' % ("py", "obj")]
    refnode += emphasis(text, text, classes=classes)
    return refnode


def remove_node_by_tagname(nodes: List, tagname: str):
    """Removes node from list of `nodes` with given `tagname` in place.

    """

    for remove in [node for node in nodes if node.tagname == tagname]:
        nodes.remove(remove)


def option_members(arg: Any) -> Union[object, List[str]]:
    """Used to convert the :members: option to auto directives.

    """

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

    @staticmethod
    def sanitize_configuration_option_name(name: str) -> str:
        """Provide full app environment configuration name for given option
        name while converting "-" to "_".

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

    def get_configuration_by_name(self, name: str) -> Any:
        """Get configuration value from app environment configuration.
        If `name` does not exist, return NONE.

        """

        config_name = self.sanitize_configuration_option_name(name)
        return getattr(self.parent.env.config, config_name, NONE)

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
            return self.get_configuration_by_name(name)

    def option_is_false(self, name: str, prefix: bool = False) -> bool:
        """Get option value for given `name`. First, looks for explicit
        directive option values (e.g. :member-order:) which have highest
        priority. Second, if no directive option is given, get the default
        option value provided via the app environment configuration.

        Enforces result to be either True or False.

        Parameters
        ----------
        name: str
            Name of the option.
        prefix: bool
            If True, add `pyautodoc_prefix` to name.

        """

        return self.get_option_value(name=name, prefix=prefix) is False

    def option_is_true(self, name: str, prefix: bool = False) -> bool:
        """Get option value for given `name`. First, looks for explicit
        directive option values (e.g. :member-order:) which have highest
        priority. Second, if no directive option is given, get the default
        option value provided via the app environment configuration.

        Enforces result to be either True or False.

        Parameters
        ----------
        name: str
            Name of the option.
        prefix: bool
            If True, add `pyautodoc_prefix` to name.

        """

        return self.get_option_value(name=name, prefix=prefix) is True


    def set_default_option(self, name: str):
        """Set default option value for given `name` from app environment
        configuration if an explicit directive option was not provided.

        Parameters
        ----------
        name: str
            Name of the option.

        """

        if (name not in self.parent.options) and (self.is_available(name)):
            self.parent.options[name] = self.get_configuration_by_name(name)

    def set_default_option_with_value(self, name: str,
                                      value_true: Any,
                                      value_false: Optional[Any] = NONE):
        """Set option value for given `name`. Depending on app environment
        configuration boolean value choose either `value_true` or
        `value_false`. This is only relevant if option value has not been set,
        yet.

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
            if self.get_configuration_by_name(name):
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

    def sanitize_configuration_option_name(self, name: str) -> str:
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
