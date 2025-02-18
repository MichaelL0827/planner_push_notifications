from pydantic import BaseModel
from datetime import datetime

class CreateUser(BaseModel):
    Username: str
    Firstname: str
    Lastname: str
    Password: str

class CreateTask(BaseModel):
    Name: str
    Description: str
    UserId: int

class CreateTodo(BaseModel):
    Name: str
    Description: str
    Completed: bool
    Start: datetime
    End: datetime
    TaskId: int

class CreateUserTask(BaseModel):
    UserId: int
    TaskId: int
    Permission: bool