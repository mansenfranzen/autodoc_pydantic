import pytest

pytest.importorskip('sphinx_rtd_theme')
pytest.importorskip('sphinx_tabs')


def test_sphinx_build_without_error(prod_app, docdir):
    """Ensure that the build succeeds."""

    sphinx_result = prod_app(source_dir=docdir)
    assert sphinx_result.return_code == 0


def test_sphinx_build_emits_no_sphinx_log_warnings(prod_app, log_capturer, docdir):
    """Ensure that the build succeeds and no warning is raised."""

    with log_capturer() as logs:
        prod_app(source_dir=docdir)

    assert len(logs) == 0
