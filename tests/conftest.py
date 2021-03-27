"""Pytest configuration which is heavily borrowed from sphinx.

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


@pytest.fixture(scope='session')
def rootdir():
    return path(__file__).parent.abspath() / 'roots'


def do_autodoc(app: Sphinx,
               documenter: str,
               object_path: str,
               options_doc: Optional[Dict]=None,
               options_app: Optional[Dict] = None) -> List[str]:
    """Run auto `documenter` for given object referenced by `object_path` within
    provided sphinx `app`. Optionally override app and documenter settings.

    Parameters
    ----------
    app: sphinx.application.Sphinx
        Sphinx app in which documenter is run.
    documenter: str
        Name of documenter which is used to document `object_path`.
    options_doc: dict
        Optional settings to be passed to documenter.
    options_app: dict
        Optional settings to be passed to app.

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

    return bridge.result

@pytest.fixture(scope='session')
def autodocument():
    return do_autodoc