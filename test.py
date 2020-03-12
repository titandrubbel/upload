import requests

url = "http://localhost:5000/"
files = {'file': open('main.py', 'rb')}

r = requests.post(url, files=files)
print(r.status_code)
print(r.text)
