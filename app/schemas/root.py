from pydantic import BaseModel, Field

class Root(BaseModel):
    message: str = Field(examples=["Welcome to the API!"])