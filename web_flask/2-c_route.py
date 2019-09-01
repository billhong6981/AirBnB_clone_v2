#!/usr/bin/python3
"""my simple Web Server API application module"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_flask():
    """my first flask application"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hello_hbnb():
    """function take the path variable"""
    return "HBNB"


@app.route('/c/<text>')
def hello_c(text):
    """function take the route variable"""
    text = 'C ' + text.replace('_', ' ')
    return text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
