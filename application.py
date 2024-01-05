from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello_world():
    return 'Hello World'

@application.route("/hello")
def hello_world():
    return 'Hello this is my second link'