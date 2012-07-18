'''
redis_response

Class that represents a redis reponse .
'''

class redis_exception(Exception):
    error_message = ""
    def __init__ (self,error_message) :
        self.error_message = error_message

    def __str__ (self) :
        return "redis error : %s" %self.error_message

    def __repr__ (self) :
        return self.__str__()

class redis_response :
    __text   = None
    response = None

    def __init__ (self,text):
        self.__text = text
        self.response = self.decode_response ()
	if(self.response_type () == "error"):
	    raise redis_exception (self.decode_response())

    def decode_response (self):
	response_type = self.response_type()
	if (response_type == "integer") :
	    return self.to_int()
	elif(response_type == "bulk"):
	    return self.to_text()
	elif (response_type == "single line"):
	    return self.to_single_line ()
	elif(response_type == "multi-bulk"):
	    return self.to_list ()
	elif(response_type == "error"):
	    return self.to_error_message ()
	
    def is_error (self):
        return self.__text[0]=="-"

    def is_regular (self):
        return not self.is_error()

    def to_single_line (self):
	text = self.__text.strip('+')
	text = text.strip("\r\n")
	print text
        return text

    def to_error_message (self):
        return self.__text.strip("-\r\n")

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
	try :
	    return int(text)
	except:
	    return 0

    def to_text (self):
        return self.__text.split("\r\n")[1]

    def response_type (self):
        reply_types = {"+"  : "single line",
                       "-"  : "error",
                       ":"  : "integer",
                       "$"  : "bulk",
                       "*"  : "multi-bulk"}

        return reply_types[self.__text[0]]
