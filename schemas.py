from pydantic import BaseModel, ConfigDict, Field

# without default values, items are required
class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)

    # items not provided by the client
    id: int
    date_posted: str