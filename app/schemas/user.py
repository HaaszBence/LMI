from pydantic import BaseModel, Field, EmailStr

class UserBase(BaseModel):
    name: str = Field(max_length=50, examples=["Alice Smith"])
    email: EmailStr = Field(max_length=100, examples=["alice@example.com"])

class UserCreate(UserBase):
    password: str = Field(min_length=8, examples=["secret-password-123"])

class User(UserBase):
    id: int = Field(examples=[1])
    class Config:
        from_attributes = True # This tells Pydantic to read data from SQLAlchemy objects

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None