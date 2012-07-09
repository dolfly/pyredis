import socket
from redis_response import redis_response

'''
redis_connection

Simple socket wrapper to make manipulating sockets simpler .
'''

class redis_connection :
    connection  = socket.socket(socket.AF_INET)
    def __init__ (self,server_name="127.0.0.1",
                  port=6379,auto_connect=True):

        if (auto_connect):
            self.connect(server_name,port)

    def connect (self,server_name="127.0.0.1",port=6379):
        self.connection.connect((self.server_name,6379))

    def send (self,cmd):
        self.connection.send (cmd)

    def recive (self,byte_count=4096):
        response_text   = self.connection.recv(byte_count)
        response_object = redis_response(response_text)
        return response_object

    def close (self):
        if (self.connection != None):
            self.connection.close ()
