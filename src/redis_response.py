class redis_response :
    response_text = None
    def __init__ (self,response_text):
        self.response_text = response_text

    def decode_reponse (self):
        return self.response_text

    def is_error (self):
        return self.response_text.startswith("-")

    def is_regular (self):
        return not self.is_error()

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
        reply_types = {"+"  : "single line",
                       "-"  : "error",
                       ":"  : "integer",
                       "$"  : "bulk",
                       "*"  : "multi-bluk"}
        return reply_types[self.response_text[0]]
