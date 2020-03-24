import requests
import os 

url = "http://localhost:5000/api/classification/classify"
ALLOWED_EXTENSIONS = set(['yaml'])

#files = os.listdir("/projects/test")

#files = {'file': open('{}'.format(files[1]), 'rb')}

file = input("Enter a filename: ")

files = {'file': open(file), 'rb')}

r = requests.post(url, files=files)
print(r.status_code)
print(r.text)
