import socket
from redis_response import redis_response

class redis_connection :
    connection = None
    def __init__ (self,server,auto_connect=True):
        self.server_name = server
        self.connection = socket.socket(socket.AF_INET)

        if (auto_connect):
            self.connect()
    def connect (self):
        self.connection.connect((self.server_name ,6379))
    def send (self,cmd):
        self.connection.send (cmd+"\r\n")
    def recive (self,byte_count=4096):
        response_text = self.connection.recv(byte_count)
        response_object =redis_response(response_text)
        return response_object
    def close (self):
        if (self.connection != None):
            self.connection.close ()
