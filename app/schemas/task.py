from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    title: str = Field(max_length=100, examples=["Buy groceries"])
    description: str | None = Field(None, max_length=500, examples=["Milk, eggs, and bread"])
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None

class Task(TaskBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True
