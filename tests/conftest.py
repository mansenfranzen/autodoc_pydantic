"""Pytest configuration which is partially borrowed from sphinx conftest.py.

"""
import copy
import inspect
import logging
from logging.handlers import MemoryHandler
from pathlib import Path
from typing import Optional, Dict, List, Callable, Union, Any
from unittest.mock import Mock

import pytest
import sphinx
from pydantic import BaseModel
from sphinx import application
from sphinx.application import Sphinx
from sphinx.cmd import build
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
    "autodoc_pydantic_model_show_field_summary": False,
    "autodoc_pydantic_model_hide_paramlist": True,
    "autodoc_pydantic_model_hide_reused_validator": False,
    "autodoc_pydantic_model_undoc_members": False,
    "autodoc_pydantic_model_members": False,

    "autodoc_pydantic_settings_show_json": False,
    "autodoc_pydantic_settings_show_config_member": False,
    "autodoc_pydantic_settings_show_config_summary": False,
    "autodoc_pydantic_settings_show_validator_members": False,
    "autodoc_pydantic_settings_show_validator_summary": False,
    "autodoc_pydantic_settings_show_field_summary": False,
    "autodoc_pydantic_settings_hide_paramlist": True,
    "autodoc_pydantic_settings_hide_reused_validator": False,
    "autodoc_pydantic_settings_undoc_members": False,
    "autodoc_pydantic_settings_members": False,

    "autodoc_pydantic_validator_replace_signature": True,
    "autodoc_pydantic_validator_list_fields": False,

    "autodoc_pydantic_field_list_validators": False,
    "autodoc_pydantic_field_show_constraints": False,
    "autodoc_pydantic_field_show_alias": False,
    "autodoc_pydantic_field_show_required": False,
    "autodoc_pydantic_field_show_optional": False,
    "autodoc_pydantic_field_show_default": False,
    "autodoc_pydantic_field_swap_name_and_alias": False

}


@pytest.fixture(scope='session')
def rootdir():
    return path(__file__).parent.abspath() / 'roots'


@pytest.fixture(scope='session')
def docdir():
    """Provides path to actual sphinx documentation of autodoc_pydantic.

    """

    return Path(__file__).parents[1].joinpath("docs", "source")


