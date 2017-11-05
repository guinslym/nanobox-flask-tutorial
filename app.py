from flask import Flask
app = Flask(__name__)

import os

user    = os.environ.get('DATA_DB_USER')
passwd  = os.environ.get('DATA_DB_PASS')
host    = os.environ.get('DATA_DB_HOST')

@app.route("/")
def hello():
    return os.environ.get('DATA_DB_PASS')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
