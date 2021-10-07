import requests as req
import time
import random

url = "http://127.0.0.1:5000"

while 1 == 1:
    time.sleep(random.randrange(0, 5))
    req.get(url + "/test/getAll")
    print("get - /test/getAll")
    req.post(url + "/test/create")
    print("post - /test/create")
    req.delete(url + "/test/delete")
    print("delete - /test/delete")
