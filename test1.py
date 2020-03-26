import requests
import os 

url = "http://localhost:5000/api/classification/classify"
#os.chdir("/projects/.theia")

def get_filename(prompt):
    while True:
        fn = input(prompt)
        if os.path.exists(fn): return fn
        print("The file you selected does not exist, please try again")

file = get_filename("Enter a filename: ")

files = {'file': open(file, 'rb')}

r = requests.post(url, files=files)
print(r.status_code)
print(r.text)
