"""Pytest configuration which is partially borrowed from sphinx conftest.py.

"""

from typing import Optional, Dict, List
from unittest.mock import Mock

import pytest
from sphinx.application import Sphinx
from sphinx.testing.path import path
from sphinx.testing.restructuredtext import parse
from sphinx.util.docutils import LoggingReporter
from sphinx.ext.autodoc.directive import (
    process_documenter_options,
    DocumenterBridge
)

pytest_plugins = 'sphinx.testing.fixtures'

CONF_DEACTIVATE = {
    "autodoc_pydantic_config_undoc_members": False,
    "autodoc_pydantic_config_members": False,

    "autodoc_pydantic_model_show_json": False,
    "autodoc_pydantic_model_show_config_member": False,
    "autodoc_pydantic_model_show_config_summary": False,
    "autodoc_pydantic_model_show_validator_members": False,
    "autodoc_pydantic_model_show_validator_summary": False,
    "autodoc_pydantic_model_hide_paramlist": True,
    "autodoc_pydantic_model_undoc_members": False,
    "autodoc_pydantic_model_members": False,

    "autodoc_pydantic_validator_replace_signature": False,
    "autodoc_pydantic_validator_list_fields": False,

    "autodoc_pydantic_field_list_validators": False,
    "autodoc_pydantic_field_show_constraints": False,
    "autodoc_pydantic_field_show_alias": False,
}


@pytest.fixture(scope='session')
def rootdir():
    return path(__file__).parent.abspath() / 'roots'


def do_autodoc(app: Sphinx,
               documenter: str,
               object_path: str,
               options_doc: Optional[Dict] = None) -> List[str]:
    """Run auto `documenter` for given object referenced by `object_path` within
    provided sphinx `app`. Optionally override app and documenter settings.

    Parameters
    ----------
    app: sphinx.application.Sphinx
        Sphinx app in which documenter is run.
    documenter: str
        Name of documenter which is used to document `object_path`.
    object_path: str
        Full path to object to be documented.
    options_doc: dict
        Optional settings to be passed to documenter.

    Returns
    -------
    result: list
        List of strings containing lines of generated restructured text.

    """

    # configure app
    app.env.temp_data.setdefault('docname', 'index')  # set dummy docname

    # get documenter and its options
    options_doc = options_doc or {}
    doc_cls = app.registry.documenters[documenter]
    doc_opts = process_documenter_options(doc_cls, app.config, options_doc)
    print(doc_opts)

    # get documenter bridge which is going to contain the result
    state = Mock()
    state.document.settings.tab_width = 8
    bridge = DocumenterBridge(app.env, LoggingReporter(''), doc_opts, 1, state)

    # instaniate documenter and run
    documenter = doc_cls(bridge, object_path)
    documenter.generate()

    return list(bridge.result)


@pytest.fixture(scope="function")
def test_app(make_app, sphinx_test_tempdir, rootdir):
    """Create callable returning a fresh test app.

    """

    def create(testroot: str,
               conf: Optional[Dict] = None,
               deactivate_all: bool = False):
        srcdir = sphinx_test_tempdir / testroot

        if rootdir and not srcdir.exists():
            testroot_path = rootdir / ('test-' + testroot)
            testroot_path.copytree(srcdir)

        kwargs = dict(srcdir=srcdir, confoverrides={})

        if deactivate_all:
            kwargs["confoverrides"].update(CONF_DEACTIVATE)

        if conf:
            kwargs["confoverrides"].update(conf)

        return make_app("html", **kwargs)

    return create


@pytest.fixture(scope='function')
def autodocument(test_app):
    """Create callable to apply auto documenter to given object path.

    """

    def _auto(documenter: str,
              object_path: str,
              options_doc: Optional[Dict] = None,
              options_app: Optional[Dict] = None,
              testroot: str = "ext-autodoc_pydantic",
              deactivate_all: bool = False):
        app = test_app(testroot,
                       conf=options_app,
                       deactivate_all=deactivate_all)

        return do_autodoc(app=app,
                          documenter=documenter,
                          object_path=object_path,
                          options_doc=options_doc)

    return _auto


@pytest.fixture(scope="function")
def parse_rst(test_app):
    """Create callable to parse restructured text and return doc tree.

    """

    def _parse(text: List[str],
               testroot: str = "ext-autodoc_pydantic",
               conf: Optional[Dict] = None,
               deactivate_all: bool = False):

        text = "\n".join(text)
        app = test_app(testroot,
                       conf=conf,
                       deactivate_all=deactivate_all)

        return parse(app=app, text=text)

    return _parse
