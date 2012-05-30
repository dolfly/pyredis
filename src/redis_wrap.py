from redis_connection import redis_connection
from redis_response import redis_response

class redis_wrap:
    connection = None
    def __init__(self,server_name):
        self.connection = redis_connection(server_name)
    def connect(self):
        self.connection.connect()
    def ping_server (self):
        self.connection.send("PING")
        response = self.connection.recive()
        return response.decode_reponse() == "PONG"
    def execute_command (self,command):
        self.connection.send(command)
        return self.connection.recive()
