from socket_wrap import socket_wrap 
from redis_response import redis_response

def encode_command (command_arguments):
    ending = "\r\n"
    encoded_command = "*"+str(len(command_arguments))+ending

    for argument in command_arguments:
        encoded_command += "$"+str(len(argument))+ending
        encoded_command += argument+ending
    return encoded_command

class redis_connection:
    connection = None

    def __init__(self,server="127.0.0.1",port=6379):
        self.connection = socket_wrap(server,port)

    def connect(self):
        self.connection.connect()

    def ping (self):
        self.connection.send("PING")
        response = self.connection.recive()
        return response.decode_reponse() == "PONG"

    def execute(self,arguments):
        encoded_command = encode_command(arguments)
        return self.__execute_command(encoded_command)

    def __execute_command (self,command):
        self.connection.send(command)
	response = redis_response(self.connection.recive())
        return response

    def close(self):
        self.connection.close()
