from flask import Flask
# Import flask_restful which gives access to the HTTP methods like GET, PUT, POST and DELETE
from flask_restful import Api

from resources.app_subscriptions import Subscriptions

app = Flask(__name__)
api = Api(app)
app.config["DEBUG"] = True

api.add_resource(Subscriptions, "/subscriptions")
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)