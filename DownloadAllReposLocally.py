import requests
import urllib.request
import time
import os
import sys

if (len(sys.argv) > 3 or len(sys.argv) < 2):
    print("Format : main.py username [download_location]")
    exit(-1)

Username = sys.argv[1]
Destination = None

if (len(sys.argv) > 2):
    Destination = sys.argv[2]

url = 'https://api.github.com/users/' + Username + '/repos'
response = requests.get(url)

if (response.status_code != 200):
    print("Error while retrieving : {}".format(response.reason))
    exit(-1)

JsonData = response.json()

if Destination:
    if not os.path. exists(Destination):
       print("mkdir {}".format(Destination))

for json in JsonData:
    if Destination:
        if not os.path.exists(Destination + "/" + json['name']):
            print("git clone {} {}".format(json['clone_url'], Destination + "/" + json['name']))
        else:
            print("cd {};git pull;cd -".format(Destination + "/" + json['name']))
    else:
        print(json['clone_url'])
