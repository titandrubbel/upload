import requests

url = "http://localhost:5000/"
fin = open('main.py', 'rb')
files = {'file': fin}

try:
  r = requests.post(url, files=files)
	print r.text
finally:
	fin.close()
