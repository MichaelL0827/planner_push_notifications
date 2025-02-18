from fastapi import APIRouter, Body
from utils.helper import MakeConnection, QueryResult, HashPassword
from models.create import CreateUser, CreateTask
from models.queries import CreateNewUser, CreateNewTask

Router = APIRouter()

@Router.post("/user")
async def CreateUser(User: CreateUser = Body(...)):
    try:
        ConnectionString = MakeConnection()
        try:
            User = QueryResult(ConnectionString, CreateNewUser, 'create', (User.Username, User.Firstname, User.Lastname, HashPassword(User.Password),))
            return True
        except Exception as Err:
            return {"Status":"Cannot Create the"}
    except:
        return {"Status":"Cannot Connect to the Database"}

@Router.post("/task")
async def CreateTask(Task: CreateTask = Body(...)):
    try: 
        ConnectionString = MakeConnection()
        try:
            Task = QueryResult(ConnectionString, CreateNewTask, 'create', (Task.Name, Task.Description, Task.Username),)
            return True
        except Exception as Err:
            return {"Status":"Cannot Create the"}
    except:
        return {"Status":"Cannot Connect to the Database"}