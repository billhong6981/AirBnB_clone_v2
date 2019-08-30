#!/usr/bin/python3
"""my first Web Server API application module"""
from flask import Flask
app = Flask(__name__)


@app.route('/', defaults={'path': ''},
           methods=["GET", "POST", "PUT", "DELETE"], strict_slashes=False)
@app.route('/<path: path>',
           methods=["GET", "POST", "PUT", DELETE"], strict_slashes=False)
def hello_flask():
    """my first flask application"""
    return Hello HBNB!

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
