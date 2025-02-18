import mysql.connector as sql

class ConnectDatabase:
    def __init__(self, Host, User, Password, Database):
        self.Host = Host
        self.User = User
        self.Password = Password
        self.Database = Database
    def Connection(self):
        try:
            ConnectionString = sql.connect(host = self.Host, user = self.User, password = self.Password, database = self.Database)
            if(ConnectionString.is_connected()):
                return ConnectionString
        except:
            return False