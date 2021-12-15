
from wsgiref import simple_server
from flask import Flask

import os


app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    return "Flask app is running and I am changing something and I made another change now !! AND HELLO and Kannan is Here"

port = int(os.getenv("PORT", 5001))

if __name__ == "__main__":
    host = '0.0.0.0'
    httpd = simple_server.make_server(host=host, port=port, app=app)
    httpd.serve_forever()
