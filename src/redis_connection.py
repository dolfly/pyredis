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
    def __init__(self,server_name):
        self.connection = redis_connection(server_name)

    def connect(self):
        self.connection.connect()

    def ping_server (self):
        self.connection.send("PING")
        response = self.connection.recive()
        return response.decode_reponse() == "PONG"

    def execute_encoded_command(self,arguments):
        encoded_command = encode_command(arguments)
        return self.execute_command(encoded_command)

    def execute_command (self,command):
        self.connection.send(command)
	response = redis_response(self.connection.recive())
        return response
