"""Pytest configuration which is partially borrowed from sphinx conftest.py.

"""

from typing import Optional, Dict, List
from unittest.mock import Mock

import pytest
from sphinx.application import Sphinx
from sphinx.ext.autodoc.directive import process_documenter_options, \
    DocumenterBridge

from sphinx.testing.path import path
from sphinx.util.docutils import LoggingReporter

pytest_plugins = 'sphinx.testing.fixtures'

CONF_DEACTIVATE = {
    "autodoc_pydantic_config_show": False,

    "autodoc_pydantic_model_show_json": False,
    "autodoc_pydantic_model_show_config": False,
    "autodoc_pydantic_model_show_validators": False,
    "autodoc_pydantic_model_show_paramlist": False,
    "autodoc_pydantic_model_undoc_members": False,
    "autodoc_pydantic_model_members": False,

    "autodoc_pydantic_validator_show": False,
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
               options_doc: Optional[Dict] = None,
               options_app: Optional[Dict] = None) -> List[str]:
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
    options_app: dict
        Optional settings to be passed to app.

    Returns
    -------
    result: list
        List of strings containing lines of generated restructured text.

    """

    # configure app
    app.env.temp_data.setdefault('docname', 'index')  # set dummy docname
    if options_app:
        for key, value in options_app.items():
            app.config[key] = value

    # get documenter and its options
    options_doc = options_doc or {}
    doc_cls = app.registry.documenters[documenter]
    doc_opts = process_documenter_options(doc_cls, app.config, options_doc)

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

    def create(testroot: str, deactivate_all: bool = False):
        srcdir = sphinx_test_tempdir / testroot

        if rootdir and not srcdir.exists():
            testroot_path = rootdir / ('test-' + testroot)
            testroot_path.copytree(srcdir)

        kwargs = dict(srcdir=srcdir)
        if deactivate_all:
            kwargs["confoverrides"] = CONF_DEACTIVATE

        return make_app("html", **kwargs)

    return create


@pytest.fixture(scope='function')
def autodocument(test_app):
    """Create callable which applies auto documenter to given object path.
    """

    def _auto(documenter: str,
              object_path: str,
              options_doc: Optional[Dict] = None,
              options_app: Optional[Dict] = None,
              testroot: str = "ext-autodoc_pydantic",
              deactivate_all: bool = False):
        app = test_app(testroot, deactivate_all)
        return do_autodoc(app=app,
                          documenter=documenter,
                          object_path=object_path,
                          options_app=options_app,
                          options_doc=options_doc)

    return _auto
