from fastapi import APIRouter, Body
from utils.helper import MakeConnection, QueryResult, HashPassword
from models.connect import ConnectDatabase
from models.create import CreateUser, CreateTask, CreateTodo, CreateUserTask
from models.queries import CreateNewUser

Router = APIRouter()

Router.post("/user")
def CreateUser(User: CreateUser = Body(...)):
    try:
        ConnectionString = MakeConnection()
        try:
            User = QueryResult(ConnectionString, CreateNewUser, 'create', (User.Username,User.Firstname, User.Lastname, HashPassword(User.Password),))
        except:
            exit()
    except:
        exit()