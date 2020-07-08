#!/usr/bin/python3
import requests
import urllib.request
import time
import os
import sys

if (len(sys.argv) > 3 or len(sys.argv) < 2) or sys.argv[1] == "--help":
    print("Format : python3 DownloadAllReposLocally.py username [download_location]")
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
       Command = "mkdir {}".format(Destination)
       os.system(Command)

for json in JsonData:
    print(json['name'] + " : ")
    if Destination:
        if not os.path.exists(Destination + "/" + json['name']):
            Command = "git clone {} {}".format(json['clone_url'], Destination + "/" + json['name'])
            os.system(Command)
        else:
            Command = "cd {};git pull;cd - >/dev/null".format(Destination + "/" + json['name'])
            os.system(Command)
    else:
        print(json['clone_url'])
