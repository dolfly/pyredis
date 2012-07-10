'''
redis_response

Class that represents a redis reponse .
'''

class redis_response :
    text = None
    def __init__ (self,text):
        self.text = text

    def decode_reponse (self):
	#TODO : add response decoding !
        return self.text

    def is_error (self):
        return self.text[0]=="-"

    def is_regular (self):
        return not self.is_error()

    def to_list (self) :
        result = []
	text = self.text.strip("\r\n")  
	for element in text.split("\r\n") :
	    if (not (element.startswith("*") 
	          or element.startswith("$"))) :
	        result.append (element)
		print element
	return result

    def to_int (self):
        text = self.text.strip("\r\n")
	text = text.strip(":")
	return int(text)

    def to_text (self):
        return self.text.split("\r\n")[1]

    def response_type (self):
        reply_types = {"+"  : "single line",
                       "-"  : "error",
                       ":"  : "integer",
                       "$"  : "bulk",
                       "*"  : "multi-bulk"}

        return reply_types[self.text[0]]
