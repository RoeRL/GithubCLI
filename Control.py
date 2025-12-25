import requests
import os
import json 

class GitCLI():
    private_key = "0"


    def createRepo():
        url = "https://api.github.com/user/repos"
        token = __private_key
        try:
            headers = {"Authorization" : "token {}".format(token)}
            RepositoryName = input("Enter your repository name: ")
            print("Making "+RepositoryName)

            data = {"name" : "{}".format(RepositoryName)}
            requests.post(url, data = json.dumps(data), headers=headers)
        except Exception as e: print(e)

    def deleteRepo(Username, RepoName):
        token = __private_key
        try:
            headers = {"Authorization" : "token {}".format(m_patkey)}
            username = Username
            RepositoryName = RepoName
            url = url = "https://api.github.com/user/repos/{}/{}".format(username, RepositoryName)
            requests.delete(url, headers=headers)
        except Exception as e: print(e)