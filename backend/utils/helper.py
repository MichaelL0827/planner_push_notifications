import hashlib as hash
import os
from dotenv import load_dotenv
from models.connect import ConnectDatabase

def HashPassword(Password: str):
    return hash.sha256(Password.encode()).hexdigest()

def MakeConnection():
    load_dotenv()
    HOST = os.getenv("HOST")
    USER = os.getenv("USER")
    PASSWORD = os.getenv("PASSWORD")
    DATABASE = os.getenv("DATABASE")
    try:
        ConnectionString = ConnectDatabase(HOST, USER, PASSWORD, DATABASE).Connection()
        return ConnectionString
    except:
        return False

def QueryResult(ConnectionString:str, Query:str, Flag:str, Params: tuple[str] | None = None):
    try:
        Cursor = ConnectionString.cursor(dictionary=True)
    except:
        return False
    try:
        match Flag:
            case 'read':
                if Params is None:
                    Cursor.execute(Query)
                else:
                    Cursor.execute(Query, Params)
                Single = Cursor.fetchone()
                return Single
            case 'readall':
                if Params is None:
                    Cursor.execute(Query)
                else:
                    Cursor.execute(Query, Params)
                Multiple = Cursor.fetchall()
                return Multiple
            case 'create':
                Cursor.execute(Query, Params)
                ConnectionString.commit()
                return True
            case 'delete':
                Cursor.execute(Query, Params)
                ConnectionString.commit()
                return True
    except:
        return False