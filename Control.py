import requests
import os
import json

from dotenv import load_dotenv, dotenv_values 
load_dotenv() 

url = "https://api.github.com/user/repos"
token = os.getenv("PAT_KEY")

headers = {"Authorization" : "token {}".format(token)}
RepositoryName = input("Enter your repository name: ")
print("Making "+RepositoryName)

data = {"name" : "{}".format(RepositoryName)}
requests.post(url, data = json.dumps(data), headers=headers)