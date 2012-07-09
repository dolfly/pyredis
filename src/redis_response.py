'''
redis_response

Class that represents a redis reponse .
'''

class redis_response :
    text = None
    def __init__ (self,response_text):
        self.text = text

    def decode_reponse (self):
	#TODO : add response decoding !
        return self.text

    def is_error (self):
        return self.response_text.startswith("-")

    def is_regular (self):
        return not self.is_error()

    def to_text (self):
        text = self.text
        text.split("\r\n")[1]
        return text

    def response_type (self):
        reply_types = {"+"  : "single line",
                       "-"  : "error",
                       ":"  : "integer",
                       "$"  : "bulk",
                       "*"  : "multi-bulk"}
        return reply_types[self.response_text[0]]
