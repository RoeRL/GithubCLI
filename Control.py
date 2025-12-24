import requests
import os
import json 

def createRepo(PAT_KEY):
    url = "https://api.github.com/user/repos"
    token = PAT_KEY

    headers = {"Authorization" : "token {}".format(token)}
    RepositoryName = input("Enter your repository name: ")
    print("Making "+RepositoryName)

    data = {"name" : "{}".format(RepositoryName)}
    requests.post(url, data = json.dumps(data), headers=headers)
