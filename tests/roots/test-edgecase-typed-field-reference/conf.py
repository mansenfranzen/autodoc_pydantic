import os
import sys

sys.path.insert(0, os.path.abspath(''))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinxcontrib.autodoc_pydantic',
]
