import requests
import os
import json 

class GitCLI():
    private_key = "0"
    username = "Unknown"


    def createRepo():
        
        __token = private_key
        try:
            __headers = {"Authorization" : "token {}".format(__token)}
            __RepositoryName = input("Enter your repository name: ")
            print("Making "+RepositoryName)
            __url = "https://api.github.com/user/repos"

            __data = {"name" : "{}".format(RepositoryName)}
            requests.post(__url, data = json.dumps(__data), headers=__headers)
        except Exception as e: print(e)

    def deleteRepo(RepoName):
        __token = self.private_key
        try:
            __headers = {"Authorization" : "token {}".format(__token)}
            __RepositoryName = RepoName
            __url = "https://api.github.com/user/repos/{}/{}".format(username, __RepositoryName)
            requests.delete(__url, headers=__headers)
        except Exception as e: print(e)

    def issuesCreate(RepoName):
        __token = private_key
        title = "No Title"
        __data = {
            "title" : title
        }
        try:
            __headers = {"Authprization" : "token {}".format(__token)}
            __RepositoryName = RepoName
            __url= "https://api.github.com/repos/{}/{}/issues".format(username, __RepoName)
            requests.post(__url, data=json.dumps(__data), headers=__headers)

        except Exception as e: print(e)

    def issuesComment(RepoName, issueNumber):
        __RepositoryName = RepoName
        __headers = {
            "Authorization" : "token {}".format(__token)
        }
        comment = "No Comment"
        __data = {
            "body" : comment
        }
        __url = "https://api.github.com/repos/{}/{}/issues/{}/comments".format(username, __RepositoryName, issueNumber)
        requests.post(__url,data=json.dumps(__data),headers=__headers)