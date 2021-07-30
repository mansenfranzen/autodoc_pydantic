import pytest
from sphinx.cmd.build import build_main
from pathlib import Path

pytest.importorskip('sphinx_rtd_theme')
pytest.importorskip('sphinx_tabs')


def test_sphinx_build_without_error(tmpdir):
    """Ensure that the build succeeds.

    """

    path_root = Path(__file__).parents[1]
    path_docs = path_root.joinpath("docs", "source")
    status_code = build_main([str(path_docs), str(tmpdir)])

    assert status_code == 0


def test_sphinx_build_emits_no_sphinx_log_warnings(tmpdir, log_capturer):
    """Ensure that the build succeeds and no warning is raised.

    """

    with log_capturer() as logs:
        path_root = Path(__file__).parents[1]
        path_docs = path_root.joinpath("docs", "source")
        build_main([str(path_docs), str(tmpdir)])

    assert len(logs) == 0
