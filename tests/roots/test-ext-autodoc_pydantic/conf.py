import os
import sys

sys.path.insert(0, os.path.abspath('.'))

extensions = ['sphinx.ext.autodoc',
              'sphinxcontrib.autodoc_pydantic']
