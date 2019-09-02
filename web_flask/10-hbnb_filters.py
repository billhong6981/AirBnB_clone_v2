#!/usr/bin/python3
"""my simple Web Server API application module"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


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


@app.route('/hbnb_filters')
def hello_hbnb_filters():
    """displays all cities under its state it belongs to"""
    dic = storage.all('State')
    a_dic = storage.all('Amenity')
    return render_template('10-hbnb_filters.html', dic=dic, a_dic=a_dic)


@app.teardown_appcontext
def do_teardown(self):
    """remove the session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
