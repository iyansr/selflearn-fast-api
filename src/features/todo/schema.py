from pydantic import BaseModel, Field
from uuid import UUID

class TodoBase(BaseModel):
    title: str = Field(description="The title of the todo")
    description: str = Field(description="The description of the todo")

class AddTodo(TodoBase):
    pass

class TodoResponse(TodoBase):
    id: UUID
    completed: bool = Field(default=False)
    
    class Config:
        from_attributes = True

class UpdateTodo(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None