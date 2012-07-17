import nose
from pyredis import redis_response

def test_response_type ():
    response = redis_response ("-somecode")
    assert response.response_type() == "error"
    response = redis_response ("*somecode")
    assert response.response_type() == "multi-bulk"
    response = redis_response (":somecode")
    assert response.response_type() == "integer"

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
