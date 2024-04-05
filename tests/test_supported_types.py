import pytest

from sphinxcontrib.autodoc_pydantic import PydanticModelDocumenter


@pytest.mark.parametrize('model_name', argvalues=['CookingModel'])
def test_autodoc_pydantic_model_no_exception(autodocument, model_name):
    """Only ensure that the model name is correct in the generated rst. This
    is sufficient to ensure that the model can be documented without raising
    an exception.

    """

    kwargs = dict(
        object_path='target.supported_types.CookingModel',
        documenter=PydanticModelDocumenter.objtype,
    )

    # explicit global
    actual = autodocument(**kwargs)
    assert actual[1] == f'.. py:pydantic_model:: {model_name}'
