"""This module contains utility functions not directly.

"""

import importlib
from types import ModuleType
from typing import Optional


def import_module(name) -> Optional[ModuleType]:
    """Simple importer intercepting import exception.

    """

    try:
        return importlib.import_module(name)
    except ModuleNotFoundError:
        return None


def get_version(name):
    """Get version info from standard __version__.

    """

    module = import_module(name)
    if module:
        return module.__version__
    else:
        return "NA"


def get_version_special(name):
    """Get version info from version.VERSION.

    """

    module = import_module(name)
    if module:
        return module.version.VERSION
    else:
        return "NA"


def show_versions():
    """Print currently used versions.

    """

    print(
        f"Version info: "
        f"autodoc_pydantic: {get_version('sphinxcontrib.autodoc_pydantic')} | "
        f"pydantic: {get_version_special('pydantic')} | "
        f"sphinx: {get_version('sphinx')} | "
        f"sphinx_rtd_theme: {get_version('sphinx_rtd_theme')} | "
        f"sphinx_tabs: {get_version('sphinx_tabs')}")
