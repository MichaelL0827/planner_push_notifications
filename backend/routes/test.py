from fastapi import APIRouter, Body
from utils.helper import MakeConnection, QueryResult

Router = APIRouter()

@Router.get("/user")
async def GetAllUser():
    try:
        ConnectionString = MakeConnection()
        try:
            Users = QueryResult(ConnectionString, "SELECT * FROM User", "readall", None)
            return Users
        except:
            return {"Status":"Unable to reterieve"}
    except:
        return {"status":"Cannot connect"}