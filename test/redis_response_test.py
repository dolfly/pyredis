import nose
from nose.tools import *
from pyredis import redis_response
from pyredis.redis_response import redis_exception

def test_response_type ():
    response = redis_response ("*somecode")
    assert response.response_type() == "multi-bulk"
    response = redis_response (":somecode")
    assert response.response_type() == "integer"
    response = redis_response ("+somecode")
    assert response.response_type() == "single line"

def test_decode_response ():
    response = redis_response ("$8\r\nsomecode\r\n")
    assert response.decode_response() == "somecode"
    response = redis_response ("$8\r\nsome text with spaces\r\n")
    assert response.decode_response() == "some text with spaces"

    # integer replies
    response = redis_response (":12\r\n")
    assert response.decode_response() == 12
    response = redis_response (":124\r\n")
    assert response.decode_response() == 124

    # multi-bulk replies
    response = redis_response ("*2\r\n$2\r\nto\r\n$5\r\ntouto")
    assert response.decode_response() == ["to","touto"]
    response = redis_response ("*3\r\n$11\r\ntoutouastro\r\n$5\r\nredis")
    assert response.decode_response() == ["toutouastro","redis"]

    # single line replies
    response = redis_response ("+OK\r\n")
    assert response.decode_response() == "OK"
    response = redis_response ("+some message\r\n")
    assert response.decode_response() == "some message"

@raises (redis_exception)
def test_redis_exception ():
    response = redis_response ("-error\r\n")
