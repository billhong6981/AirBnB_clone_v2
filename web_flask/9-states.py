#!/usr/bin/python3
"""my simple Web Server API application module"""
from flask import Flask, render_template
from models import storage
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


@app.route('/number_template/<int:n>')
def hello_template(n):
    """function takes integer number and return html page"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def hello_even_odd(n):
    """function takes number and returns different page depend on n"""
    if n % 2 == 0:
        s = "even"
    else:
        s = "odd"
    return render_template('6-number_odd_or_even.html', n=n, s=s)


@app.route('/states_list')
def hello_states():
    """displays all states"""
    dic = storage.all('State')
    return render_template('7-states_list.html', dic=dic)


@app.route('/cities_by_states')
def hello_states_cities():
    """displays all cities under its state it belongs to"""
    dic = storage.all('State')
    return render_template('8-cities_by_states.html', dic=dic)


@app.route('/states')
@app.route('/states/<id>')
def hello_states_and_cities(id=None):
    """displays all cities in state"""
    dic = storage.all('State')
    if id is None:
        return render_template('7-states_list.html', dic=dic)
    for value in dic.values():
        if value.id == id:
            new = value
            b = 'State: ' + value.name
            break
        else:
            new = None
            b = 'Not found!'
    return render_template('9-states.html', new=new, b=b)


@app.teardown_appcontext
def do_teardown(self):
    """remove the session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
