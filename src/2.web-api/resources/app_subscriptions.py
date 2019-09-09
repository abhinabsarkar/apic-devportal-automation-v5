from flask_restful import Resource
from flask import request

import processes.create_subscribe_apps_main

import configparser
# Import json module
import json

class Subscriptions(Resource):
  # def get(self):
  #     return "<h1>Steps to automate App subscriptions on Dev Portal</h1><p>Send a POST request to the endpoint</p>", 200
  # def post(self):
  #     try:
  #       # Get the request body & converts the JSON object into Python data
  #       req_data = request.get_json()
  #       username = req_data['username']
  #       password = req_data['password']
  #       b64encoded_csv = req_data['csvfile']
  #       response = processes.create_subscribe_apps_main.create_subscriptions(username, password, b64encoded_csv)    
  #       print("response received: " + response)  
  #       return response, 204
  #     except Exception as error:
  #       return repr(error), 500
  def get(self):
      try:
        # Get the request body & converts the JSON object into Python data
        username = request.headers.get('username')
        password = request.headers.get('password')
        b64encoded_csv = request.headers.get('csvfile')
        response = processes.create_subscribe_apps_main.create_subscriptions(username, password, b64encoded_csv)            
        return response, 200
      except Exception as error:
        return repr(error), 500  