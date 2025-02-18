from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

Server = FastAPI()

Server.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])

@Server.get("/")
def Root():
    return{"Routes": [
        {"Create User" : "POST, /api/create/user"},
        {"Create Task" : "POST, /api/create/task"}
        ]}

# fastapi dev server.py
# uvicorn main:Server --reload  