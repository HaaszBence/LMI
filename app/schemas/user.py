from pydantic import BaseModel, Field, EmailStr

class UserBase(BaseModel):
    name: str = Field(examples=["Alice Smith"])
    email: EmailStr = Field(examples=["alice@example.com"])

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int = Field(examples=[1])
    class Config:
        from_attributes = True # This tells Pydantic to read data from SQLAlchemy objects