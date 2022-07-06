VERSION_TEMPLATE = """
This documentation was built with the following environment:

:sphinx: {sphinx}

:pydantic: {pydantic}

:sphinx-rtd-theme: {sphinx_rtd_theme}

:sphinx-tabs: {sphinx_tabs}

:sphinx-copybutton: {sphinx_copybutton}

:sphinxcontrib-mermaid: {sphinxcontrib_mermaid}"""
CONFIG_DESC_TPL = """
.. _{confpy}:

{title}

{description}

**Configuration** *(added in version {version})*

:conf.py: *{confpy}*

:directive: *{directive_option}*

**Available values with rendered examples**

.. tabs::

{tabs}
           
   .. tab:: *example code*

      .. autocodeblock:: {example_path}

"""
CONFIG_DESC_TAB_TPL = """
   .. tab:: {value_label}

      .. {directive}:: {path}
         :__doc_disable_except__: {directive_option}
         :{directive_option}: {value}{enable}
         :noindex:
"""
