# -*- coding: utf-8 -*-
from flask import Flask, url_for, request
import logging
import json
import os

project_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test', methods=['POST'])
def webshell_scan():
    author = request.form['Author']
    time = request.form['Time']
    ref = request.form['Ref']
    files = request.form['Files']
    print author
    print time
    print ref
    print files
    return "Ok"

if __name__ == '__main__':
    # init_logger()
    app.run(host='0.0.0.0', port=8080, threaded=True)
