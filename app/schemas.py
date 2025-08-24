from pydantic import BaseModel, Field
from typing import Optional

# Auth

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    username: Optional[str] = None

class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=4, max_length=128)

class UserOut(BaseModel):
    id: int
    username: str

    model_config = {"from_attributes": True}

# Todos

class TodoBase(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    completed: Optional[bool] = None

class TodoOut(TodoBase):
    id: int
    owner_id: int

    model_config = {"from_attributes": True}
