import requests
import os 

url = "https://routejcnusx3h-rdrubbel-che.8a09.starter-us-east-2.openshiftapps.com/"
ALLOWED_EXTENSIONS = set(['yaml'])

files = os.listdir("/projects/test")

files = {'file': open('{}'.format(files[1]), 'rb')}

r = requests.post(url, files=files)
print(r.status_code)
print(r.text)
