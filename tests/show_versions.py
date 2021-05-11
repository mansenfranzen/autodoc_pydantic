"""This module is a little helper module to show dependency versions in
test execution.

"""

import pydantic
import sphinx
import sphinx_rtd_theme
import sphinx_tabs


def show_versions():
    print(f"Version info: "
          f"pydantic: {pydantic.version.VERSION} | "
          f"sphinx: {sphinx.__version__} | "
          f"sphinx_rtd_theme: {sphinx_rtd_theme.__version__} | "
          f"sphinx_tabs: {sphinx_tabs.__version__}")


if __name__ == "__main__":
    show_versions()
