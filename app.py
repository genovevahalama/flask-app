# Import necessary modules
from flask import Flask
import time
import os

# Create a Flask application instance
#app = flask.Flask(__name__)
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello():
    print("Hello from the Python script!")
    time.sleep(10)
    return "It works!"

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
