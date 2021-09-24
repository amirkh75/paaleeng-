# app.py

""" this componented after api.py
def app(environ, start_response):
    \""" this app speaks with http web server with wsgi rules.\"""
    response_body = b'Hello, world!'
    status = '200 OK'
    start_response(status, headers=[])
    return iter([response_body])
"""

from webob.descriptors import parse_int_safe
from api import API

app = API()


@app.route('/')
def home(request, response):
    """ function based and class based views (our handlers) """
    response.text = '<h1>Hello from the HOME page.</h1>'

@app.route('/about')
def about(request, response):
    """ explains the current..."""
    response.text = '<h1>Hello from the ABOUT page.</h1>'

@app.route('/hello/{name}')
def greeting(request, response, name):
    """explains here."""
    response.text = f'<h1> Hello, {name} </h1>'
