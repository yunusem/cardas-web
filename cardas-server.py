from flask import Flask, request
from flask import jsonify
from flask import g
from flask_api import status
import os
import sqlite3


app = Flask(__name__, static_url_path="/images", static_folder="images")


def get_db():
    if not hasattr(g, 'cardas.db'):
        g.db = sqlite3.connect('cardas.db')
    return g.db


@app.teardown_appcontext
def close_db(error):
    # print(error)
    if hasattr(g, 'cardas.db'):
        g.db.close()


@app.route('/')
def home():
    return ""


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)