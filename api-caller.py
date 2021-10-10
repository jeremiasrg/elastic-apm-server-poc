import requests as req
import time
import random
import json

url = "http://127.0.0.1:5000"

while 1 == 1:
    time.sleep(random.randrange(0, 5))
    req.get(url + "/team/getAll")
    print("get - /team/getAll")
    req.post(url + "/team", json={"name": "Team01", "year": 1907})
    print("post - /team/")
