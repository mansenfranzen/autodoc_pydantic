from sphinx.cmd.build import build_main
from pathlib import Path

def test_sphinx_build_without_warnings(tmpdir, recwarn):
    """Ensure that the build succeeds and no warning is raised.

    """

    path_root = Path(__file__).parents[1]
    path_docs = path_root.joinpath("docs", "source")

    status_code = build_main([str(path_docs), str(tmpdir)])
    assert status_code == 0
    assert len(recwarn) == 0
