'''
redis_response

Class that represents a redis reponse .
'''

class redis_response :
    __text   = None
    response = None
    def __init__ (self,text):
        self.__text = text
        self.response = self.decode_response ()
    def decode_response (self):
	response_type = self.response_type()
	if (response_type == "integer") :
	    return self.to_int()
	elif(response_type == "single line" or response_type == "bulk"):
	    return self.to_text()
	elif(response_type == "multi-bulk"):
	    return self.to_list ()
	
        return self.text

    def is_error (self):
        return self.__text[0]=="-"

    def is_regular (self):
        return not self.is_error()

    def to_list (self) :
        result = []
	text = self.__text.strip("\r\n")  
	for element in text.split("\r\n") :
	    if (not (element.startswith("*") 
	          or element.startswith("$"))) :
	        result.append (element)
	return result

    def to_int (self):
        text = self.__text.strip("\r\n")
	text = text.strip(":")
	return int(text)

    def to_text (self):
        return self.__text.split("\r\n")[1]

    def response_type (self):
        reply_types = {"+"  : "single line",
                       "-"  : "error",
                       ":"  : "integer",
                       "$"  : "bulk",
                       "*"  : "multi-bulk"}

        return reply_types[self.__text[0]]
