import requests
import os
import json 

class GitCLI():
    private_key = "0"
    username


    def createRepo():
        
        __token = private_key
        try:
            headers = {"Authorization" : "token {}".format(__token)}
            RepositoryName = input("Enter your repository name: ")
            print("Making "+RepositoryName)
            __url = "https://api.github.com/user/repos"

            data = {"name" : "{}".format(RepositoryName)}
            requests.post(url, data = json.dumps(data), headers=headers)
        except Exception as e: print(e)

    def deleteRepo(RepoName):
        __token = private_key
        try:
            headers = {"Authorization" : "token {}".format(__token)}
            __RepositoryName = RepoName
            __url = "https://api.github.com/user/repos/{}/{}".format(username, __RepositoryName)
            requests.delete(url, headers=headers)
        except Exception as e: print(e)

    def createIssue(RepoName):
        __token = private_key
        data = {}
        try:
            __headers = {"Authprization" : "token {}".format(__token)}
            __RepositoryName = RepoName
            __url= "https://api.github.com/repos/{}/{}/issues".format(username, __RepoName)
            requests.post(url, data=json.dumps(data), headers=headers)

        except Exception as e: print(e)
