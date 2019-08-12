# Python Notes

## References
* [Naming conventions](https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html)
## How to bypass Proxy?
```python
set http_proxy=http://<user>:<password>@<proxy_address>:<proxy_port>
set https_proxy=https://<user>:<password>@<proxy_address>:<proxy_port>
set no_proxy=.domain1.com,.domain2.com
```
## How to bypass SSL?
```python
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org <package_name>
Eg:
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org requests
```
## Suppress InsecureRequestWarning in the response
```python
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
```
## Run python script
```python
python hello-python.py
```
## REST API using Basic Auth
```python
# Library to invoke REST API using requests
import requests
# Secure Password Prompt
import getpass
url = "https://www.google.com"
# Request headers
request_headers = {"Accept":"application/html", "Content":"application/html"}
# Invoke the API passing the parameters and headers along with basic authentication
response = requests.get(url, headers=requestHeaders, auth=(input("username: "), getpass.getpass("Password: ")), verify=False)
print(response.status_code)
print(response.content)
```
## Work with JSON objects
```python
# Library to invoke REST API using requests
import requests
# Secure Password Prompt
import getpass
# Suppress InsecureRequestWarning in the response
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Import json module
import json

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
```