# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
import sys
from pathlib import Path

path = Path(__file__)
path_autodoc_pydantic = path.parents[2]
path_examples = path.parents[2].joinpath("tests",
                                         "roots",
                                         "test-base")

sys.path.insert(0, str(path.parent))
sys.path.insert(0, str(path_examples))
sys.path.insert(0, str(path_autodoc_pydantic))

# -- Project information -----------------------------------------------------

project = 'autodoc_pydantic'
copyright = '2021, Franz Wöllert'
author = 'Franz Wöllert'

# The full version, including alpha/beta/rc tags
release = '1.5.1'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx_tabs.tabs",
    "sphinx_copybutton",
    "sphinxcontrib.autodoc_pydantic",
    "sphinxcontrib.mermaid",
    "sphinx.ext.viewcode",
    "extensions"
]

autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_logo = "material/logo_white.svg"
html_theme_options = {
    'logo_only': True,
    'display_version': True
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['js']

add_module_names = False

mermaid_version = ""
html_static_path = ["_static"]
html_js_files = ['mermaid.min.js']
html_css_files = ['custom.css']
