from flask import Flask
import os

app = Flask(__name__)

DIR = os.path.dirname(__file__)
DIR += "/"

@app.route("/")
def hello_world():
    print(__name__) # Printed onto console on refresh
    return "hellooooooooooooo"

if __name__ == "__main__":
    app.debug = True
    app.run()
