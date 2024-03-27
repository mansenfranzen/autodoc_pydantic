from pydantic import BaseModel, Field


class FieldDocRender(BaseModel):
    """Doc String.

    :any:`FieldDocRender` *italic*

    :fieldlist: item
    """

    field: int = Field(
        5,
        description="""Doc String.
    
    :any:`FieldDocRender` *italic*
    
    :fieldlist: item
    """,
    )
