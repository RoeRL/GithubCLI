import requests
import os
import json 

class GitCLI():
    def __init__(self, private_key, username):
        self.private_key = private_key
        self.username = username
        self.headers = {"Authorization" : "token {}".format(private_key)}

    def testingFunc(self):
        print(self.private_key + " " + self.username)

    def createRepo(self):
        try:
            __RepositoryName = input("Enter your repository name: ")
            print("Making "+RepositoryName)
            __url = "https://api.github.com/user/repos"

            __data = {"name" : "{}".format(RepositoryName)}
            requests.post(__url, data = json.dumps(__data), headers=self.headers)
        except Exception as e: print(e)

    def deleteRepo(self, RepoName):
        try:
            __headers = {"Authorization" : "token {}".format(self.private_key)}
            __RepositoryName = RepoName
            __url = "https://api.github.com/user/repos/{}/{}".format(self.username, __RepositoryName)
            requests.delete(__url, headers=self.headers)
        except Exception as e: print(e)

    def issuesCreate(self, RepoName):
        title = "No Title"
        __data = {
            "title" : title
        }
        try:
            __headers = {"Authprization" : "token {}".format(self.private_key)}
            __RepositoryName = RepoName
            __url= "https://api.github.com/repos/{}/{}/issues".format(self.username, __RepoName)
            requests.post(__url, data=json.dumps(__data), headers=self.headers)

        except Exception as e: print(e)

    def issuesComment(self, RepoName, issueNumber):
        __RepositoryName = RepoName
        __headers = {
            "Authorization" : "token {}".format(self.private_key)
        }
        comment = "No Comment"
        __data = {
            "body" : comment
        }
        __url = "https://api.github.com/repos/{}/{}/issues/{}/comments".format(self.username, __RepositoryName, issueNumber)
        requests.post(__url,data=json.dumps(__data),headers=self.headers)