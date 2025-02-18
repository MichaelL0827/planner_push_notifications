from fastapi import APIRouter, Body
from utils.helper import MakeConnection, QueryResult, HashPassword
from models.create import CreateUser
from models.queries import CreateNewUser

Router = APIRouter()

@Router.post("/user")
async def CreateUser(User: CreateUser = Body(...)):
    try:
        ConnectionString = MakeConnection()
        try:
            User = QueryResult(ConnectionString, CreateNewUser, 'create', (User.Username, User.Firstname, User.Lastname, User.Password,))
            return True
        except Exception as Err:
            return {"Status":"Cannot Create the"}
    except:
        return {"Status":"Cannot Connect to the Database"}