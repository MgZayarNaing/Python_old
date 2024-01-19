import request as req

resp = req.get("http://www.bbc.com")
print(resp.txt)

#2
import request as req

resp = req.get("http://www.bbc.com")
print(resp.status_code)

#3
import requests

url = requests.head('https://www.google.com')
print(url.headers)