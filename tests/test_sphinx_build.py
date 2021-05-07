from sphinx.cmd.build import build_main


def test_sphinx_build_without_warnings(tmpdir, recwarn):
    """Ensure that the build succeeds and no warning is raised.

    """

    status_code = build_main(["../docs/source", str(tmpdir)])
    assert status_code == 0
    assert len(recwarn) == 0
