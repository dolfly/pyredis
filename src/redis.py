import socket

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


class redis_response :
    response_text = None
    def __init__ (self,response_text):
        self.response_text = response_text
    def decode_reponse (self):
        result = self.response_text
        #remove the first chat whether it's a '+' or '-'
        result = result[1:len(result)]
        return result.strip("\r\n")
    def is_error (self):
        return self.response_text.startswith("-")
    def is_regular_response (self):
        return self.response_text.startswith("+")
    def response_type (self):
        '''
        Replies

        Redis will reply to commands with different kinds of replies.
        It is possible to check the kind of reply from the first byte sent by the server:
        With a single line reply the first byte of the reply will be '+'
        With an error message the first byte of the reply will be '-'
        With an integer number the first byte of the reply will be ':'
        With bulk reply the first byte of the reply will be '$'
        With multi-bulk reply the first byte of the reply will be '*'
        '''
        reply_types = {"single line":"+",
                       "error"      :"-",
                       "integer"    :":",
                       "bulk"       :"$",
                       "multi-bluk" :"*"}
        return reply_types[self.response_text[0]]

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

