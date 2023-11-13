from flask import Flask, request, json, jsonify
from flask_cors import CORS, cross_origin
import pandas as pd
import numpy as np

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def home():
    return 'Home!'

@app.route('/about')
@cross_origin()
def about():
    return 'About!'

if __name__ == '__main__':
    app.run(debug=True)