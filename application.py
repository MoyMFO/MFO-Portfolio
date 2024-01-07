from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap

application = Flask(__name__)
bootstrap = Bootstrap(application)

@application.route("/")
def hello_world():
    return render_template('index.html')

