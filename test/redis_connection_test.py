import nose
from pyredis.redis_connection import encode_command

def test_encode_command ():
    assert encode_command (["ECHO","TOUTOU"]) == "*2\r\n$4\r\nECHO\r\n$6\r\nTOUTOU\r\n"
    command = encode_command (["LPUSH","TOUTOU","some value"]) 
    assert command == "*3\r\n$5\r\nLPUSH\r\n$6\r\nTOUTOU\r\n$10\r\nsome value\r\n"
