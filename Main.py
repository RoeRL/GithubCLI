import requests
import json
User = input("Enter the User you want to print repo list of: ")
print(User)
url = "https://api.github.com/users/{}/repos".format(User)

data = {"type" : "all", "sort" : "full_name", "direction": "asc"}
output = requests.get(url, data=json.dumps(data))
output = json.loads(output.text)

for i in output:
    print(i["name"])
