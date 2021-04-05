import pytest
from docutils.nodes import Text, paragraph, TextElement
from sphinx import addnodes
from sphinx.addnodes import desc, desc_signature, desc_name, desc_parameterlist, \
    desc_content, desc_annotation, desc_addname, pending_xref
from sphinx.testing.restructuredtext import parse
from sphinx.testing.util import assert_node


@pytest.mark.sphinx('html', testroot='ext-autodoc_pydantic')
def test_model_plain(app):
    """Tests plain minimal pydantic model with doc string. Ensure that
    annotation is correct.

    """

    input_rst = ('.. py:pydantic_model:: PlainModel\n'
                 '   :module: target.model\n'
                 '\n'
                 '   Model Plain.\n')

    output_nodes = (
        addnodes.index,
        [desc, ([desc_signature, ([desc_annotation, "pydantic model "],
                                  [desc_addname, "target.model."],
                                  [desc_name, "PlainModel"])],
                [desc_content, ([paragraph, "Model Plain."])])
         ]
    )

    doctree = parse(app, input_rst)
    assert_node(doctree, output_nodes)


@pytest.mark.sphinx('html', testroot='ext-autodoc_pydantic')
def test_model_with_field(app):
    """Tests plain minimal pydantic model with doc string. Ensure that
    annotation is correct.

    """

    input_rst = ('.. py:pydantic_model:: ModelWithField\n'
                 '   :module: target.model\n'
                 '\n'
                 '   Model With Field.\n'
                 '\n'
                 '\n'
                 '   .. py:pydantic_field:: ModelWithField.field\n'
                 '      :module: target.model\n'
                 '      :type: int\n'
                 '      :value: 1\n'
                 '\n'
                 '      Doc field\n'
                 '\n')

    output_nodes = (
        addnodes.index,
        [desc, ([desc_signature, ([desc_annotation, "pydantic model "],
                                  [desc_addname, "target.model."],
                                  [desc_name, "ModelWithField"])],
                [desc_content, ([paragraph, "Model With Field."],
                                addnodes.index,
                                [desc, ([desc_signature, ([desc_annotation, "field "],
                                                          [desc_name, "field"],
                                                          [desc_annotation, ()],
                                                          [desc_annotation, " = 1"])],
                                        [desc_content, ([paragraph, "Doc field"])])
                                 ])
                 ])
         ]
    )

    doctree = parse(app, input_rst)
    assert_node(doctree, output_nodes)
