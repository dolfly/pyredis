import socket

'''
socket_wrap

Simple socket wrapper to make manipulating sockets simpler .
'''

class socket_wrap:
    connection  = socket.socket(socket.AF_INET)
    def __init__ (self,server_name="127.0.0.1",
                  port=6379,auto_connect=True):

        if (auto_connect):
            self.connect(server_name,port)

    def connect (self,server_name="127.0.0.1",port=6379):
        self.connection.connect((server_name,port))

    def send (self,cmd):
        self.connection.send (cmd)

    def recive (self,byte_count=1024):
        response_text = self.connection.recv(byte_count)
        return response_text

    def close (self):
        if (self.connection != None):
            self.connection.close ()
