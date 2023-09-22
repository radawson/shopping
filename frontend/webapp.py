# Python webapp for the frontend using flask
# Author: Richard Dawson
# Date: 9/21/2023

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')