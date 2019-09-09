# devportalappmgmt.py

# Importing my libraries
import custom_exception
# Library to invoke REST API using requests
import requests
# Import json module
import json
# Library to convert string to dictionary
import ast
# Import CSV read & write module
import csv
# Importing configuration parser
import configparser
# Suppress InsecureRequestWarning in the response
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Parser to read configuration values
config = configparser.ConfigParser()
config.read("config.ini")

# Get Dev Org name
def dev_org_exists(username, password, dev_org_name):
    # Headers have to be converted from string to dictionay else it will give AttributeError: 'str' object has no attribute 'items' 
    req_headers = ast.literal_eval(config["Env"]["apim_context"])
    uri = config["Default"]["dev_org_uri"]
    query_param = "?name=" + dev_org_name
    url = "https://" + config["Env"]["apim_hostname"] + uri + query_param    

    # Invoke the REST API call to create the Dev Org
    response = requests.get(url, headers=req_headers, auth=(username, password), verify=False) 
    if response.status_code != 200:
        raise custom_exception.ApiError('Error occured: {0}:{1}'.format(response.status_code, response.text))
    output = json.loads(response.text)
    if len(output) == 0:
        return [False, 0]
    else:
        devorg_id = "" 
        for counter in range(len(output)):
            devorg_id = output[counter]["id"]
        return [True, devorg_id]

# Create a Dev Org and return the Dev Org ID
def create_dev_org(username, password, dev_org_name):
    # Headers have to be converted from string to dictionay else it will give AttributeError: 'str' object has no attribute 'items' 
    req_headers = ast.literal_eval(config["Env"]["apim_context"])
    uri =  config["Default"]["dev_org_uri"]
    url = "https://" + config["Env"]["apim_hostname"] + uri
    # Convert string to JSON
    data = json.dumps({"name": dev_org_name})
    
    # Invoke the REST API call to create the Dev Org
    response = requests.post(url, headers=req_headers, data=data, auth=(username, password), verify=False)
    if response.status_code != 201:
        raise custom_exception.ApiError('Error occured: {0}:{1}'.format(response.status_code, response.text))
    # Load output to JSON object
    output = json.loads(response.text)
    return output["id"]

# Create an App and return the App ID, Client ID & Secret
def create_app(username, password, dev_org_id, app_name):
    # Headers have to be converted from string to dictionay else it will give AttributeError: 'str' object has no attribute 'items' 
    req_headers = ast.literal_eval(config["Env"]["apim_context"]) 
    uri =  config["Default"]["dev_org_uri"] + "/" + dev_org_id + "/apps"
    url = "https://" + config["Env"]["apim_hostname"] + uri
    # Convert string to JSON
    data = json.dumps({"name": app_name, "credentials": {"clientID": "true", "clientSecret": "true"}})

    # Invoke the REST API call to create the app
    response = requests.post(url, headers=req_headers, data=data, auth=(username, password), verify=False)
    if response.status_code != 201:
        raise custom_exception.ApiError('Error occured: {0}:{1}'.format(response.status_code, response.text))
    # Load output to JSON object
    output = json.loads(response.text)
    # Return App ID, Client ID & Client Secret
    app_id = output["id"]
    client_id = output["credentials"]["clientID"]
    client_secret = output["credentials"]["clientSecret"]
    return [app_id, client_id, client_secret]

# Subscribe app to product subscription
def subscribe_app(username, password, dev_org_id, app_name, plan_name):
    # Headers have to be converted from string to dictionay else it will give AttributeError: 'str' object has no attribute 'items' 
    req_headers = ast.literal_eval(config["Env"]["apim_context"]) 
    uri =  config["Default"]["dev_org_uri"] + "/" + dev_org_id + "/apps/" + app_name + "/subscriptions"
    url = "https://" + config["Env"]["apim_hostname"] + uri
    # Get the product name and version number for the body of the request
    product_name = config["Default"]["product_name"]
    version_number = config["Default"]["version_number"]
    # Convert string to JSON
    data = json.dumps({"plan": plan_name, "product": {"name": product_name, "version": version_number}})

    # Invoke the REST API call to subscribe to the product
    response = requests.post(url, headers=req_headers, data=data, auth=(username, password), verify=False)
    if response.status_code != 201:
        raise custom_exception.ApiError('Error occured: {0}:{1}'.format(response.status_code, response.text))
    # Return true if subscibed successfully
    return True