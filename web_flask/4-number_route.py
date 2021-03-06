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
    """function takes the path variable"""
    return "HBNB"


@app.route('/c/<text>')
def hello_c(text):
    """function takes the route variable"""
    text = 'C ' + text.replace('_', ' ')
    return text


@app.route('/python/<text>')
@app.route('/python')
def hello_python(text='is cool'):
    """function takes the route variable"""
    text = 'Python ' + text.replace('_', ' ')
    return text


@app.route('/number/<int:n>')
def hello_number(n):
    """function takes route variable n only if n is integer"""
    return str(n) + " is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