def do_autodoc(app: Sphinx,
               documenter: str,
               object_path: str,
               options_doc: Optional[Dict] = None) -> List[str]:
    """Run auto `documenter` for given object referenced by `object_path`
    within provided sphinx `app`. Optionally override app and documenter
    settings.

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
    """Create callable which returns a fresh sphinx test application. The test
    application is faster than using a production application (like `prod_app`
    fixture).

    This fixture is mainly used to test generated rst (via `autodocument`
    fixture) and generated docutils (via `parse_rst` fixture).

    When testing the production behaviour including all functionality, please
    use `prod_app`.

    """

    def create(testroot: str,
               conf: Optional[Dict] = None,
               deactivate_all: bool = False):
        srcdir = sphinx_test_tempdir / testroot
        srcdir.rmtree(ignore_errors=True)

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
    """Main fixture to test generated reStructuredText from given object path
    with provided auto-documenter while optionally allowing to overwriting
    sphinx app settings `options_app` and auto-documenter directive settings
    `options_doc`.

    Parameters
    ----------
    documenter: str
        Name of the auto-documenter to be used to generate rst.
    object_path: str
        Fully qualified path to the relevant python object to be documented.
    options_doc: dict, optional
        Overwrite auto-documenter directive settings.
    options_app: dict, optional
        Overwrite sphinx app settings.
    testroot: str, optional
        Name of the sphinx test source directory which are located under
        `autodoc_pydantic/tests/roots/`. By default, it uses the `base`
        directory.
    deactivate_all: bool, optional
        If True, completely deactivates all autodoc_pydantic modifications.
        This is useful when testing individual modifications in isolation.

    """

    def _auto(documenter: str,
              object_path: str,
              options_doc: Optional[Dict] = None,
              options_app: Optional[Dict] = None,
              testroot: str = "base",
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
    """Main fixture to test generated doctree/docutil nodes from given
    reStructuredText.

    Essentially it is a wrapper around `sphinx.testing.restructuredtext.parse`
    with a custom test application.

    """

    def _parse(text: List[str],
               testroot: str = "base",
               conf: Optional[Dict] = None,
               deactivate_all: bool = False):
        text = "\n".join(text)
        app = test_app(testroot,
                       conf=conf,
                       deactivate_all=deactivate_all)

        return parse(app=app, text=text)

    return _parse


@pytest.fixture(scope="function")
def log_capturer(monkeypatch):
    """Provides a context manager to intercept all log messages emitted under
    the sphinx namespace for given log level. The returned value is the buffer
    of the user `MemoryHandler` which simply is a list of recored logs.

    To successfully intercept sphinx logs, we need to monkeypatch
    `sphinx.util.logging.setup` because this function removes all handlers
    from the sphinx main logger which we might have added before. Additionally,
    it prevents propagating messages to the root logger. Therefore, we have to
    add our log handler after this function was called.

    Example
    -------

    >>> with log_capturer() as logs:
    >>>     path_root = Path(__file__).parents[1]
    >>>     path_docs = path_root.joinpath("docs", "source")
    >>>     build_main([str(path_docs), str(tmpdir)])
    >>> assert len(logs) == 0

    """

    # deep copy setup to prevent infinite recursion upon mockup
    setup = copy.deepcopy(sphinx.util.logging.setup)

    class LogCapturer:
        def __init__(self, capacity: int = 100, level: int = logging.WARNING):
            self.handler = MemoryHandler(capacity=capacity)
            self.handler.setLevel(level)

        def __enter__(self):
            def mock_logging(*args, **kwargs):
                result = setup(*args, **kwargs)
                logger = logging.getLogger("sphinx")
                logger.addHandler(self.handler)
                return result

            monkeypatch.setattr(sphinx.util.logging, "setup", mock_logging)
            return self.handler.buffer

        def __exit__(self, type, value, traceback):
            if type:
                raise

    return LogCapturer


class SphinxResult(BaseModel):
    """Container for the result of a sphinx run.

    """

    app: Optional[application.Sphinx]
    doctree: Optional[Dict[str, Any]]
    return_code: Optional[int]

    class Config:
        arbitrary_types_allowed = True


def combine_sphinx_init_arguments(args: List, kwargs: Dict) -> Dict:
    """Merges positional and keyword arguments into a dictionary passed to
    `sphinx.application.Sphinx.__init__`. This is required for mocking and
    modifying the sphinx application because sphinx build cmd uses only
    positional arguments and modifying them via position is rather error prone.
    Hence, all positional arguments are converted into keyword arguments which
    then can be modified safely.

    """

    signature = inspect.signature(application.Sphinx.__init__)
    arg_names = list(signature.parameters.keys())[1:]
    named_args = dict(zip(arg_names, args))

    result = copy.deepcopy(kwargs)
    result.update(named_args)
    return result


def create_sphinx_app_mockup(sphinx_result: SphinxResult,
                             confoverrides: Optional[Dict]) -> Callable:
    """Generates a mockup for `sphinx.application.Sphinx` while capturing it
    via changing `sphinx_result` in place and modifying `confoverrides`.

    """

    def capture_sphinx_app(*args, **kwargs):
        safe_kwargs = combine_sphinx_init_arguments(args, kwargs)

        if confoverrides:
            if "confoverrides" in safe_kwargs:
                safe_kwargs["confoverrides"].update(confoverrides)
            else:
                safe_kwargs["confoverrides"] = confoverrides

        app = application.Sphinx(**safe_kwargs)
        sphinx_result.app = app
        return app

    return capture_sphinx_app


@pytest.fixture(scope="function")
def prod_app(tmpdir, monkeypatch) -> Callable:
    """Execute production sphinx app via main cmd entry point for given source
    directory. It returns a `SphinxResult` which allows inspection of the
    generated sphinx app and also the created doctrees.

    Use this fixture with care because it runs a complete sphinx build and may
    slow down tests. If you do not need the inspection of sphinx app please
    consider using `test_app`.

    Parameters
    ----------
    docnames: list, optional
        Provide document names for which the doctree will be loaded for
        inspection. The doctrees are available under `SphinxResult.doctrees`.
    confoverrides: dict, optional
        Force overwrite of `conf.py` settings.

    """

    def run(source_dir: Union[Path, str],
            docnames: Optional[List[str]] = None,
            confoverrides: Optional[Dict] = None) -> SphinxResult:
        sphinx_result = SphinxResult()
        capture_sphinx_app = create_sphinx_app_mockup(
            sphinx_result=sphinx_result,
            confoverrides=confoverrides
        )

        with monkeypatch.context() as m:
            m.setattr(build, "Sphinx", capture_sphinx_app)
            sphinx_result.return_code = build.build_main([str(source_dir),
                                                          str(tmpdir)])

        if docnames:
            doctree = {docname: sphinx_result.app.env.get_doctree(docname)
                       for docname in docnames}
            sphinx_result.doctree = doctree

        return sphinx_result

    return run
