from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.create import Router as Create
from routes.test import Router as Test

Server = FastAPI()

Server.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])

Server.include_router(Create, prefix="/api/create")
Server.include_router(Test, prefix="/api/test")

@Server.get("/")
async def Root():
    return{"Routes": [
        {"Create User" : "POST, /api/create/user"},
        {"Create Task" : "POST, /api/create/task"}
        ]}

# fastapi dev server.py
# uvicorn main:Server --reload  