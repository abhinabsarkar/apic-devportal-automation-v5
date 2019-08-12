# Library to invoke REST API using requests
import requests
# Secure Password Prompt
import getpass
# Suppress InsecureRequestWarning in the response
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Import json module
import json

# Get the user input
#url = input("url: ")

url = "https://api.github.com/orgs/dotnet/repos"
req_headers = {"User-Agent":".NET Foundation Repository Reporter", 
    "Accept":"application/vnd.github.v3+json"}
# Get the list of dotnet repositories    
response = requests.get(url, headers=req_headers, verify=False)
print(response.status_code)

# Load output to JSON object
output = json.loads(response.text)

# Get the url of the nth repository
print("The url of the 1st repository: " + output[0]["url"])
# Loop through the name of 1st 5 repos
print("The name of the 1st 5 repositories are listed below:")
for counter in range(5):
    print(counter + 1, output[counter]["name"])
# Loop through the names of all repos
print("The name of all the repositories are listed below:")
for item in output:
    print(item["name"])
# Loop through the names of all repos in range
print("The name of all the repositories are listed below:")
for counter in range(len(output)):
    print(counter + 1, output[counter]["name"])


