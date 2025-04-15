# Import the flask class from the flask module 
from flask import Flask

#Create an instance of the flask class
app = Flask(__name__)

#Define a route and a function to handle requests to that route
@app.route("/")
def hello_world():
    return "Testing Testing 12345"

#Run your app
if __name__ == '__main__':
  app.run(host="0.0.0.0", port=5000, debug=True)

