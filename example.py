from pyredis.redis_connection import redis_connection

con = redis_connection()
print con.ping ()
#True

con.execute(["SET","somevar","somevalue"])
response = con.execute(["GET","somevar"])
print response.decode_response ()
#'somevalue'
