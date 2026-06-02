from pydantic import BaseModel, Field
from typing import TYPE_CHECKING, Optional

# This import ONLY happens for your IDE, not at runtime
if TYPE_CHECKING:
    from .user import UserBase

class CommentBase(BaseModel):
    content: str = Field(examples=["Example comment"])
    user_id: int = Field(examples=[1])

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int = Field(examples=[1])
    # String reference to avoid circular import
    author: Optional["UserBase"] = None 

    class Config:
        from_attributes = True

# Now we perform the runtime link
from .user import UserBase
Comment.model_rebuild()
